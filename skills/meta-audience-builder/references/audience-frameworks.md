# Meta Audience Frameworks Reference

This reference summarizes the Meta Ads audience frameworks used by the `meta-audience-builder` skill and the related Meta Ads skill family (`meta-ads-manager`, `meta-creative-tester`, `meta-ads-scaler`, `campaign-optimizer`, `meta-lead-gen`). It is distilled from the Master Meta Ad knowledge base (audience strategies, Advantage+ Audience, custom audiences, lookalike tiers, retargeting sequencing, exclusions, and the shift to creative-led targeting).

**Conflict resolution rule:** where sources conflict, the principles that favor algorithmic targeting (broad, creative-led, minimal manual constraint) win for accounts with adequate data. For accounts with thin data, interest and lookalike targeting add useful signal. Use this as a field guide, then verify against the client's actual ad account data.

## The Shift to Broad Targeting

Meta's targeting architecture has been rebuilt around the algorithm. The implication for media buyers is significant: most manual targeting inputs are now treated as suggestions, not boundaries.

### Advantage+ Audience (the suggestion model)

Under modern Meta targeting, inputs like custom audiences, detailed targeting (interests), and lookalikes are no longer hard boundaries. They function as **"audience suggestions."** Meta's AI uses them as a starting point but will deliver ads beyond the selected parameters whenever the conversion signal predicts a better result.

Key facts:

- Detailed targeting (interests) is heavily de-prioritized — the system effectively operates in a broad capacity regardless.
- Advantage+ Audience has shown ~28% lower CPC and ~7% lower cost per website conversion in platform tests.
- The ad creative itself does the targeting. Meta's Andromeda/Advantage+ AI analyzes visual assets, text overlays, and video transcripts to match ads to relevant users in real time.
- Media buyers should use broad targeting (unrestricted other than basic age, gender, and location) and let the creative define the audience pocket.

### When broad beats interest

Broad targeting is not always better — it depends on data depth, creative strength, and budget. Use broad (Advantage+ Audience) as the primary acquisition approach when **all three** are true:

- **100+ conversions/month** — the algorithm has enough signal to optimize without targeting constraints.
- **Strong creative** — broad targeting relies on the creative to find the right audience. Weak creative underperforms in broad because there is no interest filter to compensate.
- **$50+/day budget** — enough spend for the algorithm to gather signal and exit the Learning Phase.

Below this threshold, interest and lookalike targeting add useful structure. A new account with 10 conversions/month and one creative should not run broad-only — it lacks the signal for the algorithm to converge.

## Audience Types

### Advantage+ Audience (Broad)

- No interests, no demographics beyond basics (age, gender, location).
- Meta finds buyers based on Pixel data, creative signals, and conversion events.
- Often outperforms interest targeting at scale.
- Requires: clean Pixel signal + strong creative + adequate budget.
- **Use as:** the primary cold ad set in a hybrid stack, or the only cold ad set for accounts above the broad-beats-interest threshold.

### Lookalike Audiences

Lookalikes use a custom first-party "seed audience" to find Meta users who share similar behavioral profiles. The seed determines the quality of the lookalike — deterministic seeding matters.

**Seed source quality (highest to lowest):**

1. **Highest-LTV customers** — the lookalike will resemble your best buyers.
2. **Top average order value (AOV) buyers.**
3. **Recent purchasers** (last 90 days).
4. **Qualified leads** (for lead-gen offers).
5. **Long session-duration visitors** — engaged but not converted.
6. **All purchasers** — broader, lower precision.
7. **All leads / email subscribers** — broadest, lowest precision (avoid as a seed unless nothing better exists).

**Lookalike percentage tiers:**

| Tier | Characteristics | When to use |
|---|---|---|
| **1%** | Closest, most precise match to the seed. Smallest audience. | Starting tier — validate audience quality and creative. |
| **1-3%** | Slightly broader, more reach, marginally lower precision. | First expansion once 1% is profitable and ready to scale. |
| **1-5%** | Meaningfully broader, lower precision, higher reach. | Scaling phase — when 1-3% is saturated or you need more volume. |
| **1-10%** | Broadest lookalike, lowest precision, maximum reach. | Late scaling, large budgets, or as a near-broad alternative. |

**Expansion strategy:** start at 1% to validate. Once profitable for 3-5 days, expand horizontally to 1-3%, then 1-5%, then 1-10% as budget and saturation demand. Do not skip to 1-10% on a new account — the lower precision wastes spend before the algorithm has learned.

**Interest stacking on lookalikes:** some media buyers layer an interest qualifier on a lookalike (e.g., "1% lookalike of top buyers" + "business decision-makers") to create a refined, multi-layer segment. Use sparingly — it narrows the audience and can starve the algorithm. Test against the unlayered lookalike before committing.

### Custom Audiences

Custom audiences are built from owned, first-party data and platform behavior. They power both retargeting and exclusions.

**First-party data sources:**

- **Customer lists:** uploaded email/phone lists from CRM, Klaviyo, Shopify, or manual export.
- **Offline conversions:** in-store purchases via an offline event set.

**Platform-based custom audiences:**

