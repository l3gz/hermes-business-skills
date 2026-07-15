---
name: offer-builder
description: Use when constructing, refining, auditing, or documenting a marketing offer for a specific business, avatar, product, funnel, launch, sales call, or campaign. Produces a structured offer document with outcome, mechanism, stack, bonuses, guarantee, scarcity, naming, price framing, and objections.
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, offers, copywriting, pricing, funnel, conversion]
    related_skills: [avatar-builder, attractive-character-builder, brand-voice-extractor, hook-angle-writer, funnel-writer, email-writer, human-editor]
---

# Offer Builder

## Overview

Build a concrete, ethical, and marketable offer for one business and one primary avatar. An offer is not just the product. It is the full buying proposition: desired result, unique mechanism, deliverables, bonuses, guarantee, scarcity, urgency, name, price framing, and objections handled before the buyer asks.

Use `references/offer-frameworks.md` for the framework reference. This skill is the operating process for turning customer research, product facts, proof, and constraints into a reusable offer document.

The discipline: increase perceived value without lying. A strong offer makes the right buyer think, "This is for me, the result matters, I believe it can work, and now is a sensible time to act." It does not fabricate outcomes, fake scarcity, hide conditions, or invent proof.

## When to Use

Use this skill when the client asks for:

- a new offer, service package, course, membership, productized service, bundle, workshop, challenge, trial, or lead magnet
- an offer audit or repositioning pass
- offer stack, bonuses, guarantee, urgency, naming, or price framing
- funnel, webinar, launch, ad, sales page, email, or sales call preparation
- an attraction offer, core offer, upsell, downsell, or continuity offer
- a structured offer document to store in the client wiki

Do not use this skill for:

- avatar research from scratch, use `avatar-builder`
- brand voice extraction, use `brand-voice-extractor`
- hooks or headlines after the offer is clear, use `hook-angle-writer`
- final copy polish, use `human-editor`
- legal, medical, financial, or compliance approval
- inventing proof, guarantees, scarcity, results, credentials, or testimonials

## Multi-Business Rule

A client can run several businesses, and each business can have many offers. Never blend offer facts across businesses. Before building or saving an offer, confirm the business, business slug, primary avatar, offer role, and intended sales motion.

Store offer work inside the client wiki under the correct business:

```text
businesses/<business-slug>/
├── brand.md
├── products.md
├── avatars/
├── characters/
└── offers/
    └── <offer-slug>.md
```

If the wiki uses a different structure, follow it while keeping every offer grouped by business. Link the offer to the relevant avatar, product, character, proof, funnel, and campaign assets.

## Source Hierarchy

Orient from the client wiki first. Read `SCHEMA.md`, `index.md`, recent `log.md`, and the target business pages before claiming facts. Then prioritize:

1. Direct client facts: product details, fulfillment, pricing, margins, capacity, guarantee policy, legal constraints, and proof.
2. Customer evidence: testimonials, interviews, sales calls, surveys, objections, support tickets, churn reasons, and top customer analysis.
3. Existing assets: sales pages, decks, webinars, checkout pages, emails, ads, onboarding, and fulfillment materials.
4. Avatar, attractive character, and brand voice pages from the wiki.
5. Category context, only as background.
6. Agent inference for structure and wording only, never for facts, proof, scarcity, or claims.

Completion: the business, avatar, existing offer assets, fulfillment reality, and save path are known or marked unknown.

## Required Inputs

Minimum useful inputs:

- business or brand
- target avatar or customer segment
- product, service, or outcome being sold
- current deliverables or fulfillment method
- price or price range, if known
- available proof or an explicit note that proof is missing

Best inputs:

- avatar profile and top customer insights
- current offer page, sales script, proposal, checkout, or webinar stack
- objections heard on sales calls
- testimonials, case studies, before and after evidence, and approved claims
- fulfillment constraints: capacity, timeline, team, cost, risk, exclusions
- brand voice and attractive character profile
- launch, evergreen, referral, sales call, or retention context

Completion: there is enough source material to describe the promise, mechanism, deliverables, proof, risk reversal, and buying context without inventing facts.

## Core Workflow

### 1. Define offer scope

Capture business, business slug, working offer name, offer role, avatar, funnel or sales motion, known price, payment options, constraints, source list, and confidence.

Offer roles:

- **Attraction:** starts the relationship with low friction, such as a lead magnet, diagnostic, workshop, trial, challenge, or entry product.
- **Core:** the main transformation and main revenue event.
- **Upsell:** adds speed, depth, support, implementation, access, or scale after a purchase.
- **Downsell:** preserves the buyer relationship when price, timing, or intensity blocks the core offer.
- **Continuity:** creates ongoing value through membership, maintenance, coaching, replenishment, community, or retained support.

Completion: the offer is tied to one business, one primary avatar, one role, and one buying context.

### 2. Improve the value equation

Use the value equation:

```text
Perceived value = (dream outcome x perceived likelihood of achievement) / (time delay x effort and sacrifice)
```

Increase value by improving:

- **Dream outcome:** make the result specific, emotionally meaningful, and written in customer language.
- **Perceived likelihood:** add proof, process clarity, diagnostics, milestones, examples, expert support, and fit criteria.

Increase value by reducing:

- **Time delay:** create quick wins, shorter paths to first progress, clear milestones, and fewer bottlenecks.
- **Effort and sacrifice:** reduce setup, confusion, complexity, hidden work, risk, social discomfort, and opportunity cost.

Completion: each lever has at least one concrete improvement or a clear reason it cannot be changed.

### 3. Construct the offer from obstacles

Use this five-step construction sequence:

1. **Name the dream result.** State the before and after in the avatar's language. Completion: the dream result is concrete and measurable where possible.
2. **List every obstacle.** Include external barriers, internal doubts, resource gaps, knowledge gaps, implementation friction, risk, and failed attempts. Completion: the obstacle list covers practical and emotional blockers.
3. **Convert obstacles into solutions.** Map each obstacle to training, tool, template, service, audit, coaching, setup, accountability, community, support, guarantee, or decision aid. Completion: each major obstacle has a solution or is marked out of scope.
4. **Package the solutions.** Choose deliverables, sequence, support, access, format, timeline, and fulfillment boundaries. Completion: the stack is clear to both buyer and operations team.
5. **Name, frame, and risk-reverse.** Create the name, explain why now, frame price against value, choose a truthful guarantee, and answer objections. Completion: the offer has a marketable presentation without unsupported claims.

### 4. Build the offer stack and bonuses

For each stack item, capture:

- item name
- what it is and what problem it solves
- format, timing, access, and fulfillment owner
- value anchor
- proof or reason to believe
- limitations, exclusions, or conditions

Value anchors must be honest. Use replacement cost, time saved, expert access, implementation help, risk reduction, comparable service value, or business impact. Do not invent retail prices. If subjective, label it an estimated value anchor.

Add bonuses only when they remove objections or speed implementation. Good bonuses include quick-start assets, templates, scripts, calculators, audits, onboarding, office hours, case study libraries, community, accountability, or decision support.

Completion: every core item and bonus maps to a real obstacle, objection, or speed improvement.

### 5. Choose risk reversal

Select a guarantee or risk reversal that fits the business model, legal constraints, fulfillment risk, and customer responsibility.

Guarantee taxonomy:

- **Unconditional:** refund within a clear window with minimal conditions.
- **Conditional:** refund or remedy requires defined buyer actions or qualifying criteria.
- **Anti-guarantee:** no refund or no guarantee because fit, customization, limited capacity, or delivery cost requires commitment.
- **Implied or performance:** confidence comes from milestones, service terms, outcome-based components, or delivery structure rather than a simple refund promise.

State window, conditions, exclusions, buyer responsibilities, and claim process. Flag health, income, legal, financial, credential, or regulated promises for review.

Completion: the risk reversal is clear, truthful, operationally possible, and matched to the offer.

### 6. Add ethical scarcity and urgency

Use scarcity and urgency only when real. Ethical scarcity can come from limited client capacity, cohort size, inventory, application windows, calendar availability, delivery bandwidth, or bonus availability tied to fulfillment limits. Ethical urgency can come from enrollment deadlines, live start dates, price change dates, seasonal timing, expiring audits, or a strategic reason to solve the problem before a known event.

Never invent fake countdowns, fake seats, fake expiring bonuses, fake demand, or fake price increases. If there is no real urgency, use cost-of-delay framing instead.

Completion: every scarcity or urgency element has a real reason or is removed.

### 7. Name the offer with MAGIC

Use MAGIC to generate names:

- **M, Magnetic reason why:** the unique mechanism, belief, method, or reason this exists.
- **A, Avatar:** who it is for or who they want to become.
- **G, Goal:** the result or transformation.
- **I, Interval:** timeframe, milestone, cadence, or season, only if true.
- **C, Container:** sprint, system, lab, accelerator, audit, challenge, workshop, protocol, membership, roadmap, or similar format.

Do not force every element into the public name. Provide 5 to 10 options and one recommended name with rationale.

Completion: the chosen name is clear, specific, believable, and brand-appropriate.

### 8. Frame price and objections

Frame price with truthful value logic: cost of staying stuck, cost of alternatives, time saved, replacement cost of the stack, risk reduction, support, convenience, or responsibly estimated upside. Include payment options only if real. Explain who should buy and who should not buy.

Then map each top objection to an offer element: proof, guarantee, stack item, bonus, onboarding, case study, fit criteria, or sales note.

Completion: price framing is honest and the main objections are answered by specific offer elements.

### 9. Assemble the structured offer document

Use this output shape:

```markdown
# Offer: [Recommended Name]

## Scope
- Business:
- Business slug:
- Offer role: attraction / core / upsell / downsell / continuity
- Primary avatar:
- Funnel or sales motion:
- Price / payment options:
- Confidence:
- Sources used:

## One-Sentence Offer
[Avatar] gets [dream outcome] through [mechanism/container] without [main pain, delay, or sacrifice].

## Dream Outcome
- Before state:
- After state:
- Emotional payoff:
- Practical payoff:
- Success metrics:

## Mechanism
- Unique mechanism:
- Why it works:
- Why other approaches fail:
- Proof available:
- Claims needing review:

## Value Equation
| Lever | Current state | Improvement |
|---|---|---|
| Dream outcome |  |  |
| Perceived likelihood |  |  |
| Time delay |  |  |
| Effort and sacrifice |  |  |

## Obstacles and Solutions
| Avatar obstacle | Offer solution | Stack item |
|---|---|---|

## Offer Stack and Bonuses
| Item | Objection solved | Format | Value anchor | Proof |
|---|---|---|---|---|

## Guarantee / Risk Reversal
- Type:
- Promise:
- Conditions:
- Exclusions:
- Buyer responsibilities:
- Claim process:

## Scarcity and Urgency
- Real scarcity:
- Real urgency:
- Reason why:
- What not to say:

## MAGIC Name Options
1.
2.
3.
4.
5.

## Recommended Name
- Name:
- Rationale:

## Price Framing and Objections
- Investment:
- Value logic:
- Cost of inaction:
- Alternatives:
- Fit / not fit:
- Objections handled:

## Needs Confirmation
- [unknown facts, risky claims, operations constraints, or legal review items]
```

Completion: the document can be handed to copywriting, sales, or operations without requiring the reader to reconstruct the offer strategy.

### 10. Update the wiki when appropriate

If working inside an LLM wiki, save the final offer under `businesses/<business-slug>/offers/<offer-slug>.md`, link it to related business assets, update `index.md` if appropriate, append to `log.md`, and run `qmd update` if the wiki uses QMD.

Completion: the offer is filed under the correct business and reusable by other skills.

## Missing Information Handling

Do not invent missing facts. Use these labels:

- `Unknown`: no source material supports the answer
- `Needs confirmation`: likely but not verified
- `Client to provide`: requires product, operations, financial, legal, or customer information
- `Risk flag`: health, income, legal, financial, credential, guarantee, or regulated claim needing review
- `Out of scope`: a desired promise or component the business cannot currently fulfill

When the offer is thin, draft what can be supported and ask the highest-leverage questions in this order: avatar, dream outcome, proof, deliverables, fulfillment constraints, guarantee policy, price, scarcity reason, objections, and brand voice.

## Quality Bar

A strong offer has:

- one primary avatar and one clear role
- a specific dream outcome in customer language
- a believable mechanism and proof path
- a stack built from real avatar obstacles
- bonuses that solve objections rather than pad the offer
- a guarantee or risk reversal that is clear and deliverable
- ethical scarcity and urgency with real reasons
- a memorable name that does not overpromise
- truthful price framing and clear fit criteria
- risky claims and unknowns flagged
- correct storage under the client wiki business when applicable

A weak offer has vague promises, a feature list with no transformation, fake bonus values, fake scarcity, unsupported proof, an impossible guarantee, no objection handling, or one offer trying to serve several businesses or avatars at once.

## Common Pitfalls

1. **Starting with deliverables instead of desire.** The stack should serve the dream outcome. Completion: every deliverable links to an outcome or obstacle.
2. **Using fake value anchors.** Do not invent prices or imply a made-up market value. Completion: each value anchor has a real basis or is labeled estimated.
3. **Adding filler bonuses.** Bonuses must remove an objection, accelerate progress, or reduce risk. Completion: every bonus has a job.
4. **Overpromising speed or ease.** Reduce delay and effort where truthful, but preserve buyer responsibility. Completion: speed claims match fulfillment reality.
5. **Choosing the wrong guarantee.** Match risk reversal to operations and legal constraints. Completion: terms and exclusions are explicit.
6. **Faking urgency.** If the reason is not real, do not use it. Completion: urgency is documented or removed.
7. **Skipping operations.** An offer that sells but cannot be delivered damages the business. Completion: fulfillment limits are captured.
8. **Ignoring regulated claims.** Health, income, legal, financial, and credential claims need review. Completion: risky claims are flagged.

## Verification Checklist

- [ ] Client wiki orientation completed when a wiki is available
- [ ] Business, business slug, avatar, and offer role confirmed
- [ ] Offer stored or prepared for storage under `businesses/<business-slug>/offers/`
- [ ] Dream outcome is specific and in customer language
- [ ] Unique mechanism or reason-to-believe is clear
- [ ] Value equation addressed: outcome, likelihood, delay, effort
- [ ] Major avatar obstacles are mapped to solutions
- [ ] Offer stack includes deliverables, formats, timing, and value anchors
- [ ] Bonuses solve real objections or implementation obstacles
- [ ] Guarantee type, conditions, exclusions, and buyer responsibilities are defined
- [ ] Scarcity and urgency are ethical and based on real constraints
- [ ] MAGIC name options and recommended name are included
- [ ] Price framing is truthful and does not rely on unsupported ROI
- [ ] Main objections are answered by specific offer elements
- [ ] Unknowns, risky claims, and compliance needs are flagged
- [ ] Final output follows the structured offer document shape
