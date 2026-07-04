---
name: funnel-page-writer
description: Use when writing or auditing landing pages, opt-in pages, sales pages, funnel sections, checkout pages, or webinar/VSL pages for a specific business, avatar, offer, and traffic source.
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, funnel, landing-page, sales-page, copywriting]
    related_skills: [avatar-builder, attractive-character-builder, offer-builder, hook-angle-writer, brand-voice-extractor, human-editor]
---

# Funnel Page Writer

## Overview

Write funnel pages that move one specific avatar toward one specific action. A funnel page is not a brochure. It is a focused sales asset with a job: opt in, buy, book, apply, register, watch, or continue to the next page.

Use `references/funnel-frameworks.md` for the concise framework reference.

This skill depends on other marketing skills. Use `avatar-builder` for customer depth, `offer-builder` for the offer, `hook-angle-writer` for headline options, `brand-voice-extractor` for voice, and `human-editor` for the final pass.

The discipline: clarity before cleverness. Every page should quickly answer: What is this? Is it for me? Why should I care? Why should I believe it? What do I do next?

## When to Use

Use this skill when the client asks for:

- landing page copy
- opt-in page copy
- lead magnet page copy
- sales page copy
- funnel page sections
- webinar registration page
- VSL page
- checkout page copy
- offer page copy
- page audit or wireframe
- StoryBrand-style page rewrite

Do not use this skill for:

- offer creation from scratch, use `offer-builder`
- avatar research from scratch, use `avatar-builder`
- full multi-page funnel copy orchestration, use `funnel-copy-writer`
- final human tone pass only, use `human-editor`
- legal, health, income, or compliance review
- building a full website with many unrelated pages

If offer, avatar, or CTA is unclear, stop and create or request those inputs first.

## Multi-Business Rule

A client can have several businesses and several funnels. Every page belongs to one business, one offer, and one traffic source.

Before writing, confirm:

- business or brand
- business slug
- offer
- primary avatar
- traffic temperature: cold, warm, or hot
- page type
- next action

Store page drafts under the correct business in the client wiki:

```text
businesses/<business-slug>/
├── offers/
├── avatars/
├── characters/
├── brand-voice.md
└── funnels/
    └── <funnel-slug>/
        ├── landing-page.md
        ├── opt-in-page.md
        ├── sales-page.md
        └── checkout-page.md
```

If the wiki uses another structure, follow it while keeping pages grouped by business and funnel.

## Required Inputs

Minimum useful inputs:

- business or brand
- page type
- target avatar
- offer or lead magnet
- next action / CTA
- traffic source or traffic temperature

Best inputs:

- avatar page
- attractive character page
- offer document
- brand voice guide
- proof/testimonials/approved claims
- customer language
- objections
- current page or competitor example
- funnel context: previous step and next step

Completion: you can explain the page's one job in one sentence.

## Core Workflow

### 1. Orient to the wiki

If working inside a client wiki, read:

- `SCHEMA.md`
- `index.md`
- recent `log.md`
- relevant business, avatar, character, offer, brand voice, proof, and funnel pages

Completion: the page context, source assets, and save path are known.

### 2. Define the page job

Classify the page:

- opt-in page
- lead magnet page
- webinar registration page
- sales page
- VSL page
- checkout page
- application page
- thank-you/next-step page

Then define:

- one primary CTA
- traffic temperature
- awareness level
- main promise
- main objection
- proof available

Completion: the page has one job and one primary CTA.

### 3. Choose the page framework

Pick the simplest framework that can do the job.

Use **Marketing Made Simple wireframe** when the page is simple or service-based:

1. Header
2. Stakes
3. Value proposition
4. Guide
5. Plan
6. Explanatory section
7. Optional video
8. Optional price/product choices
9. Footer

Use **StoryBrand SB7** when the page needs clarity:

1. Customer hero
2. Problem
3. Guide
4. Plan
5. CTA
6. Failure
7. Success

Use **long-form sales page** when the buyer needs more persuasion:

1. Hook
2. Problem
3. Stakes
4. Mechanism
5. Guide/character
6. Offer stack
7. Proof
8. Objections
9. Price framing
10. Guarantee
11. Urgency
12. CTA
13. PS

Completion: the page structure matches traffic temperature and offer complexity.

### 4. Build the headline and hook

Use `hook-angle-writer` thinking:

- call out the avatar
- name the problem or desire
- promise a clear result
- hint at a mechanism
- avoid hype that the offer cannot support

