---
name: funnel-copy-writer
description: Use when assembling, planning, or auditing the COPY for a full multi-page funnel (ad → opt-in/landing → VSL → sales page → checkout → thank-you) for a specific business, avatar, and offer. Orchestrates the other copy skills into a connected funnel with message-match continuity, hook continuity, and CTA escalation across every step. Copy only — not the HTML build.
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, funnel, copywriting, conversion, message-match, strategy, orchestration]
    related_skills: [funnel-page-writer, vsl-writer, ad-script-writer, hook-angle-writer, offer-builder, avatar-builder, brand-voice-extractor, human-editor]
---

# Funnel Copy Writer

## Overview

Plan and assemble the full copy for a connected funnel — the sequence of pages and scripts that moves one specific avatar from the first scroll-stopping ad frame to the final checkout confirmation. This skill does not write new page copy from scratch. It orchestrates the other copy skills (`funnel-page-writer`, `vsl-writer`, `ad-script-writer`) into one connected funnel copy document where every step carries the same message and every transition is seamless.

Use `references/funnel-copy-frameworks.md` for the funnel archetypes, the message-match framework, the golden-thread principle, the delegation matrix, and the common funnel disconnects.

The core discipline: **MESSAGE MATCH**. The hook that stops the scroll in the ad must be the same hook that opens the landing page, the same promise that drives the VSL, and the same offer the checkout confirms. A funnel that changes its message between steps loses the buyer. Every page is a continuation of the one before it, never a reset.

This skill is the conductor, not the instrument. It defines the funnel architecture, sets the golden thread, delegates each page to the right skill, then enforces continuity across the assembled outputs.

## When to Use

Use this skill when the client asks for:

- a full funnel copy build across multiple pages (ad → opt-in → VSL → sales → checkout → thank-you)
- funnel copy strategy or architecture planning before any page is written
- a message-match audit of an existing funnel (hook, offer, voice, CTA consistency)
- a funnel copy doc that connects every page into one continuous narrative
- mapping funnel steps, page jobs, and CTA escalation across the full buyer path
- a hook-continuity check from the ad creative through to checkout
- a golden-thread definition (the one promise, mechanism, and CTA running through every step)

Do not use this skill for:

- a single landing page, sales page, or checkout page — use `funnel-page-writer`
- a VSL script — use `vsl-writer`
- an ad script — use `ad-script-writer`
- building the offer itself — use `offer-builder`
- avatar research — use `avatar-builder`
- brand voice extraction — use `brand-voice-extractor`
- the HTML build of the funnel pages — that is a separate, deferred skill (`funnel-html-builder`) that takes this copy output plus Matt's clean HTML templates
- legal, health, income, or compliance review

This skill produces the copy strategy and the assembled copy doc. It does not produce the HTML, the design assets, or the page build.

## Multi-Business Rule

A client can run several businesses, and each business can have many funnels. Never blend funnel copy, offers, avatars, or voice across businesses. Before planning a funnel, confirm the business, business slug, primary avatar, offer, traffic source, and funnel archetype.

Store funnel copy work inside the client wiki under the correct business:

```text
businesses/<business-slug>/
├── brand.md
├── brand-voice.md
├── avatars/
├── offers/
│   └── <offer-slug>.md
└── funnels/
    └── <funnel-slug>.md
```

Each funnel copy doc is one file (`<funnel-slug>.md`) that contains the full funnel architecture, the golden thread, the delegation map, and the assembled or linked page copy for every step. Individual page scripts (VSL, long sales page) may live as separate files under the funnel and are linked from the master doc.

If the wiki uses another structure, follow it while keeping every funnel grouped by business and linked to its offer, avatar, character, and voice.

## Source Hierarchy

Orient from the client wiki first. Read `SCHEMA.md`, `index.md`, recent `log.md`, and the target business pages before claiming facts. Then prioritize:

1. The offer document: dream outcome, mechanism, stack, bonuses, guarantee, price, scarcity, and objections — from `offer-builder`.
2. The avatar profile: desires, pains, objections, false beliefs, failed attempts, and the exact words they use — from `avatar-builder`.
3. The brand voice guide and attractive character: tone, signature phrases, polarity, backstory — from `brand-voice-extractor` and `attractive-character-builder`.
4. The hook bank: the headline and hook options that will run through the funnel — from `hook-angle-writer`.
5. Existing assets: current ads, landing pages, VSLs, sales pages, checkout pages, and performance data.
6. Real proof: testimonials, case studies, results, demonstrations, and approved claims.
7. Agent inference for structure, sequencing, and continuity logic only — never for facts, proof, scarcity, or claims.

Completion: the offer, avatar, character, voice, hook bank, existing assets, and real proof are known or marked unknown. The funnel cannot be planned honestly without a real offer and avatar.

## Required Inputs

Minimum useful inputs:

- the business or brand
- the offer the funnel sells (dream outcome and mechanism at minimum)
- the primary avatar
- the traffic source and traffic temperature: cold, warm, or hot
- the funnel goal: opt-in, registration, purchase, booking, or application
- at least a working hook or headline direction

Best inputs:

- a completed offer document from `offer-builder`
- a completed avatar profile
- a brand voice guide and attractive character profile
- a hook bank from `hook-angle-writer` (5-10 hook options)
- the traffic source and exact ad angles planned or live
- real testimonials, case studies, and approved claims
- known objections and false beliefs blocking the sale
- existing funnel pages, ads, or VSLs (for an audit or rebuild)
- the checkout platform and any constraints on the checkout copy
- the post-purchase path: thank-you page, onboarding, upsell, or nurture sequence

Completion: there is enough source material to define a golden thread and delegate each page without inventing the offer, the avatar, the hook, or the proof.

## Core Workflow

### 1. Orient to the wiki

If working inside a client wiki, read:

- `SCHEMA.md`, `index.md`, recent `log.md`
- the target business's brand, offer, avatar, character, voice, and hook bank
- any existing funnel pages, ads, or VSLs for this business

Completion: the funnel context, source assets, and save path are known.

### 2. Define funnel scope

Capture before planning:

- business and business slug
- offer and offer slug
- primary avatar
- traffic source and traffic temperature
- funnel archetype (see Step 4)
- funnel goal and the one conversion event that defines success
- the post-conversion path
- confidence level and source list

Completion: the funnel is tied to one business, one offer, one avatar, one traffic temperature, and one archetype.

### 3. Pull the golden-thread inputs

The golden thread is the single promise, mechanism, and CTA that runs through every funnel step. Pull these before any page is planned:

- **The one promise:** the specific, quantifiable outcome the funnel delivers (from the offer doc).
- **The one mechanism:** the unique method or vehicle that makes the result achievable (from the offer doc).
- **The one hook:** the scroll-stopping idea that opens the ad and carries through every page (from the hook bank).
- **The one CTA arc:** how the ask escalates from the ad (click) through opt-in (email) through VSL (watch) to checkout (buy). Same destination, escalating commitment.
- **The one voice:** the brand voice and attractive character signature that every page shares.
- **The one proof path:** the testimonials and results that appear, sequenced from relatable to aspirational across the funnel.

If any of these is missing or weak, stop and route to the right skill (`offer-builder`, `avatar-builder`, `hook-angle-writer`, `brand-voice-extractor`) before planning the funnel.

Completion: the golden thread is defined in one paragraph and can be stated in a single sentence: "[Avatar] gets [promise] through [mechanism], and every step of this funnel says exactly that."

### 4. Choose the funnel archetype

Pick the archetype that matches the business model, offer, and traffic. See `references/funnel-copy-frameworks.md` for the full step maps.

