# Campaign Optimization Frameworks Reference

This reference summarizes the optimization frameworks used by the `campaign-optimizer` skill and the related Meta Ads skill family (`meta-ads-manager`, `meta-creative-tester`, `meta-audience-builder`, `meta-ads-scaler`, `meta-lead-gen`). It is distilled from the Master Meta Ad notebook (213 sources covering metrics, benchmarks, diagnosis, Learning Phase, daily/weekly/monthly workflow, and the common mistakes that reset the algorithm).

**Conflict resolution rule:** Where sources conflict, Hormozi's principles win. For non-Hormozi conflicts, majority opinion wins. Use this as a field guide, then verify against the client's actual ad account data and baselines.

## Performance Metrics and Benchmarks

Read every metric against the account's own healthy baseline first, industry medians second. The trend relative to the account's history is the strongest signal.

### Core Metrics

| Metric | What it measures | Benchmark (industry) | What it tells you |
|---|---|---|---|
| **CTR (Click-Through Rate)** | Clicks / impressions. Immediate relevance and appeal of creative to the audience. | Median **1.77%**. Target **1-2%**. High-performers aim **2.5%+**. Below **1%** = creative not stopping the scroll. | Creative hook and scroll-stop quality. |
| **CPC (Cost Per Click)** | Spend / clicks. Mathematical output of CPM and CTR. | Median **$0.49**. B2B **$0.68-$1.38**. Scaling volume targets **under $1.00**. High CPC ($3-$5+) = creative problem (low CTR) or auction problem (high CPM). | How much you pay for traffic. If CPC is too high, scaling is mathematically impossible. |
| **CPM (Cost Per 1,000 Impressions)** | Spend / impressions × 1000. The auction's real-time feedback on your ad's total value (bid + estimated action rates + user experience). | Healthy **$15-$20**. Varies wildly by vertical (jewelry ~$20, competitive beauty $40-$60). | Audience saturation or creative quality. Meta penalizes poor-experience ads with a CPM premium. |
| **CPL (Cost Per Lead)** | Spend / leads. Cost-efficiency of the lead funnel. | Median **$41.26** (Dec 2024). | Funnel landing page or application bottleneck (if front-end metrics are strong). Lead quality / pixel conditioning (if CPL is low but close rate is low). |
| **CPA (Cost Per Acquisition/Purchase)** | Spend / purchases. | Based on margin and break-even. | Offer, creative, or funnel problem. The headline efficiency metric. |
| **ROAS (Return on Ad Spend)** | Revenue / spend. | Standard **1.5-2.0x**. Top scaling **3.0-4.0x**. Ecommerce target **4:1+**. Service offers **2:1**. | Immediate platform attribution. Unstable daily. Misleading as a scoreboard — see the retargeting illusion below. |
| **Frequency** | Impressions / reach. Audience saturation and exposure limits. | Cold/prospecting **up to 3**. Retargeting **up to 7**. Above = fatigue. | Ad fatigue (high freq + rising CPA + dropping CTR) or narrow scale limitation (high freq + low CPM). |
| **Relevance / Quality Ranking** | Meta's diagnostic (Quality, Engagement Rate, Conversion Rate Rankings). Populates after **500 reach**. | — | Audience-to-creative alignment and landing page experience. A signal, not a primary metric. |

### Unique Link Clicks Discipline

Media buyers prioritize **Unique Link Clicks** over general CPC to measure actual site visitors. Rules of thumb:

- **$1.10 unique link click cutoff:** if unique CPC exceeds this, scrutinize the creative.
- **$5-$10 zero-click kill:** if an ad spends $5-$10 without a single unique link click, pause it immediately. You do not need to wait for a purchase to know the creative failed to stop the scroll.

### Benchmarks by Traffic Temperature

Benchmarks shift by temperature because the audience intent differs:

