---
name: attractive-character-builder
description: Use when building an attractive character (brand persona, founder story, spokesperson) for a business from real backstory, values, source material, and audience research. Produces an evidence-backed character profile for copy, content, email sequences, and brand voice.
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, attractive-character, brand, storytelling, copywriting]
    related_skills: [avatar-builder, brand-voice-extractor, podcast-to-copy, email-writer, human-editor]
---

# Attractive Character Builder

## Overview

Build an attractive character: the human face of a brand that a dream customer trusts, relates to, and follows. This is the character behind the copy, content, emails, and offers.

This skill is based on the full questionnaire in `references/attractive-character-profile-questionnaire.md`. The questionnaire is the detailed framework. This skill is the operating process for turning a real person's backstory and beliefs into a usable character profile.

The key discipline: the character must be true. Backstory, flaws, parables, and beliefs come from the real person or a defined persona, not from invented biography. Fabricated backstory destroys trust and creates legal and brand risk.

An attractive character pairs with an avatar. The avatar is who you sell to. The character is who does the selling. Build or reference the avatar first when possible.

## Multi-Business Rule

A client can run several businesses or brands, and a business can have more than one character.

When the request is "build an attractive character," first confirm:

- which business or brand it is for
- who the real person or persona is (founder, expert, customer, spokesperson, created mascot)
- which avatar this character speaks to

Never blend characters across businesses. Store each character inside that business's space in the client wiki, next to its avatars, brand, products, and offers. The `llm-wiki-starter` layout is only the foundation; each client wiki is adapted to their reality.

Recommended per-business path inside the client wiki:

```text
businesses/<business-slug>/
├── brand.md
├── products.md
├── offers.md
├── avatars/
│   └── <avatar-slug>.md
└── characters/
    ├── <character-slug>.md
    └── ...
```

If the client wiki already uses a different structure, follow it and keep characters grouped by business.

## When to Use

Use this skill when the client asks for:

- an attractive character, brand persona, founder story, or spokesperson identity
- a backstory or origin story for marketing
- brand voice and personality tied to a person
- content pillars, email soap opera sequences, or story banks
- polarity and positioning ("what we stand for and against")
- the human layer behind avatars, offers, and copy

Do not use this skill for:

- pure product feature writing
- avatar or customer research (use `avatar-builder`)
- brand voice extraction from existing copy only (use `brand-voice-extractor`)
- inventing a fake persona with fabricated life events

## Source Hierarchy

Prioritize sources in this order:

1. Direct input from the real person: interviews, calls, voice notes, questionnaire answers, personal stories.
2. Existing content by the person: podcasts, videos, posts, emails, talks, books.
3. Third-party accounts: testimonials about the person, press, partner descriptions.
4. Audience research: what the dream customer trusts and distrusts (from the avatar).
5. Team or founder assumptions.
6. Agent inference on tone and framing only, never on biographical facts.

Rules:

- Biographical facts (backstory, results, credentials, parables) must come from the real person or provided source. Never invent them.
- Mark anything unconfirmed as `Needs confirmation`.
- Agent inference is allowed for wording, tone, and content angles, not for life events or claims.
- Flag any claim that could be a legal or credibility risk (income claims, medical claims, credentials) for client confirmation.

## Required Inputs

Minimum useful inputs:

- the business, brand, or offer
- who the character is (real person or defined persona)
- the target avatar or at least the dream customer
- at least one source of real backstory or beliefs

Best inputs:

- completed or partial questionnaire answers
- interview or call transcripts with the person
- existing content: podcasts, posts, emails, talks
- the matching customer avatar
- brand facts, products, offers, and approved claims
- known enemies, values, and polarizing beliefs

## Core Workflow

### 1. Orient to the client wiki

If working inside a wiki, first read:

- `SCHEMA.md`
- `index.md`
- recent `log.md`
- the target business's brand, products, offers, avatars, and any existing character pages

Completion: you know the business, the avatar, existing character work, and where the new profile should live.

### 2. Confirm scope

Define before building:

- character name and who they really are
- business or brand
- target avatar
- source list
- character source type: founder, CEO, expert, customer, spokesperson, or created persona

Completion: the character is one real person or one defined persona, for one business, speaking to one primary avatar.

### 3. Choose the identity type

Select the identity that is both authentic and trusted by the avatar:

- **Leader**: already achieved the result, guides others.
- **Adventurer / Crusader**: on the journey, testing and reporting back.
- **Reporter / Evangelist**: researching and documenting, sharing findings.
- **Reluctant Hero**: did not seek the spotlight, shares because the discovery is too useful to keep quiet.

Completion: one primary identity chosen, with a one-sentence identity statement in the character's own framing.

### 4. Build the evidence table

Extract real material into these buckets before writing the profile:

| Bucket | What to capture |
|---|---|
| Backstory | start point, struggle, turning point, discovery, results |
| Flaws | real, relatable imperfections that build trust |
| Parables | short true stories with a lesson and what they support |
| Polarity | what they stand for, stand against, line in the sand |
| Core message | big idea, unique mechanism, secret, stop-doing, start-doing |
| Storylines | loss and redemption, before and after, discovery, secret, us vs them, testimonial |
| Voice | style, signature phrases, words to avoid, sample lines |
| Visual identity | wardrobe, settings, symbols, what to avoid |
| Enemy | the "them" in us vs them |

Completion: each bucket has real source material or a clear `Needs confirmation` marker. No invented biography.

### 5. Complete the questionnaire selectively

Use the full reference questionnaire for a deep build. For most deliverables, prioritize:

