---
name: ad-creative-brief-writer
description: Use when turning an offer + hook + avatar into a generation-ready creative brief for an image or video tool (Higgsfield, Nano Banana, OpenAI Images, local sd.cpp, or a human designer/editor). Produces a complete brief covering creative concept, format, aspect ratio by placement, visual concept, text overlay, caption, CTA, generation parameters, and testing tag. Covers Meta Feed, Reels, Stories, Marketplace, and cold-traffic to retargeting briefs.
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, meta-ads, ad-creative, creative-brief, image-generation, video-generation, paid-social, conversion, creative-testing]
    related_skills: [meta-creative-tester, ad-script-writer, vsl-writer, hook-angle-writer, offer-builder, avatar-builder, brand-voice-extractor]
---

# Ad Creative Brief Writer

## Overview

Write a generation-ready creative brief: the bridge between strategy (the offer, avatar, hook, and brand voice) and production (the image or video tool that will render the asset). A creative brief is not a script — that is `ad-script-writer` or `vsl-writer`. A creative brief is not a test plan — that is `meta-creative-tester`. A creative brief is the single document a generation tool — Higgsfield, Nano Banana, OpenAI Images, a local sd.cpp install, or a human designer/editor — can execute against without a second conversation.

The skill produces a complete brief covering: the creative concept (the one idea the asset must communicate), the format (static image, vertical video 9:16, horizontal video 16:9, square 1:1, carousel), the aspect ratio by placement, the visual concept (scene, hero shot, lifestyle, UGC style), the text overlay burned into the image, the caption / primary text, the CTA overlay, the generation parameters (model, style, mood, color, number of variants), and the testing tag (what this variant isolates).

The core discipline: a creative brief exists to make the asset work inside Meta's algorithm, not to look pretty in a deck. Under Meta's modern architecture (Andromeda / GEM), the creative does the targeting — the algorithm reads the image, parses the copy, transcribes the video, and matches the creative to the right audience in real time. A brief that is conceptually thin, format-mismatched, or overlay-illegible fails the scroll stop, fails the hold, and inflates CPA. A strong brief isolates one variable for testing, fits its placement, and can be handed to a machine or a human without re-explanation.

Use `references/creative-brief-frameworks.md` for the detailed framework reference (format/aspect-ratio matrix by placement, first-3-seconds patterns, text overlay rules and Meta policy, creative concept frameworks, provider-specific generation parameter guides). This file is the operating process.

## When to Use

Use this skill when the client asks for:

- a creative brief to feed an image generation tool (Higgsfield, Nano Banana / fal.ai, OpenAI Images, local sd.cpp, Midjourney, or similar)
- a creative brief to hand to a human designer, video editor, or UGC creator
- turning an existing offer + hook + avatar into a generation-ready visual brief
- planning a set of creative variants (3-5 briefs) that isolate one variable for testing — see `meta-creative-tester`
- a static image brief for a Meta Feed, Marketplace, or retargeting ad
- a vertical video brief (9:16) for Reels or Stories
- a carousel brief for multi-product or multi-feature storytelling
- a creative refresh brief when an existing winner is fatiguing

Do not use this skill for:

- the full campaign structure (objective, CBO vs ABO, retargeting setup) — use `meta-ads-manager`
- the script itself (hook, body, CTA spoken lines) — use `ad-script-writer` for ads under 60s and `vsl-writer` for long-form offer reveals
- the hook frameworks and angle ideation before the creative format is chosen — use `hook-angle-writer`
- the creative test plan (hypothesis, ad set structure, budget, kill/scale criteria) — use `meta-creative-tester`
- building the offer being advertised — use `offer-builder`
- avatar research — use `avatar-builder`
- brand voice extraction — use `brand-voice-extractor`
- the landing page or sales page the ad sends traffic to — use `funnel-writer`
- final copy polish after the brief is drafted — use `human-editor`
- inventing proof, testimonials, results, or claims the offer cannot support

The boundary with `ad-script-writer`: this skill produces the visual + overlay + generation-parameter brief; `ad-script-writer` produces the spoken script. They are complementary — a full video ad needs both. This skill does not write the spoken words.

## Multi-Business Rule