| Metric | Cold (prospecting) | Warm (engagers/visitors) | Hot (retargeting) |
|---|---|---|---|
| CTR | 1%+ (2.5%+ target) | 1.5-2%+ | 2%+ |
| Frequency ceiling | up to 3 | up to 5 | up to 7 |
| ROAS expectation | 1.5-2x (incremental) | 2-3x | 5-12x (warm — do not confuse with cold) |
| Creative role | Pattern interrupt, problem/curiosity | Mechanism, proof | Social proof, offer reminder, scarcity |

## The Diagnosis Matrix

Find the true bottleneck by reading metrics **in relationship to each other**, never in isolation. Start at the top of the funnel and move down — the first metric that breaks its benchmark is the bottleneck.

| Symptom | Likely cause | Where to look | Fix |
|---|---|---|---|
| High CPM + low CTR | Creative not stopping the scroll | Creative (first 3 seconds), hook | New opening hooks, new visual contrast |
| High CTR + low conversion | Landing page or offer problem | Funnel page, offer doc, checkout flow | Fix the page or the offer, not the ad |
| High CPC, normal CTR | Bidding competition or narrow audience | Audience size, bid strategy, placements | Widen audience, check bid, use Advantage+ placements |
| High CPA, normal CTR/CPC | Offer, price, or funnel friction | Offer doc, checkout flow, add-to-cart rate | Fix offer/price/friction |
| Rising frequency + falling CTR | Ad fatigue (definitive) | Creative refresh | Rotate new creative; do not tweak the loser |
| Low hook rate + high hold rate | Good message, weak opening visual | First 3 seconds | Keep the body, test 3-5 new opening hooks |
| High hook rate + low hold rate | Good opening, weak body or CTA | Middle-to-end of video | Redesign the body, tighten the CTA |
| High link clicks, low landing page views (>15% gap) | Technical leak — slow page or broken pixel | Page speed, server, tracking | Fix page speed / tracking before touching ads |
| High CTR + low add-to-cart | Offer/merchandising disconnect | Pricing, trust, ad-to-page congruence | Align the page to the ad's promise |
| CPA spikes after a recent edit | Learning Phase reset | Edit history | Stop editing, wait for re-learning |

### The Interdependent Diagnostic Chain

To find the true bottleneck, walk the funnel left to right. The first broken link is the problem:

```
[First 3s Hook] → [Body/Hold Rate] → [Landing Page Clicks] → [Checkout/Offer]
      │                  │                     │                      │
  "Hook Rate"       "Hold Rate"        "Landing Page Views"     "Add to Cart Rate"
      │                  │                     │                      │
 Stopped Scroll?    Held Interest?       Technical Leak?          Offer Appeal?
```

1. **Hook Rate vs Hold Rate (video diagnostics):**
   - High hook + low hold: stops the scroll, loses attention immediately → the body/CTA is weak.
   - Low hook + high hold: loses most viewers in 3s, but those who stay convert → good message, poor opening visual. Test 3-5 new hooks, keep the body.
2. **Unique Link Clicks vs Landing Page Views (technical leak):**
   - High clicks but a >15% drop-off in landing page views → slow page load or server lag. Users bounce before the pixel fires. Fix the page, not the ad.
3. **High CTR + Low Add-to-Cart (offer/merchandising leak):**
   - Ad drove cheap traffic, but users don't add to cart → pricing disconnect, lack of trust, or ad-to-page mismatch. Fix the offer or the page congruence.

### The Retargeting ROAS Illusion

High ROAS (5x-12x) is easily manufactured by retargeting warm visitors or existing customers. It is a **growth trap**: scaling requires measuring incremental lift on cold prospecting, where a lower ROAS (e.g., 2x) is acceptable if it drives net new customer acquisition. Never let retargeting ROAS set the headline expectation for cold campaigns.

### Post-Scale ROAS Decay

A sudden ROAS drop when scaling budgets does not automatically mean the ad is failing. Delayed post-iOS 14.5 conversion reporting (up to 72 hours) and natural customer consideration lag mean ROAS will temporarily decline as you warm up cold audiences. Read 7-day averages, not the day-of number.

## Learning Phase Discipline

