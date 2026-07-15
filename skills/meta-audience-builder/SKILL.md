---
name: meta-audience-builder
description: Use when building the audience strategy for a Meta (Facebook/Instagram) ad campaign — choosing between broad, lookalike, custom, and interest audiences; designing retargeting sequences; and configuring exclusions. Produces a complete audience stack document covering data sources, audience tiers, sizing, exclusion design, and sequencing. Pairs with meta-ads-manager (campaign structure) and meta-creative-tester (creative testing).
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, meta-ads, facebook-ads, audiences, targeting, lookalike, retargeting, paid-social]
    related_skills: [meta-ads-manager, meta-creative-tester, meta-ads-scaler, campaign-optimizer, meta-lead-gen, avatar-builder, offer-builder, brand-voice-extractor, human-editor]
---

# Meta Audience Builder

## Overview

Design the audience stack for a Meta ad campaign — who sees the cold ads, who gets retargeted, who is excluded, and why. This skill produces a complete audience strategy document that a media buyer can execute against: data sources inventoried, audience tiers chosen, sizing validated, retargeting sequenced, and exclusions configured.

Meta Ads targeting has been re-architected around the algorithm. The old inputs — interest stacks, layered behaviors, narrow demographics — are no longer hard boundaries. Meta treats them as "audience suggestions" and will deliver beyond them whenever the conversion signal predicts a result. Advantage+ Audience (broad targeting) has been shown to drive ~28% lower CPC and ~7% lower cost per conversion than manual interest targeting. The creative itself now does the targeting: Meta's Andromeda/Advantage+ AI analyzes the visual, the text overlays, and the video transcript to match ads to relevant users in real time.

Use `references/audience-frameworks.md` for the detailed framework reference (audience types, lookalike tier expansion, retargeting sequencing, exclusion design, sizing rules). This file is the operating process.

The core discipline: build audiences for the algorithm, not against it. Feed it high-quality first-party data as seeds, let the creative define the audience pocket, keep swim lanes clean with exclusions, and resist the urge to micro-target. Over-constraining an audience starves the algorithm, drives up CPM, and blocks the lowest-cost conversions.

## When to Use

Use this skill when the client asks for:

- an audience strategy for a new or existing Meta campaign
- a decision between broad (Advantage+ Audience), lookalike, custom, or interest targeting
- a lookalike audience build — source list selection, percentage tier, and expansion plan
- a retargeting sequence — windows, frequency, creative rotation, objection dismantling
- an exclusion design — recent purchasers, recent converters, cross-funnel integrity
- an audience sizing check — whether the available audience is large enough to run and scale
- a retargeting saturation or fatigue diagnosis
- an audit of an existing audience stack that is underperforming
- a recommendation on when to let broad replace interest targeting

Do not use this skill for:

- the overall campaign structure (objective, CBO/ABO, budget allocation, creative testing matrix) — use `meta-ads-manager`
- the creative itself (images, video, copy, hooks) — use `meta-creative-tester`, `ad-script-writer`, `hook-angle-writer`
- the avatar or persona research at the buyer-psychology level — use `avatar-builder`
- daily optimization, metrics diagnosis, and budget pacing — use `campaign-optimizer`
- the landing page or funnel the ads point to — use `funnel-writer` or `vsl-writer`

## Multi-Business Rule

A client can run several businesses, and each business can have many Meta ad accounts, customer lists, and audience sources. Never blend audiences, customer lists, Pixel data, or exclusion lists across businesses. Before building, confirm the business, business slug, Meta ad account ID, and the offer the audiences will serve.

Store audience plans inside the client wiki under the correct business:

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
    ├── audiences/
    │   └── <campaign-or-audience-slug>.md
    └── campaigns/
        └── <campaign-slug>.md
