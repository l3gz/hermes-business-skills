---
name: ad-script-writer
description: Use when writing or auditing a video ad script, cold-call script, webinar promo script, or short-form video ad for a specific business, avatar, and offer. Produces a complete, production-ready script with hook, body, CTA, on-camera direction, and B-roll guidance across 6-second to 60-second+ video ads, cold-call sequences, and webinar registration promos. Covers Becker TRT, Iman Gadzhi VSL-ad, Cardone attention, Jeremy Haynes Hollywood, Sam Ovens Perfect Webinar, Hormozi Hook-Retain-Reward, and GaryVee Jab-Jab-Jab frameworks.
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, advertising, ad-scripts, copywriting, video-ads, cold-calling, conversion, paid-traffic]
    related_skills: [vsl-writer, offer-builder, avatar-builder, attractive-character-builder, brand-voice-extractor, hook-angle-writer, funnel-page-writer, human-editor]
---

# Ad Script Writer

## Overview

Write a complete ad script: a scripted piece of paid-traffic or outbound creative that takes one specific avatar from zero attention to a micro-commitment — a click, a registration, an appointment, or a direct purchase. An ad script is not a VSL. It is a shorter, higher-intensity format optimized for the first three seconds, the scroll stop, and the single action you want the viewer or listener to take next.

This skill produces a full, production-ready script with hook, body, CTA, on-camera direction, and B-roll notes. Use `references/ad-script-frameworks.md` for the detailed framework reference (ad-type anatomy, named frameworks, hook patterns, CTA structure, testing methodology, ad-to-funnel mapping). This file is the operating process.

The core discipline: the ad sells the click, not the offer. A video ad that tries to explain the entire product burns attention and inflates cost-per-acquisition. A cold call that tries to close on the first dial gets hung up on. Every ad format has one job — earn the next step.

## When to Use

Use this skill when the client asks for:

- a video ad script (6s, 15s, 30s, or 60s+) for Meta, YouTube, TikTok, or connected TV
- a short-form video ad (Reels, Shorts, TikTok) with a hook-reward structure
- a cold-call or outbound call script with qualification and appointment-setting
- a webinar promo or registration ad (the ad that drives signups, not the webinar itself)
- a warm-call or follow-up call script
- a retargeting ad script for warm or hot traffic
- an audit or rewrite of existing ad creative that is not converting
- a creative testing brief (hook variations, body variations, CTA variations)

Do not use this skill for:

- a full VSL (Video Sales Letter) longer than 60 seconds with a complete offer reveal and stack build — use `vsl-writer`
- a landing page or sales page — use `funnel-page-writer`
- building the offer itself — use `offer-builder`
- avatar research — use `avatar-builder`
- brand voice extraction — use `brand-voice-extractor`
- hook angle ideation before the ad format is chosen — use `hook-angle-writer`
- final copy polish after the script is drafted — use `human-editor`
- inventing proof, testimonials, results, or claims the offer cannot support

The boundary with `vsl-writer`: if the script contains a full offer reveal, stack build, price anchor, and risk reversal, it is a VSL — use `vsl-writer`. If the script's job is to earn a click, registration, or appointment that leads to a separate sales conversation, it is an ad — use this skill.

## Multi-Business Rule

A client can run several businesses, and each business can have many ad campaigns. Never blend ad facts, offers, avatars, or proof across businesses. Before writing, confirm the business, business slug, primary avatar, offer, traffic temperature, and ad platform.

Store ad work inside the client wiki under the correct business:

```text
businesses/<business-slug>/
├── brand.md
├── brand-voice.md
├── products.md
├── offers/
│   └── <offer-slug>.md
├── avatars/
│   └── <avatar-slug>.md
└── ads/
    └── <ad-slug>.md
```

If the wiki uses another structure, follow it while keeping every ad grouped by business and linked to its offer, avatar, and landing page destination.

## Source Hierarchy

Orient from the client wiki first. Read `SCHEMA.md`, `index.md`, recent `log.md`, and the target business pages before claiming facts. Then prioritize:

1. The offer document: dream outcome, mechanism, stack, guarantee, price, scarcity, and objections.
2. The avatar profile: desires, pains, objections, false beliefs, failed attempts, and the exact words they use.
3. The brand voice and attractive character: tone, polarity, signature phrases, and backstory beats.
4. The destination after the ad: landing page, VSL, webinar registration, checkout, booking page, or calendar link.
5. Existing assets: past ads, ad performance data (CTR, hook rate, hold rate, CPA, ROAS), winning creatives, and creative fatigue signals.
6. Real proof: testimonials, case studies, results, and approved claims.
7. Agent inference for structure, wording, and sequencing only — never for facts, proof, scarcity, or claims.