Meta's machine learning requires data to optimize. Respecting the Learning Phase is the single highest-leverage discipline in optimization.

### The 50-Conversion Law

An ad set must record a minimum of **50 conversion events per week** (roughly 7-8 per day) to exit the Learning Phase and optimize delivery. Below this, performance is volatile and CPA is elevated.

### Budgeting for the Phase

- **Daily budget:** set at **2-3x your break-even CPA** to ensure the ad set clears Learning quickly.
- **Cost-cap / bid-cap campaigns:** set daily budget at **minimum 8x your cost cap** (50 conversions / 7 days ≈ 8x) to ensure enough daily volume to exit Learning.

### Optimization Minimums

- **8,000 impressions:** Meta needs this to begin understanding how to optimize a campaign.
- **500 reach:** the minimum to generate an early relevance / diagnostic score.

### The Midnight Launch Rule

Always schedule new campaigns, creative tests, or major budget increases to go live at **12:00 AM (midnight)** the next day. Meta's pacing clock runs midnight to midnight. Launching mid-day (e.g., 3 PM or 6 PM) forces the algorithm to cram the entire daily budget into the remaining hours, buying low-quality expensive impressions and spiking CPA.

### What Resets the Learning Phase

Every significant edit resets Learning, causing a 1-7 day performance dip while the algorithm re-learns:

- Budget change greater than 20% at once
- Changing the audience mid-Learning
- Swapping or significantly editing creatives
- Pausing and restarting ad sets
- Changing the optimization event
- Adding or removing placements mid-campaign

**Discipline:** one change at a time, then wait. If an ad set is in Learning, the answer is almost always **wait**.

### The Two-Week Stabilization Window

Allow new creative tests or structural updates to run for **two weeks** without manual adjustments to gather conclusive, weekdays-inclusive data. Weekday and weekend purchase patterns differ; judging on a partial week skews the read.

## When to Touch vs. Leave Alone

### The Golden Rule

**"If something is working, just leave it on."** Do not shut down historical winners or disrupt active, profitable ad sets simply to reorganize account structure. Profitable stability is hard to achieve and easy to destroy.

### Hands-Off Testing

Let the machine cook. The more you log into Ads Manager to adjust bids, tweak budgets, or turn ads on and off, the more you disrupt the algorithm. Give newly launched ads **48 hours to 7 days** to stabilize before stepping in.

### The Scaling Trigger

Enter scaling protocol (vertically increasing budget every 24 hours) **only** after the campaign has maintained profitable, above-target KPI performance for **48-72 consecutive hours**, AND at least **60% of conversions are click-based** (not view-through). Relying on view-through inflates ROAS and leads to scaling campaigns that aren't driving incremental lift. Scaling execution belongs to `meta-ads-scaler`.

## Kill Criteria

Cut underperforming ads early to protect budget for winners. Apply this hierarchy:

1. **$5-$10 Clicks Filter (front-end check):** if an ad spends $5-$10 without a single unique link click, pause it immediately. The creative failed to stop the scroll.
2. **1% CTR / High CPC threshold:** if CTR is below 1% or CPC is excessively high ($3-$5+), cut early. A CTR of 2.5%+ is required to drive cheap traffic.
3. **$10 Add-to-Cart cutoff (middle-funnel check):** if an ad drives traffic but cost per add-to-cart exceeds ~$10, it is not generating real intent.
4. **1x Product Cost rule:** let an ad run 2-3 days. If spend reaches 1x the product cost with zero conversions, kill it.
5. **The Break-Even Ladder (the math close):** track spend against multiples of break-even CPA. If break-even CPA is $23.78: at $23.78 (1x) with no sale, kill; if it gets a sale, let it run; at $47.56 (2x) without a second sale, kill; follow the ladder.
6. **Automated rules:** set rules to pause any ad set if 3-day average CPA exceeds target, or decrease campaign budget by 20% if 3-day ROAS drops below profitable target.

## Daily / Weekly / Monthly Workflow

### Daily (5-10 min per account)

