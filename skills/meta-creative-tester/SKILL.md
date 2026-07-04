---
name: meta-creative-tester
description: Use when designing a Meta (Facebook/Instagram) creative test, diagnosing why a creative is winning or losing, planning a creative refresh cycle, or building a creative testing calendar. Produces a structured testing plan (hypothesis, variables, ad set structure, budget, duration, kill/scale criteria) and creative lifecycle diagnostics. Covers hook vs format vs angle vs offer framing tests across video, static, and carousel formats.
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, meta-ads, facebook-ads, creative-testing, paid-social, media-buying, ad-creative]
    related_skills: [meta-ads-manager, meta-audience-builder, meta-ads-scaler, campaign-optimizer, ad-creative-brief-writer, ad-script-writer, hook-angle-writer, vsl-writer, offer-builder, human-editor]
---

# Meta Creative Tester

## Overview

Design and operate a disciplined creative testing system for Meta Ads. This skill produces a structured creative test plan — hypothesis, variable isolation, ad set structure, budget, duration, winner and kill criteria — plus creative lifecycle diagnostics (fatigue, hook vs hold rate, refresh cadence) that a media buyer can execute against.

Creative is the #1 lever in Meta Ads performance — more than targeting, bidding, or budget. Under Meta's modern architecture (Andromeda / GEM), targeting has reversed: the creative itself does the targeting. Meta analyzes the image, parses the copy, transcribes the video, and matches the creative to the right audience segment in real time. The media buyer's job is no longer to find the audience; it is to feed the algorithm conceptually diverse creative and let the market decide what wins.

Use `references/creative-testing-frameworks.md` for the detailed framework reference (testing methodologies, the creative lifecycle, fatigue signals, winner/loser criteria, format benchmarks, the first-3-seconds framework, refresh cadence). This file is the operating process.

The core discipline: treat creative testing as a scientific process, not a guessing game. One variable per test. Forced, even spend via ABO. A defined duration before judging. Winners identified by cost per conversion — never by CTR alone. Kill losers at a threshold. Graduate winners by Post ID into scaling campaigns.

## When to Use

Use this skill when the client asks for:

- a creative test design (what to test, in which structure, for how long, with what criteria)
- a creative testing matrix or calendar (what to test this week, next week, the sprint after)
- a diagnosis of why a specific creative is winning or losing (hook vs hold rate, fatigue signals, format fit)
- a creative refresh plan (when to rotate, what to kill, what to iterate)
- a winner graduation plan (how to move a proven creative into scaling without losing social proof)
- a creative testing ad set structure (ABO sandbox, CBO sticky-note, runoff testing)
- a kill/scale criteria document for an active campaign
- a creative lifecycle audit (frequency, CTR drop, CPA rise)

Do not use this skill for:

- full campaign structure (objective, CBO vs ABO for the whole account, retargeting setup) — use `meta-ads-manager`
- scaling budgets and the vertical/horizontal scaling framework — use `meta-ads-scaler`
- audience research, lookalike tiers, interest selection — use `meta-audience-builder`
- writing the creative itself (scripts, statics, video) — use `ad-script-writer`, `ad-creative-brief-writer`, `vsl-writer`, `hook-angle-writer`
- building the offer being advertised — use `offer-builder`
- daily metrics optimization across a live campaign — use `campaign-optimizer`

## Multi-Business Rule

A client can run several businesses, and each business can have many ad accounts, offers, and creative testing programs. Never blend test results, creative assets, CPA targets, or audience data across businesses. Before planning a test, confirm the business, business slug, Meta ad account ID, the offer being tested, and the conversion event the creative must drive.

Store creative test plans inside the client wiki under the correct business:

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
    └── creative-tests/
        ├── <test-slug>.md
        └── creative-calendar.md