Completion: the offer, avatar, voice, destination, and real proof are known or marked unknown.

## Required Inputs

Minimum useful inputs:

- the business or brand
- the offer the ad promotes (dream outcome and mechanism at minimum)
- the target avatar
- traffic temperature: cold, warm, or hot
- the ad platform (Meta, YouTube, TikTok, cold call, etc.)
- the destination after the click or call (landing page, booking, registration)
- at least one real proof point, or an explicit note that proof is missing

Best inputs:

- a completed offer document from `offer-builder`
- a completed avatar profile
- a brand voice guide and attractive character profile
- a hook bank from `hook-angle-writer`
- the landing page or VSL the ad sends traffic to (for message match)
- real testimonials, case studies, and approved claims
- known objections and false beliefs
- past ad performance data: hook rate (3-second view rate), hold rate, CTR, CPA, ROAS, creative fatigue signals
- the campaign objective: awareness, engagement, lead, appointment, or purchase
- budget level and scaling stage (testing, scaling, or optimization)

Completion: there is enough source material to script a believable ad without inventing proof, scarcity, or claims.

## Core Workflow

### 1. Orient to the wiki

If working inside a client wiki, read:

- `SCHEMA.md`, `index.md`, recent `log.md`
- the target business's brand, offer, avatar, character, voice, and any existing ads
- the landing page or destination the ad will send traffic to

Completion: the ad context, source assets, destination, and save path are known.

### 2. Define ad scope

Define before scripting:

- business and business slug
- offer and offer slug
- primary avatar
- traffic temperature and awareness level (unaware, problem-aware, solution-aware, product-aware)
- ad platform (Meta, YouTube, TikTok, Reels, cold call, etc.)
- campaign objective (click, registration, appointment, purchase)
- destination after the action
- ad type (see Step 3)
- confidence level and source list

Completion: the ad is tied to one business, one offer, one avatar, one traffic temperature, one platform, and one campaign objective.

### 3. Choose the ad type

The ad type determines structure, length, and intensity. Match the type to the platform and the campaign objective.

| Ad type | Length | When to use | Typical structure |
|---|---|---|---|
| Bumper / 6s | 6 seconds | Brand recall, retargeting, reinforcing a single benefit | One hook, one benefit, one logo or CTA frame |
| Short video ad / 15s | 10-15 seconds | Cold traffic scroll-stop, single benefit, sell the click | Hook (3s) → benefit → CTA |
| Standard video ad / 30s | 25-30 seconds | Cold or warm traffic, problem-solution arc, lead gen | Hook (3s) → problem → solution → CTA |
| Long video ad / 60s+ | 45-90 seconds | Warm traffic, story-driven, mechanism tease, webinar promo | Hook (3s) → story → mechanism → CTA |
| Short-form / Reels / TikTok | 15-60 seconds | Cold traffic, value-first, hook-reward structure | Hook (3s) → value delivery → reward CTA |
| Cold-call script | 60-90 seconds | Outbound, appointment-setting, B2B | Greeting → big claim → qualify → appointment → lock close |
| Webinar promo script | 60-90 seconds | Warm traffic, registration ad | Hook → who it's for → origin story tease → three pillars → register CTA |
| Retargeting ad | 15-30 seconds | Hot traffic, direct purchase | Proof hook → offer → direct CTA with urgency |

Do not pad a 15-second ad into a 60-second ad. If the message is simple, keep the ad short. Long ads with thin content inflate CPA and accelerate creative fatigue.

Completion: a target ad type, length, and structure are fixed and justified by the campaign objective.

### 4. Choose the framework

Select the framework that matches the ad type, traffic temperature, and industry. See `references/ad-script-frameworks.md` for the full detail on each.

| Framework | Best for | Traffic | Ad type |
|---|---|---|---|
| **Becker TRT** (Testimonial-Repeat-Testimonial) | SaaS, agencies, high-ticket info | Cold | 30-60s video ad |
| **Iman Gadzhi 4-Phase VSL-Ad** | E-learning, coaching, events | Cold → warm | Multi-ad funnel sequence |
| **Cardone 10X Cold-Call** | B2B, real estate, consulting | Cold | Cold-call script |
| **Jeremy Haynes Hollywood Belief-Shift** | High-ticket consulting, agencies | Problem-aware | 30-60s video ad |
| **Sam Ovens Perfect Webinar Promo** | High-ticket coaching, consulting | Warm | Webinar promo script |
| **Hormozi Hook-Retain-Reward** | Lead gen, SaaS, coaching | Cold | Short-form / Reels / TikTok |
| **GaryVee Jab-Jab-Jab Right Hook** | Ecommerce, personal brands | Cold → warm | Multi-ad content sequence |
| **PAS** (Problem-Agitate-Solve) | Universal, any industry | Cold or warm | 15-30s video ad |
| **BAB** (Before-After-Bridge) | Ecommerce, simple offers | Cold | 15s video ad |

