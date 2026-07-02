---
name: launch-email-writer
description: Use when planning or writing a launch email sequence or webinar-driven campaign for a business from its offer, avatar, and brand voice. Produces a full launch calendar and ready-to-send emails built on Product Launch Formula, prelaunch content, mental triggers, and the Perfect Webinar structure.
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, email, launch, webinar, campaign, conversion]
    related_skills: [offer-builder, hook-angle-writer, avatar-builder, attractive-character-builder, brand-voice-extractor, nurture-email-writer, funnel-page-writer, human-editor]
---

# Launch Email Writer

## Overview

Plan and write a launch: a time-bound campaign that builds anticipation, delivers value before the sale, opens the cart, sells hard while the cart is open, and closes with a real deadline. A launch is not a single email. It is a sequence with a story arc, a content phase that earns the sale, and a set of mental triggers layered across days.

This skill produces two things: a launch calendar or sequence plan, and the emails that fill it. It draws on the Product Launch Formula phases, the three prelaunch content pieces, the Sideways Sales Letter idea of selling gradually through content, the core mental triggers, and the Perfect Webinar structure when the launch runs through a webinar or live event. The framework detail lives in `references/launch-frameworks.md`; this file is the operating process.

This skill is a writer and sequencer, not a strategy source. It pulls the real inputs from the client wiki: the offer (built with `offer-builder`), the avatar, the attractive character, and the brand voice. It uses `hook-angle-writer` for subject lines and email openers. It does not invent the offer, the proof, the deadline, or the scarcity.

The core discipline: the deadline and the scarcity must be real, the value in the prelaunch must be genuine, and every claim must be one the offer can deliver. A launch that fakes urgency wins one cart and loses the list.

## When to Use

Use this skill when the client asks for:

- a full launch email sequence for a product, course, program, cohort, or service
- a prelaunch content campaign that warms a list before the cart opens
- open-cart, mid-cart, and close-cart emails
- a webinar or live-event launch sequence, including registration, show-up, and replay emails
- a launch calendar mapping emails to dates and phases
- a relaunch or evergreen launch adaptation of a past campaign

Do not use this skill for:

- defining or structuring the offer itself, use `offer-builder`
- ongoing nurture, welcome, or retention sequences with no cart event, use `nurture-email-writer`
- the sales page or webinar registration page copy, use `funnel-page-writer`
- customer research or the avatar, use `avatar-builder`
- the attractive character or brand voice, use `attractive-character-builder` and `brand-voice-extractor`
- final line-level polish, use `human-editor`
- inventing deadlines, scarcity, proof, results, or testimonials

## Multi-Business Rule

A client can run several businesses, and each business can run many launches. Never blend launch facts, offers, deadlines, or proof across businesses. Before planning or writing, confirm the business, business slug, the offer being launched, the primary avatar, the launch type, and the real cart-open and cart-close dates.

Store launch work inside the client wiki under the correct business:

```text
businesses/<business-slug>/
├── brand.md
├── products.md
├── avatars/
├── characters/
├── offers/
│   └── <offer-slug>.md
└── emails/
    └── launches/
        └── <launch-slug>.md
```

If the wiki uses a different structure, follow it while keeping every launch grouped by business and offer. Link the launch to the offer, avatar, character, brand voice, and any funnel pages it drives.

## Source Hierarchy

Orient from the client wiki first. Read `SCHEMA.md`, `index.md`, recent `log.md`, and the target business pages before claiming facts. Then prioritize:

1. The offer document: dream outcome, mechanism, stack, bonuses, guarantee, price, and the real scarcity and urgency.
2. The avatar and top customer insights: desires, pains, objections, awareness level, and the words they use.
3. The attractive character and brand voice: story, enemy, signature phrases, taboo words, and tone.
4. Existing assets: past launch emails, sales page, webinar deck, prelaunch content, and prior open and close rates.
5. Real launch logistics: cart-open date, cart-close date, price change or bonus deadlines, webinar dates, and replay windows.
6. Agent inference for structure, sequencing, and wording only, never for facts, proof, scarcity, or claims.

Completion: the offer, avatar, character, voice, launch type, and real dates are known or marked unknown.

## Required Inputs

Minimum useful inputs:

- the business or brand and the offer being launched
- the primary avatar
- the launch type (list-only, webinar, live event, challenge, or evergreen)
- the real cart-open and cart-close dates
- the real scarcity and urgency from the offer
- available proof or an explicit note that proof is missing

Best inputs:

- a completed offer document, avatar profile, attractive character, and brand voice guide
- a hook bank or subject-line options from `hook-angle-writer`
- prior launch results and email performance
- testimonials, case studies, and approved claims
- webinar or event dates, replay window, and any fast-action bonus deadlines

Completion: there is enough source material to sequence the launch and write the emails without inventing facts.

## Core Workflow

### 1. Confirm launch scope