```

If the wiki uses another structure, follow it while keeping every audience plan grouped by business and linked to its campaign, offer, and avatar.

## Source Hierarchy

Orient from the client wiki first. Read `SCHEMA.md`, `index.md`, recent `log.md`, and the target business pages before claiming facts. Then prioritize:

1. The offer document: conversion event, price, margin, and whether the offer supports a retargeting sequence (single-purchase vs repeat-purchase).
2. The avatar profile: demographics, awareness level, and traffic temperature the audiences must serve (cold, warm, hot).
3. Existing audience data: customer list size and quality, Pixel event volume, engager counts, and any pre-built lookalikes or saved audiences.
4. Conversion signal status: Pixel + CAPI firing, EMQ score, and event volume — audience quality depends on the data feeding the algorithm.
5. Past performance: which audience types have worked for this business before, and the CPA/ROAS by audience.
6. Real proof and approved claims for any retargeting creative angles.
7. Agent inference for structure and sequencing only — never for audience sizes, list counts, or event volumes.

Completion: the offer, avatar, conversion event, available data sources, and signal status are known or marked unknown.

## Required Inputs

Minimum useful inputs:

- the business or brand
- the offer or product being promoted
- the conversion event (purchase, lead form, booking, trial signup, app install)
- traffic temperature the audience must serve (cold, warm, hot, or all three)
- whether a Pixel is installed and firing the target event
- whether a customer list exists (email, phone, or both)

Best inputs:

- a completed offer document from `offer-builder`
- a completed avatar profile
- a campaign plan from `meta-ads-manager` (so the audience serves a defined structure)
- customer list size and quality (total, recent purchasers, high-LTV segment)
- Pixel event volumes in Event Manager (view content, add to cart, initiate checkout, purchase)
- engager counts (video viewers, page engagers, lead form openers)
- past audience performance data (CPA, ROAS, frequency by audience type)
- known lookalike sources and any existing saved audiences
- the daily or lifetime budget (determines how many audiences are viable)

Completion: there is enough source material to build an audience stack without guessing at list sizes, event volumes, or traffic temperature.

## Core Workflow

### 1. Orient to the wiki

If working inside a client wiki, read:

- `SCHEMA.md`, `index.md`, recent `log.md`
- the target business's brand, offer, avatar, and any existing `meta-ads/` plans and audiences

Completion: the audience context, source assets, and save path are known.

### 2. Confirm audience scope

Define before building:

- business and business slug
- Meta ad account ID
- offer and offer slug
- primary avatar
- conversion event and conversion location (website, app, Messenger, WhatsApp)
- traffic temperatures to cover: cold, warm, hot (or a subset)
- daily or lifetime budget
- campaign objective the audiences serve (determines optimization event)
- available data sources: customer list, Pixel data, engagers, app users
- confidence level and source list

Completion: the audience stack is tied to one business, one offer, one avatar, one conversion event, and one traffic-temperature scope.

### 3. Audit available data sources

Audience strategy is only as good as the data feeding it. Inventory what exists before choosing a tier strategy.

For each source, capture type, size, quality, and freshness:

- **Customer list (first-party):** total records, recency, source (CRM, Klaviyo, Shopify, manual upload), segmentation available (purchasers, high-LTV, recent buyers, churned buyers, qualified leads). This is the highest-value data — it seeds lookalikes and powers exclusions.
- **Pixel event volume (Event Manager):** event name (ViewContent, AddToCart, InitiateCheckout, Purchase), 30/90/180-day counts, and whether CAPI is enriching the signal. Look for events with at least 10,000 actions to support consistent retargeting delivery.
- **Engagers (platform-based):** video viewers by threshold (25%, 50%, 75%, 95%), page engagers, lead form openers, Instagram/Facebook profile engagers — by count and time window.
- **Website visitors:** by time window (30/90/180 days) and page visited (key landing pages, product pages, checkout).
- **App users:** if applicable, active users and in-app event volume.
- **Offline activity:** in-store conversions via offline event set, if configured.

Completion: every available first-party and platform data source is inventoried with a size estimate and a confidence label (`Verified`, `Estimated`, `Unknown`).

### 4. Choose the audience tier strategy

Pick the primary acquisition approach based on data depth, creative strength, and budget. See `references/audience-frameworks.md` for the decision matrix.

| Strategy | When to choose | Requires |
|---|---|---|
| **Broad-first (Advantage+ Audience)** | 100+ conversions/month, strong creative, $50+/day budget, clean Pixel+CAPI | Clean conversion signal + strong creative + adequate budget |
| **Lookalike-first** | Quality customer list (purchasers, high-LTV, qualified leads), newer account building first-party seed | A seeded custom audience of at least 100 quality records |
| **Interest-first** | Thin Pixel data, new market entry, niche B2B, or testing a specific hypothesis | 3-5 relevant interests; a reason for each |
| **Hybrid (recommended for most)** | Established account with data — run broad, lookalike, and interest as parallel ad sets in ABO | Enough budget to fund 3 ad sets at $20+/day each |

**The modern default:** with adequate data, run a hybrid cold stack — Advantage+ Audience (broad), a 1% lookalike on the best seed, and a 3-5 interest ad set — in ABO, let the algorithm tell you which wins, then consolidate into CBO. This gives the algorithm maximum learning surface while you gather signal on which audience type converts cheapest.

**When broad beats interest (the threshold):** when the account has 100+ conversions/month, strong creative, and $50+/day budget, Advantage+ Audience (broad) typically outperforms interest targeting. Broad gives the algorithm maximum inventory and lets the creative do the targeting. Below that threshold, interest and lookalike add useful signal.

Completion: the primary acquisition strategy is chosen and justified by data depth, creative strength, and budget.

### 5. Build the audience stack

Map the full stack across the funnel. Every campaign should have a defined cold layer, a retargeting layer, and an exclusion layer — even if some layers run in separate campaigns.

**Standard audience stack (hybrid cold + retargeting + exclusions):**

```
Cold acquisition (one campaign, ABO or CBO)
├── Ad Set 1: Advantage+ Audience (broad — age, gender, location only)
├── Ad Set 2: Lookalike 1% (seed: purchasers or high-LTV customers)
├── Ad Set 3: Interest (3-5 relevant interests)
│   Exclusions (applied to all cold ad sets):
│   - Recent purchasers (180 days to all-time)
│   - Current customers / active subscribers
│   - Recent converters (last 30 days) if running a separate retargeting campaign

