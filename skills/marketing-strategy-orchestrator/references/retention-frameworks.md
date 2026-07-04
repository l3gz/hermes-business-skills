# Retention and Churn Frameworks Reference

This reference distills the retention frameworks from $100M Money Models: Delivery System & Retention. It is relevant to `campaign-optimizer` (retention metrics and churn diagnostics), `meta-ads-scaler` (LTV impacts CAC viability), and `marketing-strategy-orchestrator` (Stage 5+ LTV extension).

**Core thesis:** Retention = LTV = acquisition power. The business that retains customers longer can afford to spend more acquiring them, which means it can outspend competitors on ads and dominate the market. Churn is not just a delivery problem — it is a marketing strategy constraint.

## The 9-Step Churn Checklist

From $100M Money Models: Retention. A systematic framework for reducing churn and extending customer lifetime.

### 1. Find Activation Points

"Every customer who does X stays longer." Identify the actions that correlate with retention using common-factors analysis on your top 20% of customers (those with the longest lifetime or highest LTV).

**How:** export your best customers, identify what they all did in their first 7-30 days, and look for shared actions. The shared action is your activation point. Drive every new customer to complete it.

**Examples:** "users who connect their Stripe account in week 1 churn 60% less." "members who attend 3 classes in their first week stay 4x longer." "clients who complete the onboarding call retain at 85% vs 40% who skip it."

### 2. Onboard Customers

Custom beats generic. Personal beats group. Live beats recorded. Carrots beat sticks.

Drive every new customer to the activation point as fast as possible. The onboarding sequence should make the first win happen within the first session or day — not the first week.

**The rule:** if a customer doesn't get value in the first interaction, churn risk doubles.

### 3. Incentivize Activation

Place unlockables (courses, calls, badges, bonus content, premium features) *just past* major churn points. The churn point is where customers typically drop off; the unlockable gives them a reason to push through.

**Example:** if month-2 is where churn spikes, unlock a premium resource or bonus call at day 45 — just before the spike. The anticipation of the unlock carries them past the danger zone.

### 4. Community Linking

Connect members to each other, not just to you. "Easy to quit a membership. Hard to leave a relationship."

**How:** pair new customers with accountability partners, create cohort-based sub-groups, facilitate peer-to-peer interaction, recognize and amplify members who help each other. The social fabric becomes the retention mechanism.

### 5. Correct or Fire Bad Customers

Not every customer should be retained. Bad customers drain support, demoralize the team, and distract from serving good customers.

**3-strike system:**
- Strike 1: identify the behavior and document it
- Strike 2: communicate the issue and the expected change
- Strike 3: fire the customer (refund and release)

Firing bad customers improves team morale, frees capacity for good customers, and often generates referrals from the customers who *want* to stay.

### 6. Add Annual Pricing

"Buy 10 get 2 free." Annual plans reduce churn dramatically and improve cash flow.

**The "big head, long tail" structure:** big upfront payment + small monthly recurring. The upfront payment funds acquisition; the monthly payment maintains the relationship.

**Billing cadence churn data (Hormozi):**
- Monthly billing: 10.7% monthly churn
- Quarterly billing: 5% monthly churn
- Annual billing: 2% monthly churn

**Implication:** moving customers from monthly to annual billing cuts churn by 5x. Even at a discount, the retained revenue far exceeds the discount cost.

### 7. Exit Interviews and Cancellation Videos

Save half of cancellations. When a customer requests to cancel, intercept with:
- A personal outreach (call or email)
- "Redo" path: offer to restart their onboarding or fix the specific issue
- "Upsell" path: offer a downsell to a lower tier or different product

**Hormozi's data:** cancellation interception saves ~50% of departing customers. The cost of the intervention (a call, a video, a personal email) is a fraction of the CAC to replace the customer.

### 8. Survey 2x Per Year

Ask the retention question: "If I removed all but one thing, what would you keep?" The answers reveal what your customers actually value — which may differ from what you think they value. Double down on what they keep, cut what they don't mention.

**The ACA framework for regular outreach:**
- **A**cknowledge: confirm you heard them
- **C**ompliment: recognize their engagement or progress
- **A**sk: ask a question that surfaces needs or concerns

### 9. The 4-Milestone Customer Journey

Map every customer through four milestones. Each milestone extends lifetime and increases LTV:

1. **Activate:** get the customer to their first result (the activation point from step 1)
2. **Testimonial:** capture their success story (use the Epiphany Script from Stage 2 of the Scaling Roadmap)
3. **Refer:** ask the happy customer to bring another customer (the cheapest, highest-quality lead source)
4. **Ascend:** move them to a higher-tier offer, upsell, or continuity program

**The compounding effect:** a customer who reaches milestone 4 has 5-10x the LTV of a customer who stalls at milestone 1. The marketing strategy should optimize for advancement through the milestones, not just for acquisition.

## Pricing and Churn Math

From $100M Money Models: Retention. The relationship between price, conversion, churn, and LTV.

### The Price-LTV Optimization Curve

Higher price → lower conversion + higher churn per unit, but higher revenue per customer. The LTV curve has an optimum — there is a price that maximizes total lifetime revenue, and it is usually higher than the price that maximizes conversion rate.

**Hormozi's testing data (gym memberships):**
- $20/month: high conversion, high churn, low LTV
- $39-59/month: the optimal range (balance of conversion, churn, and LTV)
- $100+/month: low conversion, acceptable churn, but lower total LTV due to volume loss

**Implication:** test price points. The optimal price for LTV is rarely the lowest price. Use the price-raising protocol from the Money Model construction principles.

### "Shaking the Tree"

When you raise prices or change the offer, expect a churn spike:
- Month 1 after change: churn spikes ~50% above baseline
- Month 2: churn halves from the spike
- Month 3: churn returns to baseline or below

This is normal. The customers who leave were the most price-sensitive (lowest LTV). The customers who stay have higher willingness to pay and longer projected lifetime.

## How Retention Impacts Marketing Strategy

Retention is not separate from acquisition — it is the foundation that makes aggressive acquisition possible.

1. **Higher LTV = higher allowable CAC.** If you can extend a customer's lifetime from 3 months to 12 months, you can spend 4x more to acquire them. This is the link between retention and ad scaling.

2. **Lower churn = more compounding growth.** A business with 10% monthly churn must acquire 10% of its base every month just to break even. A business with 2% monthly churn (annual billing) can grow much faster from the same acquisition spend.

3. **The 4-milestone journey creates organic lead sources.** Activated, happy customers who refer are the cheapest and highest-quality leads. A strong retention system feeds the acquisition system.

4. **Stage 5+ businesses must fix retention before scaling acquisition further.** If churn is high, pouring more leads into a leaky bucket burns cash. Fix retention first, then scale acquisition.
