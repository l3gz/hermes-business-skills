---
name: meta-static-ad
description: Use when generating static Meta ad images — text-focused, direct response ads for Feed, Marketplace, and Stories. Produces a complete image generation prompt for a specific visual style. Currently supports dark bold typography (Hormozi-style). More styles will be added as templates.
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, meta-ads, ad-creative, static-ad, image-generation, direct-response, creative-director]
    related_skills: [ad-creative-brief-writer, hook-angle-writer, offer-builder, meta-creative-tester, human-editor]
---

# Meta Static Ad

## Overview

Generate static Meta ad images that are pure typography or minimal-composition direct response ads. These are the simplest, fastest, cheapest ads to produce — no photoshoot, no stock photos, no complex compositing. Just bold text on a background, designed to stop the scroll and drive clicks.

This skill exists because most Meta ad creative can be produced as static text-focused images at near-zero cost, and they often outperform polished video on cold traffic for certain offers. The constraint is not production quality — it is copy quality and visual hierarchy. A great headline on a dark background beats a mediocre video every time.

The skill takes a headline, subheadline, and CTA as input and produces a complete image generation prompt ready for any image tool (OpenAI Images, Nano Banana, local sd.cpp, Midjourney, or a human designer). Each style template defines the exact visual rules: background color, typography, layout, spacing, tone.

## When to Use

Use this skill when the client needs:

- a static Meta ad for Feed, Marketplace, or Stories (1:1 or 4:5)
- a text-focused ad — the message IS the visual
- a fast, cheap creative batch for testing (5-10 variants in minutes)
- a direct response ad in the Hormozi / Alex Hormozi content style
- a retargeting ad with a single bold claim
- a lead gen ad with a simple CTA

Do not use this skill for:

- video ads — use `ad-creative-brief-writer` for video briefs and `ad-script-writer` for scripts
- ads that need product photos, lifestyle imagery, or UGC footage — use `ad-creative-brief-writer`
- carousel ads — use `ad-creative-brief-writer`
- the campaign structure or ad set setup — use `meta-ads-manager`
- the creative test plan — use `meta-creative-tester`
- writing the hook or offer — use `hook-angle-writer` and `offer-builder` first

## Available Style Templates

### 1. Dark Bold Typography (Hormozi-style)

**File:** `references/style-dark-bold-typography.md`

Near-black charcoal background. Large heavy white sans-serif typography centered on the frame. Main headline takes up most of the image. Smaller subheadline below. Small CTA at the bottom. Minimalist, high-contrast, aggressive, confident. Think Alex Hormozi content style.

**Best for:** B2B leads, appointment setting, high-ticket offers, bold claims, contrarian hooks.

### 2. Ad Visual Pro (Value Shock Offer)

**File:** `references/style-ad-visual-pro.md`

Realistic scene background with shallow depth of field, overlaid with hyper-realistic 3D text, a saturated urgency badge, bullet points, and a CTA button. Fuses premium magazine photography with high-converting landing page aesthetics. The hero is always a concrete value (money amount, discount, savings) that triggers value-shock / FOMO.

**Best for:** Home services, government rebates/subsidies, high-ticket offers with a concrete dollar value, local services with a clear savings angle.

**When NOT to use:** when the offer is emotional, not quantifiable. Use dark-bold-typography for lifestyle brands, coaching, and community offers.

**Example output:**
- Background: #1a1a1a solid
- Headline: "Leads Are Worthless. Booked Appointments Are Everything." (uppercase, bold, white, centered, ~60% of frame)
- Subheadline: "We don't get paid until you get booked." (smaller bold white, centered)
- CTA: "DM us APPOINTMENTS" (small clean white, bottom)

## Core Workflow

### 1. Gather inputs

Minimum required:

- **Headline** — the main bold claim or hook (the scroll-stop). ≤60 characters ideal for static.
- **Subheadline** — the supporting line that pays off the headline. ≤80 characters.
- **CTA** — the action you want them to take. ≤30 characters.
- **Style** — which template to use (currently: dark-bold-typography)

Best inputs:

- The offer document (from `offer-builder`) so the headline matches the actual promise
- The avatar profile so the language hits their exact pain
- The hook bank (from `hook-angle-writer`) so the headline is a proven hook, not a guess
- Brand voice guide so the tone is consistent
- Past creative performance data so you know what angles have already been tested

Completion: the three text elements are written and approved, and the style is chosen.

### 2. Load the style template

Read the chosen style template from `references/style-<style-name>.md`. The template defines:

- The exact background color (hex)
- The typography rules (font family, weight, case, size hierarchy)
- The layout rules (centering, spacing, proportions)
- The tone and mood
- What to exclude (no images, no gradients, no decorations)
- The generation-ready prompt structure

Completion: the visual rules are understood.

### 3. Write the generation prompt

Translate the headline, subheadline, CTA, and style rules into a single generation-ready prompt. The prompt must be:

- **Self-contained** — a tool or designer can execute it without asking a follow-up question
- **Specific** — exact hex colors, exact text, exact placement, exact font weight
- **Exclusion-rich** — explicitly state what NOT to include (no images, no illustrations, no gradients, no logos, no decorations)
- **Format-specified** — state the aspect ratio (1:1 for Feed, 9:16 for Stories, 4:5 for Feed optimized)

See the style template for the exact prompt structure.

Completion: the prompt is written and can be pasted directly into an image generation tool.

### 4. Specify generation parameters

For each provider, the key parameters:

- **OpenAI Images (DALL-E / gpt-image-1):** prompt + size (1024x1024 for 1:1, 1024x1792 for 9:16, 1792x1024 for 16:9). Plan to add text overlays in post if the tool renders text poorly — generate the background, then typeset the text in Canva/Figma/Photoshop.
- **Nano Banana / fal.ai:** prompt + aspect ratio + number of variants. Strong for concept exploration.
- **Local sd.cpp:** checkpoint + prompt + negative prompt + sampler + steps + CFG + dimensions. Use a model good at text rendering (SDXL with text-focused LoRA, or Flux).
- **Human designer:** the prompt IS the brief — hand them the style template + the three text elements and they typeset it in 5 minutes.

**Text rendering caveat:** most AI image tools struggle with exact text rendering. For client-facing ads, generate the background/texture with AI, then typeset the text in Canva or Figma for pixel-perfect typography. The skill produces both the AI prompt AND the typesetting spec so a designer can finish the job.

Completion: the generation parameters are specified for the chosen provider.

### 5. Save to the client wiki

Store the ad in the client wiki under the correct business:

```text
businesses/<business-slug>/meta-ads/static-ads/<ad-slug>.md
```

Each ad file contains:

- The headline, subheadline, CTA
- The style template used
- The generation prompt
- The generation parameters
- The testing tag (what this variant isolates)
- The date created
- A link to the offer and hook it is based on

Completion: the ad is saved and linked.

### 6. Produce variants for testing

For a creative test batch, produce 3-5 variants that each isolate ONE variable:

- **Headline variant:** same style, different headline (different hook angle)
- **Subheadline variant:** same headline, different payoff line
- **CTA variant:** same headline and subheadline, different CTA
- **Style variant:** same text, different visual style template (when more styles are available)

Tag each variant with what it isolates so `meta-creative-tester` can structure the test.

Completion: the variants are produced and tagged.

## Output Format

The skill produces a single markdown document with four sections:

```markdown
# Static Ad: <ad-slug>

## Copy
- Headline: <headline>
- Subheadline: <subheadline>
- CTA: <CTA>

## Style
<style name> — <one-line description>

## Generation Prompt
<the complete, paste-ready prompt>

## Generation Parameters
- Provider: <provider>
- Size: <dimensions>
- Variants: <count>
- Notes: <provider-specific notes>

## Testing Tag
<what this variant isolates>
```

## Multi-Business Rule

Same as `ad-creative-brief-writer`: never blend headlines, offers, claims, or brand colors across businesses. Confirm the business slug before writing.

## Pitfalls

- **Text rendering by AI tools is unreliable.** Most image generation models will misspell, kern poorly, or garble text. For client-facing ads, generate the background and typeset the text in Canva/Figma. The prompt should still specify the text so the AI attempts the layout, but expect to fix it in post.
- **Meta text-in-image policy.** Meta reads text from images. Keep text minimal and high-contrast. This style (bold text on solid background) is at the upper limit of text coverage — it works because it is deliberate and high-contrast, but avoid adding more text layers.
- **Headline length kills statics.** If the headline is too long, it shrinks to fit and becomes illegible on mobile. ≤60 characters for the headline, ≤80 for the subheadline. If the copy is longer, it belongs in the caption, not the image.
- **No proof in the image.** Do not put fake testimonials, made-up stats, or income claims in the image. The image carries the hook; proof lives in the caption and the landing page.
- **One idea per ad.** A static ad must communicate one thing in one second. If there are two ideas, make two ads. Do not compress multiple offers or angles into one image.
- **Font licensing.** If a human designer typesets the ad, ensure the font is licensed for commercial use. The style template suggests font families but the client must own the license.
