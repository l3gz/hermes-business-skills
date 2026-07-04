# Hermes Business Skills

Reusable Hermes marketing skills for client work.

This repo is separate from `llm-wiki-starter` on purpose:

- `llm-wiki-starter` defines the client knowledge-base structure
- `hermes-business-skills` installs repeatable marketing workflows into Hermes

## Current pack

`marketing` — a connected system of 21 marketing, copywriting, and paid-media skills.

### Entry point

- `marketing-strategy-orchestrator`: the diagnostic and routing skill — decides which channels to use based on offer, avatar, price, margin, and business stage. Gates on prerequisites (avatar + offer must exist), then delegates to the execution skills. **Start here for any new marketing engagement.**

### Foundation skills

- `avatar-builder`: deep customer avatar research (interviews, reviews, market research, top-20% analysis)
- `attractive-character-builder`: brand persona, founder story, spokesperson identity
- `offer-builder`: value equation, grand slam offer, stack, guarantees, scarcity, MAGIC naming
- `hook-angle-writer`: hooks, headlines, and angles by desire, awareness, and channel
- `brand-voice-extractor`: brand voice guide, one-liner, StoryBrand clarity
- `human-editor`: finishing pass for clarity, human tone, and claim safety

### Copywriting and content skills

- `podcast-to-copy`: turn transcripts into hooks, descriptions, emails, and social copy
- `nurture-email-writer`: nurture sequences, soap opera sequence, retention/onboarding copy
- `launch-email-writer`: product launch sequences, PLC content, webinar structure
- `funnel-page-writer`: landing, opt-in, sales, and funnel pages (single page)
- `funnel-copy-writer`: full multi-page funnel copy orchestration — assembles the copy skills into one connected funnel
- `vsl-writer`: video sales letter scripts (long-form, VSL framework, hook → promise → proof → offer)
- `ad-script-writer`: video ad scripts (hook, pattern interrupt, social-proof, CTA)
- `ad-creative-brief-writer`: creative briefs for ad production (angle, format, constraints, deliverables)

### Meta Ads skills

- `meta-ads-manager`: plan, structure, launch, or audit Meta ad campaigns (objective, CBO/ABO, budget, testing plan)
- `meta-audience-builder`: audience strategy (broad vs lookalike vs interest, retargeting sequences, exclusions)
- `meta-creative-tester`: creative testing design (test structure, variables, sprints, winner/kill criteria)
- `meta-ads-scaler`: scaling architecture (vertical/horizontal budget increases, scaling rules)
- `campaign-optimizer`: diagnose and optimize live campaigns (metrics, Learning Phase, frequency, kill/scale/wait)
- `meta-lead-gen`: Meta lead-gen form and qualification design (Instant Forms, qualification questions, funnel integration)

### How the skills connect

The skills are designed to work as a system with the orchestrator as entry point:

```text
marketing-strategy-orchestrator (entry point — diagnoses channels, delegates)
        ↓ gates on: avatar + offer must exist
        ↓
avatar-builder + attractive-character-builder + brand-voice-extractor + offer-builder
        ↓
hook-angle-writer
        ↓
┌─────────────────────────┬──────────────────────┬──────────────────────┐
│ copy & content          │ funnel               │ meta ads             │
│                         │                      │                      │
│ podcast-to-copy         │ funnel-copy-writer   │ meta-ads-manager     │
│ nurture-email-writer    │  (orchestrates →)    │ meta-audience-builder│
│ launch-email-writer     │ funnel-page-writer   │ meta-creative-tester │
│ ad-script-writer        │ vsl-writer           │ meta-ads-scaler      │
│ ad-creative-brief-writer│                      │ campaign-optimizer   │
│                         │                      │ meta-lead-gen        │
└─────────────────────────┴──────────────────────┴──────────────────────┘
        ↓
human-editor (final pass on any output)
```

Client-specific facts, avatars, characters, offers, and voice live in the client's LLM wiki under `businesses/<business-slug>/`. The skills are generic procedures. Build quality skills one by one.

## Quick start

Dry-run first:

```bash
python3 scripts/install_skills.py --pack marketing --dry-run
```

Install the marketing pack into the active Hermes profile:

```bash
python3 scripts/install_skills.py --pack marketing
```

Install one skill:

```bash
python3 scripts/install_skills.py --skill offer-builder
```

Guided wizard:

```bash
python3 scripts/install_wizard.py
```

## Where skills install

Skills always end up inside the active Hermes profile. The installer picks a default target with this order of precedence:

1. Explicit `--target <path>` always wins.
2. If `HERMES_PROFILE` is set (for example `matt`), the default target is `~/.hermes/profiles/<HERMES_PROFILE>/skills`. This is the common case when you run the installer from inside a Hermes session.
3. If `HERMES_HOME` is set without `HERMES_PROFILE`, the default target is `$HERMES_HOME/skills`.
4. Otherwise the default target is `~/.hermes/skills` (the shared default profile).

When the resolved target lands in the shared default profile while a non-default profile is active, the installer prints a loud warning on stderr. Pass `--target ~/.hermes/profiles/<name>/skills` (or set `HERMES_PROFILE`) to silence it.

Both `HERMES_PROFILE` and `HERMES_HOME` are honored by `install_skills.py` and by the wizard. You can also pass `--target` explicitly to install into any directory you want.

## Design rules

- Skills are procedures, not client secrets.
- Client-specific knowledge belongs in the client's wiki, not inside the skill.
- Each skill stores outputs under `businesses/<business-slug>/` in the client wiki.
- Framework reference files are original summaries, not copyrighted book text.
- Skills flag risky health, income, legal, and credential claims.
- Keep skills generic enough to reuse across clients.
