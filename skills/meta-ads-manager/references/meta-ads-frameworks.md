# Meta Ads Frameworks Reference

This reference summarizes the Meta Ads frameworks used by the `meta-ads-manager` skill and the related Meta Ads skill family (`meta-creative-tester`, `meta-audience-builder`, `meta-ads-scaler`, `campaign-optimizer`, `meta-lead-gen`). It is distilled from the Master Meta Ad notebook (213 sources covering Hormozi, Advantage+, ad types, creative, scaling, audiences, bidding, Pixel/CAPI, and optimization workflows).

**Conflict resolution rule:** Where sources conflict, Hormozi's principles win. For non-Hormozi conflicts, majority opinion wins. Use this as a field guide, then verify against the client's actual ad account data.

## Campaign Hierarchy

Meta Ads uses a three-level structure. Understanding what each level controls is the foundation of every campaign decision.

- **Campaigns:** the top level. Defines the **objective** (what you want the algorithm to optimize for: Sales, Leads, Traffic, Engagement, Awareness, App Promotion) and the **buying type** (auction or reserved). In CBO mode, the campaign also holds the budget.
- **Ad Sets:** the middle level. Defines the **conversion location** (website, app, Messenger, WhatsApp), the **optimization event** (Purchase, Lead, Add to Cart), the **audience**, the **placements**, the **schedule**, and (in ABO mode) the **budget**. Each ad set represents a distinct audience or optimization strategy.
- **Ads:** the bottom level. Defines the **creative** (image, video, carousel, collection), the **copy** (primary text, headline, description), the **CTA**, the **destination URL**, and the **tracking parameters**. Multiple ads per ad set enable creative testing.