- **Opt-in funnel:** ad → opt-in page → thank-you/delivery → nurture sequence. Goal: capture the lead. Best for lead magnets, low-friction entry, and warming cold traffic.
- **VSL funnel:** ad → VSL page → checkout → (optional) upsell → thank-you. Goal: direct purchase from a video presentation. Best for info-products, mid-to-high-ticket, and cold-to-warm traffic.
- **Webinar funnel:** ad → registration → confirmation/reminders → webinar → offer page → checkout. Goal: register, show up, buy. Best for high-ticket coaching, complex transformations, and launches.
- **Application funnel:** ad → application page → booking → sales call → (close). Goal: qualify and book a sales conversation. Best for high-ticket services, done-for-you, and capacity-limited offers.
- **Ecommerce funnel:** ad → product/landing page → cart → checkout → (optional) post-purchase upsell. Goal: direct purchase. Best for physical products, low-to-mid ticket, and impulse or comparison buys.

Hybrid funnels exist (e.g., application funnel with a VSL pre-frame, or ecommerce with an upsell VSL). Document the hybrid and its rationale.

Completion: the archetype and its step map are chosen and justified by the offer and traffic.

### 5. Map the funnel steps

For the chosen archetype, list every page and script in order. For each step, define:

- **Step name** (e.g., "Cold traffic ad," "Opt-in page," "VSL")
- **The page's one job** (what this step must achieve)
- **The primary CTA** (what the reader/viewer does next)
- **The traffic temperature arriving at this step** (cold, warm, hot)
- **The awareness level arriving at this step** (unaware, problem-aware, solution-aware, product-aware)
- **Which skill writes it** (see delegation matrix in Step 6)
- **The hook variant** (how the golden-thread hook expresses at this step)
- **The proof used** (which testimonial or result appears here)

Completion: the full step map is documented in a table before any page copy is drafted.

### 6. Apply the delegation matrix

This skill delegates page copy to the specialist skills. It does not write the copy itself.

| Funnel step | Skill that writes it |
|---|---|
| Cold / warm / hot traffic ad | `ad-script-writer` |
| Opt-in page, lead magnet page | `funnel-page-writer` |
| Landing page (pre-VSL or direct) | `funnel-page-writer` |
| VSL page (wrapper / opt-in gate) | `funnel-page-writer` |
| VSL script | `vsl-writer` |
| Sales page (long-form) | `funnel-page-writer` |
| Webinar registration page | `funnel-page-writer` |
| Webinar script / deck script | `vsl-writer` (webinar variant) |
| Application page | `funnel-page-writer` |
| Booking / calendar page copy | `funnel-page-writer` |
| Checkout page copy | `funnel-page-writer` |
| Order bump / upsell / downsell page | `funnel-page-writer` (offer from `offer-builder`) |
| Thank-you / delivery page | `funnel-page-writer` |
| Nurture / follow-up email sequence | `email-writer` |

When delegating, pass each skill the golden thread (promise, mechanism, hook, voice, proof path) and the specific step context (traffic temperature, awareness level, previous step, next step, CTA). Each skill produces its own output; this skill assembles and enforces continuity.

Completion: every step has an assigned skill and the handoff context is defined.

### 7. Enforce message match across all outputs

Once page copy starts coming back from the delegated skills, run the message-match enforcement pass. Every transition between steps must be seamless. Check the three pillars of message match at every handoff:

- **Promise match:** the outcome promised in the ad is the outcome delivered on the landing page, in the VSL, and confirmed at checkout. No new promises appear mid-funnel.
- **Language match:** the terminology, key phrases, and voice carry through every step. The avatar hears the same words from the brand at every touchpoint.
- **Aesthetic-direction match:** while this skill is copy-only, flag where the copy implies a visual or tone shift that would break continuity for the design team.

Run the message-match audit checklist (see `references/funnel-copy-frameworks.md`):