The daily review is a tripwire check, not a deep diagnosis. Its job is to catch anomalies and backend failures, not to react to normal volatility.

- [ ] **Top-line diagnostic:** total spend, contribution margin, top-line revenue across channels. Do not decide solely on in-platform ROAS (heavily modeled and manipulable).
- [ ] **Performance tracking:** yesterday's spend, ROAS, and CPA. Flag campaigns needing immediate attention (severe underperformance or a crushing winner).
- [ ] **Pacing check:** is daily spend on track? Remember Meta operates on a **weekly average** — daily spend can fluctuate up to 50% above the daily limit on high-opportunity days, balancing across the week.
- [ ] **Backend audit:** check website, cart scripts, and fulfillment. Backend failures (broken checkout, out-of-stock) masquerade as bad ad performance.
- [ ] **Error alerts:** any delivery errors, Pixel firing issues, or disapprovals.

### Weekly (30-60 min per account)

The weekly review is where real optimization happens. This is where you diagnose, decide, and plan.

- [ ] **7-day performance review:** evaluate campaigns over rolling **7-day averages**, not daily numbers. Tolerate daily inconsistency to achieve scale.
- [ ] **Per-ad-set review:** for each ad set, read the metrics in relationship (diagnosis matrix), identify the bottleneck, and choose one action (wait / kill / scale / refresh / restructure).
- [ ] **Winner / loser identification:** which creatives and ad sets are winning (at or below target CPA) and which are losing (hitting kill criteria).
- [ ] **Frequency and fatigue check:** rising frequency + falling CTR + rising CPM/CPA = fatigue. Plan refresh.
- [ ] **Creative refresh plan:** brief new concepts, schedule production, plan the next iteration. Catalog top hooks to "slice and paste" onto new bodies.
- [ ] **Re-forecasting:** align active spend, CAC, and new-customer acquisition goals with the financial model.
- [ ] **Sprint testing:** grade ad concepts in **two-week creative sprints**. Give batches a full 7 days of weekdays-inclusive data before judging. Turn off test ad sets that spend 7 days without hitting target KPI.
- [ ] **Pattern recognition:** log winning variables (top hooks, lengths, formats) and plan the next iteration.

### Monthly

The monthly review is the strategic audit and restructure window.

- [ ] **Macro planning:** update annual and monthly forecasts, adjust channel budget splits (e.g., 80% Meta prospecting, 20% secondary).
- [ ] **Full audit:** review 30-day ROAS/CPA trends across all campaigns. Identify structural problems (over-fragmentation, auction overlap, broken signal).
- [ ] **Restructure if needed:** consolidate over-fragmented budgets, fix broken conversion signals, reorganize account structure. Restructuring is expensive (resets Learning) — do it deliberately, not reactively.
- [ ] **Revenue peak isolation:** map the calendar for paydays, Sundays, holiday promos — coordinate aggressive, time-boxed scaling when demand is naturally high.
- [ ] **Audience maintenance:** revisit custom and target audiences every 30 days for CPM spikes, fatigue, and overlap.
- [ ] **Creative cataloging:** catalog top-performing ads. Isolate the first 3 seconds of the highest-velocity winners and plan to "slice and paste" those hooks onto other ad bodies to multiply creative inventory.
- [ ] **Update scaling plan:** review which campaigns are ready to scale (hand off to `meta-ads-scaler`).

## Budget Pacing Rules

### The 24-Hour Pacing Clock

Meta's pacing operates on a strict **24-hour clock starting at midnight**. A mid-day launch or edit forces the algorithm to spend the daily budget in the remaining hours, buying expensive low-quality impressions. Always schedule changes for 12:00 AM.

### Weekly Averaging

Daily budgets operate on a **weekly average**. Meta may spend up to **50% more than the daily limit** on high-opportunity days, balanced by slower days to hold the weekly average. Do not panic at a single day's high spend if the weekly average is on track.

### 7-Day Attribution Alignment

