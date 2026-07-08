# Style: Ad Visual Pro (Value Shock Offer)

## Overview

A realistic scene background with shallow depth of field, overlaid with hyper-realistic 3D text, a saturated urgency badge, bullet points, and a CTA button. The visual style fuses premium magazine photography with high-converting landing page aesthetics. The hero of the image is always a concrete value (a money amount, a discount, a savings figure) that triggers an immediate value-shock / FOMO response.

This is the most complex static ad style: it requires a scene, a brand color system, multiple text layers, and a structured layout. Use it when the offer has a concrete, quantifiable value that must be the visual hero (government subsidies, discount amounts, savings figures, ROI numbers).

**Best for:** Home services, government rebates/subsidies, high-ticket offers with a concrete dollar value, local services with a clear savings angle.

**When NOT to use:** when the offer is emotional, not quantifiable (lifestyle brands, coaching, community). Use dark-bold-typography for those.

## Visual Rules

### Background
- **Scene:** a realistic interior or lifestyle scene relevant to the offer (living room, kitchen, office, etc.). Bright, warm, well-lit by natural daylight.
- **Depth of field:** shallow. The background is blurred (bokeh effect) to create a premium magazine look and push the text overlays forward.
- **No people, no faces, no outdoor elements** (unless the offer is outdoor-specific). Indoor only for home services.
- **No patriotic cliches** (flags, monuments) that distract from the financial offer.
- Three depth planes: the scene in the back, a subtle darkening veil in the middle, and the massive text elements in the absolute foreground.