- **Website visitors:** Pixel-based, by time window (30/90/180 days) and page visited.
- **Engagers:** people who engaged with Facebook/Instagram content — video viewers by threshold (25%, 50%, 75%, 95%), page engagers, lead form openers, Instagram profile engagers.
- **App users:** active users and in-app event audiences (for mobile apps).

**Size and volume benchmarks:**

- To build a robust custom audience for high-intent retargeting (Dynamic Product Ads, specific upsells), target events with at least **10,000 actions** (e.g., 10,000 add-to-carts or view-contents). Below this, delivery is inconsistent.
- For customer lists, 1,000+ quality records produces a usable lookalike seed; 100 is the floor for Meta to accept the seed.

### Interest Targeting

- **3-5 relevant interests per ad set.** More dilutes the signal and complicates learning.
- **Use when:** Pixel data is thin, entering a new market, niche B2B targeting, or testing a specific hypothesis (e.g., "does targeting competitor brand interests lower CPA?").
- **Avoid:** stacking 10+ interests (dilutes signal), overly narrow interests (starves algorithm), and treating interests as a fixed boundary (Meta ignores them when it predicts a better result).
- **Each interest should have a reason.** "These interests seem relevant" is not a reason. Tie each to the avatar profile or a testing hypothesis.

## Retargeting Sequencing

Retargeting is not a single audience — it is a sequenced conversation that moves a warm prospect toward purchase while dismantling objections. Done wrong, it fatigues the audience and kills CTR. Done right, it converts the highest-intent traffic at the lowest CPA.

### Frequency and pacing

- Retargeting requires tight, high-frequency pacing to move people over the purchase threshold.
- **Short sales cycle:** aim for **5-8 impressions over a 7-day conversion window** for website visitors and cart abandoners.
- **High-ticket / long sales cycle:** lower frequency, longer windows (match the average sales-cycle duration).

### Multi-angle creative rotation

To address different objections without fatiguing the audience, rotate multiple ad angles:

| Objection | Retargeting angle |
|---|---|
| **Product / fit doubt** | Direct warm audiences to interactive selectors (shade-matching, product-fit quizzes, configurators). |
| **Skepticism** | UGC whitelisted creator ads — "real" people using and validating the product. |
| **Trust barrier** | Third-party publisher whitelisted editorial ads — objective, external social proof. |
| **Price / value** | Offer reminder, value-stack recap, comparison anchor. |
| **Urgency / delay** | Scarcity, cost-of-delay framing, risk reversal (guarantee). |

Rotate 2-4 angles per retargeting tier. Showing the same angle repeatedly causes fatigue; rotating angles keeps the conversation moving.

### Time-decay sequencing

For high-ticket items or products with extended consideration windows, sequence retargeting by gating audiences chronologically:

```
Level 1 — Prospecting (cold): Broad / lookalike / interest, unrestricted
  ↓ user watches ≥25% of an L1 video ad
Level 2 — Engagement (warm): Retarget strictly for a 30-day window
  - Match window to average sales-cycle duration
  ↓ user visits site or engages deeper
Level 3 — Evergreen / retention: Website visitors (30d) + add-to-carts (90d)
  - Long-term retention sequences for past buyers:
    - Target past buyers at 60 days, exclude last 45 days (repurchase / restock reminder)
    - Target past buyers at 90 days, exclude last 75 days
```

### Up-the-funnel expansion

When a retargeting audience saturates or fatigues, scale horizontally by expanding the retargeting event:

- **Up the funnel:** transition from retargeting "AddToCart 1-day" to "ViewContent 1-day" (broader, lower-intent pool).
- **Further out in time:** transition from "AddToCart 1-day" to "AddToCart 3-day" or "AddToCart 7-day" (same event, wider window).

Both expand the available audience without changing the offer or creative.

## Exclusion Design

Exclusions establish "clean swim lanes" — they ensure prospecting budgets acquire new traffic rather than retargeting warm prospects, and that retargeting does not fatigue audiences or double-count conversions.

### Mandatory exclusions

- **Recent purchasers (180 days to all-time) from all cold acquisition.** Prevents spending acquisition budget on people who already bought. This is the single most important exclusion.
- **Current customers / active subscribers from new-customer offers.** Prevents showing acquisition offers to existing customers.
- **Recent converters from conversion campaigns.** Prevents double-counting and attribution noise.

### The mid-funnel exclusion loop

Under multi-step evergreen funnels, when a cold prospect completes an initial action (clicks, views, engages), they should be excluded from the initial prospecting ad and moved into the retargeting pool:

```
Cold prospect sees cold ad → engages (click/view/25%+ watch)
  → excluded from cold prospecting
  → entered into retargeting pool (30-day window)
  → if no purchase after window (7-14 days), retargeting sequence stops
  → user cooled down to prevent fatigue and budget leakage
```

### The over-exclusion trap

While excluding recent purchasers is mandatory, **over-micromanaging exclusions is dangerous.** Removing all page engagers or all website visitors from cold prospecting:

- Limits the algorithm's delivery options.
- Drives up CPM (less inventory available).
- Restricts the algorithm's ability to find the lowest-hanging conversions.

