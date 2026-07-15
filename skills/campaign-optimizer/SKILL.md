---
name: campaign-optimizer
description: Use when diagnosing, optimizing, or managing live Meta (Facebook/Instagram) ad campaigns day-to-day. Produces a decision-and-action document covering metrics diagnosis, the Learning Phase, budget pacing review, frequency and fatigue management, creative refresh timing, and the daily/weekly/monthly review cadence. Covers Sales, Leads, and App Promotion campaigns.
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, meta-ads, facebook-ads, paid-social, optimization, metrics, media-buying]
    related_skills: [meta-ads-manager, meta-creative-tester, meta-audience-builder, meta-ads-scaler, meta-lead-gen]
---

# Campaign Optimizer

## Overview

Diagnose live Meta ad campaigns and decide the single correct next action: wait, kill, scale, refresh, or restructure. This skill produces an optimization decision document that a media buyer can execute against without second-guessing the logic.

Meta Ads operates as a machine-learning system, not a traditional media-buying platform. Optimization is not about tweaking bids and audiences until the numbers look good — it is about reading the diagnostic signals the algorithm is sending you, identifying the true bottleneck, and intervening as little as possible. Every edit has a cost: it resets the Learning Phase and forces the algorithm to re-learn. The media buyer's job is to intervene only when the data justifies it, change exactly one variable at a time, and otherwise let the machine cook.

Use `references/optimization-frameworks.md` for the detailed framework reference (metrics benchmarks table, diagnosis matrix, Learning Phase rules, daily/weekly/monthly workflow checklists, common mistakes that reset the algorithm). This file is the operating process.

The core discipline: read the system, find the bottleneck, make one change, document the decision, and wait. Most performance issues resolve by waiting, not by intervening. When you do intervene, you are either fixing creative, fixing the offer/funnel, or removing a constraint — never just "trying something."

## When to Use

Use this skill when the client asks for:

- a daily, weekly, or monthly campaign review and health check
- a metrics diagnosis (why is CPA rising, why is CTR falling, why is ROAS dropping)
- a Learning Phase decision (is this ad set still learning, did an edit reset it, when can I judge it)
- a budget pacing review (is spend on track, is the weekly average holding, are pacing rules being respected)
- a frequency and creative fatigue assessment (is the audience saturated, when to refresh)
- a creative refresh timing recommendation (when to rotate winners, how to iterate)
- a kill / scale / wait / restructure decision for a specific ad set or campaign
- an audit of recent edits and whether they helped or hurt
- a recommendation on whether to touch a campaign or leave it alone
- an optimization log entry for a client wiki

Do not use this skill for:

- initial campaign structure or launch planning — use `meta-ads-manager`
- scaling decisions (vertical/horizontal budget increases, scaling architecture) — use `meta-ads-scaler`
- creative testing design (test structure, variables, sprints) — use `meta-creative-tester`
- audience strategy (lookalike tiers, broad vs interest, exclusions) — use `meta-audience-builder`
- creative production itself (scripts, images, video) — use `ad-script-writer`, `vsl-writer`, `ad-creative-brief-writer`
- the landing page or funnel the ads point to — use `funnel-writer` or `vsl-writer`
- lead-gen form and qualification design — use `meta-lead-gen`

## Multi-Business Rule

A client can run several businesses, and each business can have many Meta ad accounts and campaigns. Never blend metrics, budgets, offers, or benchmarks across businesses. Before optimizing, confirm the business, business slug, Meta ad account ID, the campaign or ad set under review, and the target KPI (CPA, CPL, or ROAS) you are optimizing against.

Store optimization decisions inside the client wiki under the correct business:

```text
businesses/<business-slug>/
├── brand.md
├── meta-ads/
│   ├── account-overview.md
│   ├── campaigns/
│   │   └── <campaign-slug>.md
│   └── optimization/
│       └── <campaign-slug>.md
```

