# Hermes Business Skills

A connected marketing department for Hermes Agent: 21 skills across three roles — marketing strategy, creative direction, and paid media.

This repo is separate from `llm-wiki-starter` on purpose:

- `llm-wiki-starter` defines the client knowledge-base structure
- `hermes-business-skills` installs repeatable marketing workflows into Hermes

## The marketing department

The skills are organized into three roles. Each role owns a set of skills and hands off to the others:

```text
marketing-strategy-orchestrator (entry point — diagnoses channels, delegates)
        ↓ gates on: avatar + offer must exist
        ↓
┌─────────────────────────┬──────────────────────┬──────────────────────┐
│ marketing-agent         │ creative-director    │ media-buyer          │
│ (strategy + copy)       │ (visual production)  │ (paid media)         │
│                         │                      │                      │
│ avatar-builder          │ ad-creative-brief-   │ meta-ads-manager     │
│ attractive-character-   │   writer             │ meta-audience-       │
│   builder               │                      │   builder            │
│ offer-builder           │                      │ meta-creative-tester │
│ hook-angle-writer       │                      │ meta-ads-scaler      │
│ brand-voice-extractor   │                      │ campaign-optimizer   │
│ podcast-to-copy         │                      │ meta-lead-gen        │
│ nurture-email-writer    │                      │                      │
│ launch-email-writer     │                      │                      │
│ funnel-page-writer      │                      │                      │
│ funnel-copy-writer      │                      │                      │
│ vsl-writer              │                      │                      │
│ ad-script-writer        │                      │                      │
│ human-editor            │                      │                      │
└─────────────────────────┴──────────────────────┴──────────────────────┘
        ↓
human-editor (final pass on any copy output from marketing-agent)
```

### marketing-agent (14 skills)

The marketing strategist. Owns offer design, avatar research, brand voice, copywriting, content, and overall marketing orchestration. This is the entry point for any marketing engagement.

**Entry point:**

- `marketing-strategy-orchestrator`: the diagnostic and routing skill — decides which channels to use based on offer, avatar, price, margin, and business stage. Gates on prerequisites (avatar + offer must exist), then delegates to the execution skills. **Start here for any new marketing engagement.**

**Foundation skills:**

- `avatar-builder`: deep customer avatar research (interviews, reviews, market research, top-20% analysis)
- `attractive-character-builder`: brand persona, founder story, spokesperson identity
- `offer-builder`: value equation, grand slam offer, stack, guarantees, scarcity, MAGIC naming
- `hook-angle-writer`: hooks, headlines, and angles by desire, awareness, and channel
- `brand-voice-extractor`: brand voice guide, one-liner, StoryBrand clarity
- `human-editor`: finishing pass for clarity, human tone, and claim safety

**Copywriting and content skills:**

- `podcast-to-copy`: turn transcripts into hooks, descriptions, emails, and social copy
- `nurture-email-writer`: nurture sequences, soap opera sequence, retention/onboarding copy
- `launch-email-writer`: product launch sequences, PLC content, webinar structure
- `funnel-page-writer`: landing, opt-in, sales, and funnel pages (single page)
- `funnel-copy-writer`: full multi-page funnel copy orchestration — assembles the copy skills into one connected funnel
- `vsl-writer`: video sales letter scripts (long-form, VSL framework, hook → promise → proof → offer)
- `ad-script-writer`: video ad scripts (hook, pattern interrupt, social-proof, CTA)

### creative-director (1 skill)

The creative director. Owns visual direction, image-generation briefs, ad creative direction, and brand-aligned visual review. Takes the marketing strategy + hook + offer from the marketing-agent and turns it into a generation-ready visual brief.

- `ad-creative-brief-writer`: creative briefs for ad production (creative concept, format, aspect ratio by placement, visual concept, text overlay, caption, CTA, generation parameters, testing tag). Feeds image/video tools like Higgsfield, Nano Banana, OpenAI Images, local sd.cpp, or a human designer/editor.

### media-buyer (6 skills)

The media buyer. Owns paid media planning, ad account analysis, spend experiments, and campaign performance. Takes the creative assets and strategy from the other roles and deploys them inside ad platforms.

- `meta-ads-manager`: plan, structure, launch, or audit Meta ad campaigns (objective, CBO/ABO, budget, testing plan)
- `meta-audience-builder`: audience strategy (broad vs lookalike vs interest, retargeting sequences, exclusions)
- `meta-creative-tester`: creative testing design (test structure, variables, sprints, winner/kill criteria)
- `meta-ads-scaler`: scaling architecture (vertical/horizontal budget increases, scaling rules)
- `campaign-optimizer`: diagnose and optimize live campaigns (metrics, Learning Phase, frequency, kill/scale/wait)
- `meta-lead-gen`: Meta lead-gen form and qualification design (Instant Forms, qualification questions, funnel integration)

### How the roles connect

```text
marketing-agent (strategy + copy)
  │
  ├── hands off visual briefs → creative-director
  ├── hands off paid media execution → media-buyer
  └── final copy pass ← human-editor (marketing-agent owns this)
  
creative-director (visual production)
  │
  ├── receives strategy + hook + offer from marketing-agent
  ├── produces generation-ready briefs for image/video tools
  └── hands off campaign execution → media-buyer

media-buyer (paid media)
  │
  ├── receives creative assets + strategy from the other roles
  ├── deploys and manages campaigns inside ad platforms
  └── hands off creative refreshes → creative-director
      hands off copy changes → marketing-agent
```

Client-specific facts, avatars, characters, offers, and voice live in the client's LLM wiki under `businesses/<business-slug>/`. The skills are generic procedures. Build quality skills one by one.

## Quick start

Dry-run first:

```bash
python3 scripts/install_skills.py --pack marketing --dry-run
```

Install the full marketing department into the active Hermes profile:

```bash
python3 scripts/install_skills.py --pack marketing
```

Install a single role:

```bash
python3 scripts/install_skills.py --pack marketing-agent
python3 scripts/install_skills.py --pack creative-director
python3 scripts/install_skills.py --pack media-buyer
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
