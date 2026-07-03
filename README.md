# Hermes Business Skills

Reusable Hermes marketing skills for client work.

This repo is separate from `llm-wiki-starter` on purpose:

- `llm-wiki-starter` defines the client knowledge-base structure
- `hermes-business-skills` installs repeatable marketing workflows into Hermes

## Current pack

`marketing` — a connected system of copywriting and marketing skills.

### Foundation skills

- `avatar-builder`: deep customer avatar research (interviews, reviews, market research, top-20% analysis)
- `attractive-character-builder`: brand persona, founder story, spokesperson identity
- `offer-builder`: value equation, grand slam offer, stack, guarantees, scarcity, MAGIC naming
- `hook-angle-writer`: hooks, headlines, and angles by desire, awareness, and channel
- `brand-voice-extractor`: brand voice guide, one-liner, StoryBrand clarity
- `human-editor`: finishing pass for clarity, human tone, and claim safety

### Output skills

- `podcast-to-copy`: turn transcripts into hooks, descriptions, emails, and social copy
- `nurture-email-writer`: nurture sequences, soap opera sequence, retention/onboarding copy
- `launch-email-writer`: product launch sequences, PLC content, webinar structure
- `funnel-page-writer`: landing, opt-in, sales, and funnel pages

### How the skills connect

The skills are designed to work as a system:

```text
raw sources / transcripts / books
        ↓
client wiki pages
        ↓
avatar-builder + attractive-character-builder + brand-voice-extractor + offer-builder
        ↓
hook-angle-writer
        ↓
podcast-to-copy / nurture-email-writer / launch-email-writer / funnel-page-writer
        ↓
human-editor
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
