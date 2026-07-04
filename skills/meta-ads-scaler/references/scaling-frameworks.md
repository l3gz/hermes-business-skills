# Meta Ads Scaling Frameworks Reference

This reference summarizes the Meta Ads scaling frameworks used by the `meta-ads-scaler` skill and the related Meta Ads skill family (`meta-ads-manager`, `meta-creative-tester`, `meta-audience-builder`, `campaign-optimizer`, `meta-lead-gen`). It is distilled from the Master Meta Ad notebook (213 sources covering Hormozi, Advantage+, scaling signals, budget rules, Learning Phase, kill criteria, and horizontal vs vertical architecture).

**Conflict resolution rule:** Where sources conflict, Hormozi's principles win. For non-Hormozi conflicts, majority opinion wins. Use this as a field guide, then verify against the client's actual ad account data.

## Scaling Signals (When to Begin Scaling)

Scale only on statistical proof of profitability and algorithmic stability. The green-light signals:

- **The 48-72 hour rule:** consistently hit or exceed target KPI (CPA or ROAS) for 48-72 consecutive hours. Conservative operators wait 3-5 full days.
- **The 60% click-based data rule:** at least 60% of reported purchases are click-based, not view-through. Heavy view-through reliance inflates ROAS and leads to scaling campaigns that are not driving incremental lift.
- **The "new reason" factor:** aggressive scaling is safest when backed by a tangible change — a new winning creative, a fresh promotional offer, or a high-converting landing page. Scaling stale, fatigued creatives because the market had a good day usually reverses.
- **Unit economic thresholds:** Lifetime Gross Profit to Customer Acquisition Cost (LTGP:CAC) must be healthy enough to sustain rising acquisition costs. High-ticket offers with LTV of $10k+ tolerate higher front-end CPA and aggressive scaling; thin-margin ecommerce does not.
- **Conversion volume:** 50+ conversions per week (ideally 100+) keeps the algorithm stable as you scale and prevents re-entry into the Learning Phase.
- **Budget fully spent:** the campaign is delivering its full daily budget. If it is under-spending, the constraint is delivery (creative, audience, or bid), not budget — scaling the budget will not help.

**Anti-signal — do not scale if any of these are true:**
- CPA above target (optimize first)
- Performance is a single-day spike with no trend
- Creative is fatigued (frequency high, CTR dropping)
- Conversion volume is below 50/week (algorithm cannot absorb more spend)
- Attribution is view-through-heavy and unverified

## Scaling Architecture: Vertical vs Horizontal

| Dimension | Vertical Scaling | Horizontal Scaling |
|---|---|---|
| **Action** | Increase budget on the existing winning campaign/ad set | Duplicate winning ad sets to new audiences, geos, or creative angles |
| **Nickname** | "Scale it where it lies" | "Don't put all your eggs in one basket" |
| **Best for** | Winning ad set performing in place; preserving social proof; audience has room | Audience saturating; de-risking concentration; creative diversity available |
| **Efficiency** | High — keeps proven ads in place, lets Meta route additional budget at CBO level | Moderate — requires setup, monitoring, and clean structure to avoid auction overlap |
| **Primary risk** | Aggressive bumps reset the Learning Phase | Duplicating splits signal; auction overlap raises CPM |
| **Modern lever** | Incremental budget bumps within Learning Phase tolerance | Creative diversity (distinct angles/formats), not identical ads to new audiences |
| **When to prefer** | Audience not saturated, creative fresh, budget below ceiling | Frequency rising, CTR dropping, need to de-risk or extend reach |

**They are not mutually exclusive.** Mature scales use both: vertical on the proven winner, horizontal to expand reach and de-risk. Pick the primary method by the immediate constraint (saturation vs budget headroom).

### Vertical Scaling Detail

- **Strategic best practice:** "scale in place" — keep proven ads running without moving them. Let Meta allocate the additional budget at the campaign level (CBO).
- **Why it works:** the algorithm already knows who converts for this ad set. Additional budget lets it find more of the same buyer, faster, without re-learning.
- **Limit:** audience saturation. Eventually the ad set has reached everyone it can reach efficiently, and more budget buys lower-quality impressions.

### Horizontal Scaling Detail

- **The creative targeting lever:** under Meta's Andromeda architecture, the creative performs the targeting. Horizontal scaling in 2026 relies on creative diversity — distinct angles and formats (skits, UGC, static benefit grids, testimonial) to capture different persona pockets within a broad audience.
- **Expansion targets:** lookalike tiers (1% → 1-3% → 1-5% → 1-10%), broad (Advantage+ Audience), new interests, new geos, new creative concepts.
- **Discipline:** use the Post ID method to preserve social proof when duplicating winners. Avoid auction overlap via clean exclusions or consolidation. One new audience per scaling cycle, monitored 3-5 days.

## Budget Increase Rules

How aggressively you increase daily budget depends on how far performance is pacing above target KPI:

