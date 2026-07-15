---
name: email-writer
description: Use when writing any marketing email — nurture, welcome, ongoing value, promotional, retention, or broadcast. Produces ready-to-send emails built on real copywriting patterns, not framework templates. Covers subject lines, preview text, body structure, sentence rhythm, and CTAs.
version: 2.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, email, copywriting, nurture, broadcast, retention, promotion]
    related_skills: [avatar-builder, attractive-character-builder, offer-builder, brand-voice-extractor, hook-angle-writer, podcast-to-copy, human-editor]
---

# Email Writer

## Overview

Write marketing emails that earn the open, deliver one idea, and move the reader toward one action. This skill is built on observed real-world copy patterns from high-performing senders, not on named book frameworks or rigid sequence templates.

The discipline: **value per second, not seconds of value.** Less but better. One idea per email. Short paragraphs. Conversational tone. A soft, single-line call to action that puts the reader in control. No personalization tokens. No fake urgency. No framework jargon in the copy itself.

Use `references/email-patterns.md` for the full pattern library: subject-line bank, opening structures, content-type templates, CTA patterns, sentence-rhythm examples, and the principles behind why this style works. This file is the operating process; the reference is the field guide.

A strong email makes the reader think, "This is worth my time, I look forward to hearing from this person, and the next step feels obvious." It does not bury them in daily noise, recycle the same framework, or hard-sell in every message.

## When to Use

Use this skill when the client asks for:

- a welcome, indoctrination, or new-subscriber email after an opt-in
- a broadcast or one-off value email to the list
- an ongoing weekly value or daily email cadence
- a post-purchase onboarding email that drives activation
- a retention, re-engagement, or win-back email
- a promotional email or short sequence around a real event, deadline, or offer
- a lead-magnet follow-up that bridges to a paid offer
- a story-driven email that shifts a belief before an ask

Do not use this skill for:

- building the offer itself, use `offer-builder`
- avatar research from scratch, use `avatar-builder`
- the attractive character profile, use `attractive-character-builder`
- brand voice extraction, use `brand-voice-extractor`
- subject-line-only or hook-only batches as a standalone deliverable, use `hook-angle-writer`
- repurposing a podcast or video transcript into email raw material, use `podcast-to-copy` first, then write here
- final copy polish, use `human-editor`
- inventing stories, testimonials, results, or scarcity

## Multi-Business Rule

A client can run several businesses, and each business can have several email sequences and broadcasts. Never blend voice, stories, avatars, or offers across businesses. Before writing, confirm the business, business slug, target avatar, attractive character, offer being pointed toward, email type, and cadence.

Store email work inside the client wiki under the correct business:

```text
businesses/<business-slug>/
├── brand.md
├── products.md
├── avatars/
├── characters/
├── offers/
└── emails/
    ├── broadcasts/
    │   └── <email-slug>.md
    └── sequences/
        └── <sequence-slug>.md
```

If the wiki uses a different structure, follow it while keeping every email grouped by business. Link each email to the relevant avatar, character, offer, and voice pages.

## Source Hierarchy

Orient from the client wiki first. Read `SCHEMA.md`, `index.md`, recent `log.md`, and the target business pages before writing. Then prioritize:

1. Direct client facts: real stories, real results, product details, onboarding steps, activation events, support and churn insight, and approved claims.
2. Avatar pages: desires, pains, objections, awareness level, and the exact language the avatar uses.
3. Attractive character page: backstory, parables, flaws, polarizing beliefs, and character type.
4. Offer pages: the offer this email points toward, its mechanism, proof, and objections.
5. Brand voice page: common phrases, taboo phrases, tone, rhythm, enemy language, and CTA style.
6. Existing emails, sales pages, and content, only as background.
7. Agent inference for structure, sequencing, and wording only, never for facts, stories, proof, or scarcity.

Completion: the business, avatar, character, offer, voice, email type, and save path are known or marked unknown.

## Required Inputs

Minimum useful inputs:

- business or brand and target avatar
- email type: broadcast, welcome, ongoing value, onboarding, retention, win-back, or promotional
- the offer or next step the email should point toward
- at least one real story, moment, or proof point, or an explicit note that stories are missing

Best inputs:

- avatar profile, attractive character profile, offer document, and brand voice guide from the wiki
- real founder or customer stories, origin story, and turning points
- activation event and onboarding steps for post-purchase emails
- objections, FAQs, and reasons customers churn
- desired cadence, list temperature, and platform constraints