```

If the wiki uses another structure, follow it while keeping every test grouped by business and linked to its offer, avatar, and creative assets.

## Source Hierarchy

Orient from the client wiki first. Read `SCHEMA.md`, `index.md`, recent `log.md`, and the target business pages before claiming facts. Then prioritize:

1. The offer document: dream outcome, mechanism, price, objections — creative must sell the offer, not itself.
2. The avatar profile: the exact language, pains, and desires the creative must speak to.
3. Brand voice and attractive character: the tone and signature phrases that make the creative on-brand.
4. Existing creative performance data: winners, losers, known hook rates, hold rates, CPA by creative, fatigue signals.
5. The conversion event and target CPA: testing criteria are meaningless without a defined cost target.
6. Real proof and approved claims available for use in the creative.
7. Agent inference for test structure and sequencing only — never for results, proof, or claims.

Completion: the offer, avatar, conversion event, target CPA, and existing creative performance data are known or marked unknown.

## Required Inputs

Minimum useful inputs:

- the business or brand
- the offer being promoted
- the conversion event (purchase, lead, booking, trial)
- the target CPA or target ROAS (the threshold for winner/loser decisions)
- the traffic temperature (cold, warm, hot)
- whether a Pixel/CAPI signal is clean (testing against a broken signal produces garbage data)

Best inputs:

- a completed offer document from `offer-builder`
- a completed avatar profile and brand voice guide
- existing creative assets (or a creative brief from `ad-creative-brief-writer`)
- past creative performance data (CTR, hook rate, hold rate, CPA, frequency, spend by creative)
- known winning hooks and angles from past campaigns
- the live campaign structure (to know where a test fits)
- budget available for testing

Completion: there is enough source material to design a test with a real hypothesis, a real variable, and a real kill/scale threshold — not a "throw creatives at the wall" exercise.

## Core Workflow

### 1. Orient to the wiki

If working inside a client wiki, read:

- `SCHEMA.md`, `index.md`, recent `log.md`
- the target business's brand, offer, avatar, character, voice, and any existing `meta-ads/` or `creative-tests/` plans
- past creative performance data if filed

Completion: the test context, source assets, and save path are known.

### 2. Confirm test scope

Define before designing the test:

- business and business slug
- Meta ad account ID
- offer and offer slug
- primary avatar
- conversion event (the thing the creative must drive)
- target CPA or target ROAS
- traffic temperature: cold, warm, or hot
- daily or weekly testing budget
- existing creative performance baseline (what is currently winning, what is fatiguing)
- confidence level and source list

Completion: the test is tied to one business, one offer, one avatar, one conversion event, and one target CPA.

### 3. Verify the conversion signal is clean

Creative test data is only as trustworthy as the conversion signal feeding it. If the Pixel or CAPI is broken, every winner/loser decision is based on garbage. Confirm before testing:

- [ ] Pixel firing the target event (Purchase, Lead, Schedule)
- [ ] CAPI installed server-side and sharing hashed user data
- [ ] Event Match Quality (EMQ) above 6/10 (ideally 8+)
- [ ] At least 50 conversions per week per ad set is achievable at the planned budget (otherwise the test never exits the Learning Phase)

If the signal is broken or the budget cannot generate 50 conversions/week, the test is premature. Flag the gaps first.

Completion: the conversion signal is verified, or the gaps are documented as blocking the test.

### 4. Define the test hypothesis

Every test starts with a hypothesis, not a creative wishlist. A hypothesis has the shape: "We believe [variable] will [improve/worsen] [metric] because [reason tied to the avatar or offer]."

Example hypotheses:

- "We believe a UGC-style demo hook will lower CPA vs. the current founder-led hook because cold traffic responds to social proof before authority."
- "We believe a 15s static benefit-callout will outperform the 60s video on warm retargeting traffic because warm audiences need a nudge, not a pitch."
- "We believe testing the 'bad lead quality' angle will outperform the 'low show rates' angle because the avatar's stated pain is lead quality, not show rates."

A test without a hypothesis cannot be interpreted. "Let's try some new creatives" is not a test.

Completion: each test has a written hypothesis naming the variable, the expected direction, and the reason.

### 5. Choose the variable to test

Test one variable at a time. Testing multiple variables in one ad set confuses the algorithm and makes it impossible to attribute the result.

The variables, in order of impact (test the top of this list first):

1. **Hook** — the first 3 seconds (video) or the first line / text overlay (static). The hook is ~90% of the ad's success. This is the highest-leverage variable.
2. **Format** — video vs static vs carousel. Never mix formats in the same testing ad set; the delivery algorithm treats them differently and you lose the read.
3. **Angle** — the core message / pain point / desire the creative speaks to (e.g., "bad lead quality" vs "low show rates" vs "bad agencies").
4. **Offer framing** — how the offer is positioned (e.g., "free book + shipping" vs "application call" vs "direct purchase").
5. **Length** — 6s vs 15s vs 30s vs 60s+ vs long-form explainer.
6. **CTA** — the call to action and its framing.

For the 3-2-2 (or 3-2-2-2) Dynamic Creative framework, see `references/creative-testing-frameworks.md`. For Hormozi's 6-angles × 5-hooks bolt-on system, see the same reference.

Completion: the single variable (or the structured 3-2-2 set) is named, and every creative in the test differs only on that variable.

### 6. Structure the testing ad set

Use ABO (Ad Set Budget Optimization) for testing. ABO forces Meta to distribute spend evenly across creatives; CBO funnels spend to the early "lucky" favorite and starves the variants you need data on.

**Standard ABO sandbox structure:**

```
Campaign: [Offer] — Creative Test (Objective: Sales/Leads, ABO)
├── Ad Set 1: Broad (Advantage+ Audience) — Variant A
│   ├── 3-6 ads differing only on the test variable
│   └── (OR one Dynamic Creative / Flexible ad with 3 visuals × 2 texts × 2 headlines)
├── Ad Set 2: Broad — Variant B (if testing across audiences)
└── Exclusions: past purchasers (180 days to all-time)
```

Rules:

- **One concept per ad set** if running discrete creatives; **one Dynamic Creative (DCT) per ad set** if running the 3-2-2 framework.
- **3-6 creatives per ad set.** Fewer than 3 tests nothing; more than 6 splits budget too thin to reach 50 conversions each.
- **Never mix static and video in the same ad set.** The delivery algorithm treats formats differently — mixing them ruins the read.
- **Set the ad set daily minimum spend at 1x your target CPA** to force Meta to actually spend on the test creatives.
- **Exclude only past purchasers.** Over-excluding (website visitors, engagers) starves the algorithm and raises CPM.
- **Launch at midnight.** A campaign launched at 3 PM will panic-spend the daily budget before midnight, spiking CPA.

For the CBO "sticky-note" method (one consolidated campaign, champions ad set + testing ad sets) and the runoff testing method (recovering under-exposed creatives), see `references/creative-testing-frameworks.md`.

Completion: the testing ad set structure is mapped with audience, budget, exclusions, and the creatives (or DCT) assigned to each.

### 7. Set the duration and budget

- **Minimum 7 days before judging.** Meta needs ~50 conversions per ad set per 7 days to exit the Learning Phase. Judging before that is reading noise.
- **Run in two-week sprints** to collect weekdays-inclusive, conclusive data before making decisions.
- **Budget per ad set:** set daily spend at 1x target CPA minimum, ideally 2-3x to clear the Learning Phase fast. If target CPA is $20, test at $40-60/day per ad set.
- **Do not edit during the test.** Every edit (budget ±20%, audience, creative swap, bid change) resets the Learning Phase. Set it and leave it for the duration.

Completion: the test duration and per-ad-set budget are set to reach statistical signal, not to "save money."

### 8. Identify winners and losers

**Winner criteria:**

- Lowest cost per conversion (CPA at or below target) at volume — not highest CTR.
- Consistent for 48-72 hours minimum (a single good day is not a winner).
- At least 50 conversions accumulated to confirm it has exited the Learning Phase.
- At least 60% of conversions are click-based (not view-through) to confirm real incremental lift.

**Loser / kill criteria (apply in order):**

1. **The $5-$10 click filter:** if an ad spends $5-$10 with zero unique link clicks, kill it. It failed to stop the scroll; you don't need to wait for a purchase to know.
2. **The 1% CTR / high CPC threshold:** CTR below 1% or CPC above $3-$5, kill early.
3. **The 1x product cost rule:** if spend reaches 1x the product cost (or 1x break-even CPA) with zero conversions, kill it.
4. **The 2x CPA threshold:** if CPA reaches 2x target with 50+ conversions and no recovery, kill it.
5. **The break-even ladder:** track spend against multiples of break-even CPA — 1x with no sale, kill; if it sells, let it run to 2x, then re-evaluate.

Never judge a creative by CTR alone. A creative with high CTR and high CPA is sending the wrong people — it stops the scroll for non-buyers. The only metric that matters is cost per conversion.

Completion: every creative in the test has a clear winner, loser, or "needs more data" verdict tied to the criteria above.

### 9. Diagnose winners and losers (hook vs hold rate)

For video creatives, use Meta's hook rate (3-second views / impressions) and hold rate (average watch time or 15-second views) to diagnose why a creative won or lost:

| Signal | Diagnosis | Fix |
|---|---|---|
| High hook, low hold | The opening stops the scroll, but the body loses attention | Redesign the middle-to-end of the video; tighten the CTA |
| Low hook, high hold | Losing most viewers instantly, but those who stay convert | Keep the body identical; test 3-5 new opening hooks |
| Low hook, low hold | The creative fails at both | Kill it; build a conceptually new creative |
| High hook, high hold, high CPA | The creative engages but attracts non-buyers | The angle or offer framing is wrong; re-test the variable |

For static creatives, the equivalent diagnostic is CTR (did it earn the click?) vs. conversion rate (did the click convert?). High CTR + low conversion = the creative or landing page is misaligned with the offer.

Completion: every winner and loser has a diagnosed cause, which feeds the next test's hypothesis.

### 10. Handle creative fatigue and the lifecycle

Creatives on Meta have a volatile lifespan. Plan for it.

**The creative lifecycle:** launch → learning → peak → fatigue → refresh.

**Fatigue signals (any one is a warning; two or more is action):**

- Frequency above 5 (cold) or above 5-8 (retargeting, which tolerates higher frequency)
- Unique CTR dropping
- Thumbstop ratio dropping
- CPM rising
- CPA rising

**Refresh cadence:** plan to rotate or refresh active creatives every 2-4 weeks. A winning creative will fatigue; have the next batch ready before it does.

**The iterate-losers trap:** Meta's Lattice infrastructure clusters similar-looking ads by Entity ID. Making minor tweaks (background color, small headline swap) to a losing creative does not revive it — the algorithm recognizes the concept and keeps penalizing it. To iterate a winner, build conceptually diverse new visuals around the winning message. To recover a loser, start over with a new concept.

Completion: the test plan includes a refresh cadence and a fatigue-monitoring checkpoint.

### 11. Graduate winners into scaling

When a creative is a confirmed winner, graduate it into the scaling campaign — do not leave it in the testing sandbox.

**Graduation via Post ID (the only correct method):**

- Extract the exact Post ID (or ad ID) of the winning creative.
- Paste it into the scaling CBO or Advantage+ Sales Campaign (ASC).
- This preserves all accumulated social proof (likes, comments, shares), which lowers CPM and improves delivery in the scaling auction.
- Never duplicate a winner from scratch — it resets the algorithm's data and destroys social proof.

**Scale it where it lies (vertical):** if the testing ad set is performing exceptionally, do not disrupt it. Leave it in place and increase the campaign budget 20-50% every 24-72 hours.

**Hormozi's 70/20/10 iteration cycle** for the week after a winner graduates:

- 70% of new tests: slight variations of the winner (different clothing, horizontal flip, minor color filter) to extend its life.
- 20% of new tests: decent variations (new hook, different spokesperson, different setting).
- 10% of new tests: brand-new angles to discover the next winner.

See `references/creative-testing-frameworks.md` for the full graduation and iteration detail.

Completion: every winner has a graduation path (Post ID → scaling campaign) and an iteration plan.

### 12. Assemble the creative test document

Use this output shape:

```markdown
# Meta Creative Test Plan: [Offer] for [Avatar]

