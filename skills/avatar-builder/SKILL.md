---
name: avatar-builder
description: Use when building a deep customer avatar from interviews, transcripts, reviews, comments, market research, product facts, and offer context. Produces evidence-backed avatar profiles for copy, offers, funnels, hooks, objections, and content.
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, avatar, customer-research, copywriting, offer]
    related_skills: [brand-voice-extractor, podcast-to-copy, funnel-page-writer, email-writer, human-editor]
---

# Customer Avatar Builder

## Overview

Build a deep, evidence-backed customer avatar that can drive copy, hooks, offers, funnels, content, objection handling, and market positioning.

This skill is based on the full worksheet in `references/deep-customer-avatar-intelligence-worksheet.md`. The worksheet is the detailed framework. Use `references/customer-research-frameworks.md` for the customer research layer: Top 20 Percent Customer Analysis, Enter the Conversation in Their Head, F.R.E.D., awareness levels, and traffic temperature.

The key discipline: separate what the customer actually said from what the agent inferred. Exact language is more valuable than polished marketing language. The highest-leverage avatar is usually the customer segment that spends most, stays longest, gets the best results, and is easiest to serve.

## Multi-Business Rule

A client can run several businesses or brands. Every avatar belongs to one business.

When the request is "build an avatar," first confirm which business or brand it is for. Never blend avatars from different businesses into one profile.

Store each avatar inside that business's space in the client wiki, not in a shared global pile. The client wiki is the client's own adapted reality: the `llm-wiki-starter` layout is only the foundation, and each business gets its own brand facts, products, offers, sources, and avatars.

Recommended per-business path inside the client wiki:

```text
businesses/<business-slug>/
├── brand.md
├── products.md
├── offers.md
├── avatars/
│   ├── <avatar-slug>.md
│   └── ...
└── sources/            # or link to raw/ sources for this business
```

If the client wiki already uses a different structure, follow the existing structure and keep avatars grouped by business.

## When to Use

Use this skill when the client asks for:

- a customer avatar, buyer persona, ICP, or audience profile
- copywriting research before writing ads, emails, sales pages, funnels, or content
- deeper understanding of customer pain, desire, objections, and buying triggers
- interview or transcript analysis for marketing insights
- market research for an offer, product, or brand
- avatar work for a specific business, product, offer, or campaign

Do not use this skill for:

- broad market sizing only
- generic demographic personas with no copywriting use
- product strategy without customer evidence
- inventing an avatar from vibes when no source material exists

If source material is thin, run the market research sprint and label the profile `confidence: low` or `confidence: medium`.

## Source Hierarchy

Prioritize sources in this order:

1. Direct customer interviews, sales calls, testimonials, support tickets, DMs, surveys, reviews, and failed sales conversations.
2. Existing customer-facing assets: emails, sales pages, ads, podcast transcripts, webinar comments, social comments, community posts.
3. Competitor reviews and competitor comments from buyers with similar pain.
4. Public market research: Reddit, YouTube comments, Amazon reviews, forums, Facebook group posts, TikTok comments, podcasts, newsletters, and niche communities.
5. Founder or team assumptions.
6. Agent inference.

Rules:

- Label exact quotes as `customer language`.
- Label competitor/public research as `market signal`.
- Label founder/team claims as `internal assumption`.
- Label agent synthesis as `inference`.
- Never present inference as customer fact.

## Required Inputs

Minimum useful inputs:

- business, product, or offer being sold
- target customer or segment
- desired output, for example hooks, avatar page, offer angle, sales page prep
- at least one source: transcript, review set, sales call, survey, comments, or founder notes

Best inputs:

- 3 to 10 customer interviews or sales calls
- reviews or testimonials from buyers and non-buyers
- failed sales conversations and objections
- competitor reviews
- product facts and approved claims
- existing copy, emails, ads, funnel pages, and content examples

## Market Research Sprint

Run this when the client does not have enough direct customer material or asks for a stronger market-backed avatar.

1. Define the market map.
   - Product category
   - Customer segment
   - Main problem
   - Direct alternatives
   - Indirect alternatives
   - Competitors or adjacent brands
   - Completion: the market map names at least 3 places where this customer talks naturally.