Completion: the framework is chosen and justified by the ad type, traffic temperature, and avatar awareness level.

### 5. Write the hook (first 3 seconds)

Write 5-10 hook options using the patterns in `references/ad-script-frameworks.md`. The hook's only job is to earn the next 3 seconds. Choose the hook that matches the avatar's awareness level:

- **Cold / unaware traffic:** visual curiosity loops, shock statistics, provocative questions, value-first jabs — no product name, no jargon
- **Warm / solution-aware traffic:** quantifiable promised-land invitations, system-blaming hooks, exclusivity plays, mechanism teases
- **Hot / product-aware traffic:** direct offer hooks, proof-led hooks, fast-action scarcity, risk reversal

The hook must pay off in the body. Empty curiosity ("You won't believe what happened") erodes trust and spikes skip rates. The hook must also set up the landing page — whatever the ad promises, the destination must deliver.

For video ads, the first frame matters as much as the first word. Specify the thumbnail or opening visual alongside the verbal hook.

Completion: the chosen hook is specific, on-voice, honest to the offer, and matched to the awareness level.

### 6. Write the body

Write the body against the framework's structure. Rules for every section:

- one idea per beat — do not stack multiple claims
- the avatar's real language for pain and desire, not polished marketing copy
- real proof only — flag any unsupported claim with `Needs confirmation` or `Risk flag`
- for video ads: on-camera direction in `[brackets]`, B-roll notes in `{braces}`, text overlays in `{TEXT OVERLAY: ...}`
- match the brand voice rules from the wiki
- the body must deliver on the hook's promise — if the hook teases a mechanism, the body shows it
- for cold calls: keep the body under 20 seconds before qualification — the goal is an appointment, not a pitch
- for short-form: cut every word that does not earn the next second

Completion: every beat is scripted, on-voice, and free of invented facts.

### 7. Write the CTA

The CTA must match the campaign objective and traffic temperature:

- **Cold traffic video ads:** indirect CTA — sell the click, not the offer. "Click to see exactly how" or "Watch the full breakdown." The click is the micro-commitment.
- **Warm traffic:** registration or lead CTA — "Reserve your seat," "Get the free guide," "Book your call."
- **Hot traffic / retargeting:** direct CTA — "Get [product] now," with clear pricing and a frictionless buy path.
- **Cold calls:** appointment CTA — propose a specific, short time block (e.g., 18 minutes), offer today as the primary option, and lock the commitment.
- **Short-form / value-first:** reward CTA — "Click the link to download the template. No email, no paywall."

Every CTA must answer three questions: what do I do, what happens next, and why now. Weak CTAs ("learn more," "click here") kill conversion.

For video ads with urgency or scarcity, state it once, clearly, near the CTA — do not repeat it throughout. Ethical scarcity and urgency only. Never fabricate countdowns, limited spots, or expiring bonuses.

Completion: the CTA is direct, specific, matched to the objective, and honest about what happens next.

### 8. Add on-camera direction and B-roll

For every video ad section, add:

- `[ON-CAMERA: presenter direction — tone, energy, gesture, eyeline]`
- `{B-ROLL: what visual supports this beat — demo, screenshot, cutaway, product shot}`
- `{TEXT OVERLAY: key phrase, stat, or value anchor to burn in}`
- `[MUSIC: energy shift if needed — e.g., shift to intense at the problem, uplifting at the solution]`

For short-form and mobile-first ads, also specify:

- the opening frame (the still image viewers see before tapping)
- caption style and placement (most short-form is watched muted)
- the "See More" button placement and the headline above it

This makes the script usable by a video editor or creator without a separate brief.

Completion: a presenter, editor, or creator can produce the ad from the script alone.

### 9. Handle message match to the destination

Map the ad to its destination. The ad and the landing page must match on three pillars:

- **Aesthetic match:** visual styling, color, design atmosphere
- **Language match:** tone, terminology, key phrases
- **Promise match:** the core hook and promised outcome in the ad is the primary focus of the page

