---
name: meta-ads-scaler
description: Use when planning a scale from testing to full spend, deciding between vertical and horizontal scaling, setting budget increase pacing, escaping the Learning Phase, or diagnosing why a scale stalled. Produces a scaling plan with readiness criteria, method selection (vertical vs horizontal), budget ladder, Learning Phase protection rules, and kill criteria. Covers Sales, Leads, and App Promotion objectives.
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, meta-ads, facebook-ads, paid-social, scaling, budget, learning-phase]
    related_skills: [meta-ads-manager, meta-creative-tester, meta-audience-builder, campaign-optimizer, meta-lead-gen, ad-creative-brief-writer, ad-script-writer, vsl-writer, hook-angle-writer, offer-builder, avatar-builder, brand-voice-extractor, human-editor]
---

# Meta Ads Scaler

## Overview

Scale Meta ad spend from a profitable test to full-volume acquisition without resetting the Learning Phase or breaking unit economics. This skill produces a scaling plan — readiness check, method selection, budget ladder, monitoring cadence, and kill criteria — that a media buyer can execute against without choking a winning campaign.

Scaling is not "increase the budget and hope." It is a disciplined sequence of small, evidence-backed moves designed to let Meta's algorithm absorb more spend without re-entering the Learning Phase. The algorithm that found your buyers at $100/day is the same one that must find more buyers at $1,000/day — but only if you give it room to expand and refuse to panic-edit when CPA wobbles.

Use `references/scaling-frameworks.md` for the detailed framework reference (scaling signals, vertical vs horizontal comparison, budget increase tiers, Learning Phase rules, kill criteria, common scaling mistakes). This file is the operating process.

The core discipline: scale on evidence, not excitement. Every budget increase must be justified by 48-72 hours of profitable performance, executed one change at a time, and monitored for the signals that say keep going, pause, or roll back. A scale that resets the Learning Phase costs you 3-7 days of degraded performance — the single most expensive mistake in paid social.

## When to Use

Use this skill when the client asks for:

- a plan to scale a profitable campaign from testing to full spend
- a decision between vertical scaling (raise budget) and horizontal scaling (duplicate to new audiences)
- a budget increase pacing schedule (how much, how often, when to stop)
- a path out of the Learning Phase for a campaign that keeps resetting
- a diagnosis of why a scale stalled or reversed (CPA spiked after a bump)
- kill criteria for a scaling campaign that is degrading
- a budget ladder (testing budget → scaling budget → ceiling)
- a surf-scaling or aggressive-scaling playbook for a low-budget outlier
- a horizontal expansion plan (lookalike tiers, broad, new interests, new geos)

Do not use this skill for:

- initial campaign structure and setup — use `meta-ads-manager`
- creative testing methodology and winner identification — use `meta-creative-tester`
- audience research and lookalike source selection — use `meta-audience-builder`
- daily optimization, metrics diagnosis, and routine management — use `campaign-optimizer`
- building the offer or landing page the ads point to — use `offer-builder`, `funnel-writer`, or `vsl-writer`

## Multi-Business Rule

A client can run several businesses, and each business can have many scaling campaigns across multiple ad accounts. Never blend scaling signals, budgets, CPA targets, or performance data across businesses. Before planning a scale, confirm the business, business slug, Meta ad account ID, the campaign being scaled, and the offer it promotes.

Store scaling plans inside the client wiki under the correct business:

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
        └── <campaign-slug>/
            ├── campaign-plan.md
            └── scaling-plan.md