Retargeting (separate, always-on, low budget)
├── Ad Set 1: 30-day engagers (video 50%+, page engagers), excluded purchasers
├── Ad Set 2: 90-day website visitors (key pages), excluded purchasers
├── Ad Set 3: Abandoned cart / abandoned form (bottom-funnel, highest intent)
│   Exclusions: recent purchasers; anyone already in the bottom-funnel ad set
```

For each audience in the stack, define:

- **Audience type:** Advantage+ Audience, Lookalike (with tier and seed), Custom (with source and window), Interest (with the 3-5 interests listed)
- **Size estimate:** from Audience Manager or calculated from event volume
- **Optimization event:** the conversion event the ad set optimizes toward
- **Daily budget:** minimum $20/day per ad set to exit the Learning Phase
- **Creative angle:** the awareness level the creative must match (cold = pattern interrupt/problem; warm = mechanism/proof; hot = offer/scarcity)
- **Exclusions applied:** the lists/events excluded from this ad set

Completion: every audience in the stack is defined with type, size, budget, optimization event, creative angle, and exclusions.

### 6. Configure exclusions

Exclusions are what keep swim lanes clean. Without them, prospecting budget leaks into retargeting, retargeting fatigues warm audiences, and recent purchasers see purchase ads.

**Mandatory exclusions:**

- **Recent purchasers from all cold acquisition:** 180 days to all-time. Prevents spending acquisition budget on people who already bought.
- **Current customers / active subscribers from new-customer offers:** prevents showing acquisition offers to existing customers.
- **Recent converters from conversion campaigns:** prevents double-counting and attribution noise.
- **Mid-funnel handoff:** when a cold prospect engages (clicks, views, watches 25%+), they should move out of the cold pool and into the retargeting pool. Either exclude engaged users from cold ad sets or rely on a separate retargeting campaign that captures them.

**Optional / situational exclusions:**

- **Saturation control:** exclude high-frequency users (saw the ad 4+ times) to refresh delivery.
- **Funnel-stage integrity:** exclude people who reached checkout but did not purchase from upper-funnel retargeting (move them to the bottom-funnel abandoned-cart ad set instead).

**The over-exclusion trap:** do not exclude all page engagers or all website visitors from cold prospecting. Over-micromanaging exclusions limits delivery options, drives up CPM, and blocks the algorithm from finding low-cost conversions. Exclude recent purchasers and current customers; let the rest stay available.

**The 2025 platform change:** as of March 31, 2025, Meta removed detailed targeting (interest-based) exclusions from active campaigns. Custom audience exclusions (uploaded CRM lists, Klaviyo tags, Pixel events) and high-level audience controls still work — use those.

Completion: every ad set has its exclusion set defined, justified, and free of over-exclusion.

### 7. Size the audiences

An audience too small will not deliver consistently; too large and the algorithm may take longer to converge. Validate size against the optimization event and budget.

**Minimum viable audience sizes:**

| Audience type | Minimum to run | Comfortable scale |
|---|---|---|
| **Lookalike (1%)** | ~50,000+ (depends on country) | Country-dependent; 1% of US ≈ 2.6M |
| **Custom (retargeting)** | 1,000+ active users in window | 10,000+ for consistent delivery |
| **Pixel event (retargeting)** | 10,000+ actions in window | Ensures stable, non-fatiguing delivery |
| **Interest** | 500,000+ in the selected interests | 1M+ preferable for scale |
| **Broad (Advantage+ Audience)** | N/A — Meta defines the size | Works at any scale above the budget floor |

**Sizing rules:**

- Retargeting audiences below 1,000 active users will struggle to spend — either widen the time window or move the event up the funnel (retarget ViewContent instead of AddToCart).
- If a retargeting audience saturates, expand the window (30 → 90 days) or move the event up the funnel (AddToCart → ViewContent).
- Lookalike source lists should have at least 100 quality records to seed meaningfully; 1,000+ is better. Quality matters more than size — a list of 500 high-LTV purchasers beats a list of 5,000 low-value leads.
- Broad audiences have no practical size concern — the constraint is budget and creative, not audience size.

Completion: every audience meets or flags the minimum viable size, and any undersized audience has a remediation (widen window, move event up funnel, expand tier).

### 8. Document the sequencing

For retargeting, document the sequence a user moves through from first touch to purchase. This is what makes retargeting a conversation rather than a repetitive bombardment.

**Standard retargeting sequence (ecommerce, short sales cycle):**

```
Day 0: Cold ad impression (broad/lookalike/interest)
  ↓ user engages (clicks, views 25%+, visits site)