Capture business, business slug, offer, offer slug, primary avatar, launch type, list size and warmth, cart-open date, cart-close date, any interim deadlines (price step, fast-action bonus, webinar date, replay end), price, and confidence. Confirm every date and deadline is real.

Completion: the launch is tied to one business, one offer, one avatar, and a real timeline.

### 2. Map the launch phases

Lay the campaign onto the Product Launch Formula phases. Assign real dates to each:

- **Pre-prelaunch:** signal that something is coming, take the audience's temperature, and surface objections early.
- **Prelaunch:** deliver the three content pieces that teach, shift beliefs, and build desire before any cart is open. This is where the Sideways Sales Letter happens: you sell gradually through valuable content rather than one long pitch.
- **Open cart:** announce the cart is open, make the full offer, and drive the first wave of sales.
- **Cart open and mid-launch:** handle objections, add proof, answer questions, and use interim deadlines. This is the bulk of the emails.
- **Close cart:** use the real final deadline to drive the last and usually largest wave of sales.
- **Post-launch:** onboard buyers, follow up with non-buyers honestly, and capture lessons.

Completion: every phase has dates and a purpose, and the timeline matches the real cart window.

### 3. Plan the prelaunch content (PLC 1, 2, 3)

If the launch uses prelaunch content, plan the three pieces:

- **PLC 1, opportunity and transformation:** show what is possible and why it matters now. Answer "why should I care."
- **PLC 2, transformation and education:** teach something genuinely useful and show the change is achievable. Answer "how does this work."
- **PLC 3, ownership experience:** show what it is like to have the result, introduce the offer's shape, and set up the cart open. Answer "what do I do next."

Each piece delivers real value on its own, addresses objections, and moves the audience one belief closer to buying. Map which mental triggers each piece carries.

Completion: each prelaunch piece has a job, a value payload, the objections it handles, and its email support.

### 4. Choose the webinar structure if used

If the launch runs through a webinar or live training, structure it with the Perfect Webinar shape:

- **Introduction and hook:** promise the big outcome and set the one thing they will learn.
- **The one big idea and origin story:** establish the new opportunity and the attractive character's credibility.
- **Three secrets:** break the three false beliefs that block the sale, one at a time, about the vehicle, about themselves, and about external obstacles.
- **The stack and close:** present the offer as a stack of value, anchor the price, add the guarantee and real scarcity, and use the close sequence.

Plan the email support around it: registration emails, show-up and reminder emails, a live or "doors open" email, and replay emails with a real replay deadline. Belief-breaking and stack detail live in `references/launch-frameworks.md`.

Completion: the webinar arc and its email support are mapped, or this step is marked not applicable.

### 5. Assign mental triggers across the timeline

Layer the mental triggers deliberately so no single email carries all the weight. Use only triggers that are true:

- **Authority:** the character's credentials, results, and expertise.
- **Reciprocity:** the genuine value given in prelaunch earns attention at open cart.
- **Community and belonging:** the identity and group the buyer joins.
- **Anticipation:** building toward a known date, the strongest launch trigger.
- **Social proof:** real testimonials, numbers, and buyer activity.
- **Scarcity:** real limits on seats, bonuses, or price.
- **Likability and story:** the character's relatable story and shared values.
- **Event and ritual:** the launch as a shared, time-bound moment.

Map which trigger leads each email so the sequence builds rather than repeats.

Completion: each email has a lead trigger, and anticipation and scarcity are used honestly.

### 6. Write the email sequence

Write each email to the brand voice and the character's story. Use `hook-angle-writer` for subject lines and openers. For each email capture:

- phase and date
- lead mental trigger
- subject line options (from the hook bank)
- goal (teach, build belief, open cart, handle objection, add proof, deadline push)
- the one call to action
- the objection it removes or the belief it shifts

A typical list launch runs roughly: 3 to 5 prelaunch emails, an open-cart email, 4 to 8 mid-cart emails (proof, objections, FAQ, bonus deadline), and 2 to 4 close-cart emails on the final day. Close-cart days usually carry the most emails because the real deadline does the work. Adapt counts to list warmth and launch length.

Completion: every planned email is drafted with subject options, one call to action, and a clear job.

### 7. Handle the close and post-launch

Write the final-day sequence around the real deadline: last-chance, a few hours left, and cart-closing emails. State the true consequence of missing it (price, bonus, cohort start, closed doors), never a fake one. Then plan post-launch: buyer onboarding handoff to `nurture-email-writer`, an honest non-buyer follow-up, and a lessons-learned note for the wiki.

Completion: the close uses only the real deadline and the post-launch handoff is defined.

### 8. Assemble the launch document

Use this output shape:

```markdown
# Launch: [Offer Name] for [Avatar]

## Scope
- Business:
- Business slug:
- Offer + offer slug:
- Primary avatar:
- Launch type: list / webinar / live event / challenge / evergreen
- Cart open date:
- Cart close date:
- Interim deadlines:
- Price / payment options:
- Confidence:
- Sources used:

## Launch Calendar
| Date | Phase | Email | Lead trigger | Goal | CTA |
|---|---|---|---|---|---|

## Prelaunch Content Plan
- PLC 1 (opportunity):
- PLC 2 (transformation/education):
- PLC 3 (ownership + cart open):

## Webinar Structure (if used)
- Hook / big idea:
- Origin story:
- Three secrets (false beliefs broken):
- Stack + close:
- Email support (registration, show-up, live, replay):

## Emails
### [# - Phase - Date]
- Subject options:
- Lead trigger:
- Goal:
- Body:
- CTA:
- Objection/belief handled:

## Post-Launch
- Buyer onboarding handoff:
- Non-buyer follow-up:
- Lessons learned:

## Needs Confirmation
- [unknown facts, unverified proof, dates or scarcity to confirm, risky claims]
```

Completion: the document can be handed to send without the reader reconstructing the launch strategy.

### 9. Update the wiki when appropriate

If working inside an LLM wiki, save the launch under `businesses/<business-slug>/emails/launches/<launch-slug>.md`, link it to the offer, avatar, character, and any funnel pages, update `index.md` if appropriate, append to `log.md`, and run `qmd update` if the wiki uses QMD.

Completion: the launch is filed under the correct business and offer and reusable by other skills.

## Missing Information Handling

Do not invent missing facts. Use these labels:

- `Unknown`: no source material supports the answer
- `Needs confirmation`: likely but not verified
- `Client to provide`: requires offer, proof, results, or logistics only the client can give
- `Risk flag`: health, income, legal, financial, credential, guarantee, or regulated claim needing review
- `Out of scope`: a promise or urgency the business cannot honestly make

If the offer is missing, stop and route to `offer-builder` first. A launch without a real offer, real proof, and a real deadline is empty pressure. When inputs are thin, draft what can be supported and ask the highest-leverage questions in this order: offer, real deadline, real scarcity, proof, avatar objections, launch type, and brand voice.

## Quality Bar

A strong launch has:

- one business, one offer, one primary avatar, and a real timeline
- prelaunch content that delivers genuine value before any pitch
- a clear phase arc from anticipation to a real deadline
- mental triggers layered honestly across the sequence, not stacked into one email
- real scarcity and a real close-cart deadline
- proof, objections, and beliefs handled in the middle of the launch
- brand voice and the attractive character's story throughout
- one clear call to action per email
- risky claims and unknowns flagged
- correct storage under the client wiki business when applicable

A weak launch has fake deadlines, a prelaunch that only teases, one long pitch instead of a value arc, every email shouting scarcity, unsupported proof, no objection handling, multiple competing calls to action, or one sequence trying to serve several offers at once.

## Common Pitfalls

1. **Faking the deadline or scarcity.** If the limit is not real, do not use it. Completion: every deadline and scarcity element is documented as real or removed.
2. **Prelaunch with no real value.** Teasing without teaching burns goodwill. Completion: each prelaunch piece delivers a usable takeaway.
3. **Selling too soon.** The Sideways Sales Letter sells through content over time; do not open the cart in email one. Completion: the cart opens only after the prelaunch earns it.
4. **Under-emailing the close.** The final day drives the largest wave; too few emails leaves sales on the table. Completion: the close-cart day has a real deadline-driven sequence.
5. **One email carrying every trigger.** Layer triggers across the timeline. Completion: each email has a single lead trigger.
6. **Multiple calls to action.** One email, one action. Completion: every email has one CTA.
7. **Losing the character and voice.** Use the brand's story and signature phrases, not generic launch templates. Completion: emails match the brand voice guide.
8. **Ignoring regulated claims.** Health, income, legal, financial, and credential claims need review. Completion: risky claims are flagged.

## Verification Checklist

- [ ] Client wiki orientation completed when a wiki is available
- [ ] Business, business slug, offer, and avatar confirmed
- [ ] Launch stored or prepared for storage under `businesses/<business-slug>/emails/launches/`
- [ ] Cart-open, cart-close, and interim deadlines confirmed as real
- [ ] Offer, avatar, character, and brand voice pulled from the wiki, not invented
- [ ] Launch phases mapped with real dates
- [ ] Prelaunch content (PLC 1, 2, 3) planned with real value when used
- [ ] Webinar structure and email support mapped when used, or marked not applicable
- [ ] Mental triggers layered across the timeline, each email with one lead trigger
- [ ] Scarcity and the close-cart deadline are real and honestly stated
- [ ] Each email has subject options, one CTA, and a clear job
- [ ] Proof, objections, and beliefs handled in the mid-launch emails
- [ ] Post-launch buyer and non-buyer follow-up defined
- [ ] Risky claims (health, income, financial, legal) flagged
- [ ] Confidence level and source list included
- [ ] Final output follows the launch document shape