```

If the wiki uses another structure, follow it while keeping every scaling plan grouped by business and linked to its campaign, offer, and avatar.

## Source Hierarchy

Orient from the client wiki first. Read `SCHEMA.md`, `index.md`, recent `log.md`, and the target business pages before claiming facts. Then prioritize:

1. The existing campaign plan and its documented CPA/ROAS targets, budget, and creative winners.
2. Live performance data (last 7-14 days): spend, conversions, CPA, ROAS, CTR, CPC, CPM, frequency, click-vs-view attribution split.
3. The offer document: margin, LTV, break-even CPA, and the unit-economic ceiling that defines the scaling limit.
4. Creative status: which ads are winning, their age, fatigue signals, and whether fresh winners are in the pipeline.
5. Pixel/CAPI signal health: conversion volume per week (50+ needed to exit and stay out of Learning Phase), EMQ, attribution split.
6. Agent inference for pacing and sequencing only — never for facts, proof, results, or claims.

Completion: the campaign, its targets, its live performance, its creative pipeline, and its unit-economic ceiling are known or marked unknown.

## Required Inputs

Minimum useful inputs:

- the business and ad account
- the campaign or ad set being scaled
- the current daily budget
- the target CPA or ROAS
- at least 3-5 days of recent performance data (spend, conversions, CPA/ROAS)
- the current Learning Phase status (active, learning, limited)

Best inputs:

- 7-14 days of performance data with a clear profitable trend
- the break-even CPA and LTV (defines the scaling ceiling)
- the conversion volume per week (determines how aggressively you can scale)
- the click-based vs view-based conversion split (verifies the performance is real)
- the creative pipeline (winners in reserve, fatigue timeline)
- the audience saturation picture (reach, frequency, audience estimate)
- the Pixel/CAPI health (EMQ, event volume)
- past scaling history on this account (what bump sizes worked, what reset the campaign)

Completion: there is enough data to confirm scaling readiness and choose a method without guessing at the unit economics or the signal health.

## Core Workflow

### 1. Orient to the wiki and the campaign

If working inside a client wiki, read:

- `SCHEMA.md`, `index.md`, recent `log.md`
- the target business's brand, offer, avatar, and the existing `meta-ads/campaigns/<campaign-slug>/campaign-plan.md`
- any prior scaling plans for this campaign

Completion: the campaign context, targets, performance baseline, and save path are known.

### 2. Confirm scaling scope

Define before planning the scale:

- business and business slug
- Meta ad account ID
- campaign name and ID being scaled
- offer and offer slug
- current daily budget and lifetime budget (if applicable)
- target CPA and/or target ROAS
- break-even CPA and LTV (the unit-economic ceiling)
- current phase: testing, early scaling, mid scaling, mature scaling
- Learning Phase status
- confidence level and source list

Completion: the scale is tied to one business, one campaign, one target, and one ceiling.

### 3. Verify scaling readiness

Do not scale on a single good day. Verify all of the following before increasing a single dollar:

- [ ] **48-72 hour profitability:** the campaign has hit or beaten target CPA/ROAS for 48-72 consecutive hours (conservative: 3-5 full days).
- [ ] **CPA at or below target:** the rolling 3-day CPA is at or below the target CPA. If CPA is above target, the campaign is not ready — optimize first.
- [ ] **Budget not fully spent:** the campaign is spending its full daily budget and delivering. If the campaign is under-spending, the constraint is delivery (creative, audience, or bid), not budget — scaling the budget will not help.
- [ ] **Pixel signal clean:** 50+ conversions per week (ideally 100+) so the algorithm has stable signal. EMQ above 6/10. CAPI firing alongside Pixel.
- [ ] **Click-based conversions ≥60%:** at least 60% of reported purchases are click-based, not view-through. Heavy view-through reliance inflates ROAS and hides a campaign that is not driving incremental conversions.
- [ ] **Creative not fatigued:** the winning creative has room to run (frequency under 3 for cold, CTR stable, no CPM spike). Scaling a fatigued creative burns money.
- [ ] **A reason to scale:** ideally backed by a tangible change — a new winning creative, a fresh offer, or a high-converting landing page. Scaling a stale setup on a lucky day usually reverses.
- [ ] **Unit economics support it:** LTGP:CAC is healthy enough to tolerate the CPA creep that comes with scale. High-LTV offers ($10k+ LTV) tolerate aggressive scaling; thin-margin ecommerce does not.

If any readiness gate fails, do not scale. Document the gap and route to the right skill (`campaign-optimizer` for performance fixes, `meta-creative-tester` for creative fatigue, `offer-builder` for margin issues).

Completion: the campaign is confirmed ready to scale, or the blocking gaps are documented.

### 4. Choose the scaling method

Two paths. They are not mutually exclusive — mature scales use both — but pick the primary method for the immediate plan.

**Vertical scaling ("scale it where it lies"):**
- Increase the budget on the existing winning campaign or ad set
- Best when: the winning ad set is performing well in place, you want to preserve social proof, and the audience has room to absorb more spend
- Risk: aggressive bumps reset the Learning Phase
- Rule: never increase by more than 50% in a single edit; 20% is the safe standard

**Horizontal scaling ("don't put all your eggs in one basket"):**
- Duplicate winning ad sets to new audiences (lookalike tiers, broad, interests), new geos, or new creative angles
- Best when: the current audience is saturating (frequency rising, CPM climbing), you have creative diversity, and you want to de-risk concentration
- Risk: duplicating can split signal and create auction overlap if not structured cleanly
- Modern lever: creative diversity — scale with conceptually distinct ads (different angles, formats, creators), not identical ads to new audiences

See step 6 for the decision logic and `references/scaling-frameworks.md` for the full comparison.

Completion: the primary scaling method is chosen and justified by audience saturation, creative pipeline, and budget level.

### 5. Set the budget ladder

Define the full spend path before the first increase. A budget ladder prevents reactive scaling (bumping because you're excited) and defines the ceiling where scaling stops.

```text
Testing budget → Scaling budget → Ceiling
   (proven)      (stepped up)    (unit-econ limit)