| Tier | Bump size | Frequency | When to use | Risk |
|---|---|---|---|---|
| **Conservative** | 10-20% | Every 24-72 hours | Stable scaling, performance at target | Lowest; rarely resets Learning Phase |
| **Standard** | 20% | Every 2-3 days | The baseline vertical scaling increment | Low; the safe default |
| **Moderate** | 30% | Every couple of days | Performance pacing above target (1.5-2x ROAS) | Moderate; watch for reset. If performance dips, pull back 30% to stabilize. |
| **Aggressive** | 50% | Every 3-4 days | ROAS 50%+ above target (target 2x, actual 3-3.5x+) | High; can reset Learning Phase. Cap at low/mid budgets. |
| **Double-up** | 100% | Once, on low budgets | Under $1,000/day with extreme profitability | Very high; only for outlier performers |
| **Surf scaling** | Variable, same-day | Same-day, reset at midnight | Low budgets showing extreme early-day profitability | High; specialized tactic requiring daily monitoring |

**Hard rules:**
- **Never more than 50% in a single edit** on standard campaigns.
- **At enterprise spend ($10,000+/day), avoid 50-100% jumps.** Sudden spikes force Meta to buy lower-quality impressions, which can double CPA overnight.
- **Surf scaling variant:** increase budget aggressively at 6:00 AM if early performance is highly profitable; double again at noon if efficiency holds; reset to baseline at midnight to lock in daily profits. Requires active daily management.

## Learning Phase Rules of Engagement

The Learning Phase is governed by mathematical laws of Meta's machine learning. Violating them wastes budget.

- **The 50-conversions law:** an ad set or campaign needs a minimum of 50 conversion events per week (roughly 7-8 purchases per day) to exit the Learning Phase and optimize delivery.
- **Budgeting for the phase:** set daily budget at 2-3x break-even CPA to ensure the ad set clears learning quickly. For cost-cap or bid-cap campaigns, set daily budget at minimum 8x the actual cap (50 conversions ÷ 7 days ≈ 8x) to ensure enough daily volume.
- **Initial optimization data points:** Meta requires a minimum of 8,000 impressions to begin understanding how to optimize, and a minimum of 500 reach to generate early relevancy scores.
- **The two-week stabilization window:** allow new creative tests or structural updates to run for two weeks without manual adjustments to gather conclusive, weekday-inclusive data. Frequent changes reset the learning phase and destroy performance.
- **The midnight launch rule:** always schedule new campaigns, creative tests, or major budget increases to go live at 12:00 AM. Mid-afternoon launches force Meta to cram the entire daily budget into the remaining hours, spiking CPA.
- **Reset triggers (avoid during scaling):** budget changes ±20%+, audience changes, creative swaps, bid changes, placement changes, optimization event changes, pausing/restarting ad sets. Each can reset the Learning Phase, causing a 1-7 day performance dip.

## Kill Criteria

Apply this hierarchy of kill rules to cut underperforming ads and campaigns early. Scaling campaigns that degrade must be rolled back or killed.

### Scaling-campaign kill criteria

- **CPA above 2x target for 3+ consecutive days:** the scale has broken. Pause, diagnose (creative fatigue? audience saturation? signal degradation? Learning Phase reset?), route back to testing.
- **Frequency >5 with sustained CTR drop:** audience saturation. Vertical scaling cannot fix this. Refresh creative or expand horizontally.
- **ROAS below margin floor for 3+ days:** the scale is no longer profitable at current spend. Roll back to last profitable budget level.
- **Learning Phase stuck (not exited after 7 days at adequate budget):** structure or signal is broken. Restructure or fix Pixel/CAPI before scaling.
- **Automated rules:** set platform rules to auto-pause any ad set if 3-day average CPA exceeds target, and auto-decrease campaign budget by 20% if 3-day ROAS drops below profitable threshold.

### Creative-testing kill criteria (when scaling in new creative)

- **The $5-$10 clicks filter (front-end check):** if an ad has spent $5-$10 without a single unique link click, pause it. You do not need to wait for a purchase to know the creative failed to stop the scroll.
- **The 1% CTR / high CPC threshold:** if CTR is below 1% or CPC is excessively high ($3-$5+), cut the ad early. A high CTR (ideally 2.5%+) is required to drive cheap traffic.
- **The $10 add-to-cart cutoff (middle-funnel):** set a max cost per add-to-cart (e.g., $10). If an ad drives traffic but cannot get carts below this threshold, it is not generating real intent — pause it.
- **The 1x product cost rule (Alex Fedotoff):** let an ad run 2-3 days. If spend reaches 1x product cost with zero conversions, kill it.
- **The break-even ladder:** track spend against multiples of break-even CPA. If break-even CPA is $23.78: at $23.78 (1x) with no sales, kill; if it gets a sale, let it run; at $47.56 (2x) without a second sale, kill; follow the step-ladder as it converts.

## Horizontal vs Vertical Comparison