1. Business and audience foundation
2. Character source
3. Identity type
4. Backstory
5. Character flaws
6. Parables and story inventory
7. Polarity
8. Core message
9. Storyline bank
10. Voice and personality
11. Visual identity
12. Content strategy
13. Profile summary

Completion: the profile has enough depth to write on-voice content and email sequences without asking basic follow-up questions.

### 6. Synthesize the final character profile

Produce a practical profile with this structure:

```markdown
# Attractive Character: [Name]

## Scope
- Business/brand:
- Character source: (founder / expert / customer / spokesperson / persona)
- Target avatar:
- Confidence:
- Sources used:

## One-Sentence Character Profile
I am [name], the [identity] who helps [avatar] achieve [result] without [pain/sacrifice], because I discovered [big discovery] after [defining experience].

## Identity
- Primary identity type:
- Identity statement:
- Why the audience trusts this character:

## Backstory
- Where they started:
- The struggle:
- The turning point:
- The discovery:
- What changed / results:
- How it leads to the offer:

## Flaws
- Relatable flaw 1:
- Relatable flaw 2:
- Do-not-share list:

## Parables (true stories)
| Story | Lesson | Supports |
|---|---|---|

## Polarity
- Stands for:
- Stands against:
- Line in the sand:
- "Finally someone said it" belief:
- Not for people who / for people who:

## Core Message
- Big idea:
- Unique mechanism:
- Real cause of the problem:
- Real path to the result:
- Stop doing / start doing:
- Rallying cry:

## Storyline Bank
- Loss and redemption:
- Before and after:
- Amazing discovery:
- Secret telling:
- Us vs them:
- Third-person testimonial:

## Voice and Personality
- Style:
- Signature phrases:
- Words to avoid:
- Teacher / preacher / investigator / warrior / friend / guide:
- 3 sample lines:

## Visual Identity
- Wardrobe / settings / props:
- Symbols / recognizable cues:
- What to avoid visually:

## Content Strategy
- Weekly topics:
- Repeated stories:
- Reinforced beliefs:
- Attacked myths:
- Shown proof:
- Intro long-form story:
- 5-7 email soap opera outline:

## Needs Confirmation
- [unconfirmed facts, claims, or risky statements to verify with the client]
```

Completion: the profile is usable by content, email, funnel, and human-editor skills, and every biographical claim is either sourced or flagged.

### 7. Update the wiki when appropriate

If working inside an LLM wiki:

- Confirm the business the character belongs to
- Save raw sources under `raw/` (interviews, transcripts, questionnaire answers)
- Save the final character under that business's space, for example `businesses/<business-slug>/characters/<character-slug>.md`
- Link the character to its avatar, brand, products, and offers
- Update `index.md`
- Append to `log.md`
- If QMD is configured for this wiki, run `qmd update` so the character is searchable

Completion: the character is filed under the correct business, linked to its avatar, and reusable in later sessions.

### 8. Generate optional outputs

Only after the profile is complete, generate requested outputs:

- one-sentence character profile
- long-form intro story for new leads
- 5-7 email soap opera sequence
- weekly content pillars
- signature parables written out
- polarizing belief posts
- brand voice guide

Completion: outputs match the character's real voice, backstory, and polarity, not a generic guru template.

## Missing Information Handling

If information is missing, do not invent biography. Use these labels:

- `Unknown`: not enough source material
- `Needs confirmation`: drafted from weak signals, must be verified with the person
- `Client to provide`: requires a real story or fact only the person can give
- `Risk flag`: income, medical, legal, or credential claim needing verification

When the profile is thin, end with the best 5 to 10 questions to ask the real person, drawn from the reference questionnaire.

## Quality Bar

A strong attractive character has:

- a true, specific backstory
- a clear identity type
- relatable flaws
- real parables with lessons
- clear polarity and a named enemy
- a core message and unique mechanism
- a distinct voice with signature phrases
- content pillars and an email sequence outline
- confidence level and source list
- flagged unconfirmed or risky claims

A weak attractive character has:

- generic guru backstory
- invented or unverifiable life events
- no flaws or fake flaws
- no enemy or polarity
- vague voice
- claims that create legal or credibility risk
- no link to a specific avatar or business

## Common Pitfalls

1. **Inventing backstory.** Every life event, result, and credential must come from the person or source. Flag gaps, do not fill them.
2. **Building a character with no avatar.** The character exists to attract a specific avatar. Confirm or build the avatar first.
3. **Blending businesses.** Keep one character per business context; store under the correct business.
4. **No polarity.** A character who stands against nothing attracts no one. Find the real enemy and line in the sand.
5. **Fake flaws.** "I work too hard" is not a flaw. Use real, relatable imperfections that build trust.
6. **Ignoring risk.** Income, health, and credential claims need confirmation and sometimes disclaimers. Flag them.
7. **Generic voice.** Capture actual phrases the person uses and words they would never use.
8. **Skipping the story bank.** Parables and storylines are the raw material for months of content; do not stop at a summary.

## Verification Checklist

- [ ] Business and target avatar confirmed
- [ ] Character source type confirmed (real person or defined persona)
- [ ] Identity type chosen with a one-sentence statement
- [ ] Backstory is sourced, not invented
- [ ] Flaws are real and relatable, with a do-not-share list
- [ ] At least 3 parables with lessons and what they support
- [ ] Polarity, enemy, and line in the sand are defined
- [ ] Core message and unique mechanism are clear
- [ ] Voice includes signature phrases and words to avoid
- [ ] Content pillars and an email sequence outline are included
- [ ] Unconfirmed and risky claims are flagged
- [ ] If wiki-backed, character is filed under the correct business and linked to its avatar, with index and log updated