```

- **Testing budget:** the current daily spend where the campaign proved profitable.
- **Scaling budget:** the stepped target, reached via incremental bumps (e.g., $100/day → $150 → $200 → $250, each held 2-3 days to confirm stability).
- **Ceiling:** the maximum daily budget where CPA remains at or below target given the audience size, conversion volume, and unit economics. Above the ceiling, CPA inflates faster than spend. The ceiling is defined by the audience saturation point and the LTV:CAC ratio, not by ambition.

Document the ladder with dollar amounts and the trigger conditions for each step up.

Completion: the budget ladder is defined from current spend to ceiling with step amounts and hold periods.

### 6. Execute the scale — one change at a time

The execution discipline that separates scalers from spenders:

- **One change per edit.** Do not raise the budget, swap an audience, and change a bid in the same session. If performance moves, you will not know which change caused it.
- **Wait 2-3 days between changes** (conservative: 3-5 days). The algorithm needs time to absorb the new budget and re-stabilize. Editing again before it settles risks a Learning Phase reset.
- **Increase at the campaign level (CBO)** when scaling vertically, so Meta can route the additional budget to the best-performing ad set. Scaling an individual ad set budget in a CBO campaign can conflict with the algorithm's distribution logic.
- **Use the Post ID method** when graduating a winner into a scaling campaign (ASC or CBO). Never duplicate a winning ad from scratch — it resets social proof and the algorithm's learning on that creative.
- **Schedule major changes at midnight.** Budget increases and new launches go live at 12:00 AM. Launching mid-afternoon forces Meta to cram the new budget into the remaining hours, spiking CPA.

Completion: the scale is executed as a sequence of single, evidence-backed, well-timed edits.

### 7. Monitor for the three failure signals

After every budget bump, watch for:

- **Learning Phase reset:** CPA spikes 30-100% within 24 hours of the edit, delivery becomes erratic. This means the edit was too aggressive. Action: stop scaling, wait 3-5 days for re-stabilization. If severe, roll the budget back to the pre-edit level.
- **CPA spike (sustained):** rolling 3-day CPA rises above target. Action: hold the budget flat. If it persists 3+ days above 2x target, pull back 20-30% or pause the scaling campaign and route back to testing.
- **Frequency rise / creative fatigue:** frequency climbs above 3 (cold) or 5 (retargeting), CTR drops, CPM rises. Action: the audience is saturating. Refresh creative (vertical won't help here) or expand horizontally to new audiences.

Completion: the monitoring cadence is defined (daily check of spend, CPA, frequency; 3-day rolling review after each bump) with clear trigger thresholds.

### 8. Adjust or roll back if signals degrade

Scaling is reversible. Define the rollback rules before you start:

- If CPA goes above target within 48 hours of a bump: hold flat, wait 3-5 days. Volatility right after an edit is normal.
- If CPA stays above target for 3+ days after a bump: roll the budget back to the last profitable level.
- If CPA exceeds 2x target for 3+ days: pause the scaling campaign. The scale has broken — diagnose whether it's creative fatigue, audience saturation, signal degradation, or a Learning Phase reset before resuming.
- If frequency exceeds 5 with a CTR drop: stop vertical scaling. The fix is creative refresh or horizontal expansion, not more budget.

Completion: rollback triggers and actions are defined for each degradation signal.

### 9. Assemble the scaling plan document

Use this output shape:

```markdown
# Meta Ads Scaling Plan: [Campaign] for [Offer]