Pacing with cost-control bidding averages over a **7-day period**, aligning with Meta's standard 7-day attribution window. The algorithm intentionally allows high-CPA spikes on some days to learn, then balances with cheaper conversions later in the rolling week. Do not make knee-jerk daily budget adjustments when performance dips.

## Budget Increase Rules (for scale handoff)

How aggressively to increase budget depends on how far performance is pacing above target. Detailed scaling execution belongs to `meta-ads-scaler`; the thresholds matter here because crossing them resets Learning.

- **Conservative (10-20%):** increase budget 10-20% every 24-72 hours for stable scaling.
- **Standard (20%):** the baseline vertical scaling increment every few days as long as performance remains profitable. The 20% line is also the Learning Phase reset threshold.
- **Growth (30%):** every couple of days in active scaling. If performance dips, pull back 30% to stabilize.
- **Aggressive (50%):** only when ROAS is 50%+ above target (e.g., target 2x, seeing 3.5-4x), every 3-4 days.
- **Double-up / surf scaling (100%):** for low budgets (under $1,000/day) showing extreme profitability. At enterprise spend ($10,000+/day), avoid 50-100% jumps — sudden spikes force Meta to buy low-quality impressions and can double CPA overnight.

## Common Mistakes That Reset or Confuse the Algorithm

- **Frequent budget and structure tweaks:** minor daily adjustments continuously reset Learning, creating permanent instability.
- **Over-fragmentation:** spreading a tight budget across dozens of campaigns and ad sets dilutes conversion data, triggers auction overlap, and prevents ad sets from ever exiting Learning.
- **Simultaneous multi-variable testing:** testing copy, visuals, bidding, and landing pages all at once makes it impossible to isolate what drove the shift. One variable at a time.
- **Minor "loser" iterations:** swapping background colors or editing one word on a losing ad will not revive it. Meta's **Lattice** engine uses Entity IDs to cluster similar-looking creatives and continues to penalize recognized duplicates.
- **Duplicating winners from scratch:** copying a winner into a scaling campaign as a new asset destroys its historical data. Graduate proven winners using the **Page Post ID** to carry over accumulated social proof (likes, comments, shares), which lowers CPMs in the scaling auction.
- **Budget changes over 20%:** resets Learning in one step.
- **Mid-day launches and edits:** forces spend into remaining hours, spiking CPM and CPA.
- **Pausing and restarting ad sets:** resets Learning each time.

Each of these resets the Learning Phase, causing a 1-7 day performance dip while the algorithm re-learns. The discipline: **one change at a time, then wait.**

## Top Optimization Principles

1. **Wait is the default action.** Most performance issues resolve by waiting, not by intervening. If the ad set is in Learning or the 7-day average is on target, do nothing and document it.
2. **Read metrics in relationship, never in isolation.** The diagnosis matrix exists because a single metric tells you almost nothing. High CPM + low CTR = creative; high CTR + low conversion = offer/funnel. Find the bottleneck by walking the funnel.
3. **Compare to the account's own baseline first.** Industry medians are a secondary reference. The trend relative to this account's healthy history is the strongest signal.
4. **One change at a time, then wait.** Multiple simultaneous changes make cause and effect unreadable and stack Learning Phase resets. Change one variable, record the pre-change state, and wait for the 7-day average to read the effect.
5. **Respect the Learning Phase absolutely.** 50 conversions/week to exit. No edits during Learning (budget ±20%, audience, creative, bid all reset it). Launch at midnight. Budget at 2-3x break-even CPA (or 8x cost cap) to clear Learning fast.
6. **Graduate winners by Post ID.** Never duplicate a winner from scratch — it destroys the historical data and social proof that lower CPMs in the scaling auction.
7. **Check the backend before blaming the ads.** Broken checkouts, out-of-stock inventory, and slow pages show up in Ads Manager as "bad ad performance." Daily backend checks catch the real cause.
8. **Do not tweak losers; build conceptually diverse new concepts.** Meta's Lattice engine clusters look-alikes and keeps penalizing them. Minor edits to a failing ad do not revive it.