Day 1-7: Retargeting Tier 1 — 30-day engagers
  - Frequency target: 5-8 impressions over 7 days
  - Creative: objection-dismantling rotation (product/fit, UGC social proof, third-party editorial)
  ↓ no purchase
Day 8-14: Retargeting Tier 2 — 90-day visitors + cart abandoners
  - Creative: offer reminder, scarcity, risk reversal
  ↓ no purchase
Day 15+: Cool down or move to evergreen retention
  - Exclude from active retargeting to prevent fatigue
```

**High-ticket / long sales cycle sequence:**

```
Level 1 (Cold prospecting): Broad/lookalike/interest, unrestricted
  ↓ watches ≥25% of an L1 video ad
Level 2 (Warm engagement): Retarget strictly for a 30-day window
  - Match window to average sales-cycle duration
  ↓ visits site or engages deeper
Level 3 (Evergreen/retention): Website visitors (30d) + add-to-carts (90d)
  - Long-term retention sequences for past buyers:
    - Target past buyers at 60 days, exclude last 45 days (repurchase/restock)
    - Target past buyers at 90 days, exclude last 75 days
```

For each sequence, document:

- **Entry trigger:** the action that moves a user into this tier (engagement threshold, site visit, cart event)
- **Time window:** how long they stay in this tier
- **Frequency target:** impressions per user per window (5-8 for short-cycle retargeting; lower for high-ticket)
- **Creative rotation:** the 2-4 angles rotated to dismantle different objections without fatigue
- **Exit / handoff:** the action that moves them out (purchase → retention; no purchase after window → cool down or expand)

Completion: the retargeting sequence is documented end-to-end with entry triggers, windows, frequency, creative rotation, and exit rules.

### 9. Assemble the audience document

Use this output shape:

```markdown
# Meta Audience Strategy: [Offer] for [Avatar]