A client can run several businesses, and each business can have many creative briefs across many offers and placements. Never blend offer details, avatars, brand colors, or approved claims across businesses. Before writing, confirm the business, business slug, offer, avatar, and target placement.

Store creative briefs inside the client wiki under the correct business:

```text
businesses/<business-slug>/
├── brand.md
├── brand-voice.md
├── products.md
├── offers/
│   └── <offer-slug>.md
├── avatars/
│   └── <avatar-slug>.md
└── meta-ads/
    ├── creative-tests/
    │   └── <test-slug>.md
    └── creative-briefs/
        └── <brief-slug>.md
```

If the wiki uses another structure, follow it while keeping every brief grouped by business and linked to its offer, avatar, and (if applicable) the test it belongs to.

## Source Hierarchy

Orient from the client wiki first. Read `SCHEMA.md`, `index.md`, recent `log.md`, and the target business pages before claiming facts. Then prioritize:

1. The offer document: dream outcome, mechanism, price, objections — the creative must sell the offer, not itself.
2. The avatar profile: desires, pains, the exact words they use — the creative must speak to them in their language.
3. The hook bank from `hook-angle-writer`: the creative concept is the visual translation of a chosen hook.
4. The brand voice and visual identity: colors, mood, tone, signature phrases, the "ugly vs polished" posture the brand has chosen.
5. The destination page (landing page, VSL, product page): the creative's promise must match the destination (aesthetic, language, promise match). A broken message match is a primary cause of funnel drop-off.
6. Existing creative performance data: winners, losers, known hook rates, hold rates, fatigue signals — briefs that ignore what is already winning or losing are blind.
7. The conversion event and target CPA: the creative's job is to lower cost per conversion, not to win design awards.
8. Real proof and approved claims: testimonials, stats, results the creative can burn into an overlay.
9. Agent inference for visual structure, composition, and generation parameters only — never for facts, proof, prices, or claims.

Completion: the offer, avatar, hook, brand voice, destination, and real proof are known or marked unknown.

## Required Inputs

Minimum useful inputs:

- the business or brand
- the offer the creative promotes (dream outcome and mechanism at minimum)
- the target avatar and traffic temperature (cold, warm, hot)
- the target placement (Feed, Reels, Stories, Marketplace) — determines format and aspect ratio
- the hook or angle the creative must visualize (from `hook-angle-writer`, or a brief to develop one)
- the generation provider to brief for (Higgsfield, Nano Banana, OpenAI Images, local sd.cpp, or human designer/editor)
- the destination after the click (for message match)

Best inputs:

- a completed offer document from `offer-builder`
- a completed avatar profile and brand voice guide
- a hook bank from `hook-angle-writer`
- the landing page or product page the creative sends traffic to
- past creative performance data (CTR, hook rate, hold rate, CPA by creative, fatigue signals)
- the active creative test plan from `meta-creative-tester` (so the brief knows which variable it isolates)
- real testimonials, stats, and approved claims available for overlay
- the brand's visual assets (logo, product photos, brand colors, font)
- the campaign objective (click, registration, appointment, purchase) and target CPA
- the number of variants needed (3-5 for a typical test batch)

Completion: there is enough source material to brief a generation tool or designer without inventing proof, prices, or claims.

## Core Workflow

### 1. Orient to the wiki

If working inside a client wiki, read:

- `SCHEMA.md`, `index.md`, recent `log.md`
- the target business's brand, offer, avatar, character, voice, and any existing `meta-ads/` or `creative-briefs/`
- the destination page the creative will send traffic to (for message match)
- the active creative test plan, if one exists (so the brief knows its testing role)

Completion: the brief context, source assets, destination, and save path are known.

### 2. Define brief scope

Define before writing the visual concept:

- business and business slug
- offer and offer slug
- primary avatar
- traffic temperature and awareness level (unaware, problem-aware, solution-aware, product-aware)
- target placement(s) (Feed, Reels, Stories, Marketplace)
- the hook or angle the creative visualizes
- the campaign objective (what action the creative must earn)
- the generation provider (Higgsfield, Nano Banana, OpenAI Images, local sd.cpp, human)
- the destination after the click
- confidence level and source list

Completion: the brief is tied to one business, one offer, one avatar, one traffic temperature, one placement set, and one provider.

### 3. Define the creative concept (the single idea)