Completion: there is enough source material to write the email without inventing stories, proof, or scarcity.

## Core Philosophy

These principles govern every email this skill produces. They come from the real copy corpus and the underlying retention science.

### Value per second, not seconds of value

Every word earns its place. Short is better than long when the content is dense. A 200-word email with one sharp idea beats a 1,000-word email that buries three ideas under filler. **Overwhelm is the number-one reason readers disengage and unsubscribe.** Less but better.

### One idea per email

One lesson. One story. One reframe. One call to action. If you have three things to say, write three emails. Sequencing ideas across days is stronger than cramming them into one message.

### Earn the open with the subject, not with personalization

The subject line and the first sentence do the heavy lifting. Do not rely on the recipient's first name. Do not use "Hey [Name]," personalization tokens. The best senders earn opens through curiosity, specificity, and a bold or contrarian angle, not through fake familiarity.

### The first sentence is the preview

There is no separate preheader text. The first sentence of the body is what shows in the inbox preview pane, and it is written to work there and as the email's opening line. One sentence, one line, designed to pull the reader in.

### Soft CTAs beat hard sells

The call to action is a single line at the end of the email. It frames the next step as the reader's choice: "see if you qualify," "see if it's a fit," "watch the video here." It never says "BUY NOW" or "CLICK HERE TO PURCHASE." Qualification framing puts the reader in control and creates productive tension.

### Honest urgency only

If there is a real deadline, state it plainly. If there is not, use cost-of-delay framing — what the reader loses by waiting — rather than inventing a fake countdown. A launch or promotion built on fake urgency wins one conversion and loses the list.

### Conversational, not corporate

Write like one person talking to another. Short sentences. Plain words. Specific detail from real source material. No jargon, no framework names, no "as discussed in our previous communication." If it would not come out of the sender's mouth in a real conversation, it does not go in the email.

## Core Workflow

### 1. Define the email scope

Capture business, business slug, email type, target avatar, attractive character, offer or next step, list temperature (cold, warm, hot), cadence (if part of a sequence), and confidence.

Match type to goal:

- **Broadcast:** a one-off value email. One idea, one lesson, one soft CTA.
- **Welcome:** introduce the character, set expectations, shift one core belief for new subscribers.
- **Ongoing value:** a repeatable weekly rhythm. Story or observation, one lesson, one soft CTA.
- **Onboarding:** drive a new buyer to the activation point and first win.
- **Retention / win-back:** reduce churn, re-engage quiet subscribers, or recover lapsed customers.
- **Promotional:** a short sequence around a real event, deadline, or offer. Honest urgency, qualification-framed CTA.

Completion: the email is tied to one business, one avatar, one character, one offer or next step, and one type.

### 2. Pull the four foundations from the wiki

Before writing, gather:

- **Avatar:** top desires, pains, objections, awareness level, and real language.
- **Attractive character:** character type, backstory, parables, flaws, and polarizing beliefs.
- **Offer:** the mechanism, proof, and objections the email must set up.
- **Voice:** phrases to use, phrases to avoid, tone, rhythm, and CTA style.

If any foundation is missing, mark it and either request it or draft with clearly labeled placeholders. Do not invent an avatar, character, or offer to fill the gap.

Completion: each of the four foundations is loaded from the wiki or explicitly marked as missing.

### 3. Choose the content type

Select one of the six content types from the pattern library. The type drives the structure:

- **Contrarian lesson:** "Most people do X. Here's why Y wins." Opens with a common belief, reframes it, delivers the lesson.
- **Numbered framework:** "Here are N ways/steps/things…" Opens with the premise, lists the items with one-line explanations, closes with the reframe or application.
- **Story or metaphor:** A real moment or portfolio-company story, then the principle it illustrates. The metaphor does the teaching.
- **Case study or proof:** A named person's result, then the lesson behind it. Specific and verifiable.
- **Direct promo:** "You want X? Here's how we help." Short, direct, qualification-framed CTA. Used sparingly.
- **Internal memo:** A longer, leadership-tone narrative addressed to "Team." Used for culture, belief, and retention content.

See `references/email-patterns.md` for the full template, opening beats, and real examples of each type.

Completion: one content type is chosen and the opening beat is planned before the body is written.

### 4. Draft the subject line and first sentence together