If the wiki uses another structure, follow it while keeping every optimization decision grouped by business and linked to its campaign.

## Source Hierarchy

Orient from the client wiki first. Read `SCHEMA.md`, `index.md`, recent `log.md`, and the target business pages before claiming facts. Then prioritize:

1. The campaign plan from `meta-ads-manager`: objective, conversion event, budget strategy, testing vs scaling phase, and the target KPI.
2. Live performance data: spend, impressions, reach, frequency, CTR, CPC, CPM, CPL/CPA, ROAS, hook rate, hold rate, add-to-cart rate, by campaign/ad set/ad and by time window (yesterday, 3-day, 7-day, 14-day).
3. Historical benchmarks for this account: what CTR, CPC, CPM, and CPA look like when this business's ads are healthy. Account baselines beat industry medians for diagnosis.
4. The offer document and landing page: the promise, the price, the conversion flow — because offer and funnel problems masquerade as ad problems.
5. The edit history: what changed and when (budget edits, audience changes, creative swaps, bid changes) — because most sudden performance drops follow a recent edit.
6. Real proof and approved claims referenced in creative — never infer results.
7. Agent inference for diagnosis logic and sequencing only — never for facts, results, or claims.

Completion: the target KPI, the current performance data, the historical baseline, the edit history, and the phase (Learning / Active / Scaling) are known or marked unknown.

## Required Inputs

Minimum useful inputs:

- the business or brand
- the campaign or ad set under review (name or ID)
- the target KPI (target CPA, target CPL, or target ROAS)
- current performance data (spend, results, CPA/CPL/ROAS, CTR, CPC, CPM, frequency) for the relevant time window
- how long the campaign or ad set has been running
- the conversion event being optimized for

Best inputs:

- a completed campaign plan from `meta-ads-manager`
- performance data broken out by ad set and by ad (not just campaign totals)
- the historical baseline for this account (what healthy looks like here)
- the edit history (what changed and when over the last 2-4 weeks)
- traffic temperature per ad set (cold, warm, hot) — benchmarks differ by temperature
- hook rate (3-second video plays / impressions) and hold rate for video creatives
- unique link clicks vs landing page views (to detect technical leaks)
- add-to-cart rate and checkout rate (for ecommerce)
- the landing page URL and any known funnel issues
- the Pixel/CAPI and Event Match Quality status (a broken signal produces phantom metrics)

Completion: there is enough data to diagnose against a target, compare to a baseline, and identify the bottleneck without guessing.

## Core Workflow

### 1. Orient to the wiki and the account

If working inside a client wiki, read:

- `SCHEMA.md`, `index.md`, recent `log.md`
- the target business's brand, offer, avatar, and the `meta-ads/` campaign plan being optimized
- any prior `meta-ads/optimization/` entries for this campaign

Completion: the campaign context, target KPI, and save path are known.

### 2. Confirm optimization scope

Define before diagnosing:

- business and business slug
- Meta ad account ID
- the campaign and/or ad set under review
- the target KPI (target CPA, target CPL, target ROAS) and the break-even threshold
- traffic temperature per ad set (cold, warm, hot)
- the review cadence: daily, weekly, or monthly
- the time window of data being reviewed (yesterday, 3-day, 7-day, 14-day, 30-day)
- the phase of each ad set: Learning (under 50 conversions/week, or recently edited), Active (stable, past Learning), or Scaling
- confidence level and source list

Completion: the optimization is tied to one business, one campaign, one target KPI, one time window, and the phase of each ad set is known.

### 3. Pull and structure the performance data

Gather the data in a consistent shape before diagnosing. For each campaign, ad set, and ad under review, pull:

- **Spend and pacing:** spend in the window vs the expected pacing (daily budget × days, accounting for weekly averaging)
- **Results:** conversions, purchases, or leads, and the CPA / CPL / ROAS
- **Funnel metrics:** impressions, reach, frequency, CTR, CPC, CPM, unique link clicks
- **Video metrics (if video creative):** hook rate (3-second plays / impressions), hold rate (ThruPlays or average watch time)
- **Funnel-depth metrics (if available):** landing page views, add-to-cart rate, checkout rate
- **Trend direction:** is each metric improving, flat, or declining vs the prior comparable window

Always read 7-day and 14-day rolling averages alongside the daily number. Daily ROAS is volatile by design; a single bad day inside an otherwise stable 7-day average is not a signal to act. See the daily/weekly/monthly cadence in Step 6 and in `references/optimization-frameworks.md`.

Completion: the data is structured by campaign → ad set → ad, with trend direction and the relevant time window, ready for diagnosis.

### 4. Diagnose via the metrics matrix

Find the true bottleneck before deciding any action. Read metrics in relationship to each other — a single metric in isolation tells you almost nothing. Use the diagnosis matrix (full version in `references/optimization-frameworks.md`):

| Symptom | Likely cause | Where to look |
|---|---|---|
| High CPM + low CTR | Creative not stopping the scroll | Creative (first 3 seconds), hook |
| High CTR + low conversion | Landing page or offer problem | Funnel page, offer doc, checkout |
| High CPC, normal CTR | Bidding competition or narrow audience | Audience size, bid strategy, placements |
| High CPA, normal CTR/CPC | Offer, price, or funnel friction | Offer doc, checkout flow, add-to-cart rate |
| Rising frequency + falling CTR | Ad fatigue | Creative refresh |
| Low hook rate + high hold rate | Good message, weak opening visual | Test 3-5 new opening hooks, keep the body |
| High hook rate + low hold rate | Good opening, weak body or CTA | Redesign the middle-to-end of the video |
| High link clicks, low landing page views (>15% gap) | Technical leak — slow page, broken pixel | Page speed, server, tracking |
| High CTR + low add-to-cart | Offer/merchandising disconnect | Pricing, trust, ad-to-page congruence |
| CPA spikes after a recent edit | Learning Phase reset | Stop editing, wait |

**The diagnostic sequence:** start at the top of the funnel and move down. Is the creative stopping the scroll (CTR / hook rate)? Is it holding attention (hold rate)? Is it driving qualified traffic (unique link clicks)? Is the page loading and the offer resonating (landing page views, add-to-cart)? Is the checkout closing (CPA/ROAS)? The first metric that breaks its benchmark is the bottleneck. Fix that layer before judging the next.

**Account baseline rule:** compare every metric to this account's own healthy baseline first, industry medians second. A CPM of $25 might look high against a $15 industry median but be normal for a competitive beauty vertical. The trend relative to the account's own history is the strongest signal.

Completion: the single true bottleneck is identified and named, with the evidence (the metric relationships that point to it).

### 5. Decide the action: wait, kill, scale, refresh, or restructure

Once the bottleneck is identified, choose exactly one action. The phase of the ad set governs what actions are even available.

**Phase check first:**
- **Learning Phase** (under 50 conversions/week, or edited within the last 3-7 days): the only valid action is almost always **wait**. Do not edit. See Learning Phase discipline below and in `references/optimization-frameworks.md`.
- **Active / stable** (past Learning, performing near target): the valid actions are **wait**, **kill** (if failing kill criteria), or **refresh** (if fatigued).
- **Scaling** (being vertically or horizontally scaled): optimization actions must respect the scaling rules — see `meta-ads-scaler`. One change at a time.

**The five actions:**

