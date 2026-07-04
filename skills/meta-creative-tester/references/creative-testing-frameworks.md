# Creative Testing Frameworks Reference

This reference summarizes the Meta Ads creative testing frameworks used by the `meta-creative-tester` skill and the related Meta Ads skill family (`meta-ads-manager`, `meta-audience-builder`, `meta-ads-scaler`, `campaign-optimizer`). It is distilled from the Master Meta Ad notebook (213 sources covering Hormozi, Andromeda/GEM, creative testing methodology, the creative lifecycle, fatigue, format performance, and the first-3-seconds framework).

**Conflict resolution rule:** Where sources conflict, Hormozi's principles win. For non-Hormozi conflicts, majority opinion wins. Use this as a field guide, then verify against the client's actual ad account data.

## The Core Principle: Creative Is the #1 Lever

Creative performance is the single most important driver of modern paid social acquisition, accounting for an estimated 60-70% of campaign success — more than targeting, bidding, or budget.

Under Meta's modern **Andromeda** machine-learning architecture, targeting has fundamentally reversed: **the creative itself does the targeting.** Instead of forcing the algorithm to find users via manual interest groups, the system performs a visual analysis of the image, parses the ad copy, transcribes the video hooks, and evaluates user behavior to match the creative with the right audience segment in real time.

The creative serves as both a persuasive asset and an algorithmic targeting input. Because of this, testing must be structured as a disciplined scientific process — one variable at a time, forced even spend, a defined duration, and criteria-based winner/loser decisions — not a guessing game.

**Implication for media buyers:** stop obsessing over audience targeting and start obsessing over creative diversity. A broad audience with 10 conceptually diverse creatives will out-perform a hyper-targeted audience with one creative, every time.

## Creative Testing Methodology

### The scientific method applied to creative

1. **One variable at a time.** Maintain a stable control and change only one variable per ad set. Testing new copy + new hooks + a new landing page simultaneously makes it impossible to isolate which change drove the result.
2. **Forced, even spend via ABO.** ABO (Ad Set Budget Optimization) forces Meta to distribute spend across creatives. CBO funnels spend to the early favorite and starves the variants you need data on.
3. **A defined duration.** Minimum 7 days, ideally two-week sprints. Meta needs ~50 conversions per ad set per 7 days to exit the Learning Phase.
4. **Criteria-based decisions.** Winners by cost per conversion at volume; losers by a defined kill ladder. Never by CTR alone.

### Testing structures

#### The ABO Sandbox Campaign (the growth standard)

- Dedicated manual campaign using ABO.
- Daily testing budget: $100-$200 per ad set (or 1x target CPA minimum).
- Isolate every distinct creative concept into its own individual ad set.
- Within each ad set: 3-6 ads (or one Dynamic Creative / Flexible ad).
- ABO forces even spend; CBO would prematurely funnel budget into early "lucky" favorites.

#### The CBO "Sticky Note" Method (the consolidated architecture)

- One consolidated CBO campaign for the business.
- One "Champions" ad set: top 4-6 historically proven ads (via Post IDs).
- One or two testing ad sets: each containing exactly one Dynamic Creative Test (DCT) or Flexible ad representing the new variable.
- Set an ad set daily minimum spend limit equal to 1x target CPA to guarantee Meta spends on the testing ad sets.
- Exclusions: past purchasers only (180 days to all-time). Do not over-exclude — it starves the algorithm and raises CPM.

#### The Runoff Testing Strategy (underdog recovery)

In standard ad sets with multiple creatives, Meta's algorithm allocates ~80% of budget to one early favorite, leaving the rest unexposed. To recover hidden winners:

- Isolate the starved "underdog" creatives in a separate "Runoff" ad set with fresh budget.
- This gives promising creatives a fair, unencumbered shot to prove their conversion rate and uncover hidden "unicorn" ads.

### Variable frameworks

#### The 3-2-2 (or 3-2-2-2) Dynamic Creative Framework

The gold standard for testing inside a Dynamic Creative or Flexible ad:

- **3 Visual Creatives** — highly distinct images or videos.
- **2 Primary Texts** — one new variant tested against historically best-performing copy.
- **2 Headlines** — focusing on different value propositions.
- **2 Landing Pages (the 3-2-2-2 variant)** — test the same creatives pointing to two URLs (e.g., standard Product Page vs. Advertorial/Listicle). Meta dynamically determines which page converts each creative best.

#### The 3-3-3 Creative Testing Framework

Organize the creative pipeline across three dimensions to feed the algorithm without internal auction competition:

1. **Three Funnel Levels (messaging):** Top-of-Funnel (introduce the problem/category), Middle-of-Funnel (differentiate the mechanism, handle objections), Bottom-of-Funnel (urgency, social proof, direct offer).
2. **Three Distinct Angles (pain points):** Test three entirely different pain points or desires (e.g., "bad lead quality" vs. "low show rates" vs. "bad agencies").
3. **Three Creative Formats:** Static images, vertical videos, and catalog sets in parallel.

#### Hormozi's 6-Angles × 5-Hooks Bolt-On System

For high-volume testing:

- List 6 distinct "angles" (the body copy / core message of the ad).
- "Bolt on" 5 different hooks to each angle = 30 unique ads.
- Run each in its own individual ad set to force Meta to spend on every variation.
- Double to 60 by having multiple creators film each ad.

#### Hormozi's 30-Hooks × 10-Bodies Multiplier (300 variations)

- Record 10 "meaty" ad bodies (each focusing on a specific belief breakdown, skill demonstration, or nuance).
- Record 30 distinct hooks separately.
- Edit the 30 hooks onto the 10 bodies = 300 unique ad variations for testing.

### Format separation rule

**Never mix static images and video ads in the same testing ad set.** Meta's delivery algorithm treats formats differently; mixing them prevents a clean read on which creative approach is actually converting.

## Winner and Loser Criteria

### Winner criteria

A creative is a confirmed winner when ALL of the following hold:

- **Cost per conversion at or below target CPA** at meaningful volume.
- **Consistent for 48-72 hours minimum** (a single good day is noise, not a winner).
- **50+ conversions accumulated** (the Learning Phase exit threshold).
- **60%+ of conversions are click-based** (not view-through) — view-through inflates ROAS and can lead to scaling non-incremental campaigns.

The primary metric is always **cost per conversion** — never CTR, thumbstop, or engagement. A creative with high CTR and high CPA is stopping the scroll for non-buyers.

### Kill criteria (apply in order)

1. **The $5-$10 click filter (front-end check):** if an ad spends $5-$10 with zero unique link clicks, kill it immediately. It failed to stop the scroll; you do not need to wait for a purchase to know.
2. **The 1% CTR / high CPC threshold:** CTR below 1% or CPC excessively high ($3-$5+), kill early. A healthy CTR target is 2.5%+ for cold traffic.
3. **The $10 add-to-cart cutoff (mid-funnel check):** if an ad drives traffic but cannot get add-to-carts below ~$10, it is not generating real intent — kill it.
4. **The 1x product cost rule:** let an ad run 2-3 days; if spend reaches 1x the product cost (or 1x break-even CPA) with zero conversions, kill it.
5. **The break-even ladder (the math close):** track spend against multiples of break-even CPA:
   - Reaches 1x CPA with no sale → kill.
   - Gets a sale, let it run; reaches 2x CPA without a second sale → kill.
   - Continues converting → follow the ladder up.
6. **The 2x CPA threshold:** if CPA reaches 2x target at 50+ conversions with no recovery, kill it.

### Automated rules

Set automated rules to protect budget without manual monitoring:

- Pause any ad set if the 3-day average CPA exceeds target.
- Decrease campaign budget by 20% if ROAS over the past 3 days drops below the profitable target.

## The Creative Lifecycle

Creative assets on Meta have a volatile lifespan. Staying ahead of declines requires a disciplined weekly cadence.

### The lifecycle stages

1. **Launch** — the creative goes live; the Learning Phase begins.
2. **Learning** — Meta gathers data; performance is volatile; CPC/CPA elevated. Do not judge or edit here.
3. **Peak** — the creative exits Learning Phase and hits its best CPA/ROAS. This is the window to scale and iterate.
4. **Fatigue** — the audience saturates; CTR drops, frequency rises, CPM and CPA climb.
5. **Refresh** — rotate or replace the creative before fatigue compounds.