The subject and the first sentence work as a pair. The subject earns the open; the first sentence earns the read. Draft 2 to 3 subject options using the five subject-line patterns:

- **Numbered list:** `3 ways to get ignored`, `4 Step Process To Set Goals`
- **Question:** `Are you the bottleneck?`, `What is "the swamp?"`
- **Contrarian statement:** `Say no. Win bigger.`, `Worth Doing Badly`
- **Curiosity or intrigue:** `The #1 thing`, `Private video From Leila`
- **Series prefix:** `Mozi Minute: [topic]` — a brandable recurring column

Rules: 4 to 7 words. Sentence case or Title Case. No emoji. No ALL CAPS (except brand names). No personalization tokens. If subjects need a dedicated batch, hand off to `hook-angle-writer`.

Write the first sentence to function as both the preview text and the opening line. One sentence, one line, designed to pull the reader in.

Completion: each email has 2 to 3 subject options and a first sentence that doubles as the preview.

### 5. Write the body

Write in the attractive character's voice using the brand voice rules. Follow the rhythm of the real corpus:

- **Short paragraphs:** 1 to 2 sentences, then a line break. Lots of white space.
- **Mixed sentence lengths:** punchy one-liners (`Now flip it.`) between medium explanation sentences. Average 10 to 14 words per sentence. Roughly 30 to 45 percent of sentences are 8 words or fewer.
- **Bold section headers:** `Interesting Case Study:`, `Why Second-Best Problems Are Deadly:`, `Example:`, `How To Find Your #1 Thing:` — break the email into scannable blocks.
- **Conversational asides:** `Food for thought (pun intended).` — personality, not filler.
- **Questions to the reader:** `Ask yourself: "If we could only work on ONE thing…"` — pull the reader into the reasoning.
- **Directive transitions:** `Now flip it.`, `So if you aren't getting as many upsells as you want…` — move the reader from the story to the lesson to the action.
- **Target length:** 200 to 600 words for value emails. 150 to 300 words for direct promos. Longer is acceptable only when the content genuinely requires it (a detailed framework or memo).

Rules for every email:

- one primary goal and one primary call to action
- real stories only, drawn from the character or customer source
- proof and claims must be supported and traceable to the wiki
- match awareness level: teach more for colder readers, push less for hotter readers
- honest urgency only, or cost-of-delay framing when there is no real deadline
- flag any health, income, legal, financial, or credential claim for review

Completion: every email is on voice, single-goal, and free of invented facts.

### 6. Write the CTA

Write a single-line call to action at the end of the email. Use the soft qualification frame:

- `See if you qualify here.`
- `Tap here to see if it's a fit.`
- `Discover if you're a fit for our workshops here.`
- `Watch the video by tapping here.`

For ongoing-value emails, use the P.S. pattern:

- `PS - [teaser line] ([LINK])`

For direct promos with a real deadline, the CTA can be more direct but still single-line:

- `>> Book Your Call`
- `Try [product] free (24 hours only).`

Never use "BUY NOW," "CLICK HERE TO PURCHASE," or multi-line CTA blocks. One line, one link, reader's choice.

Completion: each email has one single-line CTA in the brand voice.

### 7. Sign off

Sign off with the sender's first name, casual. No title, no company line in the sign-off itself (the footer handles that).

- `- Alex`
- `- Matt`

If the brand voice calls for a different convention, follow the voice guide. Do not add a personalization token or a "Talk soon!" filler unless the voice guide explicitly calls for it.

Completion: the sign-off matches the brand voice and the attractive character.

### 8. Assemble the email document

Use this output shape:

```markdown
# Email: [Working title]

## Scope
- Business:
- Business slug:
- Email type: broadcast / welcome / ongoing value / onboarding / retention / win-back / promotional
- Content type: contrarian lesson / numbered framework / story or metaphor / case study / direct promo / internal memo
- Primary avatar:
- Attractive character:
- Offer or next step:
- List temperature: cold / warm / hot
- Cadence (if sequence):
- Confidence:
- Sources used:

## Foundations Pulled From Wiki
- Avatar page:
- Character page:
- Offer page:
- Voice page:
- Missing foundations:

## Subject Line Options
1.
2.
3.

## Preview Text (first sentence)

## Body
[Full email body, ready to paste into the ESP]

## CTA
- Primary CTA (single line):

## Claims Needing Review
- [unverified proof, risky claims, or offer details needing confirmation]
```

