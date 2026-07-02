---
name: human-editor
description: Use when polishing client-facing marketing copy after strategy, avatar, offer, and voice are already defined. Tightens clarity, rhythm, human tone, CTA strength, and claim safety without inventing new strategy.
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, editing, humanizer, copywriting, voice]
    related_skills: [avatar-builder, attractive-character-builder, brand-voice-extractor, offer-builder, hook-angle-writer]
---

# Human Editor

## Overview

Edit marketing copy so it sounds like a real person, not a generic AI draft. This is a finishing-pass skill, not a strategy skill.

Use the reference checklist in `references/editing-rules.md` when a deeper pass is needed.

The core rule: preserve the meaning, offer, avatar, and character voice while making the copy clearer, more direct, more believable, and safer to publish.

A human edit should make copy easier to read and harder to ignore. It should not flatten every brand into the same polished voice.

## When to Use

Use this skill when the client asks to:

- make copy sound more human
- remove AI tone
- simplify or tighten a draft
- edit emails, landing pages, hooks, social posts, funnel copy, or podcast descriptions
- make copy clearer, punchier, or more direct
- preserve a specific brand or attractive character voice
- flag risky health, income, legal, credential, or proof claims

Do not use this skill for:

- building a customer avatar from scratch
- creating an offer from scratch
- writing a full funnel or email sequence from nothing
- inventing proof, testimonials, credentials, or claims
- changing the strategy without saying so

If the draft is strategically broken, diagnose the problem instead of pretending editing can fix it.

## Multi-Business Rule

A client can run several businesses or brands. Every edit belongs to a specific business context.

Before editing, confirm or infer:

- business or brand
- target avatar
- attractive character or voice
- offer or product
- channel, for example email, funnel, ad, podcast, social, SMS

Do not mix voice, claims, or facts from another business.

If working inside a client wiki, read the relevant business pages first:

```text
businesses/<business-slug>/brand.md
businesses/<business-slug>/brand-voice.md
businesses/<business-slug>/avatars/<avatar-slug>.md
businesses/<business-slug>/characters/<character-slug>.md
businesses/<business-slug>/offers/<offer-slug>.md
```

If the wiki uses another structure, follow the existing structure.

## Editing Modes

### Light edit

Use when the structure is mostly good.

Do:

- fix grammar and flow
- shorten long sentences
- remove filler
- clarify confusing phrasing
- keep the original structure

Completion: the draft reads cleaner without changing the argument.

### Strong edit

Use when the draft has the right idea but weak execution.

Do:

- rewrite for punch and rhythm
- make the hook stronger
- sharpen the CTA
- cut generic sections
- preserve the intended meaning
- preserve the brand voice

Completion: the copy feels publishable and still says what the original meant to say.

### Diagnostic edit

Use when the draft has structural or proof problems.

Do:

- list the top issues first
- separate strategy issues from wording issues
- flag missing avatar, offer, proof, or CTA
- rewrite only the sections that can be fixed safely

Completion: the user knows what needs strategy work versus copy polish.

## Core Workflow

### 1. Orient to source context

If working in a client wiki, read:

- `SCHEMA.md`
- `index.md`
- recent `log.md`
- relevant business, avatar, character, offer, and brand voice pages

If no wiki is available, ask for or infer the minimum context from the draft.

Completion: you know who the copy is for, who is speaking, what is being sold, and where the copy will appear.

### 2. Identify the job of the copy

Classify the draft before editing:

- hook
- ad
- email
- nurture email
- sales email
- funnel section
- landing page
- podcast description
- social post
- SMS
- long-form sales copy

Then identify the desired action:

- click
- reply
- book call
- buy
- download
- watch
- read next email
- trust the character
- understand the mechanism

Completion: the edit has one clear success criterion.

### 3. Run the claim safety pass

Flag or soften risky claims before polishing.

Risk categories:

- health, supplement, disease, medical claims
- income, ROI, financial outcome claims
- legal or tax claims
- credentials and awards
- testimonials and specific results
- guarantees
- comparative claims against competitors

Use labels:

- `Safe`: supported or low risk
- `Needs proof`: claim may be true but no source is present
- `Risk flag`: legal, health, income, or credential issue
- `Soften`: rewrite with safer wording
- `Remove`: too risky or unsupported

Completion: no risky claim is made stronger by the edit.

### 4. Preserve the voice

Before rewriting, identify the voice traits.

Look for:

- sentence length
- rough vs polished tone
- direct vs warm tone
- humor
- signature phrases
- enemy language
- belief language
- spiritual, scientific, tactical, or rebellious flavor
- words the speaker would never use

Completion: the edited copy sounds like the intended brand or character, not a generic internet copywriter.

### 5. Simplify the language

Apply the clarity rules:

- use short familiar words
- split long sentences
- one idea per sentence when possible
- replace passive voice with active voice
- remove filler words
- remove redundant phrases
- remove corporate abstractions
- replace vague claims with concrete claims when sourced

Completion: the copy is easier to read out loud.

### 6. Strengthen the structure

A strong marketing draft usually has:

1. Hook
2. Problem or desire
3. Stakes
4. Insight or mechanism
5. Proof or credibility
6. Offer or next step
7. CTA

Do not force every small post into this full structure, but notice what is missing.

Completion: the reader understands why this matters and what to do next.

### 7. Make the CTA direct

Replace vague CTAs with clear action.

Weak:

- Learn more
- Check this out
- Get started today if interested

Stronger:

- Book the call
- Download the guide
- Reply with "soil"
- Watch the episode
- Order the starter kit

Completion: the reader knows exactly what action to take.

### 8. Return the edit in a useful format

For short drafts, return:

```markdown
## Edited Version
[copy]

## What Changed
- [short bullets]

## Flags
- [proof/risk/unknowns]
```

For long drafts, return section-by-section edits and avoid burying the user in a giant rewrite unless asked.

Completion: the user can copy/paste the edited version and see what was changed.

## Missing Information Handling

Do not invent missing strategy.

Use:

- `Missing avatar`: target buyer unclear
- `Missing offer`: unclear what is being sold
- `Missing CTA`: no action requested
- `Missing proof`: claim needs support
- `Missing voice`: no brand or character reference
- `Needs legal/medical review`: risk area

If enough is missing that an edit would be fake, say so and ask for the smallest missing input.

## Quality Bar

A strong human edit:

- sounds natural out loud
- preserves the intended meaning
- preserves the avatar and character voice
- cuts filler and generic AI phrasing
- strengthens the hook or opening
- clarifies the offer or next step
- keeps proof and claims honest
- improves rhythm and readability
- does not over-polish rough voices

A weak edit:

- makes every voice sound the same
- adds fake certainty
- invents proof
- removes useful specificity
- uses corporate filler
- makes CTAs softer
- ignores risk claims
- changes strategy without saying so

## Common Pitfalls

1. **Editing before understanding the voice.** Read the brand voice or character page first when available.
2. **Making rough voices too polished.** Some characters should sound blunt, blue-collar, rebellious, or imperfect.
3. **Turning copy into corporate filler.** Clear does not mean bland.
4. **Strengthening unsupported claims.** Never make a risky claim more absolute without proof.
5. **Fixing grammar but missing conversion.** A grammatically correct weak CTA is still weak copy.
6. **Overwriting the customer's language.** Keep exact customer phrases when they are strong.
7. **Adding strategy from nowhere.** If offer, avatar, or proof is missing, flag it.
8. **Editing too much.** If the draft is already good, make the lightest useful changes.

## Verification Checklist

- [ ] Business, avatar, voice, offer, and channel are known or explicitly marked missing
- [ ] The draft's job and CTA are clear
- [ ] Risky claims are flagged or softened
- [ ] Exact customer language is preserved where useful
- [ ] Character or brand voice is preserved
- [ ] Filler and generic AI phrasing are removed
- [ ] Sentences are easier to read out loud
- [ ] CTA is direct
- [ ] The edit does not invent proof or strategy
- [ ] Output includes edited version, changes, and flags when useful