## Scope
- Business:
- Business slug:
- Meta ad account ID:
- Offer:
- Primary avatar:
- Conversion event:
- Target CPA / ROAS:
- Traffic temperature: cold / warm / hot
- Testing budget (daily / weekly):
- Pixel/CAPI status:
- Confidence:
- Sources used:

## Conversion Signal Readiness
- [ ] Pixel firing target event
- [ ] CAPI installed server-side
- [ ] EMQ score:
- [ ] 50+ conversions/week achievable at planned budget
- Gaps blocking the test:

## Test Hypothesis
- Hypothesis: We believe [variable] will [improve/worsen] [metric] because [reason]
- Variable tested: hook / format / angle / offer framing / length / CTA
- Expected direction:

## Test Structure
- Campaign name:
- Budget strategy: ABO (testing) / CBO sticky-note
- Ad sets:
  #### Ad Set 1: [Audience] — [variable]
  - Audience: Broad / Lookalike / Custom / Interest
  - Daily budget: (1x target CPA minimum)
  - Exclusions: past purchasers (180 days)
  - Creatives (or DCT): 3-6, differing only on the test variable
    1. [Creative A — what it isolates]
    2. [Creative B — what it isolates]
    3. [Creative C — what it isolates]
- Duration: 7 days minimum / two-week sprint
- Launch time: midnight (12:00 AM)