2. Collect customer language.
   - Look for reviews, comments, forum posts, testimonials, complaints, objections, and before/after stories.
   - Capture exact phrases, not summaries.
   - Completion: at least 20 useful raw phrases or quotes are captured, unless the available market is too small.

3. Extract repeated patterns.
   - Pain patterns
   - Desire patterns
   - Skepticism patterns
   - Failed attempts
   - Enemy or broken system frames
   - Proof requirements
   - Completion: every pattern has at least one source quote or is marked as inference.

4. Compare alternatives.
   - What customers like about alternatives
   - What customers hate about alternatives
   - What promises they no longer trust
   - What gaps the client's offer can own
   - Completion: at least 3 useful differentiation angles are identified.

5. Update confidence.
   - `high`: supported by direct customer evidence and repeated external signals
   - `medium`: supported by some direct evidence or strong external market signals
   - `low`: mostly founder assumptions or early inference

## Core Workflow

### 1. Orient to the client wiki

If working inside a wiki, first read:

- `SCHEMA.md`
- `index.md`
- recent `log.md`
- relevant pages for the brand, product, offer, customer, and previous avatar work

Completion: you know what avatar already exists, what sources are available, and where the new profile should live.

### 2. Define the avatar scope

Before filling the worksheet, define:

- avatar name or working segment name
- product or offer this avatar is for
- buying situation or campaign context
- awareness level
- current stage in the customer story
- source list used

Completion: the avatar is about one clear buyer in one clear buying context. Do not merge multiple avatars into one mushy profile.

### 3. Build the evidence table

Extract evidence into these buckets before writing the profile:

| Bucket | What to capture |
|---|---|
| Customer language | exact words for pain, desire, fear, skepticism, success |
| Surface problem | what they say out loud |
| Real problem | deeper diagnosis supported by evidence |
| Desired identity | who they want to become |
| Failed attempts | what they tried and why it failed |
| False beliefs | beliefs blocking the sale |
| Objections | money, trust, timing, proof, effort, fit |
| Enemies | people, systems, beliefs, or mechanisms they blame |
| Proof needed | what would make them believe |
| Buying triggers | urgency, identity, proof, novelty, necessity, convenience |
| Media signals | platforms, influencers, content, comments, communities |

Completion: each important bucket has quotes, source references, or a clear `unknown` marker.

### 4. Complete the deep worksheet selectively

Use the full reference worksheet when the client asks for a deep build. Do not force all 25 sections into the final answer unless the client wants a full research document.

For most deliverables, complete these first:

1. Customer language
2. Surface problem vs real problem
3. Awareness level
4. Identity
5. Dreams, desires, and values
6. Hormozi value equation
7. Pains, fears, and frustrations
8. Failures and past attempts
9. Suspicion and skepticism
10. Enemies
11. Human needs and emotional drivers
12. Decision pillars
13. Locus of control
14. Story arc
15. Internal dialogue
16. Objections
17. Offer design inputs
18. BrandScript and one-liner
19. Media and influence
20. Final avatar profile
21. Copywriting output prompts

Completion: the profile has enough depth to write copy without asking basic follow-up questions.

### 5. Synthesize the final avatar

Produce a practical final profile with this structure:

```markdown
# Customer Avatar: [Name]

## Scope
- Product/offer:
- Segment:
- Awareness level:
- Confidence:
- Sources used:

## One-Sentence Avatar Summary
[Avatar Name] is a [identity] who wants [dream outcome], but is struggling with [real problem]. They believe [current belief], fear [biggest fear], and need to discover [required epiphany] before they will buy.

## Customer Language
### Pain phrases
- "..."

### Desire phrases
- "..."

### Fear/skepticism phrases
- "..."

## Surface Problem vs Real Problem
- Surface problem:
- Real problem:
- Hidden mechanism:
- What they need to understand:

## Identity
- Current identity:
- Desired identity:
- Identity they want to escape:
- Identity buying trigger:

## Value Equation
- Dream outcome:
- Proof needed to believe:
- Desired timeline:
- Effort/sacrifice to remove:

## Pains, Fears, and Frustrations
- Biggest pain:
- Biggest fear:
- Biggest frustration:
- Urgency trigger:

## Failed Attempts and False Beliefs
- Tried before:
- Why it failed:
- False beliefs:
- Promises they distrust:

## Objections and Reframes
| Objection | What it really means | Reframe | Proof needed |
|---|---|---|---|

## Enemies and Us vs Them
- Main enemy:
- Broken system:
- Us:
- Them:
- Finally someone said it angle:

## Buying Triggers
- Main emotional drivers:
- Decision pillars:
- Locus of control:
- Best urgency angle:

## Offer Inputs
- Outcome worth paying for:
- Bonuses that remove friction:
- Guarantee angle:
- Premium angle:
- Safe angle:

## Copy Angles
- Best hook angle:
- Best story angle:
- Best offer angle:
- Best proof angle:
- Best objection angle:

## Open Questions
- [unknowns that need interviews, research, or client confirmation]
```

