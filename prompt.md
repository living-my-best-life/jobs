# AI Exposure of the US Job Market

This document contains structured data on 342 US occupations from the Bureau of Labor Statistics Occupational Outlook Handbook, each scored for AI exposure on a 0-10 scale by an LLM (Gemini Flash). Use this data to analyze, question, and discuss how AI will reshape the US labor market.

Live visualization: https://karpathy.ai/jobs/
GitHub: https://github.com/karpathy/jobs

## Scoring methodology

Each occupation was scored on a single AI Exposure axis from 0 to 10, measuring how much AI will reshape that occupation. The score considers both direct automation (AI doing the work) and indirect effects (AI making workers so productive that fewer are needed).

A key heuristic: if the job can be done entirely from a home office on a computer — writing, coding, analyzing, communicating — then AI exposure is inherently high (7+), because AI capabilities in digital domains are advancing rapidly. Conversely, jobs requiring physical presence, manual skill, or real-time human interaction have a natural barrier.

Calibration anchors:
- 0-1 Minimal: roofers, janitors, construction laborers
- 2-3 Low: electricians, plumbers, firefighters, dental hygienists
- 4-5 Moderate: registered nurses, police officers, veterinarians
- 6-7 High: teachers, managers, accountants, journalists
- 8-9 Very high: software developers, graphic designers, translators, paralegals
- 10 Maximum: data entry clerks, telemarketers

## Aggregate statistics

- Total occupations: 342
- Total jobs: 143,066,500 (143M)
- Total annual wages: $8.9T
- Job-weighted average AI exposure: 0.0/10

### Breakdown by exposure tier

| Tier | Occupations | Jobs | % of jobs | Wages | % of wages | Avg pay |
|------|-------------|------|-----------|-------|------------|---------|
| Minimal (0-1) | 0 | 0 | 0.0% | $0.0T | 0.0% | $0 |
| Low (2-3) | 0 | 0 | 0.0% | $0.0T | 0.0% | $0 |
| Moderate (4-5) | 0 | 0 | 0.0% | $0.0T | 0.0% | $0 |
| High (6-7) | 0 | 0 | 0.0% | $0.0T | 0.0% | $0 |
| Very high (8-10) | 0 | 0 | 0.0% | $0.0T | 0.0% | $0 |

### Average exposure by pay band (job-weighted)

| Pay band | Avg exposure | Jobs |
|----------|-------------|------|

### Average exposure by education level (job-weighted)

| Education | Avg exposure | Jobs |
|-----------|-------------|------|

### BLS-projected declining occupations

| Occupation | Exposure | Outlook | Jobs |
|-----------|----------|---------|------|
| Adult basic and secondary education and ESL teachers | None/10 | -14% | 41K |
| Tellers | None/10 | -13% | 347K |
| Desktop publishers | None/10 | -12% | 5K |
| Cashiers | None/10 | -10% | 3.2M |
| Bill and account collectors | None/10 | -10% | 167K |
| Power plant operators, distributors, and dispatchers | None/10 | -10% | 47K |
| Nuclear technicians | None/10 | -8% | 6K |
| General office clerks | None/10 | -7% | 2.6M |
| Metal and plastic machine workers | None/10 | -7% | 1.0M |
| Correctional officers and bailiffs | None/10 | -7% | 406K |
| Library technicians and assistants | None/10 | -7% | 163K |
| Water and wastewater treatment plant and system operators | None/10 | -7% | 132K |
| Bookkeeping, accounting, and auditing clerks | None/10 | -6% | 1.6M |
| Material recording clerks | None/10 | -6% | 1.3M |
| Computer programmers | None/10 | -6% | 121K |
| Advertising sales agents | None/10 | -6% | 104K |
| Floral designers | None/10 | -6% | 44K |
| Customer service representatives | None/10 | -5% | 2.8M |
| Financial clerks | None/10 | -5% | 1.2M |
| Postal service workers | None/10 | -5% | 500K |
| Claims adjusters, appraisers, examiners, and investigators | None/10 | -5% | 365K |
| Medical transcriptionists | None/10 | -5% | 44K |
| Jewelers and precious stone and metal workers | None/10 | -5% | 35K |
| Fishing and hunting workers | None/10 | -5% | 22K |
| Forest and conservation workers | None/10 | -5% | 11K |
| Survey researchers | None/10 | -5% | 9K |
| Network and computer systems administrators | None/10 | -4% | 332K |
| Cost estimators | None/10 | -4% | 221K |
| News analysts, reporters, and journalists | None/10 | -4% | 49K |
| Information clerks | None/10 | -3% | 1.3M |
| Childcare workers | None/10 | -3% | 992K |
| Food preparation workers | None/10 | -3% | 903K |
| Computer support specialists | None/10 | -3% | 882K |
| Agricultural workers | None/10 | -3% | 813K |
| Telecommunications technicians | None/10 | -3% | 268K |
| Insurance underwriters | None/10 | -3% | 127K |
| Preschool and childcare center directors | None/10 | -3% | 90K |
| Political scientists | None/10 | -3% | 6K |
| Geographers | None/10 | -3% | 2K |
| Kindergarten and elementary school teachers | None/10 | -2% | 1.5M |
| High school teachers | None/10 | -2% | 1.1M |
| Middle school teachers | None/10 | -2% | 634K |
| Machinists and tool and die makers | None/10 | -2% | 355K |
| Elementary, middle, and high school principals | None/10 | -2% | 333K |
| Woodworkers | None/10 | -2% | 215K |
| Tax examiners and collectors, and revenue agents | None/10 | -2% | 58K |
| Logging workers | None/10 | -2% | 44K |
| Announcers and DJs | None/10 | -2% | 40K |
| Boilermakers | None/10 | -2% | 10K |
| Waiters and waitresses | None/10 | -1% | 2.3M |
| Assemblers and fabricators | None/10 | -1% | 1.9M |
| Teacher assistants | None/10 | -1% | 1.4M |
| Farmers, ranchers, and other agricultural managers | None/10 | -1% | 836K |
| Special education teachers | None/10 | -1% | 560K |
| Career and technical education teachers | None/10 | -1% | 240K |
| Construction and building inspectors | None/10 | -1% | 148K |
| Dental and ophthalmic laboratory technicians and medical appliance technicians | None/10 | -1% | 67K |
| Nuclear engineers | None/10 | -1% | 15K |
| Models | None/10 | -1% | 7K |

