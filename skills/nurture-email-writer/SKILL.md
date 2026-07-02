---
name: nurture-email-writer
description: Use when writing a nurture, welcome, indoctrination, onboarding, retention, or ongoing value email sequence for a specific business and avatar. Produces a structured email sequence document with subject lines, bodies, story beats, soft offers, and calls to action, pulled from the client wiki.
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, email, nurture, retention, onboarding, copywriting]
    related_skills: [avatar-builder, attractive-character-builder, offer-builder, brand-voice-extractor, hook-angle-writer, launch-email-writer, human-editor]
---

# Nurture Email Writer

## Overview

Write nurture email sequences that build a relationship, earn attention, and move one avatar toward one offer without hard selling. Nurture email is the connective tissue between a first opt-in and a buying decision, and between a first purchase and long-term retention. It works through story, value, belief-shifting, and consistent contact rather than pressure.

Use `references/nurture-frameworks.md` for the framework reference. This skill is the operating process for turning avatar research, the attractive character, the offer, and the brand voice into a ready-to-send sequence document stored in the client wiki.

The discipline: give before you ask, tell the truth, and let the reader feel known. A strong nurture sequence makes the reader think, "This person understands my situation, I look forward to hearing from them, and buying from them feels like the obvious next step." It does not fabricate stories, fake results, invent urgency, or bury the reader in daily noise with no value.

## When to Use

Use this skill when the client asks for:

- a welcome, indoctrination, or new-subscriber sequence after an opt-in
- a soap opera style story sequence that warms a cold list toward an offer
- an ongoing weekly value or daily email cadence
- a post-purchase onboarding sequence that drives activation
- a retention, re-engagement, or win-back sequence for existing customers or members
- a lead-magnet follow-up that bridges to a paid offer

Do not use this skill for:

- time-boxed promotional launches with open and close carts, use `launch-email-writer`
- building the offer itself, use `offer-builder`
- avatar research from scratch, use `avatar-builder`
- the attractive character profile, use `attractive-character-builder`
- brand voice extraction, use `brand-voice-extractor`
- subject-line-only or hook-only batches, use `hook-angle-writer`
- final copy polish, use `human-editor`
- inventing stories, testimonials, results, or scarcity

## Multi-Business Rule

A client can run several businesses, and each business can have several sequences. Never blend voice, stories, avatars, or offers across businesses. Before writing or saving a sequence, confirm the business, business slug, target avatar, attractive character, offer being nurtured toward, sequence type, and cadence.

Store nurture work inside the client wiki under the correct business:

```text
businesses/<business-slug>/
├── brand.md
├── products.md
├── avatars/
├── characters/
├── offers/
└── emails/
    └── nurture/
        └── <sequence-slug>.md
```

If the wiki uses a different structure, follow it while keeping every sequence grouped by business. Link the sequence to the relevant avatar, character, offer, and voice pages.

## Source Hierarchy

Orient from the client wiki first. Read `SCHEMA.md`, `index.md`, recent `log.md`, and the target business pages before writing. Then prioritize:

1. Direct client facts: real stories, real results, product details, onboarding steps, activation events, support and churn insight, and approved claims.
2. Avatar pages: desires, pains, objections, awareness level, and the exact language the avatar uses.
3. Attractive character page: backstory, parables, flaws, polarizing beliefs, and character type.
4. Offer pages: the offer this sequence points toward, its mechanism, proof, and objections.
5. Brand voice page: common phrases, taboo phrases, tone, rhythm, enemy language, and CTA style.
6. Existing emails, sales pages, and content, only as background.
7. Agent inference for structure, sequencing, and wording only, never for facts, stories, proof, or scarcity.

Completion: the business, avatar, character, offer, voice, sequence type, and save path are known or marked unknown.

## Required Inputs

Minimum useful inputs:

- business or brand and target avatar
- sequence type: welcome, soap opera, ongoing value, daily, onboarding, retention, or win-back
- the offer or next step the sequence should point toward
- at least one real story, moment, or proof point, or an explicit note that stories are missing

Best inputs:

- avatar profile, attractive character profile, offer document, and brand voice guide from the wiki
- real founder or customer stories, origin story, and turning points
- activation event and onboarding steps for post-purchase sequences
- objections, faqs, and reasons customers churn
- desired cadence, list temperature, and platform constraints