**Modern context:** Under Advantage+ (Meta's AI optimization), the hierarchy operates as a dynamic funnel. The campaign determines which ad set to fund, the ad set determines which ad receives budget, and the ad itself performs audience targeting through creative signals. The creative is the new targeting.

## Objective Selection

The objective determines what the algorithm optimizes for. Choose the objective closest to the actual business outcome.

| Objective | Optimizes for | Best for |
|---|---|---|
| **Sales (Advantage+ Shopping)** | Purchases (website/app) | Ecommerce with a product catalog. AI handles targeting, placement, creative combos. |
| **Sales (manual)** | Purchases (website) | Ecommerce without catalog, or control over audience/placement. |
| **Leads** | Lead form or onsite lead events | Services, B2B, info-products with application funnels. |
| **Engagement** | Post engagement, video views, messages | Top-of-funnel, video views, Messenger/WhatsApp. |
| **Traffic** | Link clicks | Cheap traffic; rarely converts. Use only without conversion tracking. |
| **Awareness** | Ad recall, reach | Brand awareness, retargeting pool building. |
| **App Promotion** | App installs, in-app events | Mobile apps. Pair with CAPI. |

**Rule:** never choose Traffic for a conversion campaign. The cheap CPC optimizes for clickers, not buyers.

## CBO vs ABO

**CBO (Advantage Campaign Budget):**
- Budget at campaign level; Meta distributes across ad sets
- Pros: algorithmic spend routing, simpler management
- Cons: less control, dominant ad set can starve others
- Best for: scaling winners, ecommerce, trust-the-algorithm scenarios

**ABO (Ad Set Budget Optimization):**
- Budget at ad set level; you control spend per ad set
- Pros: precise spend control, forces testing of specific audiences
- Cons: prevents optimal spend routing, more management
- Best for: testing new creative/audiences, controlled data gathering

**Modern default:** ABO for testing → CBO for scaling.

## Bidding Strategy

- **Lowest cost (no cap):** Meta spends the budget for the most conversions at the lowest cost. Default for most campaigns. Best when you want maximum volume.
- **Lowest cost with bid cap:** sets a max cost per conversion. Throttles delivery if the cap is below market. Use when you have a hard CPA target.
- **Cost cap:** sets a target average cost per conversion. Meta optimizes for efficiency around the target. Requires stable conversion data (50+ conversions/week) to work. Best for scaling efficiency.
- **Minimum ROAS bidding:** sets a minimum return on ad spend. Available for ecommerce with catalog. Use when you have clear margin targets.

**Rule:** start with lowest cost (no cap). Move to cost cap only when scaling and when you have stable data.

## Budget Strategy

### Minimum viable budgets

- **Per ad set:** $10-20/day minimum (Meta needs enough to exit Learning Phase)
- **Per campaign:** $30-100/day minimum to gather usable data
- **First-week signal:** spend 50x the CPA target (if target CPL is $20, spend $1,000+ in week 1)

### Daily vs Lifetime

- **Daily budget:** Meta paces spend evenly through the day. Default for most campaigns.
- **Lifetime budget:** Meta paces spend across the campaign's schedule. Enables dayparting (showing ads only at specific times). Use for time-bound campaigns or daypart optimization.

### Learning Phase

- Meta needs ~50 conversions per ad set per 7 days to exit the Learning Phase
- During Learning Phase, performance is volatile and CPC/CPA is elevated
- Every significant edit (budget ±20%, audience, creative, bid) resets the Learning Phase
- Discipline: set it and leave it for 4-7 days before judging

## Audience Strategy

### Advantage+ Audience (broad)

- No interests, no demographics beyond basics
- Meta finds buyers based on Pixel data, creative signals, and conversion events
- Often outperforms interest targeting at scale
- Requires: clean Pixel signal + strong creative + $50+/day budget for enough signal
- **When broad beats interest:** when you have 100+ conversions/month and strong creative. Broad gives the algorithm maximum inventory to learn from.

### Custom Audiences

- **Customer list:** uploaded email/phone lists. For retargeting or exclusion.
- **Website visitors:** Pixel-based, by time window (30/90/180 days) and page visited.
- **Engagers:** people who engaged with your Facebook/Instagram content (video views, page engagement, lead form opens) by time window.
- **App users:** for mobile apps.
- **Offline activity:** for in-store conversions (requires offline event set).

### Lookalike Audiences

- Based on a Custom Audience source (purchasers, leads, engagers)
- Meta finds people similar to the source
- **Tiers:** 1% (closest match, smallest audience), 1-3%, 1-5%, 1-10%
- Start at 1%, expand to wider tiers as you scale
- Best sources: purchaser list (highest quality), high-LTV customers, recent converters

### Interest Targeting

- 3-5 relevant interests per ad set
- Use when: Pixel data is thin, testing new markets, or specific niche targeting
- Avoid: stacking 10+ interests (dilutes signal), overly narrow interests (starves algorithm)

### Retargeting Sequencing

- **30-day engagers, excluded purchasers:** top of retargeting funnel
- **90-day visitors, excluded purchasers:** mid-funnel
- **Abandoned cart / abandoned form:** bottom-funnel (highest intent)
- Retargeting creative differs from cold: social proof, testimonials, offer reminders, scarcity

### Exclusions

- Always exclude recent purchasers from acquisition campaigns (waste prevention)
- Exclude recent converters from conversion campaigns (avoid double-counting)
- Exclude current customers from new-customer offers

## Placements

### Advantage+ Placements (recommended)

- Meta auto-selects: Facebook Feed, Instagram Feed, Reels, Stories, Marketplace, Audience Network, Messenger
- Maximizes inventory, lowers CPM, improves algorithm learning
- Default for most campaigns

### Manual Placements

- Use only when you have a specific reason (e.g., brand safety, creative format constraints)
- Reduces available inventory, raises CPM
- Common manual choices: Instagram only (visual products), Facebook Feed only (older demographics)

## Creative Best Practices

Creative is the #1 performance variable in Meta Ads.

### Formats

- **Video (vertical 9:16 or 4:5):** highest engagement, best for Reels/Stories, 6-60s
- **Static image (1:1 or 4:5):** cheapest to produce, effective for direct response with strong copy
- **Carousel (1:1 or 4:5):** 2-10 cards, tells a story or shows multiple products/angles
- **Collection:** for ecommerce, showcases a catalog
- **Reels ads:** vertical 9:16, under 30s, native-feeling

### Length

- **6s:** pure pattern interrupt, single message, CTA
- **15s:** hook + problem + solution + CTA (most common for direct response)
- **30s:** hook + story + mechanism + offer + CTA (deeper persuasion)
- **60s+:** mini-VSL, full problem-agitate-solve

### First 3 Seconds

- The first 3 seconds determine whether the ad is watched or scrolled past
- Pattern interrupt: visual change, bold statement, question, motion
- Text overlay in first frame (many viewers watch without sound)
- Hook aligned to awareness level (cold = problem/curiosity, warm = mechanism, hot = offer)

### Text on Image / Video

- Captions on all video (sound-off viewing is common)
- Text overlay: headline, key stat, offer (burn in, not burned on)
- Keep text concise — Meta's text-in-image rule is relaxed but readability matters

### Copy

- Primary text: lead with the hook, not the brand
- Headline: clear, specific, benefit-driven
- Description: supporting detail or offer framing
- CTA button: match the action (Shop Now, Learn More, Sign Up, Book Now)
- See `hook-angle-writer` for hook frameworks and `human-editor` for final polish

## Creative Testing Methodology

See `meta-creative-tester` skill for the full methodology. Summary:

- Creative is the #1 lever — invest here first
- Test one variable per ad set (hook, format, angle, offer framing)
- 3-5 creatives per ad set
- Run 4-7 days or until 50+ conversions per creative
- Winner = lowest cost per conversion (not highest CTR)
- Kill losers at 2x target CPA with 50+ conversions
- Scale winners by duplicating into CBO and iterating variations

## Scaling Framework

See `meta-ads-scaler` skill for the full framework. Summary:

- **When to scale:** consistent profitable results for 3-5 days, CPA at or below target, budget not fully spent
- **Vertical scaling:** increase budget 20-30% every 2-3 days (steeper than 50%+ risks Learning Phase reset)
- **Horizontal scaling:** duplicate winning ad sets to new audiences (lookalike tiers, broad, interests)
- **Learning Phase protection:** avoid edits during scaling; make one change at a time
- **Kill criteria:** CPA above 2x target for 3+ days with no recovery

## Performance Metrics and Benchmarks

### Core Metrics

- **CTR (Click-Through Rate):** clicks / impressions. Benchmark: 1%+ for cold, 2%+ for retargeting. Low CTR = creative or hook problem.
- **CPC (Cost Per Click):** spend / clicks. Benchmark: $0.50-$2.00 (varies by industry). High CPC = bidding competition or low relevance.
- **CPM (Cost Per 1,000 Impressions):** spend / impressions × 1000. Benchmark: $5-$20 (varies by audience). High CPM = audience saturation or bidding competition.
- **CPL (Cost Per Lead):** spend / leads. Benchmark: industry-specific. High CPL = creative, offer, or landing page problem.
- **CPA (Cost Per Acquisition/Purchase):** spend / purchases. Benchmark: based on margin. High CPA = offer, creative, or funnel problem.
- **ROAS (Return on Ad Spend):** revenue / spend. Benchmark: 2-4x for most ecommerce. Below 2x = margin pressure.
- **Frequency:** impressions / reach. Benchmark: 1-3 for cold, 3-5 for retargeting. Above 5 = ad fatigue.
- **Relevance / Quality Ranking:** Meta's diagnostic. Use as a signal, not a primary metric.

### Diagnosis Matrix

| Symptom | Likely cause | Where to look |
|---|---|---|
| High CPM, low CTR | Creative not stopping the scroll | Creative (first 3 seconds) |
| High CTR, low conversion | Landing page or offer problem | Funnel page, offer doc |
| High CPC, normal CTR | Bidding competition or narrow audience | Audience, bid strategy |
| High CPA, normal CTR/CPC | Offer, price, or funnel friction | Offer doc, checkout flow |
| Rising frequency, falling CTR | Ad fatigue | Creative refresh |
| CPA spikes after edit | Learning Phase reset | Stop editing, wait |

## Pixel and Conversions API (CAPI)

### Why CAPI matters

- iOS 14.5+ (ATT) broke Pixel-based attribution for ~30-40% of iPhone users
- CAPI sends conversion events server-side, bypassing browser tracking restrictions
- Combining Pixel + CAPI recovers 15-25% of lost attribution
- Improves Event Match Quality (EMQ), which improves algorithm optimization

### Setup checklist

- [ ] Pixel installed on all key pages (especially the conversion confirmation page)
- [ ] Pixel firing the target event (test with Meta Pixel Helper Chrome extension)
- [ ] CAPI installed server-side (via Partner Integration like Shopify/Segment, or custom code)
- [ ] CAPI sharing user data: email (hashed), phone (hashed), name, city, zip, country
- [ ] Event Match Quality (EMQ) above 6/10 (ideally 8+)
- [ ] Domain verified in Business Manager
- [ ] Aggregated Event Measurement (AEM) configured (max 8 events per domain, prioritized by value)
- [ ] First-party data enrichment (Customer Information Parameters) enabled

### Advantage+ Shopping Campaign requirements

- Product catalog configured in Business Manager
- Pixel + CAPI both firing Purchase events
- Domain verified
- Minimum 50+ Purchase events per month (ideally 100+) for the algorithm to learn
- Sufficient budget ($50+/day recommended)

## Lead Gen Specifics

See `meta-lead-gen` skill for depth. Summary:

- **Lead form vs landing page:** lead forms reduce friction (no page load) but lower lead quality; landing pages improve quality and allow for richer persuasion but add a step
- **Instant Forms:** Meta's native lead form (pre-filled with user data, customizable questions)
- **Qualification questions:** 1-3 questions max, use multiple choice, gate by budget/fit
- **Follow-up speed:** contact leads within 5 minutes for best conversion (industry standard)
- **CRM connection:** connect lead form to CRM (Zapier, Make, native integration) for instant routing

## Daily Management Workflow

See `campaign-optimizer` skill for depth. Summary:

- **Daily (5-10 min per account):** check spend pace, major anomalies (spend spike, zero conversions), error alerts
- **Weekly (30-60 min per account):** review performance per campaign/ad set, identify winners and losers, plan creative refresh, check frequency
- **Monthly:** full audit, restructure if needed, update scaling plan, review ROAS/CPA trends

**Discipline:** do not edit during the Learning Phase. Most performance issues resolve by waiting, not by intervening.

## Hormozi Content and Ad Creative Principles

(from the Master Meta Ad sources)

- **Hook, Retain, Reward:** the content framework. Hook stops the scroll, retain holds attention through value, reward delivers the payoff that earns the next piece of content.
- **Volume philosophy:** post frequently, test many hooks, let the market decide. One viral piece outperforms ten safe ones.
- **Content becomes ads:** organic content that performs (high engagement, watch time) becomes paid creative. The market pre-validates the hook.
- **Specificity converts:** "lost 23 lbs in 11 weeks" beats "lost weight." Real numbers, real timeframes, real mechanisms.
- **The offer is the ceiling:** no amount of creative skill fixes a weak offer. Fix the offer first.
- **Cost of delay:** frame urgency as what they lose by waiting, not just what they gain by acting.
- **The grand slam offer on ads:** an ad can only sell the next click. The offer is revealed on the landing page or VSL, not in the ad itself.

## Common Mistakes That Reset the Algorithm

- Editing budget by more than 20% at once
- Changing the audience mid-Learning Phase
- Swapping creatives too frequently
- Pausing and restarting ad sets
- Changing the optimization event
- Adding or removing placements mid-campaign

Each of these resets the Learning Phase, causing a 1-7 day performance dip while the algorithm re-learns. Discipline: one change at a time, then wait.