If the ad promises a specific quantifiable result (e.g., "30 to 50 high-ticket clients"), the landing page must lead with that exact outcome. If the ad uses a curiosity hook ("a Chinese import loophole"), the page must pay it off immediately.

Flag any disconnect between the ad hook and the destination page. A broken message match is a primary cause of funnel drop-off.

Completion: the ad hook, body, and CTA are consistent with the destination page's promise, language, and aesthetic.

### 10. Handle objections preemptively

Map the avatar's top objections to ad beats where they are addressed:

| Objection | Ad beat that addresses it |
|---|---|
| I don't believe it works | Bold guarantee in the hook or proof in the body |
| It won't work for me | Avatar-specific case study or "even if you've never..." language |
| It's too expensive | Value framing or risk reversal near the CTA |
| I don't trust the seller | Authority signals, testimonials, or origin story |
| Not right now | Urgency, scarcity, or cost-of-delay framing |
| I've tried this before | "New opportunity" framing — why this is different |

For cold calls, the qualification questions expose the real objections live. For video ads, objections must be answered preemptively in the script.

Completion: the top 2-3 objections are addressed before or at the CTA.

### 11. Assemble the final ad document

Use this output shape:

```markdown
# Ad: [Ad Name] for [Avatar]

## Scope
- Business:
- Business slug:
- Offer:
- Primary avatar:
- Traffic temperature: cold / warm / hot
- Awareness level: unaware / problem-aware / solution-aware / product-aware
- Platform:
- Campaign objective: click / registration / appointment / purchase
- Ad type: 6s / 15s / 30s / 60s+ / short-form / cold-call / webinar-promo / retargeting
- Length target: X seconds / Y words
- Destination after action:
- Confidence:
- Sources used:

## Ad Strategy
- One job: (earn the click / get the registration / set the appointment / drive the purchase)
- Core promise:
- Main objection addressed:
- Lead framework: (e.g., Becker TRT, PAS, BAB, Cardone Cold-Call)
- Message match to destination: confirmed / needs alignment

## Hook Options
1.
2.
3.
4.
5.

## Chosen Hook
- Hook:
- Opening frame / thumbnail:
- Rationale:

## Script

### [0:00-0:03] The Hook
[ON-CAMERA: ...]
{B-ROLL: ...}
{TEXT OVERLAY: ...}
[Script body]

### [0:03-0:15] The Body
[ON-CAMERA: ...]
{B-ROLL: ...}
[Script body]

### [0:15-0:25] The CTA
[ON-CAMERA: ...]
{B-ROLL: ...}
[Script body]

## Objection Map
| Objection | Addressed in beat |
|---|---|
| | |

## Proof and Claims
| Claim | Source | Risk |
|---|---|---|
| | | |

## Production Notes
- Presenter / creator:
- Tone and energy:
- Key B-roll assets needed:
- Text overlays to prepare:
- Caption style:
- Music direction:

## Testing Notes (if applicable)
- Hook variations to test:
- Body variations to test:
- CTA variations to test:
- Demographic matching notes:

## Needs Confirmation
- [unverified proof, risky claims, missing avatar inputs, unconfirmed scarcity, message match gaps]
```

For cold-call scripts, adapt the script section:

```markdown
## Cold-Call Script

### [0:00-0:05] The Greeting
[Script]

### [0:05-0:20] The Reason & Big Claim
[Script]

### [0:20-0:45] Qualification
[Script — problem question, magic question, money question, decision-maker filter]

### [0:45-0:60] The Appointment Proposal
[Script]

### [0:60-0:90] The Lock Close
[Script]

## Objection Responses
| Objection | Response |
|---|---|
| Not interested | |
| No time | |
| No budget | |
| Need to think about it | |
```

Completion: the document can be handed to a creator, editor, media buyer, or sales rep without reconstructing the strategy.

### 12. Update the wiki when appropriate

If working inside an LLM wiki:

- save the ad under `businesses/<business-slug>/ads/<ad-slug>.md`
- link it to the offer, avatar, character, brand voice, and destination page
- update `index.md` if appropriate
- append to `log.md`
- run `qmd update` if configured

Completion: the ad is filed under the correct business and reusable in later sessions.

## Missing Information Handling

Do not invent missing facts. Use these labels:

- `Unknown`: no source material supports the answer
- `Needs confirmation`: likely but not verified
- `Client to provide`: requires real proof, results, offer details, performance data, or platform specs only the client can give
- `Risk flag`: income, health, financial, legal, credential, or guarantee claim needing review
- `Out of scope`: a promise or component the offer or destination cannot support