Completion: the document can be handed to editing or scheduling without reconstructing the strategy.

### 9. Update the wiki when appropriate

If working inside an LLM wiki, save the final email under `businesses/<business-slug>/emails/broadcasts/<email-slug>.md` or `businesses/<business-slug>/emails/sequences/<sequence-slug>.md`, link it to the avatar, character, offer, and voice pages, update `index.md` if appropriate, append to `log.md`, and run `qmd update` if the wiki uses QMD.

Completion: the email is filed under the correct business and reusable by other skills.

## Missing Information Handling

Do not invent missing facts. Use these labels:

- `Unknown`: no source material supports the answer
- `Needs confirmation`: likely but not verified
- `Client to provide`: requires a real story, proof, onboarding detail, or offer information
- `Risk flag`: health, income, legal, financial, credential, or regulated claim needing review
- `Out of scope`: a promise or claim the business cannot currently support

When source is thin, draft what can be supported and ask the highest-leverage questions in this order: avatar, offer, at least one real story, activation event for onboarding, proof, cadence, and brand voice.

## Quality Bar

A strong email has:

- one business, one avatar, one character, and one clear next step
- a subject line built on curiosity, specificity, or a contrarian angle, not on hype or personalization
- a first sentence that doubles as the preview text and pulls the reader in
- one content type, chosen before the body is written
- one goal and one primary call to action
- short paragraphs, mixed sentence lengths, and scannable bold headers
- real stories in the attractive character's voice
- a soft, single-line CTA that puts the reader in control
- honest urgency, or cost-of-delay framing when no deadline exists
- a casual first-name sign-off
- risky claims and unknowns flagged
- correct storage under the client wiki business when applicable
- a body length matched to the content type (200 to 600 words for value, 150 to 300 for promo)

A weak email has invented stories, unsupported proof, fake scarcity, hype subject lines, personalization tokens, several goals, a hard sell, multi-line CTA blocks, generic voice that ignores the character, framework jargon in the copy, or one email trying to serve several businesses or avatars at once.

## Common Pitfalls

1. **Writing the body before choosing the content type.** Pick the type and plan the opening beat first. Completion: the content type and opening are decided before any body.
2. **Inventing stories.** Every story must come from the character or customer source. Completion: each story traces to the wiki.
3. **Selling in every email.** Value emails earn the ask. Completion: the CTA is soft and single-line, not a hard sell.
4. **Using personalization tokens.** Earn the open with the subject and first line, not with the recipient's name. Completion: no personalization tokens appear in the email.
5. **Ignoring the character voice.** The email should sound like one real person. Completion: voice rules from the wiki are applied.
6. **Mismatching awareness level.** Cold readers need belief shifts; hot readers need less teaching. Completion: teaching depth matches temperature.
7. **Faking urgency.** Use real deadlines or cost-of-delay framing. Completion: urgency is documented or removed.
8. **Writing a separate preheader.** The first sentence is the preview. Completion: the first sentence works in the inbox preview pane.
9. **Overwhelming new buyers.** Onboarding should reduce overwhelm and drive one activation. Completion: onboarding points to a single next action.
10. **Ignoring regulated claims.** Health, income, legal, financial, and credential claims need review. Completion: risky claims are flagged.

## Verification Checklist

- [ ] Client wiki orientation completed when a wiki is available
- [ ] Business, business slug, avatar, character, and email type confirmed
- [ ] Avatar, character, offer, and voice foundations pulled or marked missing
- [ ] Content type chosen and opening beat planned before the body was written
- [ ] 2 to 3 subject line options drafted using the five patterns
- [ ] First sentence doubles as the preview text and pulls the reader in
- [ ] Body is on voice, single-goal, and follows the sentence-rhythm guidelines
- [ ] Body length matches the content type
- [ ] One single-line CTA, soft and qualification-framed (or P.S. pattern for value emails)
- [ ] Casual first-name sign-off
- [ ] Stories, proof, and claims trace to real source material
- [ ] Teaching depth matches the avatar's awareness level
- [ ] Urgency is honest or replaced with cost-of-delay framing
- [ ] No personalization tokens, no framework jargon, no multi-line CTA blocks
- [ ] Email stored or prepared for storage under `businesses/<business-slug>/emails/`
- [ ] Unknowns, risky claims, and compliance needs are flagged
- [ ] Final output follows the structured email document shape
