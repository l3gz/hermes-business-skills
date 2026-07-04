---
name: marketing-strategy-orchestrator
description: Use when a client needs a go-to-market or marketing strategy — deciding WHICH channels to use, in what order, based on their offer, avatar, price, margin, business stage, and existing audience. This is the ENTRY POINT skill for any marketing engagement. It gates on prerequisites (avatar + offer must exist), diagnoses the best-fit channel mix, and delegates execution to the specialized sub-skills. It does NOT write copy, build campaigns, or create assets directly — it routes to the skills that do.
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, strategy, go-to-market, channel-selection, orchestrator, acquisition, hormozi]
    related_skills: [avatar-builder, offer-builder, meta-ads-manager, meta-creative-tester, meta-audience-builder, meta-ads-scaler, campaign-optimizer, meta-lead-gen, ad-creative-brief-writer, ad-script-writer, vsl-writer, funnel-copy-writer, funnel-page-writer, hook-angle-writer, brand-voice-extractor, human-editor]
---

# Marketing Strategy Orchestrator

## Overview

This is the diagnostic and routing skill — the entry point for any marketing engagement. Its job is to answer two questions:

1. **Given this offer, this avatar, this price, and this business stage — which channels should we use?**
2. **In what order, and what's the game plan for each?**

It then delegates each channel's execution to the specialized sub-skills (`meta-ads-manager`, `vsl-writer`, `ad-script-writer`, `funnel-copy-writer`, etc.) and assembles their outputs into one connected marketing strategy document.

The core discipline: **strategy before tactics.** Most marketing failures are not execution failures — they are channel-selection failures. Running Meta ads for a business with no margin to fund CAC. Doing cold outreach when the avatar is a warm-introduction buyer. Posting organic content to an audience of zero. This skill prevents those mismatches by diagnosing the right channels *before* any execution begins.

The framework draws from Alex Hormozi's $100M Leads (the "Core Four" channel framework + the lead-collector amplification layer) and the Acquisition.com $100M Scaling Roadmap (the business-stage progression that determines channel readiness). Where the sources conflict, Hormozi's principles win.

## When to Use

Use this skill when the client asks:

- "What marketing should I do?"
- "How should I launch this product/offer?"
- "Should I run ads, or do outreach, or content?"
- "What's the best channel for this offer?"
- "I have a budget — where should I spend it?"
- "I'm not getting enough leads/sales — what should I change?"
- "Can you build me a marketing plan?"
- "What should I do first, second, third?"

Also use this skill BEFORE loading any execution skill (`meta-ads-manager`, `vsl-writer`, etc.) if the channel choice is not yet confirmed. If the client already knows they want Meta ads and just needs the campaign built, skip this skill and go straight to `meta-ads-manager`.

Do not use this skill for:

- building a specific campaign (→ `meta-ads-manager`)
- writing a VSL (→ `vsl-writer`)
- writing ad scripts (→ `ad-script-writer`)
- building a funnel (→ `funnel-copy-writer`)
- creating the offer (→ `offer-builder`)
- defining the avatar (→ `avatar-builder`)
- extracting the brand voice (→ `brand-voice-extractor`)

## The Prerequisite Gate (Non-Negotiable)

This skill **will not produce a strategy** until the prerequisites are confirmed. A strategy built without a real avatar and a real offer is a guess.

### Hard requirements (cannot proceed without):

1. **A defined avatar** — target customer with pains, desires, objections, and language. If missing → route to `avatar-builder`.
2. **A defined offer** — dream outcome, mechanism, price, and basic value framing. If missing → route to `offer-builder`.

### Soft requirements (strategy will be weaker without, but can proceed with assumptions):