Completion: the final profile is usable by another skill, for example funnel page, email, podcast repurposing, or human editor.

### 6. Generate optional copywriting outputs

Only after the profile is complete, generate requested outputs:

- 10 pain hooks
- 10 dream outcome hooks
- 10 enemy or broken-system hooks
- 10 hidden-mechanism hooks
- 10 false-belief hooks
- offer improvements
- objection-handling bullets
- story angles
- urgency angles
- guarantee ideas
- one-liner
- sales page, webinar, VSL, ad, social, or email angles

Completion: outputs clearly trace back to the avatar, not generic marketing formulas.

### 7. Update the wiki when appropriate

If working inside an LLM wiki:

- Confirm the business the avatar belongs to
- Save raw sources under `raw/` (books, transcripts, reviews, research)
- Save the final avatar under that business's space, for example `businesses/<business-slug>/avatars/<avatar-slug>.md`, or the client's existing avatar directory
- Link the avatar to that business's brand, product, offer, and source pages
- Update `index.md`
- Append to `log.md`
- If QMD is configured for this wiki, run `qmd update` so the new avatar is searchable

Completion: the avatar is filed under the correct business and can be found and reused in later sessions.

## Missing Information Handling

If information is missing, do not hallucinate. Use one of these labels:

- `Unknown`: not enough evidence
- `Likely`: supported by weak signals
- `Market signal`: seen in public research, not direct customer evidence
- `Internal assumption`: from founder or team, not validated
- `Needs interview`: should be asked in a customer interview

When the avatar is thin, end with the best 5 to 10 interview questions to close the gaps.

## Quality Bar

A strong avatar has:

- exact customer language
- a clear surface problem and real problem
- a believable hidden mechanism
- emotional and identity drivers
- false beliefs and objections
- proof requirements
- buying triggers
- offer design inputs
- copy angles
- confidence level and source list
- explicit open questions

A weak avatar has:

- generic demographics
- polished marketing language instead of customer language
- no source references
- mixed segments
- invented fears or desires
- no objections
- no proof requirements
- no clear buying context

## Common Pitfalls

1. **Merging multiple buyers.** If homesteaders, athletes, and general wellness buyers appear, create separate avatars.
2. **Overvaluing demographics.** Age and income matter less than pain, desire, identity, skepticism, and buying trigger.
3. **Inventing emotional drivers.** Use quotes, interviews, reviews, and observable behavior. Mark guesses as inference.
4. **Skipping failed attempts.** Past failures explain skepticism and objections.
5. **Writing the avatar like a strategy memo.** The output should give copywriters usable language, hooks, fears, beliefs, and proof angles.
6. **Completing every worksheet section too early.** Start with a useful profile, then deepen it when more evidence arrives.
7. **Ignoring non-buyers.** Failed sales conversations reveal objections and missing proof.
8. **Treating market research as equal to customer evidence.** Public research is useful, but direct customer material wins.

## Verification Checklist

- [ ] Avatar scope is one clear buyer in one clear buying context
- [ ] Source list is included
- [ ] Confidence level is included
- [ ] Customer language includes exact phrases
- [ ] Surface problem and real problem are separated
- [ ] False beliefs and objections are included
- [ ] Proof requirements are included
- [ ] Offer design inputs are included
- [ ] Copy angles are included
- [ ] Unknowns are labeled instead of invented
- [ ] If wiki-backed, index and log updates are complete