## Winner and Kill Criteria
- Winner: CPA at/below target, 48-72h consistent, 50+ conversions, 60%+ click-based
- Kill filters (in order):
  1. $5-$10 spend, zero link clicks → kill
  2. CTR <1% or CPC >$3-$5 → kill
  3. Spend = 1x product cost, zero conversions → kill
  4. CPA = 2x target at 50+ conversions → kill
- Primary metric: cost per conversion (not CTR)

## Creative Lifecycle Plan
- Refresh cadence: every 2-4 weeks
- Fatigue monitors: frequency >5, CTR drop, CPM rise, CPA rise
- Iteration approach: 70/20/10 (slight / decent / new concept)

## Winner Graduation Plan
- Method: Post ID into scaling CBO / ASC
- Vertical scaling: +20-50% every 24-72h
- Next sprint tests: [list]

## Needs Confirmation
- [unverified creative assets, unconfirmed target CPA, missing performance baseline, unconfirmed Pixel status]
```

Completion: the document can be handed to a media buyer to launch the test without reconstructing the strategy.

### 13. Update the wiki when appropriate

If working inside an LLM wiki:

- save the test plan under `businesses/<business-slug>/meta-ads/creative-tests/<test-slug>.md`
- link it to the offer, avatar, character, and creative assets
- update the creative calendar (`creative-calendar.md`) if one exists
- update `index.md` if appropriate
- append to `log.md`

Completion: the test plan is filed under the correct business and reusable in later sessions.

## Missing Information Handling

Do not invent missing facts. Use these labels:

- `Unknown`: no source material supports the answer
- `Needs confirmation`: likely but not verified
- `Client to provide`: requires ad account access, target CPA, creative assets, or performance data only the client can give
- `Risk flag`: a claim in the creative (income, health, financial, legal) needing review
- `Out of scope`: a variable or format the business cannot currently support

If the target CPA, conversion event, or conversion signal status is missing, stop and route to `offer-builder` or `meta-ads-manager` first. A creative test without a target CPA has no winner or kill threshold — it is spend without criteria.

## Quality Bar

A strong creative test plan has:

- one business, one offer, one avatar, one conversion event, and one target CPA
- a verified or gap-documented conversion signal (Pixel + CAPI + EMQ)
- a written hypothesis naming the variable, the expected direction, and the reason
- one variable isolated per ad set (or a structured 3-2-2 DCT)
- 3-6 creatives per ad set, never mixing static and video
- ABO budgeting with daily minimum spend at 1x target CPA
- a 7-day minimum / two-week sprint duration
- winner criteria based on cost per conversion at volume, not CTR
- kill criteria in a defined order (click filter → CTR/CPC → product cost → 2x CPA)
- a fatigue-monitoring and refresh-cadence plan
- a Post ID graduation path for winners
- a 70/20/10 iteration plan for the next sprint
- risky claims and unknowns flagged
- a confidence level and source list

A weak creative test plan has:

- no hypothesis ("let's try some new creatives")
- multiple variables changed in one ad set (new hook + new copy + new landing page)
- CBO used for testing (funnels spend to the early favorite)
- static and video mixed in the same ad set
- under 3 creatives or over 6 per ad set
- a budget too low to reach 50 conversions in the test window
- judging before 7 days or before 50 conversions
- winners chosen by CTR or thumbstop instead of cost per conversion
- no kill criteria (creatives left running until they drain budget)
- no graduation plan (winners left in the sandbox to fatigue)
- minor tweaks to losers (the Lattice penalty)

## Common Pitfalls

1. **No hypothesis.** "Let's test some new creatives" produces no learning. Every test needs a named variable and an expected outcome.
2. **Testing multiple variables at once.** New hook + new copy + new landing page in one ad set makes it impossible to attribute the result. One variable per ad set.
3. **CBO for testing.** CBO routes spend to the early winner, starving the variants you need data on. Use ABO for testing, CBO for scaling.
4. **Mixing static and video in one ad set.** The delivery algorithm treats formats differently. Mixing them ruins the read on which approach converts.
5. **Judging too early.** A creative with 5 conversions and $20 spend tells you nothing. Wait for 50 conversions and 7 days minimum.
6. **Choosing winners by CTR.** High CTR + high CPA means the creative stops the scroll for non-buyers. The only metric that matters is cost per conversion.
7. **No kill criteria.** Creatives left running "to see what happens" drain budget. Set the click filter, CTR/CPC, product-cost, and 2x-CPA thresholds up front.
8. **Iterating losers with minor tweaks.** Meta's Lattice clusters similar ads. A background-color swap on a loser does not revive it — it keeps the penalty. Build conceptually new creatives.
9. **Duplicating winners from scratch.** Resetting the Post ID destroys social proof. Graduate winners by Post ID into the scaling campaign.
10. **No refresh plan.** Every creative fatigues. If you don't have the next batch ready before frequency crosses 5, CPA will rise before you can react.
11. **Over-excluding audiences.** Layering visitor and engager exclusions on a prospecting test starves the algorithm and raises CPM. Exclude only past purchasers.
12. **Launching mid-day.** A campaign launched at 3 PM panic-spends the daily budget before midnight. Schedule launches at 12:00 AM.
13. **Editing during the test.** Every budget, audience, or creative edit resets the Learning Phase. Set it and leave it for the duration.

## Verification Checklist

- [ ] Business, ad account, offer, avatar, conversion event, and target CPA confirmed
- [ ] Conversion signal verified (Pixel + CAPI + EMQ + 50 conversions/week achievable)
- [ ] Test hypothesis written (variable, expected direction, reason)
- [ ] Single variable isolated per ad set (or structured 3-2-2 DCT)
- [ ] 3-6 creatives per ad set, formats not mixed
- [ ] ABO budgeting with daily minimum at 1x target CPA
- [ ] Duration set to 7 days minimum / two-week sprint
- [ ] Winner criteria: cost per conversion at volume, 48-72h consistent, 60%+ click-based
- [ ] Kill criteria defined in order (click filter → CTR/CPC → product cost → 2x CPA)
- [ ] Fatigue monitors defined (frequency, CTR, CPM, CPA)
- [ ] Refresh cadence planned (2-4 weeks)
- [ ] Winner graduation path: Post ID into scaling CBO / ASC
- [ ] 70/20/10 iteration plan for the next sprint
- [ ] Hook vs hold rate diagnostic available for video creatives
- [ ] Exclusions limited to past purchasers (no over-exclusion)
- [ ] Launch scheduled at midnight
- [ ] Risky claims and unknowns flagged
- [ ] Confidence level and source list included
- [ ] If wiki-backed, plan filed under `businesses/<business-slug>/meta-ads/creative-tests/` and linked
- [ ] Final output follows the creative test document shape
