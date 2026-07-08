# Style: Dark Bold Typography (Hormozi-style)

## Visual Rules

### Background
- **Color:** Solid `#1a1a1a` (near-black dark charcoal)
- **No gradients, no textures, no patterns, no vignettes.** Flat solid color only.

### Typography
- **Font family:** Modern sans-serif (Inter, Helvetica Neue, Arial Black, or similar heavy grotesque)
- **Weight:** Black or Heavy (900 weight)
- **Case:** UPPERCASE for the headline. Subheadline and CTA can be title case or uppercase.
- **Color:** Pure white `#ffffff` for all text
- **Rendering:** Crisp, high-contrast, no glow, no shadow, no outline

### Layout (1:1 square)
- **Headline:** Centered horizontally. Vertically positioned in the upper-middle, taking up approximately 55-65% of the frame width. Font size large enough that the headline fills the space edge-to-edge with minimal margin (roughly 1/8 frame width margin on each side). Line height tight (1.0-1.1).
- **Subheadline:** Centered horizontally. Positioned directly below the headline with a gap of approximately 1/10 frame height. Font size roughly 40-50% of the headline size. Bold but not as heavy as the headline.
- **CTA:** Centered horizontally. Positioned in the bottom 10% of the frame. Font size roughly 25-30% of the headline size. Clean, readable, not as heavy as the subheadline.

### Tone
- Minimalist, aggressive, confident, direct
- No images, no illustrations, no icons, no logos, no decorations
- No gradients, no shadows, no effects
- Pure typography on dark background
- Think Alex Hormozi, Iman Gadzhi, direct response school

### Aspect Ratios
- **1:1 (1080x1080):** Default for Meta Feed, Marketplace. The primary format.
- **4:5 (1080x1350):** Feed optimized — takes more screen real estate on mobile. Add the extra height to the top/bottom margins, keep text proportions the same.
- **9:16 (1080x1920):** Stories and Reels. Stack vertically — headline upper third, subheadline middle, CTA lower third. Increase margin to account for Meta UI overlays (profile icon, CTA button) in the bottom 15%.

## Generation Prompt Template

Here is the paste-ready prompt. Replace `<HEADLINE>`, `<SUBHEADLINE>`, and `<CTA>` with the ad copy.

```
A bold direct response advertisement with a solid near-black dark charcoal background (#1a1a1a). Large, heavy white sans-serif typography centered on the image. The main headline reads: "<HEADLINE>" in a thick, uppercase, modern font taking up most of the frame. Below it in smaller but still bold white text: "<SUBHEADLINE>" At the bottom in smaller clean white text: "<CTA>" — Minimalist layout, no images, no illustrations, no gradients, no decorations. Pure typography on dark background. High contrast. Shot as a square 1:1 format social media ad. Professional, aggressive, confident tone. Think Alex Hormozi content style.
```

### Example (filled in)

```
A bold direct response advertisement with a solid near-black dark charcoal background (#1a1a1a). Large, heavy white sans-serif typography centered on the image. The main headline reads: "Leads Are Worthless. Booked Appointments Are Everything." in a thick, uppercase, modern font taking up most of the frame. Below it in smaller but still bold white text: "We don't get paid until you get booked." At the bottom in smaller clean white text: "DM us APPOINTMENTS" — Minimalist layout, no images, no illustrations, no gradients, no decorations. Pure typography on dark background. High contrast. Shot as a square 1:1 format social media ad. Professional, aggressive, confident tone. Think Alex Hormozi content style.
```

## Provider Notes

### OpenAI Images (gpt-image-1 / DALL-E 3)
- **Size:** 1024x1024 for 1:1, 1024x1792 for 9:16, 1792x1024 for 16:9
- **Text rendering:** gpt-image-1 is better at text than DALL-E 3 but still unreliable for long headlines. Expect to fix text in post.
- **Strategy:** Generate the background + approximate layout, then typeset the exact text in Canva/Figma/Photoshop using Inter Black or Helvetica Neue Black.
- **Prompt:** use the template above directly.

### Nano Banana / fal.ai
- **Aspect ratio:** pass `1:1` or `9:16` or `4:5`
- **Text rendering:** similar limitations to OpenAI. Generate the visual, typeset in post.
- **Variants:** generate 4-6 at once for a test batch.

### Local sd.cpp (SDXL / Flux)
- **Model:** Flux.1-dev or SDXL with a text-rendering LoRA. Flux handles text better than SDXL.
- **Negative prompt:** illustrations, images, photos, people, faces, gradients, textures, patterns, shadows, glow, 3d, render, watermark, logo, decoration, border, frame
- **Sampler:** DPM++ 2M Karras (SDXL) or Euler (Flux)
- **Steps:** 30-40
- **CFG:** 7-8 (SDXL), 3.5-4.5 (Flux)
- **Dimensions:** 1024x1024 (1:1), 832x1216 (4:5 portrait), 832x1216 → crop to 9:16
- **Strategy:** Flux can render short text (under 30 chars) reliably. For longer headlines, generate the background and typeset in post.

### Human Designer
- **Time:** 5-10 minutes per ad in Canva or Figma
- **Font:** Inter Black (free, Google Fonts) or Helvetica Neue Black (licensed)
- **Deliverable:** PNG 1080x1080 (1:1) and 1080x1350 (4:5)
- **Brief:** hand them this style template + the headline, subheadline, and CTA. They typeset it.
- **This is the most reliable path for pixel-perfect text.** Use when the ad is client-facing and text legibility is critical.

## Variant Ideas for This Style

To produce a test batch of 3-5 variants:

1. **Headline variant A:** Contrarian claim (e.g., "Leads Are Worthless. Booked Appointments Are Everything.")
2. **Headline variant B:** Pain-forward (e.g., "Your Ads Get Clicks. Your Sales Team Gets Voicemails.")
3. **Headline variant C:** Outcome-forward (e.g., "Booked Appointments. Not Leads. Not Clicks. Appointments.")
4. **CTA variant:** "DM us APPOINTMENTS" vs "Comment APPOINTMENTS" vs "Tap to book a call"
5. **Color variant (future style):** white background, black text (inverted) — tests contrast preference

Each variant isolates one variable (headline angle or CTA) so the test is clean.