### Fastest-growing occupations (10%+ projected growth)

| Occupation | Exposure | Outlook | Jobs |
|-----------|----------|---------|------|
| Wind turbine technicians | None/10 | +50% | 14K |
| Solar photovoltaic installers | None/10 | +42% | 29K |
| Nurse anesthetists, nurse midwives, and nurse practitioners | None/10 | +35% | 383K |
| Data scientists | None/10 | +34% | 246K |
| Information security analysts | None/10 | +29% | 183K |
| Medical and health services managers | None/10 | +23% | 616K |
| Actuaries | None/10 | +22% | 34K |
| Operations research analysts | None/10 | +21% | 112K |
| Physician assistants | None/10 | +20% | 163K |
| Computer and information research scientists | None/10 | +20% | 40K |
| Financial examiners | None/10 | +19% | 65K |
| Occupational therapy assistants and aides | None/10 | +18% | 54K |
| Home health and personal care aides | None/10 | +17% | 4.3M |
| Substance abuse, behavioral disorder, and mental health counselors | None/10 | +17% | 484K |
| Logisticians | None/10 | +17% | 241K |
| Psychiatric technicians and aides | None/10 | +16% | 183K |
| Physical therapist assistants and aides | None/10 | +16% | 157K |
| Epidemiologists | None/10 | +16% | 12K |
| Software developers, quality assurance analysts, and testers | None/10 | +15% | 1.9M |
| Financial managers | None/10 | +15% | 869K |
| Computer and information systems managers | None/10 | +15% | 667K |
| Speech-language pathologists | None/10 | +15% | 187K |
| Massage therapists | None/10 | +15% | 168K |
| Health information technologists and medical registrars | None/10 | +15% | 42K |
| Occupational therapists | None/10 | +14% | 160K |
| Industrial machinery mechanics, machinery maintenance workers, and millwrights | None/10 | +13% | 538K |
| Diagnostic medical sonographers | None/10 | +13% | 90K |
| Marriage and family therapists | None/10 | +13% | 78K |
| Medical equipment repairers | None/10 | +13% | 68K |
| Forensic science technicians | None/10 | +13% | 21K |
| Orthotists and prosthetists | None/10 | +13% | 10K |
| Medical assistants | None/10 | +12% | 811K |
| Fitness trainers and instructors | None/10 | +12% | 370K |
| Computer network architects | None/10 | +12% | 179K |
| Occupational health and safety specialists and technicians | None/10 | +12% | 164K |
| Respiratory therapists | None/10 | +12% | 140K |
| Training and development specialists | None/10 | +11% | 452K |
| Animal care and service workers | None/10 | +11% | 439K |
| Industrial engineers | None/10 | +11% | 351K |
| Physical therapists | None/10 | +11% | 267K |
| Community health workers | None/10 | +11% | 65K |
| Athletic trainers | None/10 | +11% | 34K |
| Semiconductor processing technicians | None/10 | +11% | 32K |
| Personal financial advisors | None/10 | +10% | 326K |
| Veterinarians | None/10 | +10% | 86K |
| Chiropractors | None/10 | +10% | 57K |

## All 342 occupations

Sorted by AI exposure (descending), then by number of jobs (descending).