1. **Wait.** The default. If the ad set is in Learning, if the 7-day average is on target, or if a single day's dip is inside normal volatility — do nothing. Document that you reviewed and chose to wait, with the reason and the next review date. Most performance issues resolve by waiting.
2. **Kill.** Apply the kill criteria (see `references/optimization-frameworks.md`): $5-$10 spend with zero unique link clicks; CTR below 1% or CPC above $3-$5 after enough spend; spend reaching 1x break-even CPA with zero conversions, then 2x with no second conversion. Kill losers early to protect budget for winners.
3. **Scale.** Only after 48-72 consecutive hours of profitable, above-target performance AND at least 60% of conversions being click-based (not view-through). Scaling is a `meta-ads-scaler` decision — flag it and hand off, do not execute the budget increase here unless explicitly asked.
4. **Refresh.** Triggered by rising frequency + falling CTR + rising CPM/CPA (the fatigue signature). Rotate in new creative. Do not make minor tweaks to a losing ad (Meta's Lattice engine clusters look-alikes and continues to penalize them) — build conceptually diverse new concepts, or "slice and paste" proven hooks onto new bodies. Refresh winners every 2-4 weeks proactively.
5. **Restructure.** Reserved for structural problems: over-fragmentation (budget spread too thin to exit Learning), auction overlap, broken conversion signal, or a campaign that cannot be saved by creative or offer fixes alone. Restructuring is expensive (resets Learning) — use sparingly, usually as a monthly decision.

Completion: exactly one action is chosen, justified by the diagnosis and the phase, with the specific change defined (which ad set, which edit, why).

### 6. Execute ONE change

If the action is **wait**, execute nothing. If the action is kill, scale, refresh, or restructure, make exactly one change:

- **One variable at a time.** Changing budget, audience, creative, bid, and landing page simultaneously makes it impossible to know what moved the number. Test one thing.
- **Respect the 20% budget rule.** Budget changes greater than 20% at once reset the Learning Phase. Scale in 20% (conservative) to 30% (standard) to 50% (aggressive, only when ROAS is 50%+ above target) increments every 24-72 hours.
- **Launch at midnight.** Schedule new campaigns, creative tests, and major budget increases to go live at 12:00 AM. Launching mid-day forces Meta's 24-hour pacing clock to cram the daily budget into the remaining hours, spiking CPM and CPA.
- **Graduate winners by Post ID, never from scratch.** Duplicating a winning ad as a brand-new asset destroys its historical data and social proof. Use the Page Post ID to carry over likes, comments, and shares into the scaling campaign.

Completion: the single change is executed (or the decision to wait is logged), and the pre-change state is recorded so the effect can be measured.

### 7. Document the decision

Record the diagnosis, the action, the rationale, and the expected outcome. This is what makes optimization repeatable rather than reactive. Use the output shape below. Every entry must state:

- what was reviewed (campaign / ad set / ad, time window)
- the metrics that drove the diagnosis (the actual numbers, with the baseline for comparison)
- the bottleneck identified
- the action taken (or the decision to wait)
- the expected effect and the metric to watch
- the next review date and cadence

Completion: the decision is logged in a format a future session (or another media buyer) can read and continue from.

### 8. Schedule the next review

Set the next review based on the cadence:

- **Daily (5-10 min per account):** spend pace, major anomalies (spend spike, zero conversions, error alerts), backend health (checkout working, inventory in stock). No deep diagnosis — just tripwires.
- **Weekly (30-60 min per account):** 7-day performance review per campaign and ad set, identify winners and losers, plan creative refresh, check frequency and fatigue, re-forecast against the financial model.
- **Monthly:** full audit, restructure if needed, update scaling plan, review ROAS/CPA trends over 30 days, catalog top performers, revisit audiences for overlap and saturation.

See `references/optimization-frameworks.md` for the full checklists.

Completion: the next review is scheduled with its cadence and its specific trigger metrics.

## Missing Information Handling

Do not invent missing facts or metrics. Use these labels:

- `Unknown`: no source material or data supports the answer
- `Needs confirmation`: likely but not verified against the live account
- `Client to provide`: requires ad account access, live performance data, Pixel/EMQ status, or budget confirmation
- `Risk flag`: a claim about results, ROAS, or conversions that needs verification before it is repeated
- `Out of scope`: a structural, creative, or scaling decision that belongs to another skill

If the target KPI is missing, stop and confirm it. Diagnosing metrics without a target is scoreboard-watching, not optimization. If the performance data is missing or stale, say so — do not diagnose from guessed numbers. If the conversion signal (Pixel/CAPI) is broken, flag it as the root cause: every metric derived from a broken signal is unreliable.

## Quality Bar

A strong optimization decision has:

- one business, one campaign, one target KPI, one time window, and the phase of each ad set stated
- the data structured by campaign → ad set → ad with trend direction
- metrics read in relationship (the diagnosis matrix), not in isolation
- every metric compared to the account's own baseline, with industry medians as a secondary reference
- the single true bottleneck identified and named with evidence
- exactly one action chosen, justified by the diagnosis and the phase
- the Learning Phase respected — no edits during Learning unless the kill criteria are met
- the pre-change state recorded so the effect is measurable
- the expected effect and the metric to watch stated
- the next review date and cadence set
- frequency and fatigue assessed for every active creative
- the backend (checkout, inventory, page speed) checked before blaming the ads
- a confidence level and source list

A weak optimization decision has:

- a single day's ROAS treated as a signal to act
- metrics read in isolation ("CTR is low") without the related metrics that explain why
- industry medians used as the target instead of the account's own baseline
- multiple changes made at once (budget + audience + creative), making cause and effect unreadable
- an edit made during the Learning Phase
- a budget increase larger than 20% in one step, resetting Learning
- a campaign launched or edited mid-day instead of at midnight
- a winning ad duplicated from scratch instead of graduated by Post ID
- minor tweaks to a losing ad (background color, one word) expecting it to revive
- no documentation of what was changed or why
- backend failures (broken checkout, out-of-stock) misdiagnosed as ad problems
- no next review scheduled

## Common Pitfalls

1. **Acting on daily volatility.** Meta's pacing averages over 7 days by design. A single bad day inside a stable 7-day average is not a signal. Review rolling 7-day and 14-day averages before deciding.
2. **Reading metrics in isolation.** "CTR is low" tells you nothing without CPM, CPC, and conversion context. High CPM + low CTR = creative; high CTR + low conversion = offer/funnel. Read the relationships.
3. **Editing during the Learning Phase.** Every significant edit (budget ±20%, audience, creative, bid) resets Learning. If the ad set is under 50 conversions/week or was edited in the last 3-7 days, the answer is almost always wait.
4. **Multiple changes at once.** Changing budget, audience, creative, and landing page simultaneously makes it impossible to isolate what moved the number. One variable at a time.
5. **Budget jumps over 20%.** Increasing budget by more than 20% in a single step resets the Learning Phase and causes a 1-7 day performance dip. Scale in 20-30% increments.
6. **Launching or editing mid-day.** Meta's pacing clock runs midnight to midnight. A mid-day launch forces the daily budget into the remaining hours, spiking CPM and CPA. Schedule changes for 12:00 AM.
7. **Duplicating winners from scratch.** Copying a winning ad as a new asset destroys its historical data and social proof. Graduate winners using the Page Post ID to carry over engagement.
8. **Tweaking losers.** Meta's Lattice engine clusters look-alike creatives by Entity ID. Minor visual tweaks to a failing ad do not revive it — the algorithm recognizes the concept and keeps penalizing it. Build conceptually diverse new concepts instead.
9. **Treating retargeting ROAS as the headline number.** Retargeting routinely produces 5x-12x ROAS off warm traffic. It is a growth trap. Scaling decisions must measure incremental lift on cold prospecting, where 2x may be perfectly healthy.
10. **Blaming the ads for backend failures.** A broken checkout script, an out-of-stock product, or a slow landing page will show up in Ads Manager as "bad ad performance." Check the backend daily before diagnosing the ads.
11. **Ignoring frequency.** Rising frequency + falling CTR + rising CPM is the definitive fatigue signature. If you miss it, you keep spending against an audience that has stopped reacting. Refresh proactively every 2-4 weeks.
12. **No documentation.** An optimization decision that isn't logged is a decision that can't be continued, audited, or learned from. Every review produces an entry: what was reviewed, what was found, what was done, what to watch next.

## Verification Checklist

- [ ] Business, ad account, campaign, and target KPI confirmed
- [ ] Traffic temperature per ad set stated (cold / warm / hot)
- [ ] Time window of data confirmed (yesterday / 3-day / 7-day / 14-day / 30-day)
- [ ] Phase of each ad set stated (Learning / Active / Scaling)
- [ ] Performance data structured by campaign → ad set → ad with trend direction
- [ ] Every metric compared to the account's own baseline (industry medians secondary)
- [ ] Metrics read in relationship (diagnosis matrix applied), not in isolation
- [ ] Single true bottleneck identified and named with evidence
- [ ] Exactly one action chosen (wait / kill / scale / refresh / restructure), justified by diagnosis and phase
- [ ] Learning Phase respected — no edits during Learning unless kill criteria met
- [ ] Change executed is one variable only (or decision to wait logged)
- [ ] Budget change within 20% (or 30% standard / 50% aggressive with justification)
- [ ] Change scheduled for midnight if it is a launch or major budget increase
- [ ] Winner graduated by Post ID, not duplicated from scratch (if scaling/refreshing)
- [ ] Frequency and fatigue assessed for every active creative
- [ ] Backend checked (checkout, inventory, page speed) before blaming ads
- [ ] Pre-change state recorded so effect is measurable
- [ ] Expected effect and metric to watch stated
- [ ] Next review date and cadence (daily / weekly / monthly) set
- [ ] Decision documented in the output shape below
- [ ] Confidence level and source list included
- [ ] If wiki-backed, decision filed under `businesses/<business-slug>/meta-ads/optimization/` and linked
- [ ] Final output follows the optimization decision document shape

## Output Shape

```markdown
# Campaign Optimization: [Campaign Name] — [Date]

## Scope
- Business:
- Business slug:
- Meta ad account ID:
- Campaign / ad set under review:
- Target KPI (CPA / CPL / ROAS):
- Break-even threshold:
- Traffic temperature: cold / warm / hot
- Review cadence: daily / weekly / monthly
- Time window: yesterday / 3-day / 7-day / 14-day / 30-day
- Phase: Learning / Active / Scaling
- Confidence:
- Sources used:

## Performance Data
### Campaign: [Name]
| Ad set | Spend | Pacing | Results | CPA/CPL/ROAS | CTR | CPC | CPM | Frequency | Trend |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

### Video metrics (if applicable)
| Ad | Hook rate | Hold rate | Note |
|---|---|---|---|
| | | | |

### Funnel-depth metrics (if available)
| Ad set | Link clicks | Landing page views | Add-to-cart | Checkout | Note |
|---|---|---|---|---|---|
| | | | | | |

## Account Baseline (for comparison)
- Healthy CTR:
- Healthy CPC:
- Healthy CPM:
- Healthy CPA/CPL:
- Healthy frequency:

## Diagnosis
- Bottleneck identified:
- Evidence (metric relationships):
- Layer (creative / offer / funnel / audience / bidding / technical):
- Backend checked (checkout, inventory, page speed): yes / no / n/a

## Decision
- Action: wait / kill / scale / refresh / restructure
- Rationale (tie to diagnosis and phase):
- Specific change made (or "no change — waiting"):
- Pre-change state recorded:

## Expected Effect
- Metric to watch:
- Expected direction:
- Re-evaluate on (date):

## Next Review
- Cadence: daily / weekly / monthly
- Trigger metrics:
- Next review date:

## Needs Confirmation
- [unverified data, missing baseline, unconfirmed Pixel/EMQ, stale numbers]
```