## Scope
- Business:
- Business slug:
- Meta ad account ID:
- Campaign being scaled:
- Offer:
- Current daily budget:
- Target CPA / ROAS:
- Break-even CPA:
- LTV:
- Scaling ceiling (daily budget):
- Confidence:
- Sources used:

## Scaling Readiness
- [ ] 48-72 hours profitable:
- [ ] CPA at or below target:
- [ ] Budget fully spent (delivery healthy):
- [ ] 50+ conversions/week:
- [ ] EMQ above 6/10:
- [ ] Click-based conversions ≥60%:
- [ ] Creative not fatigued (frequency <3):
- [ ] Reason to scale (new winner / fresh offer / fresh LP):
- [ ] Unit economics support it:
- Gaps blocking scale:

## Scaling Method
- Primary method: vertical / horizontal / both
- Justification:
- Secondary method:

## Budget Ladder
| Step | Daily budget | Bump size | Hold period | Trigger to advance |
|---|---|---|---|---|
| Current | $ | — | — | — |
| Step 1 | $ | +X% | 2-3 days | 3-day CPA ≤ target |
| Step 2 | $ | +X% | 2-3 days | 3-day CPA ≤ target |
| Ceiling | $ | — | — | unit-econ limit |

## Execution Rules
- One change at a time:
- Wait period between changes:
- Budget edits at: campaign level (CBO)
- Major changes scheduled at: 12:00 AM
- Winner graduation method: Post ID

## Monitoring Cadence
- Daily check: spend pace, CPA, frequency, delivery errors
- Post-bump check (24-48h): Learning Phase reset signs, CPA volatility
- 3-day rolling review: CPA trend, frequency trend, creative fatigue signals

## Failure Signals and Rollback
| Signal | Threshold | Action |
|---|---|---|
| Learning Phase reset | CPA spike 30%+ within 24h of edit | Hold flat, wait 3-5 days; rollback if severe |
| Sustained CPA spike | 3-day CPA > target for 3+ days | Roll back to last profitable level |
| Kill trigger | 3-day CPA > 2x target for 3+ days | Pause, diagnose, route back to testing |
| Creative fatigue | Frequency >5 + CTR drop | Stop vertical; refresh creative or expand horizontal |

## Horizontal Expansion Plan (if applicable)
- Lookalike tiers to add: 1-3%, 1-5%, 1-10%
- Broad expansion: yes / no
- New interests: 
- New geos: 
- Creative diversity required: distinct angles/formats, not duplicates

## Kill Criteria for Scaling Campaign
- CPA above 2x target for 3+ consecutive days:
- Frequency >5 with sustained CTR drop:
- ROAS below margin floor for 3+ days:
- Learning Phase stuck (not exited after 7 days of adequate budget):