Every creative brief must express one idea the asset must communicate. Not a feature list, not a tagline — the single visual idea that earns the scroll stop and the click. The concept is the visual translation of the chosen hook.

Write the concept as a single sentence: "This creative shows [the avatar] that [the single promise] by [the visual proof]."

Choose the concept framework (see `references/creative-brief-frameworks.md` for detail):

- **Hero product shot** — the product as the focal point, benefits called out as overlays. Best for product-aware and warm traffic.
- **Lifestyle context** — the product in the avatar's real environment, showing the desired outcome in use. Best for problem-aware traffic.
- **UGC style** — raw, smartphone-authentic, "real person discovers" framing. Best for cold traffic and feeds where polished ads trigger ad-blindness.
- **Problem visualization** — show the pain vividly (the messy desk, the overflowing inbox, the before state) before the solution. Best for problem-aware traffic.
- **Transformation reveal** — the before-and-after split, the result made visible. Best for solution-aware traffic where proof drives the click.
- **Authority / proof stack** — testimonial screenshots, logos, stats burned in as the hero visual. Best for product-aware and retargeting traffic.

Completion: the concept framework is chosen and written as a single sentence.

### 4. Choose the format and aspect ratio

Match the format to the placement and the campaign objective. Never mix formats in one testing ad set — see `meta-creative-tester`.

| Format | Best for | Aspect ratio by placement |
|---|---|---|
| Static image | Retargeting, high-CPM periods, fast iteration, single benefit, warm traffic | Feed 4:5; Marketplace 1:1; Reels/Stories 9:16 (full-bleed) |
| Vertical video 9:16 | Cold traffic scroll-stop, Reels/Stories, UGC, demo | 9:16 (keep key content within 4:5 safe zone for Feed delivery) |
| Horizontal video 16:9 | YouTube, connected TV, in-stream, founder-led explainers | 16:9 |
| Square 1:1 | Feed fallback, Marketplace, low-budget multi-placement | 1:1 |
| Carousel | Multi-product, multi-feature, step-by-step story, catalog | 1:1 or 4:5 per card |

Aspect ratio rules (distilled from source):

- Producing only one ratio (e.g., square) restricts placement reach. Plan for the placement the creative will run in.
- For vertical video 9:16, keep all key content (face, text, product, CTA) within a 4:5 safe zone so it still works if delivered to the Feed.
- For static images, prefer 4:5 for Feed — it takes more screen real estate than 1:1 and outperforms on mobile.
- Reels and Stories demand 9:16 full-bleed; letterboxed 1:1 looks broken there.

Completion: the format and aspect ratio are fixed and justified by the placement.

### 5. Write the visual concept

Write the scene description the generation tool or designer will execute. For each brief, specify:

- **Scene:** the setting, the moment, the action captured. One scene per creative — do not stack.
- **Subject / hero:** the product, the person, or the transformation that is the focal point. Specify the product hero shot if applicable.
- **Composition:** framing (close-up, medium, wide), rule-of-thirds, where the eye should land first.
- **Mood and color:** the emotional register (calm, intense, aspirational, raw) and the palette (brand colors, contrast for scroll-stop, the "ugly vs polished" choice).
- **Texture and authenticity:** whether the creative should feel polished (studio) or raw (smartphone, shaky, grainy). Raw, "ugly" creatives frequently outperform polished ones on cold feeds because they read as native content, not ads.
- **Props and pattern interrupts:** the whiteboard-with-handwritten-math, the post-it note, the unexpected object close to the lens — the visual pattern interrupt that earns the first 3 seconds.

For video briefs, also specify the opening frame (the still frame before play) — on mobile feeds it is the first impression.

Completion: the scene, subject, composition, mood, and texture are specified such that a tool or designer can render the visual without guessing.

### 6. Write the text overlay

Text burned into the image or the first frame of a video. Rules (distilled from source and Meta policy):