1. **Hook continuity:** does the hook from the ad reappear as the headline on the landing page and the opening of the VSL?
2. **Offer consistency:** is the same offer, price, guarantee, and scarcity stated identically across the VSL, sales page, and checkout?
3. **Voice consistency:** does every page sound like the same brand and character?
4. **CTA escalation:** does the ask escalate logically (click → email → watch → buy) without a jarring jump?
5. **Proof sequencing:** is proof deployed in the right order (relatable early, aspirational late) without repeating or contradicting across steps?

Where a disconnect is found, fix it by aligning the downstream page to the golden thread — not by changing the golden thread to fit a page.

Completion: every step-to-step transition passes the three pillars and the five-point audit.

### 8. Assemble the connected funnel copy doc

Pull all delegated outputs into one master funnel copy document. Use this output shape:

```markdown
# Funnel Copy: [Funnel Name]

## Scope
- Business:
- Business slug:
- Offer:
- Primary avatar:
- Traffic source / temperature:
- Funnel archetype:
- Funnel goal:
- Confidence:
- Sources used:

## The Golden Thread
- The one promise:
- The one mechanism:
- The one hook:
- The one CTA arc:
- The one voice:
- The one proof path:
- One-sentence thread: [Avatar] gets [promise] through [mechanism], and every step of this funnel says exactly that.

## Funnel Step Map
| Step | Page / asset | One job | Primary CTA | Traffic temp | Awareness | Skill | Hook variant | Proof |

## Message-Match Audit
| Check | Status | Notes |
|---|---|---|
| Hook continuity | Pass / Fix | |
| Offer consistency | Pass / Fix | |
| Voice consistency | Pass / Fix | |
| CTA escalation | Pass / Fix | |
| Proof sequencing | Pass / Fix | |

## Step Copy

### Step 1: [Ad / Cold traffic]
- Asset:
- Skill: ad-script-writer
- File: [link or inline]
- Hook variant:
- CTA:

### Step 2: [Landing / Opt-in]
- Asset:
- Skill: funnel-page-writer
- File: [link or inline]
- Headline:
- CTA:

### Step 3: [VSL]
- Asset:
- Skill: vsl-writer
- File: [link or inline]
- Opening hook:
- CTA:

(repeat for every step through thank-you)

## Disconnects Found and Fixed
- [each disconnect, the fix applied, and where]

## Open Questions / Needs Confirmation
- [unknowns, risky claims, missing inputs]
```

Completion: the funnel copy doc is a single source of truth that a builder, media buyer, or designer can work from without reconstructing the strategy.

### 9. Update the wiki when appropriate

If working inside an LLM wiki:

- save the funnel copy doc under `businesses/<business-slug>/funnels/<funnel-slug>.md`
- link it to the offer, avatar, character, voice, and the individual page files
- update `index.md` if appropriate
- append to `log.md`
- run `qmd update` if configured

Completion: the funnel is filed under the correct business and reusable by later sessions and by the deferred `funnel-html-builder`.

## Missing Information Handling

Do not invent missing facts. Use these labels:

- `Missing offer`: no offer document exists — route to `offer-builder` first
- `Missing avatar`: no avatar profile exists — route to `avatar-builder` first
- `Missing hook bank`: no hook options exist — route to `hook-angle-writer` first
- `Missing voice`: no brand voice guide exists — route to `brand-voice-extractor` first
- `Missing proof`: no testimonials or results are sourced — flag every claim that needs proof
- `Missing traffic source`: the ad angles or traffic temperature are unknown — confirm before planning the hook variants
- `Needs confirmation`: likely but not verified
- `Risk flag`: income, health, financial, legal, credential, guarantee, or regulated claim needing review

A funnel cannot be planned honestly without a real offer, a real avatar, and at least one real hook direction. If those are missing, stop and route to the foundation skills first. A funnel planned on assumptions produces disconnected copy that will not convert.

## Quality Bar

A strong funnel copy build has:

- one business, one offer, one avatar, one traffic temperature, and one archetype
- a defined golden thread (promise, mechanism, hook, CTA arc, voice, proof path)
- a complete step map where every page has one job and one CTA
- every page delegated to the correct specialist skill
- message match enforced across every step-to-step transition
- hook continuity from the ad opening through the checkout confirmation
- CTA escalation that moves logically from micro-commitment to purchase
- proof sequenced from relatable to aspirational without contradiction
- the same offer, price, guarantee, and scarcity stated identically wherever they appear
- one consistent brand voice across every page
- real proof or clearly flagged missing proof
- risky claims flagged
- a confidence level and source list
- a single assembled copy doc that downstream builders can work from

A weak funnel copy build has pages written in isolation with no shared thread, a hook that changes between the ad and the landing page, an offer stated differently on the VSL and the checkout, a CTA that jumps from "learn more" to "buy now," proof that contradicts itself across steps, or no master document tying the funnel together.

## Common Pitfalls

1. **Writing page copy before defining the golden thread.** If the promise, mechanism, and hook are not fixed first, every page drifts. Completion: the golden thread is locked before any page is delegated.
2. **Letting each page reinvent the hook.** The ad hook, landing headline, and VSL opener must be the same idea expressed for the step. Completion: every hook variant traces back to the one hook.
3. **Breaking message match at the checkout.** The checkout is where trust is most fragile. If the offer, price, or guarantee reads differently here than on the VSL, buyers abandon. Completion: checkout copy is verified against the VSL and sales page word for word on offer terms.
4. **Jumping the CTA.** Going from "click to learn more" in the ad to "buy now for $997" on the landing page breaks the commitment arc. Completion: the CTA escalates one logical step at a time.
5. **Contradicting proof across steps.** A testimonial quoted one way on the sales page and another way on the checkout erodes credibility. Completion: proof is sourced once and quoted consistently.
6. **Treating the thank-you page as an afterthought.** It is the start of retention and the first upsell or nurture touch. Completion: the thank-you page has a job and a next step.
7. **Planning the funnel without the offer.** A funnel without a real offer is a template. Completion: the offer document exists or is requested first.
8. **Ignoring the traffic temperature shift.** Traffic arrives cold at the ad and is warm or hot by the checkout. The copy must match the awareness level at each step, not speak to cold traffic the whole way through. Completion: each step's copy matches the arriving awareness level.
9. **Blending funnels across businesses or offers.** Never pull copy, proof, or voice from one business into another's funnel. Completion: every asset traces to one business and one offer.
10. **Confusing copy with build.** This skill produces copy and strategy. The HTML build is a separate, deferred skill. Completion: the handoff to the builder is explicit and the copy doc is build-ready.

## Verification Checklist

- [ ] Client wiki orientation completed when a wiki is available
- [ ] Business, business slug, avatar, offer, and traffic source confirmed
- [ ] Funnel archetype chosen and justified
- [ ] Golden thread defined (promise, mechanism, hook, CTA arc, voice, proof path)
- [ ] Full step map documented (every page, its job, its CTA, its skill)
- [ ] Every step delegated to the correct specialist skill
- [ ] Each delegated skill received the golden thread and step context
- [ ] Message-match audit passed (hook continuity, offer consistency, voice consistency, CTA escalation, proof sequencing)
- [ ] Hook continuity verified from ad opening through checkout confirmation
- [ ] Offer, price, guarantee, and scarcity stated identically wherever they appear
- [ ] CTA escalation is logical (no jarring jumps)
- [ ] Proof sequenced from relatable to aspirational without contradiction
- [ ] Brand voice consistent across every page
- [ ] Proof is real or flagged as missing
- [ ] Risky claims (income, health, financial, legal) flagged
- [ ] Funnel copy doc assembled and stored under `businesses/<business-slug>/funnels/`
- [ ] Confidence level and source list included
- [ ] Handoff to `funnel-html-builder` (deferred) is explicit and the doc is build-ready
