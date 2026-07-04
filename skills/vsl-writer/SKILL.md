---
name: vsl-writer
description: Use when writing or auditing a Video Sales Letter (VSL) script for a specific business, avatar, and offer. Produces a complete, time-stamped VSL script from opening hook to final CTA, with section-by-section structure, on-camera direction, and B-roll guidance. Covers B2B/SaaS, ecommerce, and info-product VSLs.
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, vsl, video-sales-letter, copywriting, conversion, script]
    related_skills: [avatar-builder, attractive-character-builder, offer-builder, hook-angle-writer, brand-voice-extractor, funnel-page-writer, human-editor, ad-script-writer]
---

# VSL Writer

## Overview

Write a complete Video Sales Letter: a scripted, on-camera video presentation that takes one specific avatar from cold attention to a buying decision. A VSL is not a landing page read aloud. It is a distinct persuasion format built on the Sideways Sales Letter principle — selling gradually through value, story, and structured belief shifts rather than a single pitch.

This skill produces a full, time-stamped script ready to record or hand to a voiceover. Use `references/vsl-frameworks.md` for the detailed framework reference (section anatomy, hook patterns, story arcs, offer reveal psychology, industry variants). This file is the operating process.

The core discipline: every section must earn the next section. A VSL that front-loads hype loses the viewer before the offer reveal. A VSL that hides the offer too long loses the buyer who was ready at minute three. Structure creates the tension that holds attention through the sale.

## When to Use

Use this skill when the client asks for:

- a full VSL script for a product, course, service, SaaS, or ecommerce offer
- a webinar-style video script (registration-to-sale flow)
- a video ad script longer than 60 seconds with an offer reveal
- an audit or rewrite of an existing VSL that is not converting
- a long-form video sales presentation for a launch, evergreen funnel, or paid traffic
- a speaker-ready script with on-camera direction and B-roll notes

Do not use this skill for:

- short video ads (under 60s) with no offer reveal — use `ad-script-writer`
- a landing page or sales page — use `funnel-page-writer`
- building the offer itself — use `offer-builder`
- avatar research — use `avatar-builder`
- brand voice extraction — use `brand-voice-extractor`
- final copy polish after the script is drafted — use `human-editor`
- inventing proof, testimonials, results, or claims the offer cannot support

## Multi-Business Rule

A client can run several businesses, and each business can have many VSLs. Never blend VSL facts, offers, avatars, or proof across businesses. Before writing, confirm the business, business slug, primary avatar, offer, and traffic temperature.

Store VSL work inside the client wiki under the correct business:

```text
businesses/<business-slug>/
├── brand.md
├── brand-voice.md
├── products.md
├── offers/
│   └── <offer-slug>.md
├── avatars/
│   └── <avatar-slug>.md
└── vsls/
    └── <vsl-slug>.md
```

If the wiki uses another structure, follow it while keeping every VSL grouped by business and linked to its offer, avatar, and character.

## Source Hierarchy

Orient from the client wiki first. Read `SCHEMA.md`, `index.md`, recent `log.md`, and the target business pages before claiming facts. Then prioritize:

1. The offer document: dream outcome, mechanism, stack, bonuses, guarantee, price, scarcity, and objections.
2. The avatar profile: desires, pains, objections, false beliefs, failed attempts, and the exact words they use.
3. The attractive character and brand voice: backstory, parables, signature phrases, polarity, and tone.
4. Existing assets: past VSLs, sales pages, webinars, ad creative, and performance data.
5. Real proof: testimonials, case studies, results, demonstrations, and approved claims.
6. Agent inference for structure, wording, and sequencing only — never for facts, proof, scarcity, or claims.

Completion: the offer, avatar, character, voice, and real proof are known or marked unknown.

## Required Inputs

Minimum useful inputs:

- the business or brand
- the offer the VSL sells (dream outcome and mechanism at minimum)
- the target avatar
- traffic temperature: cold, warm, or hot
- at least one real proof point, or an explicit note that proof is missing

Best inputs:

- a completed offer document from `offer-builder`
- a completed avatar profile
- an attractive character profile and brand voice guide
- a hook bank from `hook-angle-writer`
- real testimonials, case studies, and approved claims
- known objections and false beliefs blocking the sale
- the destination after the CTA (checkout, booking, application, trial signup)
- past VSL performance data if available (retention curve, drop-off points)

