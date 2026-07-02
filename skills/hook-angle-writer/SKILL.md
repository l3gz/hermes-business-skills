---
name: hook-angle-writer
description: Use when generating hooks, headlines, and marketing angles for a business from its avatar, offer, and brand voice. Produces batches of scroll-stopping hooks tagged by desire, awareness level, and channel for ads, emails, social, funnel headers, and podcast clips.
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, hooks, headlines, angles, copywriting]
    related_skills: [avatar-builder, attractive-character-builder, brand-voice-extractor, offer-builder, podcast-to-copy, launch-email-writer, nurture-email-writer, funnel-page-writer, human-editor]
---

# Hook and Angle Writer

## Overview

Generate hooks, headlines, and angles that stop attention and pull a specific dream customer into the next line, then toward a specific offer.

An angle is the underlying idea: which desire, which promise, which enemy, which mechanism. A hook is the exact line that grabs attention. A headline is the hook at the top of an ad, page, email, or post. One angle produces many hooks. This skill builds angles first, then hooks, then tags and packages them for use.

This skill is a generator, not a strategy source. It pulls the real inputs from the client wiki: the avatar (who we are talking to and what they want), the offer (what we are promising and the mechanism), and the brand voice (how this brand sounds). It does not invent the avatar, the offer, or the claims. The detailed framework library lives in `references/hook-frameworks.md`; this file is the operating process.

The core discipline: a hook may dramatize a real benefit, but it may never promise something the offer cannot deliver. A hook that wins the click and loses the customer is a failure.

## When to Use

Use this skill when the client asks for:

- hooks, headlines, or subject lines for ads, emails, social posts, funnel pages, or video and podcast clips
- fresh marketing angles for an offer or campaign
- a hook bank or headline swipe file for a business
- new ways to open a piece of content
- angle variations for split testing across awareness levels or channels

Do not use this skill for:

- customer research or building the avatar (use `avatar-builder`)
- defining or structuring the offer itself (use `offer-builder`)
- extracting the brand voice from existing copy (use `brand-voice-extractor`)
- writing full emails, pages, or scripts (use the relevant writer skill; this skill feeds them)
- inventing claims, results, or a persona that the wiki does not support

## Multi-Business Rule

A client can run several businesses or brands, and each has its own avatars, offers, and voice. Hooks are only as good as the specific avatar and offer behind them, so they must never be blended across businesses.

When the request is "write hooks" or "give me angles," first confirm:

- which business or brand it is for
- which offer the hooks point to
- which avatar the hooks speak to
- which channels are needed

Store hook banks inside that business's space in the client wiki, next to its avatars, offers, brand, and characters. The `llm-wiki-starter` layout is only the foundation; adapt to the client's real structure.

Recommended per-business path inside the client wiki:

```text
businesses/<business-slug>/
├── brand.md
├── offers.md
├── avatars/
│   └── <avatar-slug>.md
├── characters/
│   └── <character-slug>.md
└── hooks/
    ├── <offer-slug>-hook-bank.md
    └── ...
```

If the client wiki already uses a different structure, follow it and keep hook banks grouped by business and offer.

## Required Inputs

Minimum useful inputs:

- the business or brand
- the offer the hooks point to (promise and mechanism)
- the target avatar or at least the dream customer and their top desire
- the channels needed

Best inputs:

- a completed avatar profile (desires, pains, objections, words they use, awareness level)
- a structured offer doc (dream outcome, unique mechanism, proof, guarantee)
- a brand voice guide or an attractive character profile (signature phrases, words to avoid, enemy)
- known proof, results, and approved claims
- prior winning and losing hooks for this audience

## Core Workflow

### 1. Orient to the client wiki

If working inside a wiki, first read:

- `SCHEMA.md`
- `index.md`
- recent `log.md`
- the target business's brand, offers, avatars, characters, and any existing hook banks

Completion: you know the business, the offer, the avatar, the voice, and where the hook bank should live.

### 2. Confirm scope

Define before writing:

- business or brand
- specific offer and its unique mechanism
- specific avatar and their dominant desire
- channels required (ad, email subject, social, funnel header, podcast clip)
- awareness levels to cover (cold, warm, hot)
- how many hooks per group

Completion: one offer, one avatar, a named channel set, and a target count are fixed.

### 3. Pull the raw material

From the avatar, offer, and voice, extract into a working table before writing:

| Input | What to capture |
|---|---|
| Dominant desire | the Life-Force 8 or secondary want the offer truly serves |
| Pains | the specific problems, in the avatar's own words |
| Dream outcome | the after state the offer delivers |
| Unique mechanism | why this offer works when others failed |
| Proof | results, numbers, testimonials, credentials |
| Enemy | the villain or false belief the brand stands against |
| Voice | signature phrases, tone, words to avoid |
| Approved claims | what can be said safely, and what is risky |

Completion: every cell has real wiki-sourced material or a clear `Needs confirmation` marker. Nothing invented.

### 4. Build angles before hooks

List distinct angles first, so the hooks are varied rather than ten rewrites of one idea. Draw angles from:

- the dominant desire and secondary wants (Life-Force 8)
- the top pains (problem-led angles)
- the unique mechanism (how-it-works angles)
- the enemy or false belief (contrarian angles)
- proof and results (proof-led angles)
- the transformation gap (before and after angles)

Completion: at least 5 to 8 distinct angles are named for the offer.

### 5. Generate hooks per angle using the frameworks

For each angle, write hooks using the structures in `references/hook-frameworks.md`:

- Hook, Story, Offer (the hook wins the next line, nothing more)
- the four headline qualities (self-interest, news, curiosity, quick and easy)
- headline template patterns (How to, Who else wants, Warning, At last, Secrets of, Now you can, They didn't think I could but I did, Are you)
- PAS (problem, agitate, solve)
- Before, After, Bridge
- If, Then
- curiosity and fascination bullets

Match the framework to the awareness level:

- cold: problem-led, pattern interrupt, big curiosity gap, story open; no jargon or product name
- warm: unique mechanism, differentiation, proof, "how to get X without Y"
- hot: direct offer, price, bonuses, guarantee, scarcity, direct call to action

Completion: each angle has multiple hooks spanning the requested awareness levels.

### 6. Tag and package every hook

Give every hook three tags so it can be deployed correctly:

- **Desire**: which Life-Force 8 or secondary want it pulls
- **Awareness**: cold, warm, or hot
- **Channel**: ad, email subject, social, funnel header, or podcast clip

Adapt the shape to the channel: subject lines short and honest to the body, ad hooks front-loaded, funnel headers matched to the driving ad, podcast and video hooks written as spoken openers. See the channel adaptation section of the reference.

Completion: every hook carries desire, awareness, and channel tags and is shaped for its channel.

### 7. Output the hook bank

Produce the batch in this structure:

```markdown
# Hook Bank: [Offer] for [Avatar]

## Scope
- Business/brand:
- Offer + unique mechanism:
- Avatar + dominant desire:
- Channels:
- Confidence:
- Sources used:

## Angles
1. [angle] - desire: [x], based on: [pain/mechanism/enemy/proof]
2. ...

## Hooks
| # | Hook | Angle | Desire | Awareness | Channel | Framework |
|---|---|---|---|---|---|---|
| 1 | ... | ... | ... | cold/warm/hot | ad/email/social/funnel/podcast | HSO/PAS/BAB/... |

## Top picks to test first
- [3 to 5 highest-confidence hooks and why]

## Needs Confirmation
- [risky claims, unverified results, gaps to confirm with the client]
```

Completion: the bank is a ready-to-test batch, tagged and sourced, usable by the email, funnel, launch, and podcast skills.

### 8. Update the wiki when appropriate

If working inside an LLM wiki:

- save the hook bank under `businesses/<business-slug>/hooks/<offer-slug>-hook-bank.md`
- link it to the offer, avatar, and character it draws from
- update `index.md`
- append to `log.md`
- if QMD is configured, run `qmd update` so the bank is searchable

Completion: the hook bank is filed under the correct business and offer and reusable in later sessions.

## Missing Information Handling

If information is missing, do not invent the avatar, the offer, or claims. Use these labels:

- `Unknown`: not enough source material to write from
- `Needs confirmation`: drafted from weak signals, must be verified
- `Client to provide`: requires a real result, story, or claim only the client can give
- `Risk flag`: income, health, financial, or legal claim needing verification or a disclaimer

If the avatar or offer is missing entirely, stop and route to `avatar-builder` or `offer-builder` first. Hooks written without a real avatar and offer are generic and worthless. When inputs are thin, deliver the best hooks possible from what exists and list the specific questions that would sharpen the rest.

## Quality Bar

A strong hook batch has:

- hooks tied to a genuine dominant desire, not vague hype
- distinct angles, not one idea reworded
- coverage across the requested awareness levels and channels
- specificity: real numbers, timeframes, mechanisms, and the avatar's own words
- the brand voice, not a generic guru template
- every hook tagged by desire, awareness, and channel
- honest promises the offer can deliver
- risky claims flagged
- a confidence level and source list

A weak hook batch has:

- generic lines that could sell anything
- clickbait curiosity the content does not pay off
- fake scarcity or fake results
- one angle repeated ten times
- no channel or awareness matching
- claims that create legal or credibility risk
- no link to a specific avatar or offer

## Common Pitfalls

1. **Writing hooks with no avatar or offer.** Hooks are downstream of research and the offer. Pull them from the wiki or build them first.
2. **Overpromising.** A hook that promises what the offer cannot deliver wins the click and loses the customer. Keep it honest.
3. **One angle, ten rewrites.** Build the angle list first so the batch is genuinely varied.
4. **Ignoring awareness level.** A hot-traffic offer hook shown to cold traffic fails. Match and tag every hook.
5. **Clickbait curiosity.** Curiosity must be backed by a real payoff. Empty teases erode trust.
6. **Losing the brand voice.** Use the brand's signature phrases and avoid its taboo words; do not default to hype.
7. **Fake scarcity and fake numbers.** Never fabricate urgency, results, or proof. Flag anything unverified.
8. **Vague desire.** "Be better" is not a desire. Anchor to a specific Life-Force 8 or secondary want the offer truly serves.
9. **Channel mismatch.** A page headline is not an email subject line. Shape each hook for its surface.

## Verification Checklist

- [ ] Business, offer, and target avatar confirmed
- [ ] Avatar, offer, and brand voice pulled from the wiki (not invented)
- [ ] Dominant desire identified and honestly served by the offer
- [ ] At least 5 distinct angles built before writing hooks
- [ ] Hooks span the requested awareness levels (cold, warm, hot)
- [ ] Hooks cover the requested channels
- [ ] Every hook tagged by desire, awareness, and channel
- [ ] Hooks use specific words, numbers, and mechanisms, not vague hype
- [ ] Hooks match the brand voice and avoid taboo words
- [ ] No hook overpromises beyond what the offer delivers
- [ ] Risky claims (income, health, financial, legal) flagged
- [ ] Top picks to test first are called out
- [ ] Confidence level and source list included
- [ ] If wiki-backed, hook bank filed under the correct business and offer, linked to avatar and offer, with index and log updated
