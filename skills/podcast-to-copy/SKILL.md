---
name: podcast-to-copy
description: Use when turning a podcast, interview, webinar, talk, or long-form video transcript into a full repurposing package for a business, including podcast descriptions, titles, hooks, social posts, emails, sales-page angles, plus avatar and attractive-character updates. Extracts hooks, stories, parables, quotes, contrarian beliefs, enemies, epiphanies, proof, objections, product claims, and content pillars from the transcript.
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, podcast, repurposing, copywriting, content]
    related_skills: [avatar-builder, attractive-character-builder, hook-angle-writer, brand-voice-extractor, offer-builder, nurture-email-writer, launch-email-writer, funnel-page-writer, human-editor]
---

# Podcast to Copy Repurposer

## Overview

Turn one long-form recording into a structured repurposing package: a mined asset list plus finished copy plus updates to the business's living knowledge.

A single podcast, interview, webinar, keynote, or long video contains months of marketing material. The value is not in transcribing it. It is in mining the raw assets a marketer needs (hooks, stories, parables, quotes, contrarian beliefs, enemies, epiphanies, proof, objections, product claims, content pillars) and then converting those assets into finished copy and into durable updates for the avatar and the attractive character.

Use `references/repurposing-frameworks.md` for the extraction taxonomy and asset definitions. This file is the operating process for going from a transcript to a stored, client-ready package.

The core discipline: extract, never invent. Every hook, story, quote, and claim in the output must trace back to a specific place in the transcript. If the speaker said it, it is usable. If the speaker did not say it, it does not go in the package. Paraphrasing for polish is fine; fabricating stories, results, or claims is not.

## When to Use

Use this skill when the client asks for:

- repurposing a podcast episode, interview, webinar, talk, live stream, or long video into copy
- podcast or episode descriptions, show notes, and episode titles
- hooks, clips, or captions pulled from a recording
- social posts, threads, or emails built from an episode
- sales-page angles or proof pulled from what the speaker actually said
- mining a transcript to enrich an avatar or attractive character
- building a content backlog from a founder or expert's own words

Do not use this skill for:

- building the avatar from scratch (use `avatar-builder`)
- building the attractive character from scratch (use `attractive-character-builder`, this skill feeds it)
- structuring the offer (use `offer-builder`)
- writing a full launch or nurture sequence (use `launch-email-writer` or `nurture-email-writer`, this skill supplies the raw material)
- final polish (use `human-editor`)
- inventing stories, results, claims, or quotes the speaker did not actually say

## Multi-Business Rule

A client can run several businesses or brands, and each has its own podcast, avatars, characters, and voice. Repurposed content is only useful when it is filed against the right business, so it must never be blended across businesses.

Before extracting, confirm:

- which business or brand the recording belongs to
- who is speaking (founder, expert, guest, customer) and which attractive character they map to
- which avatar the content should speak to
- which offer, if any, the content should point toward

Always link the package back to the raw transcript so any claim can be verified later.

Recommended per-business path inside the client wiki:

```text
businesses/<business-slug>/
├── brand.md
├── products.md
├── offers/
├── avatars/
│   └── <avatar-slug>.md
├── characters/
│   └── <character-slug>.md
├── podcast-transcripts/
│   └── <episode-slug>.md        (raw transcript, or a link to it)
└── content/
    └── <episode-slug>-repurposing.md   (the extracted package)
```

If the recording's raw transcript is large or lives elsewhere, store it (or a link to it) under `podcast-transcripts/` and reference that path from the package so the mined assets stay traceable. If the client wiki already uses a different structure, follow it and keep every package grouped by business and linked to its source transcript.

## Required Inputs

Minimum useful inputs:

- the business or brand
- the transcript, recording, or accurate notes
- who is speaking
- the target avatar or at least the dream customer

Best inputs:

- a clean, timestamped transcript
- a completed avatar profile
- an existing attractive character profile for the speaker
- the offer the content should support
- a brand voice guide
- the approved-claims list and any compliance constraints

## Core Workflow

### 1. Orient to the client wiki

If working inside a wiki, first read:

- `SCHEMA.md`
- `index.md`
- recent `log.md`
- the target business's brand, products, offers, avatars, characters, and any prior repurposing packages

Completion: you know the business, the speaker, the avatar, the offer, the voice, and where both the transcript and the package should live.

### 2. Confirm scope

Define before extracting:

- business or brand and slug
- speaker and mapped attractive character
- target avatar
- offer the content should point to, if any
- which outputs are needed (description, titles, hooks, social, emails, sales-page angles, avatar update, character update)
- channels and volume for each output