### Brand Color System
- **Primary brand color:** deep, rich (e.g., forest green `#008A4E`, deep blue, or the client's brand color)
- **Accent / urgency color:** highly saturated golden yellow or orange (e.g., `#FFB300`) — used only for the urgency badge and key highlights
- **Text:** white for main text, brand color for the CTA button
- **Bottom bar:** clean white band for the CTA section

### Typography
- **Font family:** modern bold sans-serif (Montserrat, Poppins, Inter Black, or similar)
- **Weight:** Black or Extra Bold (800-900)
- **Color:** white for main text, brand green for the CTA button text
- **The money amount** is the largest element in the image — it takes up roughly one-third of the frame and must be the visual hero.

### Layout (1:1 square, 1080x1080)
- **Top-left:** main headline / hook. Left-aligned. Large, bold, white. The money amount dominates.
- **Right side:** large circular urgency badge in saturated golden yellow. Dominant, eye-catching, screams urgency.
- **Mid-left:** 3 short bullet points, benefit-oriented, left-aligned above the white bottom bar. Each bullet has a small icon (emoji-style).
- **Bottom:** clean white horizontal bar spanning the width. Contains the CTA button (rich brand green with white centered text) and a secondary subtitle line.

### Tone
- Premium, reassuring, magazine-quality scene
- Aggressive, high-converting landing page overlays
- Value-shock / FOMO — the prospect must feel a large sum of money is available and they'd be crazy to scroll past it
- Clear, direct, benefit-forward

### Aspect Ratios
- **1:1 (1080x1080):** Default for Meta Feed, Marketplace. The primary format.
- **4:5 (1080x1350):** Feed optimized — extend the top/bottom margins, keep proportions.
- **9:16 (1080x1920):** Stories and Reels — stack vertically: scene at top, badge middle, text and CTA bottom. Account for Meta UI overlays in the bottom 15%.

## Composition Blueprint

```
┌─────────────────────────────────┐
│ [HEADLINE - left aligned]       │
│ Up to $6,275 in subsidies       │
│ with zero paperwork.        ╭───╮│
│                            │BADGE││
│                            │$6275││
│                            ╰───╯│
│                                 │
│ • Subsidies: up to $6,275       │
│ • Check: free, 2 min, no commit │
│ • Limited spots remaining       │
├─────────────────────────────────┤
│ EcoAide Quebec. Certified.      │
│ ┌─────────────────────────────┐ │
│ │   CLAIM MY SUBSIDY NOW      │ │
│ └─────────────────────────────┘ │
└─────────────────────────────────┘
         (white bottom bar)
```

## Generation Prompt Template

Here is the paste-ready prompt. Replace the bracketed placeholders with the actual offer details.

```
Cinematic view of a [SCENE DESCRIPTION — e.g., bright, cozy living room interior], warm sunlight streaming through large windows, highlighting [PRODUCT/SERVICE VISUAL — e.g., a sleek heat pump unit subtly visible on the wall in the background]. The background is slightly blurred with a shallow depth of field to create a premium magazine look. The foreground is entirely dominated by hyper-realistic, ultra-bold graphic UI elements: massive 3D text numbers and a highly saturated, dominant [ACCENT COLOR — e.g., golden-yellow] circular badge that screams urgency. High-end advertising photography mixed with high-converting landing page aesthetics, perfectly balanced lighting, no people, no outdoor elements, indoor only.
```

### Example (filled in — heat pump subsidies)

```
Cinematic view of a bright, cozy Quebec living room interior, warm sunlight streaming through large windows, highlighting a modern minimalist decor with a sleek heat pump unit subtly visible on the wall in the background. The background is slightly blurred with a shallow depth of field to create a premium magazine look. The foreground is entirely dominated by hyper-realistic, ultra-bold graphic UI elements: massive 3D text numbers and a highly saturated, dominant golden-yellow circular badge that screams urgency. High-end advertising photography mixed with high-converting landing page aesthetics, perfectly balanced lighting, no people, no outdoor elements, indoor only.
```

## Text Overlay Spec (for typesetting in post)

AI image tools will NOT render the exact text correctly. Generate the background scene with AI, then typeset these elements in Canva/Figma/Photoshop:

### Headline (top-left, large, white, left-aligned)
```
Up to $6,275 in subsidies
with zero paperwork to handle.
```

### Subtitle (below headline, smaller white)
```
EcoAide Quebec. Certified installation. We handle everything.
```

### Urgency Badge (right side, circular, golden yellow #FFB300, large)
```
$6,275
CLAIM NOW
```

### Bullet Points (mid-left, white text, small icons)
```
💰 Subsidies: Up to $6,275 claimed for you
✅ Check: Free, no commitment, 2 minutes
⚡ Availability: Limited program — reduced spots
```

### CTA Bar (bottom, white background, green button)
```
Button (forest green #008A4E, white text, centered):
CLAIM MY SUBSIDY NOW
```

## What to Avoid

- **Hiding or minimizing the money amount.** It must be the visual hero. If it's small, the ad fails.
- **Patriotic cliches** (flags, monuments, national symbols) that distract from the financial offer.
- **Technical jargon** about how the product works. The ad sells the money saved, not the machinery.
- **Too many text layers.** Headline + badge + 3 bullets + CTA. That's the maximum. More kills legibility.
- **People or faces.** The scene is empty. People distract from the value overlay.
- **Outdoor shots** (unless the offer is outdoor-specific). Indoor lifestyle scene only.
- **Cluttered background.** The bokeh must be clean enough that text is readable against it.

## Variant Ideas for This Style

1. **Value variant:** different money amount (e.g., "$6,275" vs "$5,500" vs "up to $7,000") — tests which number drives more clicks
2. **Badge variant:** circular badge vs rectangular banner vs stamp-style — tests urgency visual format
3. **Scene variant:** living room vs kitchen vs basement — tests which scene resonates with the avatar
4. **CTA variant:** "CLAIM MY SUBSIDY NOW" vs "CHECK MY ELIGIBILITY" vs "GET MY FREE QUOTE" — tests directness
5. **Color variant:** green badge vs yellow badge vs red badge — tests urgency color

## Provider Notes

### OpenAI Images (gpt-image-1)
- Generate the background scene + approximate layout. Text will be garbled — typeset in post.
- **Size:** 1024x1024 for 1:1.

### Nano Banana / fal.ai
- Generate the scene with the badge and text positions roughly placed. Typeset exact text in post.
- Generate 4-6 variants for scene exploration.

### Local sd.cpp (SDXL / Flux)
- **Flux** is better at composing scene + text overlays than SDXL.
- Use a depth-of-field prompt: "shallow depth of field, bokeh, blurred background."
- Generate the scene, then composite text overlays in post with Canva/Figma.

### Human Designer
- **This is the recommended path for this style.** The multi-layer composition (scene + badge + bullets + CTA bar) is too complex for AI to render perfectly.
- **Workflow:** generate the background scene with AI (or use a stock photo), then typeset all text layers in Canva/Figma.
- **Time:** 15-30 minutes per ad.
- **Deliverable:** PNG 1080x1080, with editable Canva/Figma source.