## Needs Confirmation
- [unverified ceiling, unconfirmed LTV, missing attribution split, pending creative pipeline]
```

Completion: the document can be handed to a media buyer to execute the scale without reconstructing the strategy.

### 10. Update the wiki when appropriate

If working inside an LLM wiki:

- save the scaling plan under `businesses/<business-slug>/meta-ads/campaigns/<campaign-slug>/scaling-plan.md`
- link it to the campaign plan, offer, avatar, and creative assets
- update `index.md` if appropriate
- append to `log.md` when a scaling step is executed or a rollback is triggered
- run `qmd update` if configured

Completion: the plan is filed under the correct business and campaign, and reusable in later sessions.

## Scaling Readiness Criteria (Quick Reference)

The signals that say scale now — all must be true:

| Signal | Threshold | Why it matters |
|---|---|---|
| Profitable streak | 48-72 hours (conservative: 3-5 days) at/under target CPA | Confirms the performance is real, not a lucky day |
| CPA vs target | Rolling 3-day CPA ≤ target CPA | Scaling above target amplifies a loss, not a win |
| Budget delivery | Campaign spending its full daily budget | Under-spending means the constraint is delivery, not budget |
| Conversion volume | 50+ conversions/week (ideally 100+) | Keeps the algorithm out of the Learning Phase as you scale |
| Signal health | EMQ ≥ 6/10, Pixel + CAPI firing | Clean signal is what lets the algorithm absorb more spend |
| Attribution split | ≥60% click-based conversions | View-through-heavy ROAS is inflated and unsafe to scale |
| Creative health | Frequency <3 (cold), CTR stable, no CPM spike | Fatigued creative burns the additional budget instantly |
| Unit economics | LTGP:CAC healthy; LTV tolerates CPA creep | The ceiling is defined by margin, not by ambition |

## Vertical Scaling Rules

The budget increase tiers. Choose by how far performance is pacing above target:

| Tier | Bump size | Frequency | When to use | Risk |
|---|---|---|---|---|
| **Conservative** | 10-20% | Every 24-72 hours | Stable scaling, steady performance at target | Lowest; rarely resets Learning Phase |
| **Standard** | 20% | Every 2-3 days | The baseline vertical scaling increment | Low; the safe default |
| **Moderate** | 30% | Every 2-3 days | Performance pacing well above target (e.g., 1.5-2x ROAS) | Moderate; watch for reset signals. If performance dips, pull back 30%. |
| **Aggressive** | 50% | Every 3-4 days | ROAS is 50%+ above target (e.g., target 2x, actual 3-3.5x+) | High; can reset Learning Phase. Cap at low/mid budgets. |
| **Double-up (100%)** | 100% | Once, on low budgets | Under $1,000/day with extreme profitability | Very high; only for outlier performers. Reset risk is real. |

**Hard rules:**
- Never increase by more than 50% in a single edit on standard campaigns.
- At enterprise spend ($10,000+/day), avoid 50-100% jumps — sudden spikes force Meta to buy low-quality impressions and can double CPA overnight.
- Surf scaling (aggressive same-day bumps on early-morning profitability) is a specialized tactic for low budgets; reset to baseline at midnight to lock in daily profits.

## Horizontal Scaling

Duplicate winning ad sets to expand reach without concentrating spend on one audience. Use when the current audience is saturating or when you want to de-risk a vertical scale.

**Expansion targets (in order of typical ROI):**

1. **Lookalike tiers:** start at 1% (built from purchaser list), expand to 1-3%, 1-5%, 1-10% as you scale. Each tier is a new ad set with the winning creative (via Post ID).
2. **Broad (Advantage+ Audience):** remove interest targeting, let Meta find buyers across the full audience. Often outperforms interest targeting at scale when the Pixel signal is strong.
3. **New interests:** 3-5 relevant interests per ad set, distinct from the original winner's audience.
4. **New geos:** expand to adjacent markets where the offer and creative translate.
5. **Creative diversity (the modern lever):** scale with conceptually distinct ads — different angles, formats (skits, UGC, static grids, testimonial), creators — rather than identical ads to new audiences. Under Meta's Andromeda architecture, the creative does the targeting; diverse creative reaches diverse persona pockets within a broad audience.

**Horizontal scaling discipline:**
- Use the Post ID method to preserve social proof when duplicating winners.
- Avoid auction overlap: if two ad sets target overlapping audiences in the same campaign, Meta competes with itself and raises CPM. Use exclusions or consolidate.
- One new audience per scaling cycle, monitored for 3-5 days before adding the next.

## Learning Phase Protection

The Learning Phase is the single most expensive thing to trigger during a scale. Protect it ruthlessly.

- **The 50-conversions law:** an ad set needs 50+ conversion events per 7 days to exit the Learning Phase. During a scale, keep volume above this threshold or the campaign re-enters learning with every bump.
- **Budget for the phase:** set daily budget at 2-3x break-even CPA to ensure the ad set clears learning quickly. For cost-cap campaigns, set daily budget at minimum 8x the cap.
- **Avoid edits during scaling:** every significant edit (budget ±20%+, audience change, creative swap, bid change, placement change, optimization event change) can reset the Learning Phase. Make one change at a time, then wait.
- **Wait 3-5 days between changes:** give the algorithm time to absorb the change and re-stabilize before the next move.
- **The midnight launch rule:** schedule budget increases and new launches for 12:00 AM. Mid-day changes force Meta to cram the new budget into remaining hours, spiking CPA.
- **The two-week stabilization window:** for new creative tests or structural changes, allow two weeks without manual adjustments to gather conclusive data including weekday/weekend variance.

## Kill Criteria for Scaling Campaigns

A scaling campaign that degrades must be killed or rolled back. Apply these thresholds:

- **CPA above 2x target for 3+ consecutive days:** the scale has broken. Pause, diagnose (creative fatigue? audience saturation? signal degradation? Learning Phase reset?), and route back to testing before resuming.
- **Frequency >5 with a sustained CTR drop:** the audience is saturated. Vertical scaling cannot fix this. Refresh creative or expand horizontally.
- **ROAS below the margin floor for 3+ days:** the scale is no longer profitable at the current spend. Roll back to the last profitable budget level.
- **Learning Phase stuck:** the campaign has not exited the Learning Phase after 7 days at adequate budget (50+ conversions/week). The structure or signal is broken — restructure or fix the Pixel/CAPI before scaling.
- **Automated rule triggers:** set platform rules to auto-pause any ad set if 3-day average CPA exceeds target, and auto-decrease campaign budget by 20% if 3-day ROAS drops below the profitable threshold.

## The Budget Ladder

The full spend path, defined before the first increase:

```text
Testing budget  →  Scaling budget  →  Ceiling
   (proven)         (stepped up)       (unit-econ limit)
