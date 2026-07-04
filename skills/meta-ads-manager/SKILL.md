---
name: meta-ads-manager
description: Use when planning, structuring, launching, or auditing Meta (Facebook/Instagram) ad campaigns for a business. Produces a complete campaign structure document covering objectives, budget strategy (CBO vs ABO), ad set configuration, audience strategy, creative testing plan, and scaling readiness. Covers Sales, Leads, and App Promotion objectives.
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, meta-ads, facebook-ads, paid-social, campaigns, scaling]
    related_skills: [meta-creative-tester, meta-audience-builder, meta-ads-scaler, campaign-optimizer, meta-lead-gen, ad-creative-brief-writer, ad-script-writer, vsl-writer, hook-angle-writer, offer-builder, avatar-builder, brand-voice-extractor, human-editor]
---

# Meta Ads Manager

## Overview

Plan and structure Meta ad campaigns that turn ad spend into measurable outcomes. This skill produces a complete campaign architecture document — objectives, budget strategy, ad set configuration, audience strategy, creative plan, and scaling readiness — that a media buyer can execute against.

Meta Ads operates as a machine-learning system, not a traditional media-buying platform. The old playbook (interest stacking, manual bid manipulation, micro-targeting) has been replaced by Advantage+ (Meta's AI optimization). The media buyer's job is no longer to outsmart the algorithm; it is to feed it the right inputs: a clear objective, a clean conversion signal (Pixel/CAPI), strong creative, and a logical account structure that lets the algorithm learn.

Use `references/meta-ads-frameworks.md` for the detailed framework reference (campaign hierarchy, objective selection, CBO vs ABO, budget strategy, bidding, Pixel/CAPI setup). This file is the operating process.

The core discipline: structure for the algorithm, not against it. Every campaign decision should either improve the conversion signal, improve the creative, or remove friction from the buying path. Decisions that do none of these (vanity segmentation, over-testing, constant edits) reset the Learning Phase and waste spend.

## When to Use

Use this skill when the client asks for:

- a new Meta ad campaign from scratch
- a campaign structure or account audit
- a launch plan for a product, offer, or funnel on Meta
- a CBO vs ABO decision for a specific scenario
- an objective and conversion-location recommendation
- a budget strategy and pacing plan
- a creative testing structure (how many ad sets, how many creatives per ad set)
- a scaling plan (when and how to increase budget)
- a campaign restructure to escape the Learning Phase or fix broken performance
- a lead-gen or ecommerce campaign blueprint

Do not use this skill for:

- creative production itself (images, video, copy) — use `ad-script-writer`, `vsl-writer`, `ad-creative-brief-writer`
- audience research at the avatar level — use `avatar-builder`
- offer construction — use `offer-builder`
- daily optimization and metrics diagnosis — use `campaign-optimizer`
- the landing page or funnel the ads point to — use `funnel-page-writer` or `vsl-writer`

## Multi-Business Rule

A client can run several businesses, and each business can have many Meta ad accounts or campaigns. Never blend account facts, offers, avatars, or budgets across businesses. Before planning, confirm the business, business slug, Meta ad account ID, and the offer the campaign will promote.

Store campaign plans inside the client wiki under the correct business:

```text
businesses/<business-slug>/
├── brand.md
├── brand-voice.md
├── offers/
│   └── <offer-slug>.md
├── avatars/
│   └── <avatar-slug>.md
└── meta-ads/
    ├── account-overview.md
    └── campaigns/
        └── <campaign-slug>.md
```

If the wiki uses another structure, follow it while keeping every campaign grouped by business and linked to its offer, avatar, and creative assets.

## Source Hierarchy

Orient from the client wiki first. Read `SCHEMA.md`, `index.md`, recent `log.md`, and the target business pages before claiming facts. Then prioritize:

1. The offer document: dream outcome, price, mechanism, proof, objections, and the conversion event (purchase, lead, booking, trial).
2. The avatar profile: demographics, interests, awareness level, and the exact language that will stop their scroll.
3. Brand voice and attractive character: for creative direction and ad copy tone.
4. Existing assets: past campaign performance, winning creatives, known audience data, and Pixel/CAPI status.
5. Real proof and approved claims for ad copy.
6. Agent inference for structure and sequencing only — never for facts, proof, results, or claims.

Completion: the offer, avatar, conversion event, Pixel/CAPI status, and budget are known or marked unknown.

## Required Inputs

Minimum useful inputs:

- the business or brand
- the offer or product being promoted
- the conversion event (purchase, lead form, booking, trial signup, app install)
- the daily or lifetime budget range
- whether the Pixel and Conversions API are installed and firing

Best inputs:

- a completed offer document from `offer-builder`
- a completed avatar profile
- a brand voice guide
- existing creative assets (images, videos, copy) or a creative brief from `ad-creative-brief-writer`
- past campaign performance data (CTR, CPC, CPM, CPL, ROAS by campaign/creative)
- the landing page or funnel URL the ads will point to
- known audience data (customer list size, lookalike sources, retargeting pool)
- product catalog (for ecommerce / Advantage+ Shopping Campaigns)

Completion: there is enough source material to structure a campaign without guessing at the offer, the conversion event, or the creative direction.

## Core Workflow

### 1. Orient to the wiki

If working inside a client wiki, read:

- `SCHEMA.md`, `index.md`, recent `log.md`
- the target business's brand, offer, avatar, character, voice, and any existing `meta-ads/` plans

Completion: the campaign context, source assets, and save path are known.

### 2. Confirm campaign scope

Define before structuring:

- business and business slug
- Meta ad account ID (or a note that one needs to be created)
- offer and offer slug
- primary avatar
- conversion event and conversion location (website, app, Messenger, WhatsApp)
- traffic temperature: cold, warm, or hot
- daily or lifetime budget
- campaign objective (see objective selection below)
- campaign type: manual structure or Advantage+ (Shopping, Audience)
- Pixel and CAPI status
- confidence level and source list

Completion: the campaign is tied to one business, one offer, one avatar, one conversion event, and one budget.

### 3. Verify the conversion signal first

Before any campaign structure, confirm the conversion signal is clean. This is non-negotiable — Meta's algorithm optimizes against the conversion events it receives. A broken or partial signal produces broken optimization.

Checklist:

- [ ] Pixel installed on the conversion page (checkout, lead form confirmation, booking confirmation)
- [ ] Pixel firing on the target event (Purchase, Lead, CompleteRegistration, Schedule)
- [ ] Conversions API (CAPI) installed server-side (reduces iOS 14.5+ attribution loss)
- [ ] Event Match Quality (EMQ) above 6/10 (ideally 8+)
- [ ] Domain verified in Meta Business Manager
- [ ] Aggregated Event Measurement (AEM) events configured (max 8 domain events per domain, prioritized)
- [ ] First-party data enrichment enabled (CAPI sharing user data: email, phone, name)

If any of these are missing, the campaign structure is premature. Flag the gaps and recommend the Pixel/CAPI setup be completed first. A campaign launched against a broken signal will spend money learning the wrong thing.

Completion: the conversion signal is verified or the gaps are documented as blocking.

### 4. Choose the objective

Meta's objective determines what the algorithm optimizes for. Pick the objective that matches the conversion event — not the one that sounds cheapest.

| Objective | Optimizes for | When to use |
|---|---|---|
| **Sales (Advantage+ Shopping)** | Purchases on website or app | Ecommerce with a product catalog. Meta's AI handles targeting, placement, and creative combinations. |
| **Sales (manual)** | Purchases on website | Ecommerce without a catalog, or when you need control over audience/placement. |
| **Leads** | Lead form submissions or onsite lead events | Lead gen (B2B, services, info-products with application funnels). |
| **Engagement** | Post engagement, video views, messages | Top-of-funnel awareness, video view campaigns, Messenger/WhatsApp lead-in. |
| **Traffic** | Link clicks (optimized for landings) | Cheap traffic, but rarely converts. Use only when conversion tracking is unavailable or for content promotion. |
| **Awareness** | Ad recall or reach | Brand awareness, retargeting pool building. Not for direct response. |
| **App Promotion** | App installs or in-app events | Mobile apps. Pair with CAPI for in-app events. |

**Objective selection rule:** always choose the objective closest to the actual business outcome. "Traffic" is cheaper than "Sales" but optimizes for clickers, not buyers. The cheap CPC is a trap if the conversion event is purchase.

For most direct-response campaigns, the answer is **Sales** (ecommerce) or **Leads** (services, info-products, B2B).

Completion: the objective is chosen and justified by the conversion event.

### 5. Choose CBO vs ABO

This is the most consequential structural decision after objective selection.

**CBO (Advantage Campaign Budget, now "Advantage campaign budget"):**
- Budget is set at the campaign level; Meta distributes it across ad sets based on performance
- Best for: scaling winners, ecommerce, campaigns where you trust the algorithm
- Pros: lets Meta route spend to the best-performing ad set automatically, simplifies management
- Cons: less control over individual ad set spend, a dominant ad set can starve others
- Use when: you have 2-5 ad sets with proven creative, you want to scale, you trust the Pixel signal

**ABO (Ad Set Budget Optimization):**
- Budget is set at the ad set level; you control spend per ad set
- Best for: testing, forced spend on specific audiences, control-oriented buyers
- Pros: precise spend control, forces the algorithm to spend on audiences you want tested
- Cons: prevents the algorithm from routing spend optimally, more management overhead
- Use when: testing new creative/audiences, you need to force spend on a specific segment, you are launching a new offer and want controlled data

**The modern default:** start with ABO for testing (forces spend evenly to gather data), switch to CBO once you identify winners and want to scale.

Completion: the budget strategy is chosen and justified by the testing vs scaling phase.

### 6. Structure the campaign

Build the campaign → ad set → ad hierarchy. See `references/meta-ads-frameworks.md` for the detailed structure patterns.

**Standard testing structure (ABO, new offer or new creative):**

```
Campaign 1: [Offer] — Cold Testing (Objective: Sales/Leads, ABO)
├── Ad Set 1: Broad Audience (Advantage+ Audience, no interests)
│   ├── Ad 1: Creative Variant A (hook 1, static)
│   ├── Ad 2: Creative Variant B (hook 2, video)
│   └── Ad 3: Creative Variant C (hook 3, carousel)
├── Ad Set 2: Lookalike 1% (based on purchaser list)
│   ├── Ad 1: Creative Variant A
│   ├── Ad 2: Creative Variant B
│   └── Ad 3: Creative Variant C
└── Ad Set 3: Interest Stack (3-5 relevant interests)
    ├── Ad 1: Creative Variant A
    ├── Ad 2: Creative Variant B
    └── Ad 3: Creative Variant C
```

**Standard scaling structure (CBO, once winners are identified):**

```
Campaign 2: [Offer] — Scaling (Objective: Sales/Leads, CBO)
├── Ad Set 1: Broad (Advantage+ Audience) — winning creative
│   ├── Ad 1: Winning Creative (proven)
│   ├── Ad 2: Variation of Winner (new hook, same body)
│   └── Ad 3: Variation of Winner (new visual, same hook)
├── Ad Set 2: Lookalike 1-3% — winning creative
│   └── Ad 1: Winning Creative
└── Ad Set 3: Retargeting (90-day engagers, excluded purchasers)
    └── Ad 1: Winning Creative (social proof variant)
```

**Retargeting campaign (separate, always-on):**

```
Campaign 3: [Offer] — Retargeting (Objective: Sales/Leads, ABO, low budget)
└── Ad Set 1: 30-day engagers, excluded 30-day purchasers
    ├── Ad 1: Social proof creative (testimonials, UGC)
    └── Ad 2: Offer reminder / scarcity creative
```

Completion: the full campaign hierarchy is mapped with budget allocation per ad set.

### 7. Configure each ad set

For each ad set, define:

- **Conversion location:** website, app, Messenger, WhatsApp
- **Optimization event:** Purchase, Lead, Add to Cart, etc.
- **Bid strategy:** see bidding section in `references/meta-ads-frameworks.md`
- **Budget:** daily or lifetime, amount
- **Audience:** Advantage+ Audience (broad), Lookalike, Custom, or Interest
- **Placements:** Advantage+ placements (recommended) or manual
- **Schedule:** start date, end date, dayparting (if lifetime budget)
- **Exclusions:** recent purchasers (to avoid wasting spend on converters)

**Audience strategy summary** (see `meta-audience-builder` skill for depth):
- **Broad (Advantage+ Audience):** no interests, let Meta find buyers. Works well with strong creative and a clean Pixel. Often outperforms interest targeting at scale.
- **Lookalike:** based on purchaser list, lead list, or engagers. Start at 1%, expand to 1-3%, 1-5%, 1-10% as you scale.
- **Custom:** retargeting (engagers, visitors, customer list), exclusions (recent purchasers).
- **Interest:** 3-5 relevant interests, used primarily for testing and when Pixel data is thin.

Completion: every ad set has a fully defined configuration.

### 8. Plan the creative testing matrix

Creative is the #1 variable in Meta Ads performance (more than targeting, bidding, or budget). Structure creative testing deliberately.

**Creative testing principles:**
- Creative is the #1 lever — allocate budget and effort here first
- Test one variable per ad set (hook, format, angle, offer framing)
- 3-5 creatives per ad set for testing
- Run for at least 4-7 days or until each creative has 50+ conversions before judging
- Identify winners by cost per conversion, not CTR alone
- Kill losers at a defined threshold (e.g., 2x target CPL with 50+ conversions)
- Scale winners by duplicating into a CBO campaign

See the `meta-creative-tester` skill for the full testing methodology.

Completion: the creative testing matrix is defined — what is being tested, in which ad set, for how long, and with what kill/scale criteria.

### 9. Set the budget strategy

Budget decisions depend on the phase.

**Testing phase (ABO):**
- Minimum $10-20/day per ad set (Meta needs enough spend to exit the Learning Phase)
- 3 ad sets × $20/day = $60/day minimum to gather usable data
- Run for 4-7 days minimum before judging

**Scaling phase (CBO):**
- Start with the total daily budget of the winning ABO campaign
- Scale vertically (increase budget) or horizontally (duplicate to new audiences)
- See `meta-ads-scaler` skill for the scaling rules

**Budget rule of thumb:** spend at least 50x the CPA target in the first week to give the algorithm enough signal. If the target CPL is $20, plan to spend at least $1,000 in the first week.

Completion: the budget plan covers the testing and scaling phases with clear dollar amounts and timelines.

### 10. Assemble the campaign document

Use this output shape:

```markdown
# Meta Ads Campaign Plan: [Offer] for [Avatar]

## Scope
- Business:
- Business slug:
- Meta ad account ID:
- Offer:
- Primary avatar:
- Conversion event:
- Traffic temperature: cold / warm / hot
- Daily / lifetime budget:
- Pixel/CAPI status:
- Confidence:
- Sources used:

## Conversion Signal Readiness
- [ ] Pixel installed on conversion page
- [ ] Pixel firing target event
- [ ] CAPI installed server-side
- [ ] EMQ score:
- [ ] Domain verified
- [ ] AEM events configured
- [ ] First-party data enrichment
- Gaps blocking launch:

## Campaign Strategy
- Objective:
- Campaign type: Advantage+ / manual
- Budget strategy: CBO / ABO
- Phase: testing / scaling
- Estimated launch date:

## Campaign Structure

### Campaign 1: [Name] — [Phase]
- Objective:
- Budget strategy:
- Daily budget:
- Bid strategy:

#### Ad Set 1: [Audience name]
- Conversion location:
- Optimization event:
- Audience type: Broad / Lookalike / Custom / Interest
- Audience definition:
- Placements: Advantage+ / manual
- Daily budget:
- Exclusions:
- Ads:
  1. [Creative variant A — what it tests]
  2. [Creative variant B — what it tests]
  3. [Creative variant C — what it tests]

#### Ad Set 2: ...

### Campaign 2: [Retargeting — always-on]
...

## Creative Testing Plan
- Variables tested (by ad set):
- Creatives per ad set:
- Test duration:
- Winner criteria:
- Kill criteria:

## Budget Plan
- Testing phase: $X/day for Y days
- Scaling phase trigger:
- Scaling budget ceiling:

## Scaling Readiness
- Conditions to move from testing to scaling:
- Scaling method: vertical / horizontal
- Scaling budget steps:

## Needs Confirmation
- [unverified audience sizes, unconfirmed Pixel status, missing creative assets, unconfirmed budget]
```

Completion: the document can be handed to a media buyer to execute without reconstructing the strategy.

### 11. Update the wiki when appropriate

If working inside an LLM wiki:

- save the campaign plan under `businesses/<business-slug>/meta-ads/campaigns/<campaign-slug>.md`
- link it to the offer, avatar, character, and creative assets
- update `index.md` if appropriate
- append to `log.md`
- run `qmd update` if configured

Completion: the plan is filed under the correct business and reusable in later sessions.

## Missing Information Handling

Do not invent missing facts. Use these labels:

- `Unknown`: no source material supports the answer
- `Needs confirmation`: likely but not verified
- `Client to provide`: requires ad account access, Pixel status, budget confirmation, or creative assets
- `Risk flag`: income, health, financial, or legal claim in ad copy needing review
- `Out of scope`: a campaign type, objective, or audience the business cannot currently support

If the offer, avatar, or conversion event is missing, stop and route to `offer-builder` or `avatar-builder` first. A campaign structure built without a clear conversion event is a plan to waste budget.

## Quality Bar

A strong campaign plan has:

- one business, one offer, one avatar, one conversion event, and one traffic temperature
- a verified or gap-documented conversion signal (Pixel + CAPI)
- an objective justified by the conversion event
- a CBO vs ABO decision justified by the testing vs scaling phase
- a clear campaign → ad set → ad hierarchy with budget allocation
- a creative testing matrix with clear variables and criteria
- a budget plan covering testing and scaling phases
- realistic minimum budgets (not $5/day expecting conversions)
- retargeting separated from cold acquisition
- exclusions configured (recent purchasers)
- risky claims and unknowns flagged
- a confidence level and source list

A weak campaign plan has:

- an objective chosen for cheap CPC rather than business outcome
- ABO used for scaling or CBO used for testing (backwards)
- micro-budgets expecting meaningful data ($5/day, 2 days)
- no conversion signal verification
- interest-stacked audiences with no clear rationale
- no creative testing structure (one creative per ad set, no variables)
- retargeting mixed with cold acquisition
- no exclusions (wasting spend on recent converters)
- no scaling plan beyond "increase budget"

## Common Pitfalls

1. **Choosing Traffic objective.** Traffic optimizes for clickers, not buyers. The cheap CPC is a trap if you want conversions. Choose Sales or Leads.
2. **CBO for testing.** CBO routes spend to the early winner, starving the variants you need to test. Use ABO for testing, CBO for scaling.
3. **Skipping the Pixel/CAPI check.** Launching against a broken signal teaches the algorithm the wrong thing. Verify first.
4. **Micro-budgets.** $5/day for 2 days produces no usable data. Meta needs ~50 conversions per ad set per week to exit the Learning Phase.
5. **Interest stacking.** Over-targeting (10+ interests, narrow ages, narrow placements) starves the algorithm. Broad often beats interest at scale.
6. **No creative testing structure.** One creative per ad set tests nothing. You need 3-5 variants to learn what works.
7. **Mixing retargeting with cold.** Retargeting creative (social proof, offer reminders) is different from cold creative (pattern interrupts, problem agitation). Separate them.
8. **Editing during the Learning Phase.** Every edit (budget, audience, creative) resets the Learning Phase. Set it and leave it for 4-7 days.
9. **Judging too early.** A campaign with 5 conversions and $20 spend tells you nothing. Wait for statistical significance.
10. **No exclusions.** Showing purchase ads to recent purchasers wastes spend and annoys customers.
11. **Ignoring Advantage+ placements.** Manual placement selection (only Facebook feed, only Instagram) reduces inventory and raises CPM. Let Advantage+ optimize unless you have a specific reason.
12. **Bidding too conservatively.** Lowest cost with a bid cap set too low throttles delivery. Use lowest cost (no cap) for most campaigns; use cost cap only for efficiency optimization at scale.

## Verification Checklist

- [ ] Business, ad account, offer, avatar, and conversion event confirmed
- [ ] Conversion signal verified (Pixel + CAPI + EMQ + AEM)
- [ ] Objective chosen and justified by the conversion event
- [ ] CBO vs ABO chosen and justified by testing vs scaling phase
- [ ] Campaign hierarchy mapped with budget allocation per ad set
- [ ] Each ad set has a fully defined configuration
- [ ] Creative testing matrix defines variables, creatives per ad set, duration, winner and kill criteria
- [ ] Budget plan covers testing and scaling phases with realistic minimums
- [ ] Retargeting separated from cold acquisition
- [ ] Exclusions configured (recent purchasers, recent converters)
- [ ] Placements strategy justified (Advantage+ default unless specific reason)
- [ ] Bid strategy justified
- [ ] Scaling readiness conditions documented
- [ ] Risky claims and unknowns flagged
- [ ] Confidence level and source list included
- [ ] If wiki-backed, plan filed under `businesses/<business-slug>/meta-ads/campaigns/` and linked
- [ ] Final output follows the campaign document shape