Exclude recent purchasers and current customers. Let the rest of the warm audience remain available to cold prospecting — the algorithm handles the routing.

### The 2025 platform change

As of **March 31, 2025**, Meta removed detailed targeting (interest-based) exclusions from active campaigns in Ads Manager. Media buyers can still enforce brand protection and budget control using:

- **Custom audience exclusions:** upload CRM lists, Klaviyo tags, and Pixel events as exclusion sources.
- **High-level audience controls:** age, gender, location, and placement-level controls.

Do not rely on interest-based exclusions — they no longer fire on active campaigns.

## Audience Sizing Rules

| Audience type | Minimum to run | Comfortable scale | Notes |
|---|---|---|---|
| **Lookalike (1%)** | ~50,000+ (country-dependent) | 1% of US ≈ 2.6M | Floor varies by country population. |
| **Custom (retargeting)** | 1,000+ active users in window | 10,000+ | Below 1,000, delivery is inconsistent. |
| **Pixel event (retargeting)** | 10,000+ actions in window | 50,000+ | Ensures stable, non-fatiguing delivery. |
| **Interest** | 500,000+ in selected interests | 1M+ | Narrower interests deliver poorly. |
| **Broad (Advantage+ Audience)** | N/A — Meta defines size | Any | Constraint is budget and creative, not size. |

### Lookalike seed sizing

- Minimum 100 quality records for Meta to accept the seed.
- 1,000+ quality records for a meaningful lookalike.
- Quality beats quantity: 500 high-LTV purchasers produce a better lookalike than 5,000 low-value leads.

### Remediation for undersized audiences

If an audience is below minimum:

- **Retargeting too small:** widen the time window (30 → 90 days) or move the event up the funnel (AddToCart → ViewContent).
- **Lookalike too small:** expand the percentage tier (1% → 1-3%) or use a broader seed.
- **Interest too narrow:** add 1-2 adjacent interests or switch to broad.
- **Customer list too small:** focus on list growth before investing in list-based audiences.

## Audience Tier Decision Matrix

| Scenario | Recommended approach | Why |
|---|---|---|
| New account, no Pixel data, no customer list | Interest-first (3-5 interests), low budget | Interest is the only signal available; build Pixel data first. |
| New account, customer list exists, no Pixel data | Lookalike-first (1% on customer list) | The list seeds the algorithm; lookalike extends reach. |
| Established account, 100+ conv/mo, strong creative, $50+/day | Broad-first (Advantage+ Audience) | Broad beats interest above the threshold; creative does the targeting. |
| Established account, scaling, proven winners | Hybrid: Broad + Lookalike (1-3% / 1-5%) + Interest, in CBO | Maximum learning surface; CBO routes spend to the winner. |
| Niche B2B, specific decision-maker targeting | Interest-first with layered qualifiers | Broad too diffuse for niche B2B; interest adds needed structure. |
| Ecommerce with catalog | Advantage+ Shopping Campaign (ASC) + DPA retargeting | Meta's AI handles targeting/placement/creative combos; DPA retargets warm visitors. |
| High-ticket / long sales cycle | Broad/lookalike cold + sequenced time-decay retargeting | Long consideration needs sequenced nurturing, not impulse retargeting. |

## Integration with the Campaign Structure

This skill produces the audience stack. The campaign structure (objective, CBO/ABO, budget allocation, creative testing matrix) is the domain of `meta-ads-manager`. The two pair as follows:

- `meta-ads-manager` defines the campaign → ad set → ad hierarchy, objective, budget strategy, and creative testing plan.
- `meta-audience-builder` defines the audiences that populate each ad set: cold broad, cold lookalike, cold interest, retargeting tiers, and exclusions.
- The audience plan should be referenced from the campaign plan, and vice versa. Each ad set in the campaign plan points to an audience defined here.

For ecommerce with a product catalog, Advantage+ Shopping Campaigns (ASC) consolidate prospecting and retargeting into one AI-driven campaign — the audience stack simplifies to ASC + a separate Dynamic Product Ad (DPA) retargeting layer. See `meta-ads-manager` for the ASC structure.

## Common Mistakes That Break Audience Strategy

- **Interest stacking** (10+ interests, narrow ages, narrow placements) — starves the algorithm, raises CPM.
- **No exclusions** — wastes acquisition budget on recent purchasers.
- **Over-exclusion** — removing all engagers/visitors from cold, limiting delivery and raising CPM.
- **Seeding lookalikes on low-quality lists** — produces low-value lookalikes.
- **Undersized retargeting audiences** — inconsistent delivery, wasted budget.
- **Ignoring the broad-beats-interest threshold** — running only interest at scale leaves efficiency on the table; running only broad below the threshold wastes spend.
- **No retargeting sequence** — same angle, same audience, rapid fatigue.
- **Editing audiences during the Learning Phase** — resets learning, causes performance dip.
- **Trusting interest exclusions post-March-2025** — they no longer fire; use custom audience exclusions.
- **Judging audiences too early** — an audience needs 50+ conversions per week per ad set to exit the Learning Phase.