## Scope
- Business:
- Business slug:
- Meta ad account ID:
- Offer:
- Primary avatar:
- Conversion event:
- Traffic temperatures covered: cold / warm / hot
- Daily / lifetime budget:
- Pixel/CAPI status:
- Confidence:
- Sources used:

## Data Source Inventory
| Source | Type | Size | Quality | Freshness | Confidence |
|---|---|---|---|---|---|
| Customer list (purchasers) | First-party | | | | |
| Customer list (high-LTV) | First-party | | | | |
| Pixel — Purchase event | Platform | | | | |
| Pixel — AddToCart event | Platform | | | | |
| Pixel — ViewContent event | Platform | | | | |
| Engagers (video 50%+) | Platform | | | | |
| Page engagers | Platform | | | | |
| Website visitors (90d) | Platform | | | | |

## Audience Tier Strategy
- Primary approach: Broad-first / Lookalike-first / Interest-first / Hybrid
- Rationale:
- Broad-beats-interest threshold met? (100+ conversions/mo, strong creative, $50+/day)

## Audience Stack

### Cold Acquisition
#### Ad Set 1: Advantage+ Audience (Broad)
- Definition: age, gender, location only — no interests
- Size estimate:
- Optimization event:
- Daily budget:
- Creative angle:
- Exclusions:

#### Ad Set 2: Lookalike 1%
- Seed source:
- Tier: 1% / 1-3% / 1-5% / 1-10%
- Size estimate:
- Optimization event:
- Daily budget:
- Creative angle:
- Exclusions:

#### Ad Set 3: Interest
- Interests (3-5):
- Size estimate:
- Optimization event:
- Daily budget:
- Creative angle:
- Exclusions:

### Retargeting (separate, always-on)
#### Ad Set 1: 30-day engagers
- Source:
- Size estimate:
- Frequency target:
- Creative rotation (angles):
- Exclusions:

#### Ad Set 2: 90-day website visitors
...

#### Ad Set 3: Abandoned cart / abandoned form
...

## Exclusion Design
- Recent purchasers: window (180d / all-time)
- Current customers / subscribers:
- Recent converters:
- Mid-funnel handoff rule:
- Over-exclusion check (no blanket engager/visitor exclusions):

## Retargeting Sequence
| Tier | Entry trigger | Time window | Frequency | Creative angles | Exit / handoff |
|---|---|---|---|---|---|
| Tier 1 (warm) | | | | | |
| Tier 2 (mid) | | | | | |
| Tier 3 (bottom) | | | | | |

## Sizing Validation
| Audience | Size | Minimum met? | Remediation if undersized |
|---|---|---|---|
| | | | |