Completion: there is enough source material to script a believable VSL without inventing proof, scarcity, or claims.

## Core Workflow

### 1. Orient to the wiki

If working inside a client wiki, read:

- `SCHEMA.md`, `index.md`, recent `log.md`
- the target business's brand, offer, avatar, character, voice, and any existing VSLs

Completion: the VSL context, source assets, and save path are known.

### 2. Confirm VSL scope

Define before scripting:

- business and business slug
- offer and offer slug
- primary avatar
- traffic temperature and awareness level
- VSL length target (see length guidance below)
- industry variant: info-product, B2B/SaaS, or ecommerce
- delivery format: on-camera presenter, voiceover over B-roll, or animated
- CTA destination
- confidence level and source list

Completion: the VSL is tied to one business, one offer, one avatar, one traffic temperature, and one industry variant.

### 3. Choose the VSL length

Length depends on offer complexity, price, and traffic temperature:

| Length | When to use | Typical word count |
|---|---|---|
| Short (3-8 min) | Low-price impulse buys, warm traffic, simple ecommerce demos | 450-1,200 words |
| Medium (10-20 min) | Mid-price info-products, SaaS demos, cold-to-warm traffic | 1,500-3,000 words |
| Long (25-45 min) | High-ticket offers, complex transformations, cold traffic needing full belief shifts | 3,500-6,500 words |
| Webinar-style (45-90 min) | Launches, high-ticket coaching, offers requiring live demonstration | 6,500-12,000 words |

Do not pad a short offer into a long VSL. A 5-minute offer stretched to 30 minutes creates drop-off, not conversion. Match length to the buyer's decision complexity.

Completion: a target length and word count are fixed and justified by the offer complexity.

### 4. Build the VSL structure

Every VSL follows this anatomy (see `references/vsl-frameworks.md` for detail on each section). Adapt the section weights to the industry variant, but do not skip sections unless you have a reason.

1. **The Hook (0:00-0:15)** — the pattern interrupt that stops the scroll and promises the payoff for watching. See hook patterns below.
2. **The Intro / Big Promise (0:15-1:00)** — state who this is for, what they will learn or get, and why it matters now. Set the stakes.
3. **The Origin Story / Credibility (1:00-3:00)** — establish why the viewer should listen. Backstory, the discovery, the mechanism. Builds the attractive character's authority.
4. **The Problem Amplification (3:00-6:00)** — name the real problem in the avatar's language. Agitate the pain. Introduce the villain or false belief.
5. **The Mechanism / Unique Solution (6:00-10:00)** — reveal the unique mechanism that makes the result achievable. The "why this works when other things failed."
6. **The Transformation / Proof (10:00-15:00)** — show the before-and-after. Real testimonials, case studies, demonstrations. Make the result believable.
7. **The Offer Reveal (15:00-20:00)** — introduce the offer as the vehicle for the transformation. Frame it as the logical next step, not a pitch.
8. **The Stack Build (20:00-25:00)** — present each deliverable, its value anchor, and the objection it removes. Build the perceived value before revealing price.
9. **The Price Reveal and Anchor (25:00-28:00)** — reveal the price against the stacked value. Use the anchoring principles from `references/vsl-frameworks.md`.
10. **The Risk Reversal (28:00-30:00)** — present the guarantee. Make acting feel safer than not acting.
11. **The Scarcity and Urgency (30:00-32:00)** — real reasons to act now. Never fake these.
12. **The CTA (32:00-35:00)** — direct, specific, repeated. Tell the viewer exactly what to do, what happens next, and why doing it now is the right move.
13. **The Close / FAQ (35:00+)** — handle remaining objections, restate the big promise, final CTA.

Completion: every section has a goal, a time estimate, and a word count budget before any body copy is written.

### 5. Write the hook

Write 5-10 hook options using the patterns in `references/vsl-frameworks.md`. Choose the one that best matches the avatar's awareness level:

- **Cold traffic:** curiosity hooks, problem hooks, contrarian hooks — no product name, no jargon
- **Warm traffic:** mechanism hooks, "how to get X without Y," differentiation hooks
- **Hot traffic:** direct offer hooks, price anchors, proof-led hooks