### The two-week sprint

- Do not make knee-jerk daily edits or launch ad-hoc tests.
- Run tests in strict two-week sprints to collect weekdays-inclusive, conclusive data.
- Let ads run a minimum of 7 days before deciding their fate.
- If a test ad set gets no spend and fails to hit target KPI after 7 days, turn it off.

### Fatigue signals

An ad is fatiguing when any of these appear (two or more = act now):

- **Frequency above 5** (cold) — retargeting tolerates higher frequency (5-8 in a 7-day window for short sales cycles).
- **Unique CTR dropping** — the audience has seen it and is no longer clicking.
- **Thumbstop ratio dropping** — fewer 3-second views per impression.
- **CPM rising** — Meta is paying more to reach a saturated audience.
- **CPA rising** — the conversion cost is climbing as the creative loses effectiveness.

### Refresh cadence

Plan to completely refresh or rotate active creatives every **2-4 weeks**. A winning creative will fatigue; have the next batch ready before it does.

### Hook vs. Hold Rate Diagnostics (video)

Analyze the relationship between hook rate (3-second views / impressions) and hold rate (average watch time or 15-second views) to diagnose why a video ad is failing:

| Signal | Diagnosis | Fix |
|---|---|---|
| **High hook, low hold** | Opening stops the scroll, but the body loses attention immediately | Redesign the middle-to-end of the video; tighten the CTA |
| **Low hook, high hold** | Losing most viewers instantly, but those who stay are highly likely to convert | Keep the body identical; test 3-5 new visual opening hooks |
| **Low hook, low hold** | Fails at both | Kill it; build a conceptually new creative |
| **High hook, high hold, high CPA** | Engages but attracts non-buyers | The angle or offer framing is wrong; re-test the variable |

## The Iterate-Losers Trap (Lattice / Entity IDs)

Meta's **Lattice** infrastructure uses Entity IDs to cluster similar-looking ads. Making minor visual tweaks (background colors, small headline swaps on the same image) to a losing ad will **not** revive it — the algorithm recognizes the concept and continues to penalize it.

**The fix:** take the core message of your winners and build entirely new, conceptually diverse visual concepts. Do not iterate losers with cosmetic changes.

**Implication:** "Ugly" simple ads frequently outperform highly produced, expensive creatives because they feel native. Do not over-polish. The content on social feeds is grainy, blurry, shaky, and imperfect — matching that aesthetic removes consumer bias and makes the ad feel like organic content.

## Creative Format Performance Benchmarks

### Video

- **Best for:** top-of-funnel demand generation, visual storytelling, product demos, emotional connection, capturing cold traffic.
- **Strong formats:** UGC, scripted UGC, founder-led explainers.
- **Aspect ratio:** vertical 9:16 (with key content fitting a 4:5 safe frame) for Reels/Stories and feed.
- **Length guidance:**
  - **6s:** pure pattern interrupt, single message, CTA.
  - **15s:** hook + problem + solution + CTA (most common for direct response).
  - **30s:** hook + story + mechanism + offer + CTA (deeper persuasion).
  - **60-90s:** the standard individualized direct-response video ad. Allocate 3-5s for the opening hook, 5-10s for the final CTA, and the rest for the body.
  - **Long-form explainer (1-10+ min):** "long-form" is an intentional departure from short, rushed formats — use whatever time the product requires to explain every key feature and benefit. Founder-led explainers perform exceptionally well.
- **Captions:** always on. Sound-off viewing is common.

### Static image

- **Best for:** direct response, lower-funnel, high-CPM periods (statics waste fewer impressions on non-buyers), rapid iteration.
- **Aspect ratio:** vertical (fitting within a 1:1 frame) or 1:1 / 4:5.
- **Strengths:** cheap, fast, easy to build and iterate; allows rapid knee-jerk decisions.
- **Tested styles:** benefit call-outs, us-vs-them tables, "ugly" ad statics, feature/problem-focused layouts, text-only stills, testimonials.
- **The "Scratch Out" test:** a strong static must be completely unique. If you can scratch out your logo, write in a competitor's, and the ad still functions, it is not a high-quality ad.
- **Text overlay:** large, bold, highly readable on mobile. Pose a question or make a bold claim that arouses curiosity. Meta's algorithm reads text overlays directly from the image file to help target.
- **Post-It Note ads:** photograph handwriting or text in context (post-it note, letterboard, written on the product) rather than designing text digitally on an image.

