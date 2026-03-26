"""
Score each occupation's AI exposure using Claude via the claude CLI.

Reads Markdown descriptions from pages/, sends each to Claude with a scoring
rubric, and collects structured scores. Results are cached incrementally to
scores.json so the script can be resumed if interrupted.

Uses the `claude` CLI for authentication (no API key needed).

Usage:
    uv run python score.py
    uv run python score.py --start 0 --end 10   # test on first 10
"""

import argparse
import json
import os
import subprocess
import time

OUTPUT_FILE = "scores.json"

SYSTEM_PROMPT = """\
You are an expert analyst evaluating how exposed different occupations are to \
AI. You will be given a detailed description of an occupation from the Bureau \
of Labor Statistics.

Rate the occupation's overall **AI Exposure** on a scale from 0 to 10.

AI Exposure measures: how much will AI reshape this occupation? Consider both \
direct effects (AI automating tasks currently done by humans) and indirect \
effects (AI making each worker so productive that fewer are needed).

A key signal is whether the job's work product is fundamentally digital. If \
the job can be done entirely from a home office on a computer — writing, \
coding, analyzing, communicating — then AI exposure is inherently high (7+), \
because AI capabilities in digital domains are advancing rapidly. Even if \
today's AI can't handle every aspect of such a job, the trajectory is steep \
and the ceiling is very high. Conversely, jobs requiring physical presence, \
manual skill, or real-time human interaction in the physical world have a \
natural barrier to AI exposure.

Use these anchors to calibrate your score:

- **0–1: Minimal exposure.** The work is almost entirely physical, hands-on, \
or requires real-time human presence in unpredictable environments. AI has \
essentially no impact on daily work. \
Examples: roofer, landscaper, commercial diver.

- **2–3: Low exposure.** Mostly physical or interpersonal work. AI might help \
with minor peripheral tasks (scheduling, paperwork) but doesn't touch the \
core job. \
Examples: electrician, plumber, firefighter, dental hygienist.

- **4–5: Moderate exposure.** A mix of physical/interpersonal work and \
knowledge work. AI can meaningfully assist with the information-processing \
parts but a substantial share of the job still requires human presence. \
Examples: registered nurse, police officer, veterinarian.

- **6–7: High exposure.** Predominantly knowledge work with some need for \
human judgment, relationships, or physical presence. AI tools are already \
useful and workers using AI may be substantially more productive. \
Examples: teacher, manager, accountant, journalist.

- **8–9: Very high exposure.** The job is almost entirely done on a computer. \
All core tasks — writing, coding, analyzing, designing, communicating — are \
in domains where AI is rapidly improving. The occupation faces major \
restructuring. \
Examples: software developer, graphic designer, translator, data analyst, \
paralegal, copywriter.

- **10: Maximum exposure.** Routine information processing, fully digital, \
with no physical component. AI can already do most of it today. \
Examples: data entry clerk, telemarketer.

Respond with ONLY a JSON object in this exact format, no other text:
{
  "exposure": <0-10>,
  "rationale": "<2-3 sentences explaining the key factors>"
}\
"""


def score_occupation(text):
    """Send one occupation to Claude CLI and parse the structured response."""
    prompt = f"{SYSTEM_PROMPT}\n\n---\n\n{text}"

    result = subprocess.run(
        ["claude", "-p", "--model", "haiku", prompt],
        capture_output=True,
        text=True,
        timeout=120,
    )

    if result.returncode != 0:
        raise RuntimeError(f"claude CLI failed: {result.stderr.strip()}")

    content = result.stdout.strip()

    # Strip markdown code fences if present
    if content.startswith("```"):
        content = content.split("\n", 1)[1]  # remove first line
        if content.endswith("```"):
            content = content[:-3]
        content = content.strip()

    return json.loads(content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--end", type=int, default=None)
    parser.add_argument("--delay", type=float, default=0.5)
    parser.add_argument("--force", action="store_true",
                        help="Re-score even if already cached")
    args = parser.parse_args()

    with open("occupations.json") as f:
        occupations = json.load(f)

    subset = occupations[args.start:args.end]

    # Load existing scores
    scores = {}
    if os.path.exists(OUTPUT_FILE) and not args.force:
        with open(OUTPUT_FILE) as f:
            for entry in json.load(f):
                scores[entry["slug"]] = entry

    print(f"Scoring {len(subset)} occupations with Claude (haiku via CLI)")
    print(f"Already cached: {len(scores)}")

    errors = []

    for i, occ in enumerate(subset):
        slug = occ["slug"]

        if slug in scores:
            continue

        md_path = f"pages/{slug}.md"
        if not os.path.exists(md_path):
            print(f"  [{i+1}] SKIP {slug} (no markdown)")
            continue

        with open(md_path) as f:
            text = f.read()

        print(f"  [{i+1}/{len(subset)}] {occ['title']}...", end=" ", flush=True)

        try:
            result = score_occupation(text)
            scores[slug] = {
                "slug": slug,
                "title": occ["title"],
                **result,
            }
            print(f"exposure={result['exposure']}")
        except Exception as e:
            print(f"ERROR: {e}")
            errors.append(slug)

        # Save after each one (incremental checkpoint)
        with open(OUTPUT_FILE, "w") as f:
            json.dump(list(scores.values()), f, indent=2)

        if i < len(subset) - 1:
            time.sleep(args.delay)

    print(f"\nDone. Scored {len(scores)} occupations, {len(errors)} errors.")
    if errors:
        print(f"Errors: {errors}")

    # Summary stats
    vals = [s for s in scores.values() if "exposure" in s]
    if vals:
        avg = sum(s["exposure"] for s in vals) / len(vals)
        by_score = {}
        for s in vals:
            bucket = s["exposure"]
            by_score[bucket] = by_score.get(bucket, 0) + 1
        print(f"\nAverage exposure across {len(vals)} occupations: {avg:.1f}")
        print("Distribution:")
        for k in sorted(by_score):
            print(f"  {k}: {'█' * by_score[k]} ({by_score[k]})")


if __name__ == "__main__":
    main()