```

- **Testing budget:** the daily spend where the campaign proved profitable (typically the ABO testing phase).
- **Scaling budget:** the stepped target, reached via incremental bumps held 2-3 days each. The number of steps depends on the gap between current spend and ceiling.
- **Ceiling:** the maximum daily budget where CPA stays at or below target, defined by audience saturation (reach vs audience size) and the LTV:CAC ratio. Above the ceiling, CPA inflates faster than spend — scaling past it loses money regardless of how good the creative is.

The ceiling is not a guess. Estimate it from:
- Audience size ÷ target frequency ÷ campaign duration = max sustainable daily impressions
- Conversion rate × max daily impressions = max daily conversions
- LTV × target CAC ratio = max acceptable CPA (the margin floor)

If the estimated ceiling is below the desired spend, the constraint is the audience or the margin — not the budget. Fix the offer (raise LTV), expand the audience (horizontal), or improve creative (raise conversion rate) before pushing spend past the ceiling.

## Missing Information Handling

Do not invent missing facts. Use these labels:

- `Unknown`: no source material supports the answer
- `Needs confirmation`: likely but not verified
- `Client to provide`: requires ad account access, live performance data, LTV, or margin confirmation
- `Risk flag`: a budget recommendation that depends on unverified unit economics
- `Out of scope`: a scaling tactic the business cannot currently support (e.g., surf scaling without daily monitoring capacity)

If the target CPA, break-even CPA, or live performance data is missing, stop and require it before planning a scale. A scaling plan built without a defined CPA target and ceiling is a plan to spend money without a stop condition.

## Quality Bar

A strong scaling plan has:

- one business, one campaign, one target CPA, and one defined ceiling
- a readiness check with all gates verified or gaps documented
- a scaling method justified by audience saturation, creative pipeline, and budget level
- a budget ladder with specific dollar amounts, bump sizes, and hold periods
- a ceiling defined by unit economics and audience size, not by ambition
- execution rules enforcing one change at a time and 3-5 day wait periods
- Learning Phase protection rules explicit
- monitoring cadence with daily and post-bump checks
- failure signals and rollback triggers defined before the first bump
- kill criteria for the scaling campaign
- horizontal expansion plan if the audience is saturating
- a confidence level and source list

A weak scaling plan has:

- "increase the budget" with no pacing, amounts, or hold periods
- no readiness check — scaling on a single good day
- no ceiling — scaling until performance breaks, then reacting
- multiple changes per edit (budget + audience + creative at once)
- no rollback rules — riding a degrading campaign hoping it recovers
- scaling a fatigued creative (frequency already high, CTR dropping)
- vertical scaling past audience saturation (the fix is horizontal, not more budget)
- no Learning Phase awareness — bumping every day and resetting the algorithm repeatedly
- no unit-economic check — scaling past the margin floor into unprofitable volume

## Common Pitfalls

1. **Scaling on a lucky day.** One profitable day is not a signal. Wait for 48-72 hours of consistent performance before the first bump.
2. **Bumping too fast.** Increases over 50% in a single edit risk a Learning Phase reset. The recovery costs 3-7 days of degraded performance.
3. **Bumping every day.** The algorithm needs 2-3 days to absorb a budget change. Daily bumps stack resets and prevent stabilization.
4. **Multiple changes at once.** Raising budget, swapping audience, and changing creative in one session makes diagnosis impossible when performance moves.
5. **Scaling a fatigued creative.** If frequency is above 3 and CTR is dropping, more budget burns money faster. Refresh creative first.
6. **Vertical scaling past saturation.** When the audience is saturated, the constraint is reach, not budget. Expand horizontally.
7. **No ceiling.** Scaling without a defined stop condition guarantees you scale past the point of profitability. Define the ceiling from unit economics and audience size first.
8. **No rollback plan.** A scale that degrades with no rollback rules becomes a bleed. Define the triggers before the first bump.
9. **Ignoring the attribution split.** Scaling view-through-heavy ROAS inflates a number that is not real incremental lift. Verify ≥60% click-based.
10. **Duplicating winners from scratch.** Duplicating an ad without the Post ID resets social proof and the algorithm's learning on that creative. Always use the Post ID method.
11. **Mid-day budget increases.** Editing the budget at 3 PM forces Meta to spend the new budget in the remaining hours, spiking CPA. Edit at midnight.
12. **Scaling at enterprise levels like a small account.** At $10,000+/day, 50-100% bumps force Meta to buy low-quality impressions and can double CPA overnight. Scale conservatively at high spend.

## Verification Checklist

- [ ] Business, ad account, campaign, offer, and target CPA confirmed
- [ ] Break-even CPA and LTV confirmed (defines the ceiling)
- [ ] Scaling readiness gates all verified or documented as blocking
- [ ] Click-based vs view-based conversion split checked (≥60% click-based)
- [ ] Scaling method chosen and justified (vertical / horizontal / both)
- [ ] Budget ladder defined from current spend to ceiling with step amounts and hold periods
- [ ] Ceiling defined by unit economics and audience size
- [ ] Execution rules enforce one change at a time and 3-5 day waits
- [ ] Learning Phase protection rules explicit (50+ conv/week, midnight edits, no stacked edits)
- [ ] Monitoring cadence defined (daily + post-bump checks)
- [ ] Failure signals and rollback triggers defined before the first bump
- [ ] Kill criteria defined for the scaling campaign
- [ ] Horizontal expansion plan included if audience is saturating
- [ ] Post ID method specified for winner graduation
- [ ] Confidence level and source list included
- [ ] If wiki-backed, plan filed under `businesses/<business-slug>/meta-ads/campaigns/<campaign-slug>/` and linked
- [ ] Final output follows the scaling plan document shape
