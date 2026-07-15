---
name: brand-voice-extractor
description: Use when you need a reusable brand voice guide and a clear one-liner for a business, extracted from real transcripts, pages, emails, and content. Produces an evidence-backed voice guide plus message clarity assets that other copy skills reuse.
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, brand, voice, messaging, copywriting, clarity]
    related_skills: [attractive-character-builder, avatar-builder, hook-angle-writer, funnel-page-writer, email-writer, human-editor]
---

# Brand Voice Extractor

## Overview

Turn a pile of real brand material into two reusable assets: a **brand voice guide** (how the brand sounds) and a **one-liner** (what the brand says and why it matters). Together they let every downstream copy skill write in a consistent, on-brand way without reinventing the voice each time.

This skill is based on the frameworks in `references/voice-frameworks.md`: the seven-part clarity framework (SB7), the one-liner, the voice extraction checklist, and plain-language writing rules. That reference is the detail; this file is the operating process.

Two disciplines run through the whole skill:

1. **Extract, do not invent.** Voice is captured from real source material (transcripts, emails, pages, posts, calls), not imagined. If there is no source, say so and gather it before claiming a voice exists.
2. **Clarity before style.** A distinctive voice on top of a confusing message just makes the confusion memorable. Get the message clear first, then capture how it should sound.

An attractive character (from `attractive-character-builder`) is the person doing the talking; the brand voice is the rules for how that talking sounds across all assets. When a character already exists, pull its voice section as a primary source. When it does not, this skill can still extract a voice from existing brand copy.

## When to Use

Use this skill when the client asks for:

- a brand voice guide, tone-of-voice document, or style guide
- a one-liner, tagline, elevator pitch, or clear "what we do" statement
- voice rules to keep multiple writers or AI drafts consistent
- extraction of how an existing brand or founder actually sounds from their content
- message clarity cleanup when the brand cannot explain itself simply

Do not use this skill for:

- inventing a personality or backstory (use `attractive-character-builder`)
- customer or avatar research (use `avatar-builder`)
- writing finished campaigns (use the hook, email, or funnel skills, which consume this output)
- a final line-editing pass on copy (use `human-editor`)

## Multi-Business Rule