### Carousel & Catalog

- **Carousel:** best for showing multiple products, highlighting specific features, or telling a quick story. 2-10 cards.
- **Catalog / Dynamic Product Ads (DPA):** highly automated, integrated with the product feed, excellent for retargeting warm site traffic.

### Placement note

Running only one aspect ratio (e.g., square only) restricts where ads can display, capping reach. Produce vertical 9:16 video (with 4:5 safe content) and vertical images (within 1:1) to fit seamlessly across Stories/Reels and feed.

## The First 3 Seconds (Hook Framework)

The first 3 seconds determine whether the ad is watched or scrolled past. The first line of primary copy represents ~90% of the ad's success; if it doesn't make someone stop, nothing else matters.

### The four elements of a 3-second hook

A high-converting video hook requires four synchronized elements:

1. **Text overlay hook** — burned-in text in the first frame (many viewers watch without sound).
2. **Sound hook** — audio that grabs attention in the first beat.
3. **Visual hook** — motion, contrast, an unexpected visual, a prop.
4. **Vibe** — the tone/energy that signals "this is for you."

### Tested hook styles

- **Stalker hooks:** hyper-contextual hooks that make the viewer feel you are reading their thoughts (e.g., "Are you getting booked calls from ads, but they show up unqualified with terrible show rates?" — not the generic "Are your ads not making money?").
- **Visual and verbal pattern interrupts:** visual props, contrasting colors, unexpected motion, a whiteboard with hand-written math or logic.
- **Specificity over generics:** "lost 23 lbs in 11 weeks" beats "lost weight." Real numbers, real timeframes, real mechanisms.

### Hook aligned to awareness level

- **Cold traffic:** curiosity hooks, problem hooks, contrarian hooks — no product name, no jargon.
- **Warm traffic:** mechanism hooks, "how to get X without Y," differentiation hooks.
- **Hot traffic:** direct offer hooks, price anchors, proof-led hooks.

### The 10-second scroll test

A user should be able to scroll through the ad copy and landing page for 10 seconds and instantly understand the value proposition, pain points, credibility, and offer.

### The "See More" signal

When a user clicks "See More" on truncated primary copy, it sends a positive signal that lowers overall ad costs. Write the first line to earn that click.

## Text and Copy Best Practices

- **Avoid walls of text.** Clean, spaced-out primary copy with short lines and clear bullet points.
- **Lead with the hook, not the brand.** The first line must stop the scroll; the brand comes later.
- **Headline:** clear, specific, benefit-driven.
- **CTA button:** match the action (Shop Now, Learn More, Sign Up, Book Now).
- **Compliance:** ensure all copy is strictly compliant with Meta's policies to avoid account restrictions or high rejection rates.
- See `hook-angle-writer` for hook frameworks and `human-editor` for final polish.

## Post-Winner Graduation and Scaling

### Graduation via Post ID (the only correct method)

Never duplicate a winning ad from scratch — it resets the algorithm's data and destroys user engagement (likes, comments, shares).

1. Extract the exact **Post ID** (or ad ID) of the winner.
2. Paste it into the scaling CBO or Advantage+ Sales Campaign (ASC).
3. This preserves all accumulated social proof, which lowers CPMs and improves delivery in the scaling auction.

### Scale it where it lies (vertical scaling)

If the testing ad set is performing exceptionally well, do not disrupt it. Leave it in place and vertically increase the campaign budget:

- **+20% every 24-72 hours** (conservative, stable).
- **+30% every couple of days** (standard growth).
- **+50% every 3-4 days** (only if ROAS is 50%+ above target).
- If performance dips, pull budget back by the same increment to let the algorithm stabilize.
- At high spend ($10,000+/day), avoid aggressive 50-100% jumps — sudden spikes force Meta to buy lower-quality impressions and can double CPA overnight.