## Needs Confirmation
- [unverified audience sizes, unconfirmed Pixel event volumes, missing customer list, unconfirmed budget]
```

Completion: the document can be handed to a media buyer to build the audiences in Ads Manager without reconstructing the strategy.

### 10. Update the wiki when appropriate

If working inside an LLM wiki:

- save the audience plan under `businesses/<business-slug>/meta-ads/audiences/<audience-slug>.md`
- link it to the campaign, offer, avatar, and creative assets
- update `index.md` if appropriate
- append to `log.md`
- run `qmd update` if configured

Completion: the plan is filed under the correct business and reusable in later sessions.

## Missing Information Handling

Do not invent missing facts. Use these labels:

- `Unknown`: no source material supports the size, volume, or quality
- `Needs confirmation`: likely but not verified (e.g., estimated customer list size)
- `Client to provide`: requires ad account access, Event Manager export, CRM export, or Pixel diagnostics
- `Risk flag`: an exclusion or targeting choice that could exclude buyers, violate policy, or cause delivery failure
- `Out of scope`: an audience type the business cannot currently support (e.g., app users without an app, offline events without an offline event set)

If the conversion event or customer list is missing entirely, flag it as blocking. Audience strategy built without a conversion event or any first-party data is a plan built on guesses.

## Quality Bar

A strong audience plan has:

- one business, one offer, one avatar, one conversion event, and a defined traffic-temperature scope
- a data source inventory with sizes, quality, and confidence labels
- a tier strategy justified by data depth, creative strength, and budget
- a cold stack (broad + lookalike + interest, or a justified subset)
- a retargeting layer separated from cold acquisition
- exclusions configured (recent purchasers, current customers, recent converters)
- no over-exclusion (blanket engager/visitor exclusions flagged and removed)
- audience sizes validated against minimums, with remediation for any undersized audience
- a retargeting sequence documented with entry triggers, windows, frequency, creative rotation, and exits
- the broad-beats-interest threshold explicitly checked
- risky choices and unknowns flagged
- a confidence level and source list

A weak audience plan has:

- interest-stacked audiences with no rationale beyond "these seem relevant"
- a single audience type with no cold/warm/hot separation
- no exclusions (wasting spend on recent purchasers)
- over-exclusion that starves the algorithm
- retargeting mixed into cold acquisition with no sequence
- no sizing check (running on an audience too small to deliver)
- lookalikes seeded on low-quality or generic lists
- no documented creative angle per audience

## Common Pitfalls

1. **Interest stacking.** Layering 10+ interests or narrowing ages and placements starves the algorithm. Modern Meta treats interests as suggestions anyway. Use 3-5 relevant interests, or go broad.
2. **No exclusions.** Showing purchase ads to recent purchasers wastes spend and annoys customers. Always exclude recent purchasers (180 days to all-time) from cold acquisition.
3. **Over-exclusion.** Removing all page engagers or all website visitors from cold prospecting limits delivery and drives up CPM. Exclude recent purchasers; let the rest stay available.
4. **Retargeting mixed with cold.** Retargeting creative (social proof, offer reminders) is different from cold creative (pattern interrupts, problem agitation). Separate the campaigns and the audiences.
5. **Seeding lookalikes on low-quality lists.** A lookalike is only as good as its seed. A list of 5,000 low-value leads produces a low-value lookalike. Seed with high-LTV purchasers or qualified buyers.
6. **Undersized retargeting audiences.** A retargeting pool of 500 users will not deliver consistently. Widen the window or move the event up the funnel (AddToCart → ViewContent).
7. **Ignoring the broad-beats-interest threshold.** Below 100 conversions/month, interest and lookalike help. Above it, broad usually wins. Running only interest at scale leaves efficiency on the table.
8. **No retargeting sequence.** Hitting the same warm audience with the same angle causes fatigue. Rotate angles (product/fit, UGC, third-party proof) and sequence by time window.
9. **Judging audiences too early.** An audience needs 50+ conversions per week per ad set to exit the Learning Phase. Judging at 10 conversions tells you nothing.
10. **Editing during the Learning Phase.** Every audience edit (adding/removing interests, changing exclusions, swapping seeds) resets the Learning Phase. Set it and leave it for 4-7 days.
11. **Trusting interest exclusions post-March-2025.** Meta removed detailed targeting exclusions from active campaigns. Use custom audience exclusions (lists, tags, Pixel events) instead.
12. **Forgetting frequency caps on retargeting.** Short-cycle retargeting should aim for 5-8 impressions over 7 days; high-ticket needs less. Uncapped retargeting fatigues the audience and kills CTR.

## Verification Checklist

- [ ] Business, ad account, offer, avatar, and conversion event confirmed
- [ ] Data source inventory complete with sizes, quality, and confidence labels
- [ ] Audience tier strategy chosen and justified (data depth, creative, budget)
- [ ] Broad-beats-interest threshold explicitly checked
- [ ] Cold stack defined (broad + lookalike + interest, or justified subset)
- [ ] Each audience has type, size, optimization event, budget, creative angle, and exclusions
- [ ] Retargeting layer separated from cold acquisition
- [ ] Exclusions configured (recent purchasers, current customers, recent converters)
- [ ] Over-exclusion check passed (no blanket engager/visitor exclusions)
- [ ] Audience sizes validated against minimums; remediation for any undersized audience
- [ ] Retargeting sequence documented (entry triggers, windows, frequency, creative rotation, exits)
- [ ] Lookalike seeds are high-quality (purchasers, high-LTV, qualified leads) — not generic lists
- [ ] Retargeting frequency target defined per tier
- [ ] Risky choices and unknowns flagged
- [ ] Confidence level and source list included
- [ ] If wiki-backed, plan filed under `businesses/<business-slug>/meta-ads/audiences/` and linked
- [ ] Final output follows the audience document shape