Completion: one business, one recording, one avatar, and a named output list are fixed.

### 3. Store and read the full transcript

Save the raw transcript (or a link to it) under `podcast-transcripts/<episode-slug>.md`. Read the entire transcript before extracting. Do not work from the first few minutes or from a summary. The strongest assets often appear mid-conversation.

Completion: the raw transcript is stored and linked, and it has been read in full.

### 4. Mine the eleven asset types

Work through the transcript once and pull every instance of these asset types into an extraction table, each with a location marker (timestamp or quote) so it is traceable. See `references/repurposing-frameworks.md` for the full definition of each type.

| Asset type | What to capture |
|---|---|
| Hooks | lines that stop attention, could open a clip, post, or subject line |
| Stories | narratives with a beginning, tension, and resolution |
| Parables | short illustrative stories that carry a lesson |
| Quotes | quotable, standalone lines in the speaker's own words |
| Contrarian beliefs | claims that push against conventional wisdom |
| Enemies | the villain, myth, system, or false belief the speaker stands against |
| Epiphanies | turning-point realizations and "the moment I understood" beats |
| Proof | results, numbers, case studies, credentials, demonstrations, named examples |
| Objections | doubts, worries, and pushbacks the speaker raises or answers |
| Product claims | specific statements about what a product or method does or delivers |
| Content pillars | recurring themes the speaker returns to across the recording |

Completion: every asset type has been scanned for, each captured asset has a location marker, and thin categories are noted as thin rather than padded.

### 5. Flag risky and unverified assets

As you mine, tag anything that needs review before it can be published:

- `Risk flag` for health, medical, income, earnings, financial, legal, or credential claims
- `Needs confirmation` for proof, numbers, or results stated loosely or without support
- `Client to provide` for a claim that needs documentation the client holds

Do not silently drop these. They may still be usable with a disclaimer or after verification, so keep them in the package and mark them clearly.

Completion: every health, income, financial, legal, and credential claim in the mined set is flagged, and shaky proof is marked.

### 6. Convert mined assets into finished copy

Turn the extracted assets into the requested outputs. Reuse the foundation skills rather than reinventing them: hand hooks and angles to the logic in `hook-angle-writer`, and pull the avatar, offer, and voice from the wiki as those skills do.

- **Podcast description:** a short and a long version. Lead with the strongest hook, state who it is for and what they will learn, weave in one proof point, and close with a soft call to action. No fabricated takeaways.
- **Episode titles:** 8 to 12 options mixing curiosity, benefit, and contrarian angles, drawn from the hooks and contrarian beliefs. Keep them honest to the content.
- **Hooks:** a batch tagged by desire, awareness level, and channel, following the `hook-angle-writer` process. Include spoken-style hooks for clips.
- **Social posts:** posts and short threads built from stories, parables, quotes, contrarian beliefs, and epiphanies, shaped per channel.
- **Emails:** 2 to 5 emails built from stories and epiphanies, each with one idea, one story, and one call to action, ready to feed `nurture-email-writer` or `launch-email-writer`.
- **Sales-page angles:** proof points, objection-handling lines, and contrarian belief framings mapped to sales-page sections (headline, mechanism, proof, objections), ready for `funnel-page-writer`.

Completion: each requested output exists, is built only from mined assets, and carries the risk flags from step 5 where relevant.

### 7. Produce avatar and attractive-character updates

The recording is also research. Convert what the speaker revealed into durable updates:

- **Avatar insights:** desires, pains, objections, and the exact words the audience or speaker used, formatted as suggested additions to the avatar profile. Route deep changes through `avatar-builder`.
- **Attractive-character updates:** new backstory beats, flaws, parables, polarity, enemies, core-message language, and signature phrases, formatted as suggested additions to the character profile. Route deep changes through `attractive-character-builder`.

Present these as proposed diffs to the existing profiles, not as silent rewrites, and keep source markers.

Completion: avatar insights and character updates are drafted as sourced, reviewable additions to the existing profiles.

### 8. Assemble the package

Use this output shape:

```markdown
# Repurposing Package: [Episode / Recording Title]

## Scope
- Business / brand:
- Business slug:
- Speaker / character:
- Target avatar:
- Offer pointed to:
- Raw transcript: [link to podcast-transcripts/<episode-slug>.md]
- Outputs requested:
- Confidence:

## Mined Assets
| # | Type | Asset | Location | Risk / status |
|---|---|---|---|---|

## Podcast Description
### Short
### Long

## Episode Titles
1.

## Hooks
| # | Hook | Desire | Awareness | Channel |
|---|---|---|---|---|

## Social Posts
- [post / thread, tagged by channel and source asset]

## Emails
- [email: one idea, one story, one CTA, source-marked]

## Sales-Page Angles
| Section | Angle / proof / objection line | Source | Risk |
|---|---|---|---|

## Avatar Insights (proposed additions)
- Desire / pain / objection / language: [text] (source: [location])

## Attractive-Character Updates (proposed additions)
- Backstory / flaw / parable / polarity / phrase: [text] (source: [location])

## Risk Flags and Needs Confirmation
- [health / income / financial / legal / credential claims and unverified proof]
```

Completion: the package presents every mined asset, every finished output, both profile updates, and a consolidated risk list, all traceable to the transcript.

### 9. Update the wiki when appropriate

If working inside an LLM wiki:

- confirm the raw transcript is stored or linked under `businesses/<business-slug>/podcast-transcripts/`
- save the package under `businesses/<business-slug>/content/<episode-slug>-repurposing.md`
- link the package to the transcript, avatar, character, and offer it draws from
- apply the avatar and character updates only after review, through the relevant skill
- update `index.md`
- append to `log.md`
- if QMD is configured, run `qmd update` so the package is searchable

Completion: the package is filed under the correct business, linked to its source transcript, and reusable by the email, funnel, and launch skills.

## Missing Information Handling

Do not invent missing material. Use these labels:

- `Unknown`: the transcript does not support the answer
- `Needs confirmation`: stated loosely or without support, must be verified
- `Client to provide`: requires documentation only the client holds
- `Risk flag`: health, income, financial, legal, or credential claim needing review

If no transcript exists, stop and request one. This skill extracts from real recordings and cannot manufacture a founder's stories or claims. If the avatar or character does not yet exist, deliver the mined assets and route profile creation to `avatar-builder` or `attractive-character-builder`.

## Quality Bar

A strong package has:

- every asset traceable to a location in the transcript
- all eleven asset types scanned, with thin categories noted honestly
- finished outputs built only from mined assets
- hooks tagged by desire, awareness, and channel
- descriptions and titles honest to the content, with no invented takeaways
- avatar and character updates drafted as sourced, reviewable additions
- health, income, financial, legal, and credential claims flagged
- the raw transcript stored or linked and referenced from the package
- correct storage under the client wiki business

A weak package has:

- invented stories, quotes, results, or takeaways
- clickbait titles the episode does not pay off
- untraceable claims with no location markers
- unflagged health or income claims
- profile rewrites made silently instead of proposed for review
- content blended across businesses or detached from its source transcript

## Common Pitfalls

1. **Inventing assets.** Every hook, story, quote, and claim must come from the transcript. Mark gaps, do not fill them. Completion: each asset has a location marker.
2. **Skimming the recording.** The best material is often mid-conversation. Completion: the full transcript was read.
3. **Losing traceability.** Without location markers, claims cannot be verified. Completion: every mined asset is sourced.
4. **Ignoring risk.** Health and income claims from a guest are still risky. Completion: they are flagged, not published blindly.
5. **Clickbait titles.** Titles must match what the speaker actually said. Completion: each title is honest to the content.
6. **Silent profile edits.** Avatar and character changes are proposed for review, not merged silently. Completion: updates are presented as diffs.
7. **Orphaned packages.** A package detached from its transcript cannot be verified. Completion: the transcript is stored or linked and referenced.
8. **Blending businesses.** Keep each package tied to one business. Completion: the package is filed under the correct business slug.

## Verification Checklist

- [ ] Client wiki orientation completed when a wiki is available
- [ ] Business, business slug, speaker, avatar, and offer confirmed
- [ ] Raw transcript stored or linked under `podcast-transcripts/` and read in full
- [ ] All eleven asset types scanned, each mined asset carrying a location marker
- [ ] Podcast description (short and long) built only from mined assets
- [ ] Episode titles are honest to the content
- [ ] Hooks tagged by desire, awareness, and channel
- [ ] Social posts and emails built from mined stories, quotes, and epiphanies
- [ ] Sales-page angles mapped to page sections with sources
- [ ] Avatar insights drafted as sourced, reviewable additions
- [ ] Attractive-character updates drafted as sourced, reviewable additions
- [ ] Health, income, financial, legal, and credential claims flagged
- [ ] Package stored under `businesses/<business-slug>/content/` and linked to its transcript
- [ ] Output follows the repurposing package shape