### Horizontal scaling (creative diversity)

Modern horizontal scaling relies on **creative diversity**, not audience duplication. Instead of scaling identical ads to different audiences, scale by launching diverse angles and formats (skits, UGC, static benefit grids, testimonial text) to capture different persona pockets within a broad audience.

### Hormozi's 70/20/10 Iteration Cycle

Once a mega-winner graduates, squeeze maximum value out of it by generating variations in the following week:

- **70% of Week 2 ad tests:** extremely slight variations of the winner (different clothing, horizontal flips, minor color filters) to extend its life.
- **20% of Week 2 ad tests:** decent variations (different hook, different spokesperson, different background setting).
- **10% of Week 2 ad tests:** brand-new angles to ensure continuous discovery of future winners.

The same 70/20/10 split applies to creative resource allocation during filming and scripting: 70% on proven concepts, 20% on adjacent ideas, 10% on wild-card experiments.

### "Use and abuse" the winner

When a creative outperforms baseline, extend its lifespan by spinning up 100+ variations: sepia filters, black-and-white scales, reordering the back end, swapping hooks, changing fonts, swapping headlines. You can also slice the first 3 seconds off top-performing winners and paste them onto other ads to yield 10-50x more efficient creatives.

## Hormozi Content and Creative Principles

- **Hook, Retain, Reward:** the content framework. Hook stops the scroll, retain holds attention through value, reward delivers the payoff that earns the next piece of content.
- **Volume negates luck:** sales and advertising success is a game of high volume. Massive repetition pushes an advertiser through the learning curve and builds the skills for predictable scaling.
- **Content becomes ads:** organic content that performs (high engagement, watch time) becomes paid creative. The market pre-validates the hook. Organic and paid operate on the same algorithms.
- **Specificity converts:** "lost 23 lbs in 11 weeks" beats "lost weight." Real numbers, real timeframes, real mechanisms.
- **The offer is the ceiling:** no amount of creative skill fixes a weak offer. Fix the offer first.
- **Cost of delay:** frame urgency as what they lose by waiting, not just what they gain by acting.
- **The grand slam offer on ads:** an ad can only sell the next click. The offer is revealed on the landing page or VSL, not in the ad itself.
- **The Salty Pretzel lead magnet:** rather than driving cold traffic to a high-ticket sales page, "sell" a free, high-value lead magnet (a $0 book, blueprint, trial) that solves a narrow problem while revealing a larger problem only the core offer can solve.

## Learning Phase Rules (Testing Constraints)

- **The 50 conversions law:** an ad set needs a minimum of 50 conversion events per week (~7-8 purchases/day) to exit the Learning Phase and optimize delivery.
- **Budget for the phase:** set daily budget at 2-3x break-even CPA to clear the Learning Phase fast. For cost-cap campaigns, set daily budget at minimum 8x the cap.
- **Initial optimization data points:** Meta needs ~8,000 impressions to begin understanding how to optimize, and ~500 reach to generate early relevancy scores.
- **The two-week stabilization window:** allow new tests to run two weeks without manual adjustments for conclusive, weekdays-inclusive data.
- **The midnight launch rule:** always schedule new tests to go live at 12:00 AM. A launch at 3 PM or 6 PM forces Meta to spend the entire daily budget in the remaining hours, spiking CPA.
- **Every significant edit resets the Learning Phase:** budget ±20%, audience change, creative swap, bid change, placement change — all reset it. Discipline: one change at a time, then wait.

## Common Mistakes That Reset or Ruin the Test

- Editing budget by more than 20% at once.
- Changing the audience mid-test.
- Swapping creatives too frequently.
- Pausing and restarting ad sets.
- Changing the optimization event.
- Adding or removing placements mid-test.
- Launching mid-day instead of at midnight.
- Mixing static and video in one ad set.
- Judging before 50 conversions or 7 days.
- Iterating losers with cosmetic tweaks (the Lattice penalty).
- Duplicating winners from scratch instead of graduating by Post ID.

Each of these either resets the Learning Phase (causing a 1-7 day performance dip) or destroys the validity of the test read. Discipline: structure the test, set it, leave it for the duration, then judge by the criteria.