Create 5 to 10 headline options before choosing one.

Completion: the header passes the grunt test: what it is, how it helps, what to do next.

### 5. Write the page sections

For each section, write:

- section goal
- headline/subhead
- body copy
- proof or source used
- CTA if relevant

Keep copy practical and scannable. Use tables, bullets, and short sections when useful.

Completion: every section moves the reader toward the CTA or answers a buying question.

### 6. Add proof and risk handling

Use only sourced proof.

Proof can include:

- testimonials
- case studies
- founder credibility
- demonstrations
- screenshots
- process clarity
- mechanism explanation
- guarantees
- comparison to alternatives
- customer language

Flag:

- health claims
- income claims
- legal/financial claims
- credentials
- guarantees
- unsupported testimonials

Completion: every major claim is sourced, softened, or flagged.

### 7. Address objections

Map objections to sections:

| Objection | Page element |
|---|---|
| I do not understand it | mechanism / plan |
| I do not believe it works | proof |
| It will not work for me | avatar-specific examples |
| Too expensive | value stack / cost of inaction |
| Too much work | effort reduction |
| Too risky | guarantee / risk reversal |
| Not now | cost of delay / real urgency |

Completion: the top objections are answered before the CTA.

### 8. Write the CTA path

A page should make the next step obvious.

For each CTA, define:

- action verb
- destination
- what happens after click
- risk reducer
- urgency or reason why, if real

Completion: a reader never has to wonder what to do next.

### 9. Create the final page draft

Use this output shape:

```markdown
# Funnel Page: [Page Name]

## Scope
- Business:
- Funnel:
- Page type:
- Primary avatar:
- Offer:
- Traffic source / temperature:
- Primary CTA:
- Sources used:
- Confidence:

## Page Strategy
- One job:
- Main promise:
- Main objection:
- Framework used:

## Headline Options
1.
2.
3.

## Recommended Header
- Headline:
- Subheadline:
- CTA:

## Page Copy
[section-by-section copy]

## Proof and Claims
| Claim | Source | Risk |
|---|---|---|

## Open Questions / Needs Confirmation
- [unknowns]
```

Completion: the page can be passed to design or pasted into a builder.

### 10. Update the wiki

If working in an LLM wiki:

- save the page under the correct business/funnel
- link to avatar, offer, character, and proof pages
- update `index.md` if appropriate
- append to `log.md`
- run `qmd update` if configured

Completion: the page is stored, searchable, and reusable.

## Missing Information Handling

Use labels:

- `Missing avatar`
- `Missing offer`
- `Missing CTA`
- `Missing proof`
- `Missing traffic source`
- `Needs confirmation`
- `Risk flag`

If a page cannot be written honestly, produce a page brief and the highest-leverage questions instead.

## Quality Bar

A strong funnel page:

- has one avatar and one CTA
- makes the offer clear quickly
- uses the customer's language
- shows a believable mechanism
- proves claims or flags missing proof
- answers objections
- makes the next step obvious
- matches the brand voice
- avoids fake urgency and unsupported results

A weak funnel page:

- tries to serve everyone
- has no clear CTA
- starts with company bragging
- uses clever but unclear headlines
- hides the offer
- makes unsupported claims
- has generic benefits
- has no proof or objection handling

## Common Pitfalls

1. **Writing before the offer is clear.** Use `offer-builder` first.
2. **Starting with the brand story.** The customer is the hero. The brand is the guide.
3. **Using vague CTAs.** Replace "learn more" with the actual action.
4. **Overwriting customer language.** Keep strong phrases from avatar research.
5. **Inventing proof.** If proof is missing, mark it.
6. **Faking urgency.** Use only real deadlines or cost-of-delay framing.
7. **Making every page long.** Simple offers need simple pages.
8. **Skipping mobile readability.** Use short sections, clear headers, and direct copy.

## Verification Checklist

- [ ] Business, funnel, avatar, offer, and CTA confirmed
- [ ] Page type and traffic temperature identified
- [ ] Framework selected intentionally
- [ ] Header passes the grunt test
- [ ] Page has one primary CTA
- [ ] Offer links to a saved offer doc or clear source
- [ ] Proof and claims are sourced or flagged
- [ ] Main objections are answered
- [ ] Brand voice is followed
- [ ] Risky claims are softened or marked for review
- [ ] If wiki-backed, page is filed under the correct business/funnel and linked