The hook must pay off in the first 15 seconds. Empty curiosity erodes trust and inflates drop-off.

Completion: the chosen hook is specific, on-voice, and honest to the offer.

### 6. Write the body section by section

Write each section against its goal. Rules for every section:

- one idea per section
- earned attention — each section makes the viewer want the next
- on-camera direction in `[brackets]` for the presenter or editor
- B-roll notes in `{braces}` for visuals, demos, screenshots, text overlays
- the avatar's real language for pain and desire, not polished marketing copy
- real proof only — flag any unsupported claim with `Needs confirmation` or `Risk flag`
- match the brand voice rules from the wiki

For the offer reveal and stack build, follow the exact sequence in `references/vsl-frameworks.md`: reveal the offer as the vehicle, build the stack item by item with value anchors, then reveal price against the total stack value. Never reveal price before the stack is built.

Completion: every section is scripted, on-voice, and free of invented facts.

### 7. Industry variant adjustments

Apply the variant that matches the business:

**Info-product / coaching VSL:**
- Lead with origin story and transformation
- Heavier proof section (testimonials, case studies)
- Strong scarcity tied to cohort, capacity, or deadline
- Price reveal against a high-value stack

**B2B / SaaS VSL:**
- Lead with the problem and cost of the status quo
- Demo-driven mechanism section (show the product working)
- ROI math and time-saved framing in the stack
- Trial or demo CTA instead of direct purchase
- Shorter origin story; lead with the buyer's problem, not the founder's

**Ecommerce VSL:**
- Lead with the product demo
- Problem-solution-demo arc is tighter
- UGC-style authenticity over studio polish
- Price comparison handled honestly against commodity alternatives
- Direct purchase CTA, minimal friction

Completion: the script reflects the industry's real buying behavior, not a generic template.

### 8. Add on-camera direction and B-roll

For every section, add:

- `[ON-CAMERA: presenter direction — tone, expression, gesture]`
- `{B-ROLL: what visual supports this beat — demo, screenshot, text overlay, cutaway}`
- `{TEXT OVERLAY: key phrase, stat, or value anchor to burn in}`
- `[MUSIC: shift in tone if needed — e.g., shift to uplifting at the transformation]`

This makes the script usable by a video editor without a separate brief.

Completion: a presenter or editor can produce the video from the script alone.

### 9. Handle objections preemptively

Map the avatar's top objections to VSL sections where they are answered:

| Objection | VSL section that answers it |
|---|---|
| I don't believe it works | Mechanism + Proof |
| It won't work for me | Avatar-specific case studies in Transformation |
| It's too expensive | Stack Build + Price Anchor |
| It's too much work | Effort reduction in Mechanism + Guarantee |
| I don't trust the seller | Origin Story + Credibility |
| Not right now | Scarcity/Urgency + Cost of Delay |

Completion: the top objections are answered before the CTA, not after.

### 10. Assemble the final VSL document

Use this output shape:

```markdown
# VSL: [Offer Name] for [Avatar]

## Scope
- Business:
- Business slug:
- Offer:
- Primary avatar:
- Traffic temperature: cold / warm / hot
- Industry variant: info-product / B2B-SaaS / ecommerce
- Length target: X min / Y words
- CTA destination:
- Confidence:
- Sources used:

## VSL Strategy
- One job:
- Big promise:
- Main objection:
- Lead framework: (e.g., Perfect Webinar, Sideways Sales Letter, Problem-Agitate-Solve)

## Hook Options
1.
2.
3.
4.
5.

## Chosen Hook
- Hook:
- Rationale:

## Time-Stamped Script

### [0:00-0:15] The Hook
[ON-CAMERA: ...]
{B-ROLL: ...}
[Script body]

### [0:15-1:00] The Intro / Big Promise
[Script body]

### [1:00-3:00] Origin Story / Credibility
[Script body]

(repeat for each section through the CTA)

## Objection Map
| Objection | Answered in section |
|---|---|
| | |

## Proof and Claims
| Claim | Source | Risk |
|---|---|---|
| | | |

## Production Notes
- Presenter:
- Tone:
- Key B-roll assets needed:
- Text overlays to prepare:

## Needs Confirmation
- [unverified proof, risky claims, missing avatar inputs, unconfirmed scarcity]
```