- **Short.** The overlay is the hook compressed — aim for ≤20 characters for the headline. The full hook lives in the caption; the overlay is the scroll-stop.
- **Large, bold, readable on a muted mobile screen.** If a user cannot read it in 1 second on a phone, it fails.
- **Pose a question or make a bold claim** that arouses curiosity and earns the click to "See More."
- **Be hyper-specific, not generic.** "Are your ads not making money?" is dead. "Booked calls from ads, but they show up unqualified?" is alive. Use the avatar's exact pain language.
- **Meta text-in-image policy:** Meta's algorithm reads text overlays directly from the image file for targeting, and historically penalizes images with more than ~20% text coverage. Keep text minimal, high-contrast, and off the subject's face. Prefer text photographed in context (a post-it note, a letterboard, handwriting on a product) over digitally overlaid text — it reads as native and avoids the over-text penalty.
- **The "Scratch Out" test:** a strong creative must be unique to this brand. If you can scratch out the logo, write in a competitor's, and the creative still works, it is not a strong creative — rework it.

Completion: the overlay is written, ≤20 chars for the headline, hyper-specific, and compliant with Meta text policy.

### 7. Write the caption / primary text

The caption is the ad copy below or beside the visual. Rules:

- **The first line is ~90% of the ad's success.** It must stop the scroll on its own — many users read the first line before looking at the image.
- **No walls of text.** Short lines, clear spacing, bullet points where useful.
- **The 10-second scroll test:** a user should be able to scroll the caption and the visual for 10 seconds and instantly understand the value proposition, the pain, the credibility, and the offer.
- **Match the brand voice** from the wiki — tone, signature phrases, polarity.
- **Compliance:** all copy must be Meta-policy compliant to avoid ad rejection or account restrictions. Flag any income, health, financial, or credential claims for review.

Completion: the caption is written, leads with a scroll-stopping first line, passes the 10-second test, and is on-voice and compliant.

### 8. Write the CTA overlay and button

The CTA must match the campaign objective and traffic temperature:

- **Cold traffic:** indirect CTA — "See how," "Watch the breakdown," "Get the guide." Sell the click, not the offer.
- **Warm traffic:** registration or lead CTA — "Reserve your seat," "Book your call," "Get the free template."
- **Hot traffic / retargeting:** direct CTA — "Get [product] now," "Shop now," with clear pricing if the page confirms it.

Every CTA must answer three questions: what do I do, what happens next, and why now. Weak CTAs ("learn more," "click here") kill conversion.

For the visual CTA overlay, specify placement (bottom third, above the "See More" button on mobile) and wording.

Completion: the CTA is direct, specific, matched to the objective, and placed correctly on the visual.

### 9. For video briefs: write the first-3-seconds framework

For any video brief (9:16, 16:9, or 1:1 video), the first 3 seconds carry the entire ad. Specify all four synchronized elements (see `references/creative-brief-frameworks.md`):

1. **The text overlay hook** — the burned-in headline from Step 6.
2. **The sound hook** — the first audio beat (a provocative question, a sound effect, a music drop). Assume 67% of mobile traffic is muted; the sound hook rewards those who unmute but must not be required to understand the ad.
3. **The visual hook** — the opening frame and the first movement (a pattern interrupt: an unexpected object, a contrasting color, a sudden motion, a whiteboard reveal).
4. **The vibe** — the emotional register of the opening (urgent, conspiratorial, excited, deadpan).

Then specify the body beat (the payoff of the hook) and the CTA beat (the final 5-10 seconds). For a 60-90s video, allocate 3-5s to the hook, 5-10s to the CTA, and the remainder to the body.

Completion: the video brief specifies the four hook elements, the opening frame, the body beat, and the CTA beat.

### 10. Specify the generation parameters

Translate the creative concept into the parameters the provider needs. This is what makes the brief "generation-ready" rather than "a description." See `references/creative-brief-frameworks.md` for the provider-specific guides.

**Common parameters (all providers):**

- Model / preset (e.g., Higgsfield preset, Nano Banana model id, OpenAI image model, local sd.cpp checkpoint)
- Style (photorealistic, illustrated, UGC-raw, cinematic, minimal)
- Aspect ratio (from Step 4)
- Mood / lighting (from Step 5)
- Color palette (brand colors or contrast choice)
- Number of variants to generate (3-5 for a test batch; more for a concept exploration)
- Negative prompts / exclusions (what to avoid: text artifacts, extra fingers, watermark, distorted faces)
- Seed or reference image (if iterating a winner — see variant planning below)

**Provider notes (translate the brief per provider):**