Completion: there is enough source material to write the sequence without inventing stories, proof, or scarcity.

## Core Workflow

### 1. Define sequence scope

Capture business, business slug, sequence type, target avatar, attractive character, offer or next step, list temperature (cold, warm, hot), cadence, number of emails, and confidence.

Match type to goal:

- **Welcome / indoctrination:** introduce the character, set expectations, and shift core beliefs for new subscribers.
- **Soap opera:** a short story-driven arc that warms a list and bridges to an offer.
- **Ongoing value:** a repeatable weekly rhythm that keeps the list engaged with useful, entertaining, or story-led emails.
- **Daily:** high-frequency, story-first emails that entertain and consistently point to one offer.
- **Onboarding:** drive a new buyer to the activation point and first win.
- **Retention / win-back:** reduce churn, re-engage quiet subscribers, or recover lapsed customers.

Completion: the sequence is tied to one business, one avatar, one character, one offer or next step, and one cadence.

### 2. Pull the four foundations from the wiki

Before writing a single line, gather from the wiki:

- **Avatar:** top desires, pains, objections, awareness level, and real language.
- **Attractive character:** character type, backstory, parables, flaws, and polarizing beliefs.
- **Offer:** the mechanism, proof, and objections the sequence must set up.
- **Voice:** phrases to use, phrases to avoid, tone, rhythm, and CTA style.

If any foundation is missing, mark it and either request it or draft with clearly labeled placeholders. Do not invent an avatar, character, or offer to fill the gap.

Completion: each of the four foundations is loaded from the wiki or explicitly marked as missing.

### 3. Plan the arc

Map the emails before writing bodies. For each email capture: position, goal, story or value beat, belief to shift, and call to action.

Use the framework that fits the type:

- For story-driven warm-up, use the five-part soap opera arc: set the stage, open a high-drama moment, share the epiphany, reveal the hidden benefits, then invite the reader to act with urgency that is real.
- For welcome sequences, sequence belief shifts: who the character is, why this problem matters, why the usual approach fails, why this mechanism works, and what to do next.
- For ongoing and daily cadence, lead with a story, hook, or observation, then bridge to one lesson and one soft call to action.
- For onboarding, sequence the buyer toward the activation point, then to first win, then to the next milestone.
- For retention and win-back, celebrate progress, reduce overwhelm, remind them why they started, and point to the next milestone.

Completion: every email has a position, a single goal, a beat, a belief to shift, and one primary call to action.

### 4. Draft subject lines and open loops

For each email draft two to three subject line options plus a preview line. Favor curiosity, specificity, story, and the avatar's own language over hype. Where a sequence benefits from continuity, open a loop in one email and close it in the next. If subject lines need a dedicated batch, hand off to `hook-angle-writer`.

Completion: each email has subject options and a preview line in the brand voice.

### 5. Write the bodies

Write each body in the attractive character's voice using the brand voice rules. Keep to one idea per email. Lead with the story or hook, deliver the value or belief shift, then make one clear call to action. Use short sentences, simple words, and specific detail from real source material.

Rules for every email:

- one primary goal and one primary call to action
- real stories only, drawn from the character or customer source
- proof and claims must be supported and traceable to the wiki
- match awareness level: teach more for colder readers, push less for hotter readers
- honest urgency only, or cost-of-delay framing when there is no real deadline
- flag any health, income, legal, financial, or credential claim for review

Completion: every email is on voice, single-goal, and free of invented facts.

### 6. Set cadence and calls to action

Recommend send timing and spacing for the sequence, and define the call to action ladder from soft (read, reply, watch) to direct (book, buy, join). Do not ask for the sale in every email of a value sequence, and do not stay soft forever in a sequence meant to convert.

Completion: cadence and a call to action ladder are documented.

### 7. Assemble the structured sequence document

Use this output shape:

```markdown
# Nurture Sequence: [Sequence Name]

## Scope
- Business:
- Business slug:
- Sequence type: welcome / soap opera / ongoing value / daily / onboarding / retention / win-back
- Primary avatar:
- Attractive character:
- Offer or next step:
- List temperature: cold / warm / hot
- Cadence:
- Number of emails:
- Confidence:
- Sources used:

## Foundations Pulled From Wiki
- Avatar page:
- Character page:
- Offer page:
- Voice page:
- Missing foundations:

## Sequence Arc
| # | Goal | Story / value beat | Belief to shift | Primary CTA |
|---|---|---|---|---|

## Emails
### Email 1 - [Working title]
- Subject options:
- Preview line:
- Goal:
- Body:
- CTA:
- Open loop opened / closed:
- Claims needing review:

(repeat for each email)

## Cadence and CTA Ladder
- Send timing:
- CTA progression:

## Needs Confirmation
- [missing stories, unverified proof, risky claims, or offer details]
```

Completion: the document can be handed to editing or scheduling without reconstructing the strategy.

### 8. Update the wiki when appropriate

If working inside an LLM wiki, save the final sequence under `businesses/<business-slug>/emails/nurture/<sequence-slug>.md`, link it to the avatar, character, offer, and voice pages, update `index.md` if appropriate, append to `log.md`, and run `qmd update` if the wiki uses QMD.

Completion: the sequence is filed under the correct business and reusable by other skills.

## Missing Information Handling

Do not invent missing facts. Use these labels:

- `Unknown`: no source material supports the answer
- `Needs confirmation`: likely but not verified
- `Client to provide`: requires a real story, proof, onboarding detail, or offer information
- `Risk flag`: health, income, legal, financial, credential, or regulated claim needing review
- `Out of scope`: a promise or claim the business cannot currently support

When source is thin, draft what can be supported and ask the highest-leverage questions in this order: avatar, offer, at least one real story, activation event for onboarding, proof, cadence, and brand voice.

## Quality Bar

A strong nurture sequence has:

- one business, one avatar, one character, and one clear next step
- an arc that is planned before the bodies are written
- subject lines built on curiosity and real language, not hype
- one goal and one primary call to action per email
- real stories in the attractive character's voice
- belief shifts matched to the avatar's awareness level
- honest urgency, or cost-of-delay framing when no deadline exists
- onboarding emails aimed at the activation point and first win
- retention emails that celebrate progress and point to the next milestone
- risky claims and unknowns flagged
- correct storage under the client wiki business when applicable

A weak sequence has invented stories, unsupported proof, fake scarcity, hype subject lines, several goals per email, a hard sell in every message, generic voice that ignores the character, or one sequence trying to serve several businesses or avatars at once.

## Common Pitfalls

1. **Writing bodies before the arc.** Plan positions and goals first. Completion: the arc table exists before any body.
2. **Inventing stories.** Every story must come from the character or customer source. Completion: each story traces to the wiki.
3. **Selling in every email.** Value sequences earn the ask. Completion: the CTA ladder moves from soft to direct.
4. **Ignoring the character voice.** The sequence should sound like one real person. Completion: voice rules from the wiki are applied.
5. **Mismatching awareness level.** Cold readers need belief shifts; hot readers need less teaching. Completion: teaching depth matches temperature.
6. **Faking urgency.** Use real deadlines or cost-of-delay framing. Completion: urgency is documented or removed.
7. **Overwhelming new buyers.** Onboarding should reduce overwhelm and drive one activation. Completion: onboarding points to a single next action.
8. **Ignoring regulated claims.** Health, income, legal, financial, and credential claims need review. Completion: risky claims are flagged.

## Verification Checklist

- [ ] Client wiki orientation completed when a wiki is available
- [ ] Business, business slug, avatar, character, and sequence type confirmed
- [ ] Avatar, character, offer, and voice foundations pulled or marked missing
- [ ] Sequence stored or prepared for storage under `businesses/<business-slug>/emails/nurture/`
- [ ] Sequence arc planned before bodies were written
- [ ] Each email has subject options, a preview line, one goal, and one primary CTA
- [ ] Stories, proof, and claims trace to real source material
- [ ] Belief shifts and teaching depth match the avatar's awareness level
- [ ] Onboarding emails drive toward the activation point and first win
- [ ] Retention emails celebrate progress and point to the next milestone
- [ ] Urgency is honest or replaced with cost-of-delay framing
- [ ] Cadence and CTA ladder are documented
- [ ] Unknowns, risky claims, and compliance needs are flagged
- [ ] Final output follows the structured sequence document shape