Completion: the document can be handed to a presenter, editor, or media buyer without reconstructing the strategy.

### 11. Update the wiki when appropriate

If working inside an LLM wiki:

- save the VSL under `businesses/<business-slug>/vsls/<vsl-slug>.md`
- link it to the offer, avatar, character, and brand voice
- update `index.md` if appropriate
- append to `log.md`
- run `qmd update` if configured

Completion: the VSL is filed under the correct business and reusable in later sessions.

## Missing Information Handling

Do not invent missing facts. Use these labels:

- `Unknown`: no source material supports the answer
- `Needs confirmation`: likely but not verified
- `Client to provide`: requires real proof, results, or offer details only the client can give
- `Risk flag`: income, health, financial, legal, credential, or guarantee claim needing review
- `Out of scope`: a promise or component the offer cannot support

If the offer or avatar is missing entirely, stop and route to `offer-builder` or `avatar-builder` first. A VSL written without a real offer and avatar is a generic template, not a conversion asset.

## Quality Bar

A strong VSL script has:

- one business, one offer, one avatar, one traffic temperature, and one industry variant
- a hook that pays off in 15 seconds
- a structure where every section earns the next
- the avatar's real language for pain and desire
- real proof, or clearly flagged missing proof
- a stack build that precedes the price reveal
- risk reversal that makes acting feel safer than waiting
- ethical scarcity and urgency only
- a direct, specific, repeated CTA
- on-camera direction and B-roll notes throughout
- the brand voice and attractive character's signature phrases
- risky claims flagged
- a confidence level and source list

A weak VSL script has:

- a hook that promises what the body does not deliver
- a pitch-first structure that reveals price before building value
- invented testimonials or results
- generic guru copy with no avatar specificity
- fake scarcity or countdown pressure
- no on-camera direction, making it unusable for production
- no objection handling
- claims that create legal or credibility risk

## Common Pitfalls

1. **Revealing price before the stack.** The stack builds the perceived value that makes the price feel logical. Reveal price only after the stack is complete.
2. **Front-loading hype.** A VSL that opens with "this will change your life" loses viewers who have heard that before. Open with specificity and a real pattern interrupt.
3. **Skipping the mechanism.** The "why this works" section is what separates a VSL from a pitch. Without it, the offer is just a claim.
4. **Inventing proof.** Every testimonial and result must come from real source material. Flag missing proof; do not fabricate it.
5. **Ignoring the industry variant.** A B2B SaaS VSL is not an info-product VSL with the words changed. Match the buying behavior.
6. **Faking urgency.** If there is no real deadline, use cost-of-delay framing. Fake countdowns destroy trust.
7. **No on-camera direction.** A script without direction is a document, not a production asset. Add direction for every section.
8. **Ignoring retention.** Long VSLs must earn attention every 60-90 seconds with a pattern interrupt, story beat, or open loop.
9. **Weak CTA.** "Click the button" is not a CTA. Tell the viewer exactly what happens next, why it is safe, and why now.
10. **No objection map.** Objections answered reactively in the comments are too late. Answer them preemptively in the script.

## Verification Checklist

- [ ] Business, offer, avatar, traffic temperature, and industry variant confirmed
- [ ] Offer, avatar, character, and voice pulled from the wiki, not invented
- [ ] Length target justified by offer complexity
- [ ] VSL structure complete (all sections present or intentionally omitted with reason)
- [ ] 5-10 hook options written, chosen hook justified
- [ ] Hook pays off in 15 seconds
- [ ] Every section has a goal, time estimate, and word count budget
- [ ] Body copy uses the avatar's real language
- [ ] Offer reveal follows the stack build (price never precedes the stack)
- [ ] Risk reversal is clear, deliverable, and matched to the offer
- [ ] Scarcity and urgency are ethical and documented
- [ ] CTA is direct, specific, and repeated
- [ ] On-camera direction and B-roll notes present throughout
- [ ] Top objections mapped to answering sections
- [ ] Proof is real or flagged as missing
- [ ] Risky claims (income, health, financial, legal) flagged
- [ ] Brand voice and character signature phrases used
- [ ] Confidence level and source list included
- [ ] If wiki-backed, VSL filed under `businesses/<business-slug>/vsls/` and linked
- [ ] Final output follows the VSL document shape