3. Brand voice (→ `brand-voice-extractor`)
4. Existing performance data (what's been tried, what worked, what failed)
5. Production capacity (how many leads/sales can the business handle per week)

If a hard requirement is missing, **stop and route to the prerequisite skill.** Do not produce a partial strategy on assumptions about who the customer is or what the offer is.

Completion: avatar and offer exist in the wiki or are confirmed verbally, and their presence is documented in the strategy output.

## Source Hierarchy

Orient from the client wiki first. Read `SCHEMA.md`, `index.md`, recent `log.md`, and the target business pages before claiming facts. Then prioritize:

1. The offer document: price, margin (if known), mechanism, stack, guarantee, and the conversion event.
2. The avatar profile: awareness level, demographics, existing relationship with the brand, and where they spend attention.
3. Financial inputs: price, cost of delivery, target CAC, and whether the business can fund upfront acquisition (CFA viability).
4. Business stage: where the business is on the scaling roadmap (see frameworks reference).
5. Existing assets: audience size, content library, past campaign performance, team capacity.
6. Real proof and approved claims for any strategy rationale.
7. Agent inference for channel weighting and sequencing only — never for facts, proof, or claims.

Completion: offer, avatar, financial inputs, business stage, and existing assets are known or marked unknown.

## Required Inputs (Discovery)

Minimum useful inputs:

- **The avatar**: who they are, their awareness level (unaware, problem-aware, solution-aware, product-aware, most-aware)
- **The offer**: what is being sold, the price, and the dream outcome
- **Business stage**: 0 (just starting) through 9 (scaling/capitalizing) — see the frameworks reference
- **Audience size**: do they have an existing audience/following/list, or are they starting from zero?
- **Budget**: is there money for paid acquisition, or must channels be free (outreach/content)?

Best inputs:

- A completed offer document from `offer-builder`
- A completed avatar profile
- Margin or cost of goods sold (to calculate CAC viability)
- Existing audience metrics (followers, email list size, engagement rate)
- Team capacity (can they handle 10 leads/day? 100? 1000?)
- Past channel performance (what's been tried, results, cost per lead/sale)
- Sales motion: self-serve, sales-assisted, or sales-led
- Timeline: immediate revenue needed, or building for long-term?

Completion: the discovery answers are sufficient to populate the strategy matrix and rank channels.

## Core Workflow

### 1. Orient to the wiki

If working inside a client wiki, read:

- `SCHEMA.md`, `index.md`, recent `log.md`
- the target business's brand, offer, avatar, character, voice, and any existing strategy docs

Completion: the strategy context, source assets, and save path are known.

### 2. Run the prerequisite gate

Confirm:
- [ ] Avatar exists → if not, route to `avatar-builder`
- [ ] Offer exists → if not, route to `offer-builder`

If either is missing, **stop here.** Do not produce a partial strategy.

Completion: avatar and offer are confirmed and documented.

### 3. Run discovery

Ask or extract the discovery inputs (see Required Inputs above). Frame the questions in plain language:

- "Who exactly is this for?" (avatar awareness level)
- "What are you selling, and for how much?" (offer + price)
- "Do you have an existing audience — followers, email list, past customers?" (audience size)
- "Do you have budget for paid ads, or do we need to start with free channels?" (budget)
- "How many new leads or sales can your team handle per week?" (capacity)
- "What have you already tried?" (past performance)

Completion: all discovery inputs are captured, with unknowns explicitly marked.

### 4. Determine the business stage

Using the $100M Scaling Roadmap framework (see `references/strategy-frameworks.md`), classify the business:

| Stage | Name | What it means | Channel implication |
|---|---|---|---|
| 0 | Improvise | No product, no customers, figuring it out | Warm outreach only — find your first customers manually |
| 1 | Monetize | First product, first customers, proving the offer | Warm outreach + cold outreach + free content. No paid yet. |
| 2 | Advertise | Offer proven, ready to pour fuel | Add paid ads. The transition from free to paid channels. |
| 3 | Stabilize | Ads working, but chaotic, need systems | Refine paid, add retargeting, build the funnel |
| 4 | Prioritize | Too many leads, need to focus on best customers | Optimize paid, filter leads, build qualification |
| 5 | Productize | Need a second product for existing customers | Cross-sell, upsell, retention campaigns |
| 6+ | Optimize → Capitalize | Scaling, specialization, market dominance | Full-stack: paid + content + referrals + affiliates + agencies |

**The critical transition is Stage 1 → Stage 2.** A business should NOT run paid ads until the offer is proven (Stage 1). Running ads on an unproven offer burns money. If the business is Stage 0 or 1, the strategy should focus on free channels (warm outreach, cold outreach, content) until the offer converts organically.

Completion: the business stage is classified and documented with its channel implications.

### 5. Apply the Core Four channel framework

Using the $100M Leads framework, evaluate each of the four primary channels against the avatar, offer, and business stage.

#### The Core Four (Hormozi's channel framework)

**1. Warm Outreach** — reaching people who already know you
- Best when: you have an existing network, past clients, followers, or an email list
- Cost: free (time only)
- Speed: fastest — you can message people today
- Best for: Stage 0-1 businesses, high-ticket offers, relationship-based sales, B2B

**2. Posting Free Content** — one-to-many organic (social posts, videos, podcasts, articles)
- Best when: you can create consistent content and the avatar consumes content on a specific platform
- Cost: free (time only), but slow to compound
- Speed: slow — audience building takes months
- Best for: building authority, warming cold audiences over time, any business stage as a long-term play
- Platform selection depends on where the avatar spends attention (Instagram, LinkedIn, YouTube, TikTok, X)

**3. Cold Outreach** — reaching strangers who don't know you (cold email, cold DM, cold calls)
- Best when: the avatar is identifiable and reachable, the offer is compelling enough to earn a response, and free/organic is too slow
- Cost: low (tool costs + time)
- Speed: medium — days to weeks for pipeline to materialize
- Best for: B2B, high-ticket, localized businesses, Stage 1-2 businesses without budget for paid

**4. Paid Ads** — paying platforms for distribution (Meta, Google, YouTube, TikTok, LinkedIn)
- Best when: the offer is proven (converts organically), there is budget to fund CAC upfront, the avatar is reachable on the platform, and the business can handle the lead volume
- Cost: direct spend + creative production
- Speed: fastest scalable channel — can go from 0 to 100 leads/day in days
- Best for: Stage 2+ businesses with proven offers and CAC-positive economics (CFA viable)

#### The Lead Collectors (amplification layer — Section IV)

Once the Core Four are flowing, add amplification:
1. **Customer referrals** — happy customers bring more customers
2. **Employees** — team members generate leads through their networks
3. **Agencies** — outsource acquisition to specialists
4. **Affiliates & partners** — others promote your offer for a cut

These are Stage 3+ plays. Do not recommend them before the Core Four are working.

Completion: each of the four primary channels is evaluated against the avatar, offer, stage, and budget with a fit assessment.

### 6. Rank the top-3 channels

Based on the evaluation, rank the channels in priority order. The output is a **top-3**, not a "do everything" list.

The ranking logic (Hormozi-aligned):
- **#1 Channel**: the highest-ROI channel given the current avatar + offer + stage + budget. The one that will produce leads or sales fastest.
- **#2 Channel**: the channel that supports #1 — either warming the audience for #1, or capturing demand #1 misses.
- **#3 Channel**: the long-term play — the channel that compounds over time but won't produce immediate revenue.

**Example rankings by scenario:**

| Scenario | #1 | #2 | #3 |
|---|---|---|---|
| Stage 1, B2B, high-ticket, no audience | Warm outreach | Cold outreach | Free content (LinkedIn) |
| Stage 1, B2C, low-ticket, no audience | Free content (TikTok/IG) | Cold outreach | Warm outreach |
| Stage 2, ecommerce, $50 product, proven | Paid ads (Meta) | Free content (IG/TikTok) | Email retention |
| Stage 2, info-product, $2000, proven | Paid ads (Meta/YouTube) | Free content | Warm outreach (referrals) |
| Stage 0, no offer proven yet | Warm outreach | Cold outreach | (no content until offer is proven) |

Completion: the top-3 channels are ranked with clear rationale tied to the avatar, offer, stage, and budget.

### 7. Build the game plan for each channel

For each ranked channel, define:

- **Why this channel** (one sentence tied to the diagnosis)
- **What success looks like** (the target metric: leads, sales, cost per lead, ROAS)
- **The first 4 actions** (concrete next steps to start)
- **Which sub-skill executes it** (the delegation target)
- **Estimated timeline to first results**
- **Budget requirement** (dollars or hours per week)

Then map the delegation:

| Channel | Delegates to | What the sub-skill produces |
|---|---|---|
| Paid ads (Meta) | `meta-ads-manager` + `ad-creative-brief-writer` + `ad-script-writer` | Campaign structure, creative briefs, ad scripts |
| Paid ads (lead gen) | `meta-lead-gen` + `funnel-copy-writer` | Instant Forms, qualification, funnel copy |
| Warm/cold outreach | `ad-script-writer` (cold-call patterns adapted for DM/email) | Outreach scripts, sequence structure |
| Free content | `hook-angle-writer` + `brand-voice-extractor` | Hook banks, content angles, voice guide |
| Funnel (any channel) | `funnel-copy-writer` + `vsl-writer` | Connected funnel copy, VSL script |

Completion: each of the top-3 channels has a clear game plan with delegation targets defined.

### 8. Assemble the strategy document

Use this output shape:

```markdown
# Marketing Strategy: [Business] — [Offer] for [Avatar]

## Prerequisites
- [ ] Avatar: confirmed / routed to avatar-builder
- [ ] Offer: confirmed / routed to offer-builder

## Discovery Summary
- Avatar awareness level:
- Offer and price:
- Business stage: Stage X — [name]
- Audience size:
- Budget:
- Team capacity:
- Past channel performance:
- Sales motion: self-serve / sales-assisted / sales-led
- Timeline:

## Business Stage Analysis
- Stage: X — [name]
- Channel implication:
- CFA viability: viable / not yet viable
- Rationale:

## Channel Evaluation
| Channel | Fit | Rationale |
|---|---|---|
| Warm outreach | High/Med/Low | ... |
| Free content | High/Med/Low | ... |
| Cold outreach | High/Med/Low | ... |
| Paid ads | High/Med/Low | ... |

## Ranked Top-3 Channels

### #1: [Channel name]
- Why:
- Success metric:
- First 4 actions:
  1.
  2.
  3.
  4.
- Delegates to: [skill name]
- Timeline to first results:
- Budget:

### #2: [Channel name]
- (same structure)

### #3: [Channel name]
- (same structure)

## Delegation Map
| Channel | Skill | Output |
|---|---|---|
| | | |

## NOT Recommended (and why)
- [Channels evaluated and rejected, with rationale]
- This prevents "should we also do X?" scope creep

## Next Steps
1. [First action on #1 channel]
2. [Prerequisite if any sub-skill needs inputs]

## Needs Approval
- [ ] This strategy requires client approval before any execution begins
- [ ] No execution skills should be loaded until this plan is confirmed

## Needs Confirmation
- [unknowns, assumptions, unconfirmed financials, unconfirmed stage]
```

Completion: the strategy document is complete, honest about unknowns, and explicitly gates on approval.

### 9. Gate on approval

**The strategy must be approved by the client before any execution begins.** Present the document, ask for confirmation, and only then load the delegated sub-skills.

If the client wants to change the channel mix, revise the ranking and re-present before proceeding.

Completion: the strategy is presented, and the client has either approved, requested changes, or deferred.

### 10. Update the wiki when appropriate

If working inside an LLM wiki:

- save the strategy under `businesses/<business-slug>/strategies/<strategy-slug>.md`
- link it to the offer, avatar, character, and brand voice
- update `index.md` if appropriate
- append to `log.md`
- run `qmd update` if configured

Completion: the strategy is filed under the correct business and reusable in later sessions.

## Missing Information Handling

Do not invent missing facts. Use these labels:

- `Unknown`: no source material supports the answer
- `Needs confirmation`: likely but not verified
- `Client to provide`: requires business stage, budget, capacity, or past performance data only the client can give
- `Assumption`: a working assumption made explicit, not a fact
- `Out of scope`: a channel, platform, or tactic outside this strategy's scope

If the avatar or offer is missing, do not proceed — route to the prerequisite skill.

## Quality Bar

A strong strategy document has:

- a confirmed avatar and offer (prerequisites gate passed)
- a clear business-stage classification with channel implications
- the Core Four evaluated against the avatar, offer, stage, and budget
- a ranked top-3 with rationale tied to the diagnosis
- a game plan for each channel with concrete first actions
- a delegation map pointing to the right sub-skills
- a "not recommended" section preventing scope creep
- honest treatment of unknowns and assumptions
- an explicit approval gate before execution
- no execution (no campaigns, no scripts, no copy) — this is strategy only

A weak strategy document has:

- no prerequisite gate (strategy produced without a confirmed avatar or offer)
- "do everything" (all four channels ranked equally with no prioritization)
- paid ads recommended for a Stage 0-1 business (unproven offer + paid = burned budget)
- no business-stage analysis (ignores whether the business is ready for the recommended channels)
- no delegation map (strategy with no execution path)
- no approval gate (jumps straight to execution)
- generic advice not tied to the specific avatar, offer, or stage

## Common Pitfalls

1. **Recommending paid ads for an unproven offer.** The #1 mistake. Paid ads scale what works. If the offer hasn't converted organically (warm/cold/outreach), ads will scale the failure. Stage 1 → prove the offer first.
2. **Skipping the prerequisite gate.** Producing a strategy without a confirmed avatar and offer. The strategy will be generic and wrong.
3. **"Do everything" ranking.** All four channels ranked equally with no prioritization. The value is in the ranking, not the menu.
4. **Ignoring business stage.** Recommending referrals, affiliates, or agencies to a Stage 0 business. Those are Stage 3+ amplification plays.
5. **Ignoring capacity.** Recommending a channel that will generate 500 leads/week for a team that can handle 20. The strategy must match the delivery capacity.
6. **Ignoring CFA viability.** Recommending paid ads for a business that can't fund the CAC upfront. If the margin can't cover acquisition cost, paid is not viable yet.
7. **No delegation map.** A strategy with no path to execution. Each channel must point to the skill that builds it.
8. **No approval gate.** Jumping from strategy to execution without client confirmation. The client must approve the channel mix before work begins.
9. **Platform selection without avatar data.** Recommending TikTok because "it's trending" when the avatar is on LinkedIn. Match the platform to where the avatar spends attention.
10. **Ignoring the long-term play.** Filling the top-3 with only fast channels. Channel #3 should be the compounding long-term asset (usually content or referral system).
11. **Not documenting what was rejected.** Without a "not recommended" section, the client will ask "should we also do X?" and scope creep begins.
12. **Jumping to execution.** This skill produces a strategy, not campaigns or copy. If the client wants to start building, load the delegated sub-skill — do not build in this skill.

## Verification Checklist

- [ ] Avatar confirmed (prerequisite gate passed)
- [ ] Offer confirmed (prerequisite gate passed)
- [ ] Discovery inputs captured (awareness, price, stage, audience, budget, capacity, past performance)
- [ ] Business stage classified with channel implications
- [ ] CFA viability assessed (can the business fund upfront CAC?)
- [ ] Core Four channels evaluated against the diagnosis
- [ ] Top-3 channels ranked with rationale
- [ ] Each ranked channel has a game plan (why, success metric, first 4 actions, delegate, timeline, budget)
- [ ] Delegation map points to the correct sub-skills
- [ ] "Not recommended" section prevents scope creep
- [ ] Unknowns and assumptions explicitly labeled
- [ ] Approval gate is present — no execution until confirmed
- [ ] No execution content (no campaigns, scripts, or copy — strategy only)
- [ ] If wiki-backed, strategy filed under `businesses/<business-slug>/strategies/`
- [ ] Final output follows the strategy document shape