A client can run several businesses or brands, and each has its own voice and one-liner. A single business can even carry more than one voice (for example a founder's personal brand versus the company brand).

When the request is "extract the brand voice," first confirm:

- which business or brand it is for
- which brand or character the voice belongs to (company voice, founder voice, product line)
- which avatar the voice speaks to, since tone is calibrated to the audience

Never blend voices across businesses. Store each voice guide inside that business's space in the client wiki, next to its brand, avatars, characters, and offers. The `llm-wiki-starter` layout is only the foundation; follow whatever structure the client wiki already uses.

Recommended per-business path inside the client wiki:

```text
businesses/<business-slug>/
├── brand.md
├── brand-voice.md        <- output of this skill
├── products.md
├── offers.md
├── avatars/
│   └── <avatar-slug>.md
└── characters/
    └── <character-slug>.md
```

If a business needs multiple distinct voices, store them as `brand-voice-<voice-slug>.md` and label each clearly.

## Source Hierarchy

Prioritize sources in this order:

1. The person or team speaking naturally: call recordings, interviews, voice notes, unscripted video.
2. Existing published content by the brand: podcasts, posts, emails, sales pages, talks.
3. An existing attractive-character profile's voice section.
4. Customer language from the avatar (words the audience uses and trusts).
5. Team descriptions of how the brand "should" sound.
6. Agent inference on tone and framing only, never on facts, claims, or invented phrases.

Rules:

- Signature phrases and sample lines must be real examples from the source, quoted accurately. Do not fabricate phrases the brand never said.
- Mark anything drafted from weak signal as `Needs confirmation`.
- Flag any claim inside the source that could be a legal or credibility risk (income, medical, legal, credentials) for client confirmation before it becomes part of the voice.

## Required Inputs

Minimum useful inputs:

- the business or brand this voice is for
- at least one real source of brand language (a transcript, a page, or a set of emails)
- the target avatar or at least a description of the dream customer

Best inputs:

- multiple transcripts or recordings of the person speaking unscripted
- existing high-performing brand copy
- the matching avatar and attractive-character profiles
- known enemies, values, and taboo words the brand refuses to use
- brand facts, products, offers, and approved claims

## Core Workflow

### 1. Orient to the client wiki

If working inside a wiki, first read:

- `SCHEMA.md`
- `index.md`
- recent `log.md`
- the target business's `brand.md`, avatars, characters, offers, and any existing `brand-voice.md`

Completion: you know the business, the avatar, any existing character or voice work, and where the new voice guide should live.

### 2. Confirm scope

Define before extracting:

- business or brand
- which voice this is (company, founder, product line)
- target avatar
- source list actually available
- whether a character profile exists to pull from

Completion: the voice is scoped to one brand context, for one business, speaking to one primary avatar, with a known source list.

### 3. Gather and read the source material

Collect the real material and read it in full, not in snippets. As you read, keep a running collection of raw quotes: strong lines, repeated phrases, distinctive word choices, and how the brand opens and closes.

Completion: you have read every available source end to end and have a raw quote bank to draw from. If there is no usable source, stop and request material rather than inventing a voice.

### 4. Nail the message with SB7 and the one-liner

Before capturing style, get the message clear. Using the clarity framework in the reference:

- identify the customer (hero) and their simple want
- name the problem on all three levels: external, internal, philosophical
- name the villain (the personified root cause)
- confirm the brand's guide role: empathy plus authority
- confirm the plan, the direct and transitional calls to action, the stakes of failure, and the picture of success

Then draft the **one-liner** in both builds from the reference:

- Problem + Solution + Result
- Character + Problem + Plan + Success

Completion: there is a clear three-level problem, a named villain, and at least one tested one-liner that leads with the customer's problem and states a single clear result.

### 5. Run the voice extraction checklist

Work through each item in the reference checklist, filling it with real examples from the quote bank:

- common phrases (real, verbatim)
- taboo phrases and words to avoid
- tone
- rhythm (sentence length and cadence)
- level of polish
- enemy language
- proof language
- CTA style

For each, write a short rule plus one or two real sample lines. Adjectives alone ("friendly, bold") are not enough; anchor every rule to evidence.

Completion: every checklist item has a concrete rule with at least one real example, or a `Needs confirmation` marker where the source was thin.

### 6. Apply the plain-language rules

Draft the guide's sample copy and the one-liner using the plain-language rules from the reference: simple reading level, active voice, present tense, short sentences, no redundant words, few adverbs, positive framing. These rules make the voice land; the character makes it distinctive. Keep both.

Completion: the sample lines and one-liner follow the plain-language rules and still sound like the brand.

### 7. Synthesize the brand voice guide

Produce a practical guide with this structure:

```markdown
# Brand Voice: [Business / Brand]

## Scope
- Business/brand:
- Voice type: (company / founder / product line)
- Target avatar:
- Confidence:
- Sources used:

## One-Liner
- Problem + Solution + Result:
- Character + Problem + Plan + Success:
- Where to use it:

## Core Message (SB7)
- Customer (hero) and their want:
- Problem - external:
- Problem - internal:
- Problem - philosophical:
- Villain:
- Guide - empathy line:
- Guide - authority / proof:
- Plan (steps):
- Direct CTA:
- Transitional CTA:
- Stakes of failure:
- Picture of success:

## Voice Rules
| Dimension | Rule | Real example |
|---|---|---|
| Common phrases | | |
| Taboo phrases | | |
| Tone | | |
| Rhythm | | |
| Level of polish | | |
| Enemy language | | |
| Proof language | | |
| CTA style | | |

## Do / Do Not
- Do:
- Do not:

## Sample Lines (on-voice)
- [3 to 5 lines that show the voice in action]

## Needs Confirmation
- [thin, unconfirmed, or risky items to verify with the client]
```

Completion: the guide is usable by the hook, email, and funnel skills, and every signature phrase is a real quote or flagged.

### 8. Save to the wiki

If working inside an LLM wiki:

- confirm the business the voice belongs to
- save raw sources under `raw/` (transcripts, exported copy)
- save the final guide at `businesses/<business-slug>/brand-voice.md` (or `brand-voice-<voice-slug>.md` if the business has several voices)
- link the voice to its brand, avatar, and any character
- update `index.md`
- append to `log.md`
- if QMD is configured for this wiki, run `qmd update` so the voice guide is searchable

Completion: the voice guide is filed under the correct business, linked to its brand and avatar, and reusable in later sessions.

## Missing Information Handling

If information is missing, do not invent voice. Use these labels:

- `Unknown`: not enough source material to judge
- `Needs confirmation`: drafted from weak or single-source signal, verify with the client
- `Client to provide`: needs real content the client must supply (recordings, past copy)
- `Risk flag`: an income, medical, legal, or credential claim in the source that needs verification before it enters the voice

When sources are thin, end the guide with the best 5 to 10 questions to ask the client, and request specific material (for example three recent emails and one podcast transcript) rather than guessing.

## Quality Bar

A strong brand voice guide has:

- a clear one-liner in both builds that leads with the customer's problem
- a complete SB7 message with all three problem levels and a named villain
- voice rules anchored to real, quoted examples
- an explicit do and do-not list with taboo phrases
- three to five on-voice sample lines
- a confidence level and source list
- flagged unconfirmed and risky claims
- output filed per business, not blended across brands

A weak brand voice guide has:

- vague adjectives ("professional yet friendly") with no examples
- invented phrases the brand never used
- a one-liner about company history instead of the customer's problem
- missing internal or philosophical problem
- no taboo list, so writers repeat off-brand language
- voice mixed across two businesses

## Common Pitfalls

1. **Inventing phrases.** Signature phrases must be real quotes from the source. If there is no source, gather it; do not fabricate a voice.
2. **Adjectives instead of evidence.** "Bold and warm" is useless without sample lines that prove it. Anchor every rule to a real example.
3. **Skipping clarity.** A memorable voice on a confusing message just makes confusion stick. Fix the SB7 message and one-liner first.
4. **A company-centric one-liner.** Leading with what the company is or does, instead of the customer's problem and result, fails the test.
5. **Ignoring taboo language.** Without a do-not list, downstream writers reintroduce off-brand words. Capture what the brand refuses to say.
6. **Blending businesses.** Keep one voice per brand context and store it under the correct business.
7. **Missing the internal problem.** Brands over-index on the external problem; the internal problem is usually why people actually buy.
8. **Passing risky claims through.** Income, health, and credential statements in the source need a risk flag before they become brand voice.

## Verification Checklist

- [ ] Business, voice type, and target avatar confirmed
- [ ] Real source material read in full, with a quote bank captured
- [ ] One-liner drafted in both builds, leading with the customer's problem
- [ ] SB7 message complete: three problem levels, named villain, guide empathy and authority, plan, both CTAs, stakes, success
- [ ] Voice extraction checklist filled with real examples for every dimension
- [ ] Plain-language rules applied to sample lines and one-liner
- [ ] Do and do-not list with taboo phrases included
- [ ] Three to five on-voice sample lines included
- [ ] Confidence level and source list recorded
- [ ] Unconfirmed and risky claims flagged
- [ ] If wiki-backed, guide saved at businesses/<business-slug>/brand-voice.md, linked to brand and avatar, with index and log updated