If the offer or avatar is missing entirely, stop and route to `offer-builder` or `avatar-builder` first. An ad written without a real offer and avatar is generic noise, not a conversion asset.

If the destination page does not exist yet, flag the message-match risk and note what the page must deliver to pay off the ad's hook.

## Quality Bar

A strong ad script has:

- one business, one offer, one avatar, one traffic temperature, one platform, and one campaign objective
- a hook that stops the scroll in 3 seconds and pays off in the body
- a structure matched to the ad type and awareness level
- the avatar's real language for pain and desire
- real proof, or clearly flagged missing proof
- a CTA matched to the campaign objective — indirect for cold, direct for hot
- message match confirmed between the ad hook and the destination page
- ethical scarcity and urgency only, stated once near the CTA
- on-camera direction and B-roll notes throughout (for video ads)
- the brand voice and attractive character's signature phrases
- risky claims flagged
- a confidence level and source list
- testing notes if the ad is part of a creative testing campaign

A weak ad script has:

- a hook that promises what the body does not deliver
- a pitch-first structure that tries to sell the offer inside the ad
- invented testimonials or results
- generic guru copy with no avatar specificity
- fake scarcity or countdown pressure
- no on-camera direction, making it unusable for production
- a broken message match between the ad and the landing page
- a CTA that does not answer what happens next
- claims that create legal or credibility risk

## Common Pitfalls

1. **Selling the offer inside the ad.** The ad's job is to sell the click, registration, or appointment — not the full product. Trying to explain the entire mechanism in a 30-second ad burns attention and inflates CPA. Sell the next step.
2. **Weak first 3 seconds.** The hook is the entire ad. If the first frame and first line do not stop the scroll, the rest does not matter. Write 5-10 hooks and choose the strongest.
3. **Ignoring the awareness level.** A curiosity hook works on cold traffic but wastes hot traffic. A direct offer hook works on hot traffic but alienates cold traffic. Match the hook to the awareness level.
4. **Broken message match.** If the ad promises a specific outcome and the landing page leads with something different, the click is wasted. Confirm aesthetic, language, and promise match before the ad goes live.
5. **Inventing proof.** Every testimonial, stat, and result must come from real source material. Flag missing proof; do not fabricate it.
6. **Faking urgency.** If there is no real deadline or limited capacity, use cost-of-delay framing. Fake countdowns destroy trust and violate platform policies.
7. **No on-camera direction.** A video ad script without direction is a document, not a production asset. Add direction for every beat.
8. **Mismatched framework.** Using a webinar promo framework for a 15-second cold ad creates a structural mismatch. Choose the framework for the ad type, not the other way around.
9. **Padding short ads.** A 15-second ad stretched to 30 seconds with filler creates drop-off. If the message is simple, keep the ad short.
10. **Ignoring the opening frame.** On mobile feeds, the still frame before the video plays is the first impression. Specify it alongside the verbal hook.
11. **Cold-call scripts that pitch instead of qualify.** The goal of a cold call is an appointment, not a sale. State the reason, deliver the big claim, qualify, and propose a short meeting. Do not pitch the product on the first call.
12. **No testing plan.** A single ad is a gamble. Provide hook, body, and CTA variations for testing, and note which variables to isolate.

## Verification Checklist

- [ ] Business, offer, avatar, traffic temperature, platform, and campaign objective confirmed
- [ ] Offer, avatar, character, and voice pulled from the wiki, not invented
- [ ] Ad type chosen and justified by the campaign objective
- [ ] Framework chosen and justified by the ad type and awareness level
- [ ] 5-10 hook options written, chosen hook justified
- [ ] Hook pays off in the first 3 seconds and is delivered in the body
- [ ] Opening frame / thumbnail specified for video ads
- [ ] Body uses the avatar's real language
- [ ] CTA matched to the campaign objective (indirect for cold, direct for hot)
- [ ] CTA answers: what to do, what happens next, why now
- [ ] Message match confirmed between ad and destination page
- [ ] Top 2-3 objections addressed before or at the CTA
- [ ] Scarcity and urgency are ethical and documented, or replaced with cost-of-delay framing
- [ ] On-camera direction and B-roll notes present throughout (video ads)
- [ ] Proof is real or flagged as missing
- [ ] Risky claims (income, health, financial, legal) flagged
- [ ] Brand voice and character signature phrases used
- [ ] Testing notes included if part of a creative testing campaign
- [ ] Confidence level and source list included
- [ ] If wiki-backed, ad filed under `businesses/<business-slug>/ads/` and linked
- [ ] Final output follows the ad document shape