| Factor | Vertical | Horizontal |
|---|---|---|
| Speed to execute | Fast — one budget edit | Slower — duplicate, configure, monitor |
| Signal preservation | High — algorithm keeps learning on the same ad set | Split — new ad sets start with less data |
| Social proof | Preserved (ads stay in place) | Preserved only via Post ID method |
| Audience saturation risk | High at scale | Low — expands to new audiences |
| Creative fatigue exposure | High — same creative, more spend | Lower — can introduce diverse creative |
| Auction overlap risk | Low (single ad set) | Moderate — manage exclusions |
| Best when | Audience has headroom, creative fresh | Audience saturating, need to de-risk |
| Ceiling | Defined by audience size + unit economics | Defined by creative pipeline + audience count |

## Common Scaling Mistakes

1. **Scaling on a lucky day.** One profitable day is noise. Wait for 48-72 hours of consistent performance.
2. **Bumping over 50% in one edit.** Triggers Learning Phase reset; costs 3-7 days of degraded performance.
3. **Bumping every day.** The algorithm needs 2-3 days to absorb a change. Daily bumps stack resets.
4. **Multiple changes per edit.** Budget + audience + creative at once makes diagnosis impossible.
5. **Scaling a fatigued creative.** Frequency above 3 + CTR dropping = more budget burns money faster. Refresh creative first.
6. **Vertical scaling past saturation.** When the audience is saturated, the constraint is reach, not budget. Go horizontal.
7. **No ceiling defined.** Scaling without a stop condition guarantees scaling past profitability.
8. **No rollback plan.** A degrading scale with no rollback rules becomes a bleed. Define triggers before the first bump.
9. **View-through-heavy scaling.** Scaling inflated view-through ROAS burns money on non-incremental conversions.
10. **Duplicating winners from scratch.** Resets social proof and algorithmic learning. Always use the Post ID method.
11. **Mid-day budget edits.** Forces Meta to cram new budget into remaining hours, spiking CPA. Edit at midnight.
12. **Enterprise-level aggressive bumps.** At $10k+/day, 50-100% jumps force low-quality impressions and can double CPA overnight.
13. **Ignoring auction overlap.** Duplicating ad sets with overlapping audiences in the same campaign makes Meta compete with itself, raising CPM.
14. **Scaling with a thin creative pipeline.** Horizontal scaling needs creative diversity. Scaling with identical ads to new audiences fails under Andromeda's creative-led targeting.

## The Budget Ladder

```text
Testing budget  →  Scaling budget  →  Ceiling
   (proven)         (stepped up)       (unit-econ limit)
```

- **Testing budget:** the daily spend where the campaign proved profitable (ABO testing phase).
- **Scaling budget:** the stepped target, reached via incremental bumps held 2-3 days each.
- **Ceiling:** the max daily budget where CPA stays at or below target, defined by audience saturation and LTV:CAC ratio. Above the ceiling, CPA inflates faster than spend.

**Ceiling estimation:**
- Audience size ÷ target frequency ÷ campaign duration = max sustainable daily impressions
- Conversion rate × max daily impressions = max daily conversions
- LTV × target CAC ratio = max acceptable CPA (the margin floor)

If the estimated ceiling is below desired spend, the constraint is the audience or the margin — fix the offer (raise LTV), expand the audience (horizontal), or improve creative (raise conversion rate) before pushing spend past the ceiling.

## Scaling Account Structures (from meta-ads-manager)

Scaling works best inside a consolidated account structure. See `meta-ads-manager` for full detail. The relevant scaling containers:

- **Advantage+ Shopping Campaign (ASC):** the primary scaling container for ecommerce. Duplicate proven winners via Post ID. Meta's AI handles targeting, placement, and creative combinations.
- **CBO scaling campaign:** one consolidated campaign with a Champions ad set (top 4-6 proven ads via Post ID) and 1-2 testing ad sets (DCT/Flexible ads). Set ad set daily minimum spend limits at 1x target CPA to force spend on testing.
- **Spend-level evolution (Ole Strand):**
  - $0-$1,000/day: single CBO testing campaign, one new ad set per week.
  - $1,000-$5,000/day: split into testing (20-40%), scaling ASC (60-80%), DPA retargeting (15-30%).
  - $5,000-$10,000+/day: scale testing volume to 6-15 ads per batch; add a retention CBO campaign for past purchasers.

## Hormozi Scaling and Iteration Principles

- **Volume negates luck:** scaling success is a high-volume game. Massive creative throughput pushes through the learning curve and builds predictable scaling.
- **The 70/20/10 iteration cycle:** once a mega-winner is identified, Week 2 testing allocates 70% slight variations of the winner, 20% decent variations (new hook, speaker, setting), 10% brand-new angles.
- **"Use and abuse" winners:** spin up 100+ variations of a winner (filters, reorders, hook swaps) to extend its lifespan. Slice the first 3 seconds off winners and paste onto other ads to yield 10-50x more efficient creatives.
- **Creative diversity at scale:** under Andromeda, similar-looking ads are consolidated and penalized. Scaling demands conceptually diverse, visual-led angles in parallel — not minor headline tweaks.
- **Organic as a safe test bed:** organic posts that earn real traction have high probability of succeeding as paid ads. Use organic to pre-validate hooks before scaling them paid.