- **Higgsfield (premium video):** specify the preset, the motion intensity, the camera move, and the first-frame reference. Best for high-production vertical video where motion and polish matter.
- **Nano Banana / fal.ai (quality at cost):** specify the model, the prompt, the aspect ratio, and the number of variants. Strong for concept exploration and static generation.
- **OpenAI Images (cheap, simple):** specify the prompt and the size (1024×1024, 1024×1792, 1792×1024). Best for fast, simple statics; weaker for fine text rendering — plan to add overlays in post.
- **Local sd.cpp (free):** specify the checkpoint / LoRA, the sampler, the steps, the CFG scale, and the dimensions. Best when the client wants full control, no API cost, and custom-trained models.
- **Human designer / editor:** specify the scene, the assets to source, the overlays to typeset, and the cut. A human can handle fine text and brand-perfect typography that AI tools cannot — use them when text legibility and brand precision are critical.

Completion: the generation parameters are specified for the chosen provider, including model, style, mood, color, variants, and provider-specific notes.

### 11. Add the testing tag

If the brief is part of a creative test (see `meta-creative-tester`), tag it with the single variable it isolates. One variable per brief — do not stack.

| Variable | What the brief isolates | Example tag |
|---|---|---|
| Hook | The first 3 seconds / first line / overlay | `TEST: hook — stalker-pain vs curiosity` |
| Format | Static vs video vs carousel | `TEST: format — 4:5 static vs 9:16 video` |
| Angle | The core pain point / desire | `TEST: angle — lead-quality vs show-rates` |
| Offer framing | How the offer is positioned | `TEST: offer — free-book vs application-call` |
| Length | 15s vs 30s vs 60s+ | `TEST: length — 15s vs 60s` |
| CTA | The call to action and framing | `TEST: CTA — indirect vs direct` |

For a test batch of 3-5 briefs, every brief in the batch differs only on the tagged variable. This is what makes the test interpretable — see `meta-creative-tester`.

Completion: every brief in a test batch carries a tag naming the single variable it isolates.

### 12. Plan the variant set (if briefing a batch)

When the client asks for a set of creative variants for testing, structure 3-5 briefs that isolate one variable (from Step 11). Rules:

- **Isolate one variable.** If testing hooks, every brief shares the same format, angle, offer framing, length, and CTA — only the hook changes.
- **3-5 briefs per batch.** Fewer than 3 tests nothing; more than 6 splits the testing budget too thin to reach 50 conversions each.
- **Never mix static and video in the same batch.** Meta's delivery algorithm treats formats differently; mixing ruins the test read.
- **Include a control.** If there is a known winner, one brief in the batch should be the control (the current winner) so the variants are measured against it.
- **Plan the 70/20/10.** Per Hormozi's iteration cycle: 70% slight variations of a winner, 20% decent variations (new hook, new setting), 10% brand-new concepts. Tag each brief with its role.

Completion: the batch is structured with one isolated variable, 3-5 briefs, a control if one exists, and each brief tagged with its iteration role.

### 13. Confirm message match to the destination

Map the creative to its destination. The creative and the landing page must match on three pillars:

- **Aesthetic match:** visual styling, color, design atmosphere.
- **Language match:** tone, terminology, key phrases.
- **Promise match:** the core hook and promised outcome in the creative is the primary focus of the page.

If the creative promises a specific quantifiable result, the landing page must lead with that exact outcome. Flag any disconnect — a broken message match is a primary cause of funnel drop-off.

Completion: the creative's hook, visual, and CTA are consistent with the destination page's promise, language, and aesthetic, or the gap is flagged.

### 14. Assemble the final brief document

Use this output shape:

```markdown
# Creative Brief: [Brief Name] for [Avatar]

## Scope
- Business:
- Business slug:
- Offer:
- Primary avatar:
- Traffic temperature: cold / warm / hot
- Awareness level: unaware / problem-aware / solution-aware / product-aware
- Placement(s): Feed / Reels / Stories / Marketplace
- Campaign objective: click / registration / appointment / purchase
- Generation provider: Higgsfield / Nano Banana / OpenAI Images / local sd.cpp / human
- Destination after click:
- Confidence:
- Sources used:

## Creative Concept
- Single idea (one sentence): This creative shows [avatar] that [promise] by [visual proof].
- Concept framework: hero product / lifestyle / UGC / problem visualization / transformation reveal / authority-proof stack
- Testing tag: TEST: [variable] — [this variant's value]

## Format and Aspect Ratio
- Format: static image / vertical video 9:16 / horizontal video 16:9 / square 1:1 / carousel
- Aspect ratio: (by placement)
- Safe zone: (for 9:16 video delivered to Feed — keep key content in 4:5)
- Rationale:

## Visual Concept
- Scene:
- Subject / hero shot:
- Composition:
- Mood and color:
- Texture (polished vs raw / UGC):
- Props / pattern interrupt:
- Opening frame (video only):

## Text Overlay
- Headline (≤20 chars):
- Supporting text (if any):
- Placement:
- Meta text-in-image compliance: confirmed

## Caption / Primary Text
- First line (the scroll-stop):
- Body:
- Brand voice check:

## CTA
- CTA text:
- CTA type: indirect (cold) / registration (warm) / direct (hot)
- Overlay placement:

## First 3 Seconds (video briefs only)
- Text overlay hook:
- Sound hook:
- Visual hook:
- Vibe:
- Body beat (the payoff):
- CTA beat (final 5-10s):

## Generation Parameters
- Provider:
- Model / preset:
- Style:
- Aspect ratio:
- Mood / lighting:
- Color palette:
- Number of variants:
- Negative prompts / exclusions:
- Seed / reference image (if iterating):

## Provider Notes
- [provider-specific translation — presets, model ids, sizes, checkpoints, or designer instructions]

## Message Match
- Destination page:
- Aesthetic match: confirmed / gap
- Language match: confirmed / gap
- Promise match: confirmed / gap

## Variant Set (if part of a batch)
- Batch variable:
- This brief's role: control / 70% slight / 20% decent / 10% new concept
- Other briefs in batch:

## Needs Confirmation
- [unverified claims, missing brand assets, unconfirmed destination page, missing performance baseline]
```

Completion: the document can be handed to a generation tool, designer, editor, or media buyer without reconstructing the strategy.

### 15. Update the wiki when appropriate

If working inside an LLM wiki:

- save the brief under `businesses/<business-slug>/meta-ads/creative-briefs/<brief-slug>.md`
- link it to the offer, avatar, brand voice, destination page, and (if applicable) the creative test it belongs to
- update `index.md` if appropriate
- append to `log.md`
- run `qmd update` if configured

Completion: the brief is filed under the correct business and reusable in later sessions.

## Missing Information Handling

Do not invent missing facts. Use these labels:

- `Unknown`: no source material supports the answer
- `Needs confirmation`: likely but not verified
- `Client to provide`: requires brand assets, product photos, approved claims, performance data, or destination page only the client can give
- `Risk flag`: an income, health, financial, legal, or credential claim in the overlay or caption needing review
- `Out of scope`: a format, claim, or visual the offer or brand cannot support

If the offer or avatar is missing entirely, stop and route to `offer-builder` or `avatar-builder` first. A creative brief written without a real offer and avatar is a pretty picture, not a conversion asset.

If the hook has not been chosen, stop and route to `hook-angle-writer` first — the creative concept is the visual translation of a hook; without a hook, there is no concept to brief.

If the destination page does not exist yet, flag the message-match risk and note what the page must deliver to pay off the creative's hook.

## Quality Bar

A strong creative brief has:

- one business, one offer, one avatar, one traffic temperature, one placement set, and one provider
- a creative concept expressed as a single sentence (avatar + promise + visual proof)
- a format and aspect ratio matched to the placement, with the safe zone specified for 9:16
- a visual concept a tool or designer can render without guessing (scene, subject, composition, mood, texture, props)
- a text overlay ≤20 chars, hyper-specific, readable on a muted phone, and Meta-text compliant
- a caption that leads with a scroll-stopping first line and passes the 10-second test
- a CTA matched to the campaign objective (indirect for cold, direct for hot)
- the four first-3-seconds elements specified for any video brief
- generation parameters specified for the chosen provider, including provider-specific notes
- a testing tag naming the single variable the brief isolates (if part of a test)
- message match confirmed between the creative and the destination page
- real proof or clearly flagged missing proof
- risky claims flagged
- a confidence level and source list

A weak creative brief has:

- a vague concept ("make it look premium") with no single idea
- a format mismatched to the placement (square for Reels, letterboxed 9:16)
- a text overlay that is too long, too generic, or over-covers the image
- a caption that is a wall of text with no scroll-stopping first line
- a CTA that does not answer what happens next
- no generation parameters — just a description a tool cannot execute
- multiple variables changed across the batch (uninterpretable test)
- a broken message match between the creative and the landing page
- invented testimonials, stats, or prices burned into the overlay
- no testing tag, so the media buyer cannot place it in a test

## Common Pitfalls

1. **Briefing a format without the placement.** A 1:1 static briefed for Reels will letterbox and look broken. Match the format to the placement first; everything else follows.
2. **Over-polishing cold-traffic creative.** Polished studio creative reads as an ad and triggers ad-blindness on cold feeds. Raw, smartphone-authentic, "ugly" creative frequently outperforms. Choose texture deliberately.
3. **Text overlays that are too long.** The overlay is the hook compressed, not the caption. ≤20 chars for the headline. If the user cannot read it in 1 second on a phone, it fails the scroll stop.
4. **Generic pain language.** "Are your ads not making money?" is dead. Use the avatar's exact, hyper-specific pain ("booked calls from ads, but they show up unqualified?"). Pull the language from the avatar profile, not from a template.
5. **Ignoring Meta's text-in-image behavior.** Meta reads text overlays for targeting and historically penalizes images with more than ~20% text. Prefer text photographed in context (post-it, letterboard, handwriting on product) over digitally overlaid text.
6. **No generation parameters.** A brief without model, style, mood, color, variants, and provider notes is a description, not a brief. The tool or designer will guess, and the output will miss.
7. **Mixing variables in a test batch.** If every brief in the batch changes the hook, the format, and the angle, the test is uninterpretable. One variable per batch.
8. **Missing the opening frame for video.** On mobile feeds, the still frame before play is the first impression. If the opening frame does not stop the scroll on its own, the video never plays.
9. **No message match to the destination.** A creative that promises one outcome and sends traffic to a page that leads with another wastes every click. Confirm aesthetic, language, and promise match.
10. **Inventing proof in the overlay.** Every stat, testimonial, and price burned into the visual must come from real source material. Flag missing proof; do not fabricate it.
11. **Briefing without a hook.** The creative concept is the visual translation of a chosen hook. If no hook is chosen, there is no concept to brief — route to `hook-angle-writer` first.
12. **Ignoring the 4:5 safe zone for 9:16 video.** Vertical video delivered to the Feed is often cropped to 4:5. Keep faces, text, product, and CTA inside the safe zone or they get cut off.

## Verification Checklist

- [ ] Business, offer, avatar, traffic temperature, placement, and provider confirmed
- [ ] Offer, avatar, hook, and voice pulled from the wiki, not invented
- [ ] Creative concept written as a single sentence (avatar + promise + visual proof)
- [ ] Concept framework chosen and justified
- [ ] Format and aspect ratio matched to the placement
- [ ] 4:5 safe zone specified for 9:16 video
- [ ] Visual concept complete (scene, subject, composition, mood, texture, props)
- [ ] Opening frame specified for video briefs
- [ ] Text overlay ≤20 chars, hyper-specific, readable, Meta-text compliant
- [ ] Caption leads with a scroll-stopping first line and passes the 10-second test
- [ ] CTA matched to the campaign objective (indirect for cold, direct for hot)
- [ ] CTA answers: what to do, what happens next, why now
- [ ] Four first-3-seconds elements specified (video briefs)
- [ ] Generation parameters specified for the chosen provider
- [ ] Provider notes translate the brief to the provider's inputs
- [ ] Testing tag names the single variable the brief isolates (if part of a test)
- [ ] Variant batch isolates one variable, 3-5 briefs, includes a control if one exists
- [ ] Message match confirmed between creative and destination page
- [ ] Proof is real or flagged as missing
- [ ] Risky claims (income, health, financial, legal) flagged
- [ ] Brand voice and visual identity respected
- [ ] Confidence level and source list included
- [ ] If wiki-backed, brief filed under `businesses/<business-slug>/meta-ads/creative-briefs/` and linked
- [ ] Final output follows the creative brief document shape
