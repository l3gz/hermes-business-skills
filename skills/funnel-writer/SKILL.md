---
name: funnel-writer
description: Use when writing or auditing funnel copy — single pages (landing, opt-in, sales, checkout, webinar, VSL pages) or full multi-page funnel builds (ad → opt-in → VSL → sales → checkout → thank-you). Handles both the page-level copy and the funnel-level orchestration (golden thread, message match, CTA escalation) so every step carries the same message and every transition is seamless. Copy only — not the HTML build.
version: 2.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, funnel, landing-page, sales-page, copywriting, conversion, message-match, orchestration]
    related_skills: [avatar-builder, attractive-character-builder, offer-builder, hook-angle-writer, brand-voice-extractor, vsl-writer, ad-script-writer, email-writer, human-editor]
---

# Funnel Writer

## Overview

Write funnel copy that moves one specific avatar toward one specific action — whether that is a single page or a full multi-page funnel. A funnel page is not a brochure. It is a focused sales asset with a job: opt in, buy, book, apply, register, watch, or continue to the next page. A full funnel is one continuous conversation where every page carries the same message and every transition is seamless.

This skill does both: it writes individual pages (landing, opt-in, sales, checkout, VSL wrapper, webinar registration, application, thank-you) and it plans the full funnel architecture when the client needs a connected multi-page build. When working on a full funnel, this skill defines the golden thread, maps the steps, writes each page, and enforces message match across every transition.

Use `references/funnel-frameworks.md` for the page frameworks, funnel archetypes, the message-match framework, the golden-thread principle, and the common funnel disconnects. This file is the operating process; the reference is the field guide.

This skill depends on other marketing skills. Use `avatar-builder` for customer depth, `offer-builder` for the offer, `hook-angle-writer` for headline options, `brand-voice-extractor` for voice, `vsl-writer` for VSL scripts, `ad-script-writer` for ad copy, `email-writer` for nurture sequences, and `human-editor` for the final pass.

The core discipline: **MESSAGE MATCH**. The hook that stops the scroll in the ad must be the same hook that opens the landing page, the same promise that drives the VSL, and the same offer the checkout confirms. A funnel that changes its message between steps loses the buyer. Every page is a continuation of the one before it, never a reset. And at the page level: clarity before cleverness. Every page should quickly answer: What is this? Is it for me? Why should I care? Why should I believe it? What do I do next?

## When to Use

Use this skill when the client asks for:

**Single pages:**
- landing page copy
- opt-in page copy
- lead magnet page copy
- sales page copy
- webinar registration page
- VSL page (the wrapper, not the script — use `vsl-writer` for the script)
- checkout page copy
- application page copy
- booking / calendar page copy
- thank-you / delivery page copy
- page audit or wireframe
- StoryBrand-style page rewrite

**Full funnel builds:**
- a full funnel copy build across multiple pages (ad → opt-in → VSL → sales → checkout → thank-you)
- funnel copy strategy or architecture planning before any page is written
- a message-match audit of an existing funnel (hook, offer, voice, CTA consistency)
- a funnel copy doc that connects every page into one continuous narrative
- mapping funnel steps, page jobs, and CTA escalation across the full buyer path

Do not use this skill for:

- the VSL script itself, use `vsl-writer`
- the ad script itself, use `ad-script-writer`
- building the offer itself, use `offer-builder`
- avatar research from scratch, use `avatar-builder`
- the attractive character profile, use `attractive-character-builder`
- brand voice extraction, use `brand-voice-extractor`
- nurture or follow-up email sequences, use `email-writer`
- final copy polish only, use `human-editor`
- the HTML build of the funnel pages — that is a separate, deferred skill (`funnel-html-builder`) that takes this copy output plus Matt's clean HTML templates
- legal, health, income, or compliance review

If offer, avatar, or CTA is unclear, stop and create or request those inputs first.

## Multi-Business Rule

A client can have several businesses and several funnels. Every page and every funnel belongs to one business, one offer, and one traffic source. Never blend funnel copy, offers, avatars, or voice across businesses.

Before writing, confirm:

- business or brand
- business slug
- offer
- primary avatar
- traffic source and traffic temperature: cold, warm, or hot
- scope: single page or full funnel
- if full funnel: funnel archetype and goal

Store funnel work inside the client wiki under the correct business:

```text
businesses/<business-slug>/
├── brand.md
├── brand-voice.md
├── avatars/
├── characters/
├── offers/
│   └── <offer-slug>.md
└── funnels/
    └── <funnel-slug>.md          ← master funnel copy doc (full builds)
    └── <funnel-slug>/
        ├── landing-page.md       ← individual page files (single-page or full builds)
        ├── opt-in-page.md
        ├── sales-page.md
        └── checkout-page.md
```

For a full funnel build, the master doc (`<funnel-slug>.md`) contains the golden thread, step map, message-match audit, and links to (or inline) every page. For a single page, the page file stands alone.

If the wiki uses another structure, follow it while keeping every funnel grouped by business and linked to its offer, avatar, character, and voice.

## Source Hierarchy

Orient from the client wiki first. Read `SCHEMA.md`, `index.md`, recent `log.md`, and the target business pages before claiming facts. Then prioritize:

1. The offer document: dream outcome, mechanism, stack, bonuses, guarantee, price, scarcity, and objections — from `offer-builder`.
2. The avatar profile: desires, pains, objections, false beliefs, failed attempts, and the exact words they use — from `avatar-builder`.
3. The brand voice guide and attractive character: tone, signature phrases, polarity, backstory — from `brand-voice-extractor` and `attractive-character-builder`.
4. The hook bank: the headline and hook options that will run through the funnel — from `hook-angle-writer`.
5. Existing assets: current ads, landing pages, VSLs, sales pages, checkout pages, and performance data.
6. Real proof: testimonials, case studies, results, demonstrations, and approved claims.
7. Agent inference for structure, sequencing, and continuity logic only — never for facts, proof, scarcity, or claims.

Completion: the offer, avatar, character, voice, hook bank, existing assets, and real proof are known or marked unknown. The funnel or page cannot be written honestly without a real offer and avatar.

## Required Inputs

Minimum useful inputs:

- the business or brand
- the offer the funnel or page sells (dream outcome and mechanism at minimum)
- the primary avatar
- the traffic source and traffic temperature: cold, warm, or hot
- the page type (single page) or funnel goal (full build: opt-in, registration, purchase, booking, application)
- at least a working hook or headline direction

Best inputs:

- a completed offer document from `offer-builder`
- a completed avatar profile
- a brand voice guide and attractive character profile
- a hook bank from `hook-angle-writer` (5-10 hook options)
- the traffic source and exact ad angles planned or live
- real testimonials, case studies, and approved claims
- known objections and false beliefs blocking the sale
- existing funnel pages, ads, or VSLs (for an audit or rebuild)
- the checkout platform and any constraints on the checkout copy
- the post-purchase path: thank-you page, onboarding, upsell, or nurture sequence
- funnel context: previous step and next step (for single-page work inside an existing funnel)

Completion: there is enough source material to write the page or plan the funnel without inventing the offer, the avatar, the hook, or the proof.

---

## Mode A: Single-Page Workflow

Use this mode when the client needs one page, not a full funnel build.

### A1. Define the page job

Classify the page:

- opt-in page
- lead magnet page
- webinar registration page
- sales page
- VSL page (wrapper)
- checkout page
- application page
- booking / calendar page
- thank-you / next-step page

Then define:

- one primary CTA
- traffic temperature
- awareness level
- main promise
- main objection
- proof available

Completion: the page has one job and one primary CTA.

### A2. Choose the page framework

Pick the simplest framework that can do the job. See `references/funnel-frameworks.md` for details.

Use **Marketing Made Simple wireframe** when the page is simple or service-based:

1. Header
2. Stakes
3. Value proposition
4. Guide
5. Plan
6. Explanatory section
7. Optional video
8. Optional price/product choices
9. Footer

Use **StoryBrand SB7** when the page needs clarity:

1. Customer hero
2. Problem
3. Guide
4. Plan
5. CTA
6. Failure
7. Success

Use **long-form sales page** when the buyer needs more persuasion:

1. Hook
2. Problem
3. Stakes
4. Mechanism
5. Guide/character
6. Offer stack
7. Proof
8. Objections
9. Price framing
10. Guarantee
11. Urgency
12. CTA
13. PS

Completion: the page structure matches traffic temperature and offer complexity.

### A3. Build the headline and hook

Use `hook-angle-writer` thinking:

- call out the avatar
- name the problem or desire
- promise a clear result
- hint at a mechanism
- avoid hype that the offer cannot support

Create 5 to 10 headline options before choosing one.

Completion: the header passes the grunt test: what it is, how it helps, what to do next.

### A4. Write the page sections

For each section, write:

- section goal
- headline/subhead
- body copy
- proof or source used
- CTA if relevant

Keep copy practical and scannable. Use tables, bullets, and short sections when useful.

Completion: every section moves the reader toward the CTA or answers a buying question.

### A5. Add proof and risk handling

Use only sourced proof.

Proof can include: testimonials, case studies, founder credibility, demonstrations, screenshots, process clarity, mechanism explanation, guarantees, comparison to alternatives, customer language.

Flag: health claims, income claims, legal/financial claims, credentials, guarantees, unsupported testimonials.

Completion: every major claim is sourced, softened, or flagged.

### A6. Address objections

Map objections to sections:

| Objection | Page element |
|---|---|
| I do not understand it | mechanism / plan |
| I do not believe it works | proof |
| It will not work for me | avatar-specific examples |
| Too expensive | value stack / cost of inaction |
| Too much work | effort reduction |
| Too risky | guarantee / risk reversal |
| Not now | cost of delay / real urgency |

Completion: the top objections are answered before the CTA.

### A7. Write the CTA path

For each CTA, define:

- action verb
- destination
- what happens after click
- risk reducer
- urgency or reason why, if real

Completion: a reader never has to wonder what to do next.

### A8. Assemble the page document

Use this output shape:

```markdown
# Funnel Page: [Page Name]

## Scope
- Business:
- Funnel:
- Page type:
- Primary avatar:
- Offer:
- Traffic source / temperature:
- Primary CTA:
- Sources used:
- Confidence:

## Page Strategy
- One job:
- Main promise:
- Main objection:
- Framework used:

## Headline Options
1.
2.
3.

## Recommended Header
- Headline:
- Subheadline:
- CTA:

## Page Copy
[section-by-section copy]

## Proof and Claims
| Claim | Source | Risk |
|---|---|---|

## Open Questions / Needs Confirmation
- [unknowns]
```

Completion: the page can be passed to design or pasted into a builder.

---

## Mode B: Full Funnel Workflow

Use this mode when the client needs a connected multi-page funnel build. This mode includes planning the architecture, defining the golden thread, writing each page, and enforcing message match across all transitions.

### B1. Define funnel scope

Capture before planning:

- business and business slug
- offer and offer slug
- primary avatar
- traffic source and traffic temperature
- funnel archetype (see Step B4)
- funnel goal and the one conversion event that defines success
- the post-conversion path
- confidence level and source list

Completion: the funnel is tied to one business, one offer, one avatar, one traffic temperature, and one archetype.

### B2. Pull the golden-thread inputs

The golden thread is the single promise, mechanism, and CTA that runs through every funnel step. Pull these before any page is planned:

- **The one promise:** the specific, quantifiable outcome the funnel delivers (from the offer doc).
- **The one mechanism:** the unique method or vehicle that makes the result achievable (from the offer doc).
- **The one hook:** the scroll-stopping idea that opens the ad and carries through every page (from the hook bank).
- **The one CTA arc:** how the ask escalates from the ad (click) through opt-in (email) through VSL (watch) to checkout (buy). Same destination, escalating commitment.
- **The one voice:** the brand voice and attractive character signature that every page shares.
- **The one proof path:** the testimonials and results that appear, sequenced from relatable to aspirational across the funnel.

If any of these is missing or weak, stop and route to the right skill (`offer-builder`, `avatar-builder`, `hook-angle-writer`, `brand-voice-extractor`) before planning the funnel.

Completion: the golden thread is defined in one paragraph and can be stated in a single sentence: "[Avatar] gets [promise] through [mechanism], and every step of this funnel says exactly that."

### B3. Choose the funnel archetype

Pick the archetype that matches the business model, offer, and traffic. See `references/funnel-frameworks.md` for the full step maps.

- **Opt-in funnel:** ad → opt-in page → thank-you/delivery → nurture sequence. Goal: capture the lead.
- **VSL funnel:** ad → VSL page → checkout → (optional) upsell → thank-you. Goal: direct purchase from a video presentation.
- **Webinar funnel:** ad → registration → confirmation/reminders → webinar → offer page → checkout. Goal: register, show up, buy.
- **Application funnel:** ad → application page → booking → sales call → (close). Goal: qualify and book a sales conversation.
- **Ecommerce funnel:** ad → product/landing page → cart → checkout → (optional) post-purchase upsell. Goal: direct purchase.

Hybrid funnels exist (e.g., application funnel with a VSL pre-frame, or ecommerce with an upsell VSL). Document the hybrid and its rationale.

Completion: the archetype and its step map are chosen and justified by the offer and traffic.

### B4. Map the funnel steps

For the chosen archetype, list every page and script in order. For each step, define:

- **Step name** (e.g., "Cold traffic ad," "Opt-in page," "VSL")
- **The page's one job** (what this step must achieve)
- **The primary CTA** (what the reader/viewer does next)
- **The traffic temperature arriving at this step** (cold, warm, hot)
- **The awareness level arriving at this step** (unaware, problem-aware, solution-aware, product-aware)
- **The hook variant** (how the golden-thread hook expresses at this step)
- **The proof used** (which testimonial or result appears here)

Completion: the full step map is documented in a table before any page copy is drafted.

### B5. Write the pages

For each page in the step map, run the single-page workflow (Mode A, steps A2 through A8). This skill writes every page. When a step requires a VSL script or an ad script, delegate to `vsl-writer` or `ad-script-writer` and pass the golden thread and step context.

The delegation map for scripts:

| Funnel step | Skill | Notes |
|---|---|---|
| Cold / warm / hot traffic ad | `ad-script-writer` | Pass the hook, the avatar, the traffic temperature, and the CTA (sell the click). |
| VSL script | `vsl-writer` | Pass the offer, avatar, hook, industry variant, and CTA destination. |
| Webinar script / deck script | `vsl-writer` (webinar variant) | Long-form; pass the three pillars and the offer reveal plan. |
| Nurture / follow-up email sequence | `email-writer` | Pass the golden thread, the offer, and the sequence goal. |

All page copy (opt-in, landing, VSL wrapper, sales page, webinar registration, application, booking, checkout, order bump, thank-you) is written by this skill using the page frameworks in the reference.

Completion: every page is written and every script is delegated.

### B6. Enforce message match across all pages

Once all pages are written, run the message-match enforcement pass. Every transition between steps must be seamless. Check the three pillars of message match at every handoff:

- **Promise match:** the outcome promised in the ad is the outcome delivered on the landing page, in the VSL, and confirmed at checkout. No new promises appear mid-funnel.
- **Language match:** the terminology, key phrases, and voice carry through every step. The avatar hears the same words from the brand at every touchpoint.
- **Aesthetic-direction match:** flag where the copy implies a visual or tone shift that would break continuity for the design team.

Run the message-match audit checklist (see `references/funnel-frameworks.md`):

1. **Hook continuity:** does the hook from the ad reappear as the headline on the landing page and the opening of the VSL?
2. **Offer consistency:** is the same offer, price, guarantee, and scarcity stated identically across the VSL, sales page, and checkout?
3. **Voice consistency:** does every page sound like the same brand and character?
4. **CTA escalation:** does the ask escalate logically (click → email → watch → buy) without a jarring jump?
5. **Proof sequencing:** is proof deployed in the right order (relatable early, aspirational late) without repeating or contradicting across steps?

Where a disconnect is found, fix it by aligning the downstream page to the golden thread — not by changing the golden thread to fit a page.

Completion: every step-to-step transition passes the three pillars and the five-point audit.

### B7. Assemble the connected funnel copy doc

Pull all page copy into one master funnel copy document. Use this output shape:

```markdown
# Funnel Copy: [Funnel Name]

## Scope
- Business:
- Business slug:
- Offer:
- Primary avatar:
- Traffic source / temperature:
- Funnel archetype:
- Funnel goal:
- Confidence:
- Sources used:

## The Golden Thread
- The one promise:
- The one mechanism:
- The one hook:
- The one CTA arc:
- The one voice:
- The one proof path:
- One-sentence thread: [Avatar] gets [promise] through [mechanism], and every step of this funnel says exactly that.

## Funnel Step Map
| Step | Page / asset | One job | Primary CTA | Traffic temp | Awareness | Hook variant | Proof |

## Message-Match Audit
| Check | Status | Notes |
|---|---|---|
| Hook continuity | Pass / Fix | |
| Offer consistency | Pass / Fix | |
| Voice consistency | Pass / Fix | |
| CTA escalation | Pass / Fix | |
| Proof sequencing | Pass / Fix | |

## Step Copy

### Step 1: [Ad / Cold traffic]
- Asset:
- Skill: ad-script-writer
- File: [link or inline]
- Hook variant:
- CTA:

### Step 2: [Landing / Opt-in]
- Asset:
- Skill: funnel-writer
- File: [link or inline]
- Headline:
- CTA:

### Step 3: [VSL]
- Asset:
- Skill: vsl-writer
- File: [link or inline]
- Opening hook:
- CTA:

(repeat for every step through thank-you)

## Disconnects Found and Fixed
- [each disconnect, the fix applied, and where]

## Open Questions / Needs Confirmation
- [unknowns, risky claims, missing inputs]
```

Completion: the funnel copy doc is a single source of truth that a builder, media buyer, or designer can work from without reconstructing the strategy.

### B8. Update the wiki when appropriate

If working inside an LLM wiki:

- save the funnel copy doc under `businesses/<business-slug>/funnels/<funnel-slug>.md`
- save individual page files under `businesses/<business-slug>/funnels/<funnel-slug>/`
- link to the offer, avatar, character, voice, and the individual page files
- update `index.md` if appropriate
- append to `log.md`
- run `qmd update` if configured

Completion: the funnel is filed under the correct business and reusable by later sessions and by the deferred `funnel-html-builder`.

---

## Missing Information Handling

Do not invent missing facts. Use these labels:

- `Missing offer`: no offer document exists — route to `offer-builder` first
- `Missing avatar`: no avatar profile exists — route to `avatar-builder` first
- `Missing hook bank`: no hook options exist — route to `hook-angle-writer` first
- `Missing voice`: no brand voice guide exists — route to `brand-voice-extractor` first
- `Missing proof`: no testimonials or results are sourced — flag every claim that needs proof
- `Missing traffic source`: the ad angles or traffic temperature are unknown — confirm before planning the hook variants
- `Missing CTA`
- `Needs confirmation`: likely but not verified
- `Risk flag`: income, health, financial, legal, credential, guarantee, or regulated claim needing review
- `Out of scope`: a promise or claim the business cannot currently support

A funnel or page cannot be written honestly without a real offer, a real avatar, and at least one real hook direction. If those are missing, stop and route to the foundation skills first.

## Quality Bar

A strong funnel page or full funnel build has:

- one business, one offer, one avatar, one traffic temperature
- a defined golden thread (for full builds: promise, mechanism, hook, CTA arc, voice, proof path)
- a complete step map where every page has one job and one CTA (for full builds)
- message match enforced across every step-to-step transition
- hook continuity from the ad opening through the checkout confirmation
- CTA escalation that moves logically from micro-commitment to purchase
- proof sequenced from relatable to aspirational without contradiction
- the same offer, price, guarantee, and scarcity stated identically wherever they appear
- one consistent brand voice across every page
- real proof or clearly flagged missing proof
- risky claims flagged
- a confidence level and source list
- a single assembled copy doc that downstream builders can work from (for full builds)

A weak funnel has pages written in isolation with no shared thread, a hook that changes between the ad and the landing page, an offer stated differently on the VSL and the checkout, a CTA that jumps from "learn more" to "buy now," proof that contradicts itself across steps, or no master document tying the funnel together.

## Common Pitfalls

1. **Writing page copy before defining the golden thread.** If the promise, mechanism, and hook are not fixed first, every page drifts. Completion: the golden thread is locked before any page is written.
2. **Letting each page reinvent the hook.** The ad hook, landing headline, and VSL opener must be the same idea expressed for the step. Completion: every hook variant traces back to the one hook.
3. **Breaking message match at the checkout.** The checkout is where trust is most fragile. If the offer, price, or guarantee reads differently here than on the VSL, buyers abandon. Completion: checkout copy is verified against the VSL and sales page word for word on offer terms.
4. **Jumping the CTA.** Going from "click to learn more" in the ad to "buy now for $997" on the landing page breaks the commitment arc. Completion: the CTA escalates one logical step at a time.
5. **Contradicting proof across steps.** A testimonial quoted one way on the sales page and another way on the checkout erodes credibility. Completion: proof is sourced once and quoted consistently.
6. **Treating the thank-you page as an afterthought.** It is the start of retention and the first upsell or nurture touch. Completion: the thank-you page has a job and a next step.
7. **Planning the funnel without the offer.** A funnel without a real offer is a template. Completion: the offer document exists or is requested first.
8. **Ignoring the traffic temperature shift.** Traffic arrives cold at the ad and is warm or hot by the checkout. The copy must match the awareness level at each step. Completion: each step's copy matches the arriving awareness level.
9. **Blending funnels across businesses or offers.** Never pull copy, proof, or voice from one business into another's funnel. Completion: every asset traces to one business and one offer.
10. **Confusing copy with build.** This skill produces copy and strategy. The HTML build is a separate, deferred skill. Completion: the handoff to the builder is explicit and the copy doc is build-ready.
11. **Writing before the offer is clear.** Use `offer-builder` first.
12. **Starting with the brand story.** The customer is the hero. The brand is the guide.
13. **Using vague CTAs.** Replace "learn more" with the actual action.
14. **Overwriting customer language.** Keep strong phrases from avatar research.
15. **Inventing proof.** If proof is missing, mark it.
16. **Faking urgency.** Use only real deadlines or cost-of-delay framing.
17. **Making every page long.** Simple offers need simple pages.
18. **Skipping mobile readability.** Use short sections, clear headers, and direct copy.

## Matt's Design Preferences (Growthsquare)

These preferences apply when building HTML landing pages for Growthsquare or GS clients:

### Landing page theme
- **Prefer WHITE/light backgrounds** with purple (#8457FF) accents — NOT dark by default. Matt explicitly asked "why not white" when every previous funnel was dark. Default to light unless the client/offer specifically calls for dark.
- **No gradient text effects.** Use flat purple `color: var(--purple)` for accent text, not `background-clip: text` gradients. Matt finds gradient text distracting and asked for its removal.
- **Comparison sections: use card-based layouts, not tables.** Tables "look really bad." Use "dueling cards" (two side-by-side cards with a VS badge in the middle) — loser card (muted, X icons) vs winner card (purple border, glow, scale 1.03, green checkmarks).

### Quebec French copy rules (QC market)
- **"ta business" not "ton business"** — the joual possessive. Same for "ta niche" not "ton niche".
- **"un sous" not "un cent"** — Quebec colloquial for "a penny/cent."
- **Contractions are natural:** "t'as pas" not "tu n'as pas", "c'est pas" not "ce n'est pas", "t'a l'option" not "tu as l'option."
- **Direct/informal "tu" always** — never "vous" in marketing copy for the QC SMB market. This applies to EVERY asset in a campaign, not just funnels: if you build ads (`meta-static-ad`), emails, or VSL scripts for the same client, run a consistency pass. A real audit (July 2026) caught 4 of 5 visual-pro ads using "Transformez vos..." / "Retrouvez..." while the funnels and dark-bold ads in the same campaign used "tu" — this voice break requires regenerating the ads. Before shipping a multi-asset campaign, grep all assets for `vous|vos|Transformez|Retrouvez|Comprendre.*vos` and flip any hit to the "tu" form.
- **Joual phrases land:** "de la marde" (bad quality), "poignes" (get stuck), "embarque" (get on board), "faire la job" (do the job).
- **Watch for anglicisms in QC copy and internal avatar docs.** QC clients flag these: "mindset" → "mentalité" / "état d'esprit", "badluck" → "imprévu", "feast or famine" → "cycle d'abondance-rareté", "fit" → "le bon choix". They creep into internal avatar docs and can percolate into client-facing copy. Run a grep sweep before delivery.

### Testimonials and social proof
- **Use REAL local sources** — Quebec forums (r/Quebec), real client names with companies. NOT generic Hacker News or IndieHackers quotes for a Quebec market page.
- **When reframing agency-service testimonials for a DIY product:** "If we did it for them, we can install the same system for you" — the testimonial proves capability, the offer transfers it to the buyer's ownership.
- **Video testimonials: use a GRID layout, NOT a carousel or fanned cards.** Matt explicitly rejected BOTH a simple auto-rotating carousel ("the carousel ish is terrible") AND the fanned stacked-card design from the FR funnels ("I don't want them in the carousel format. What I want is a grid layout, in rows and columns"). The preferred pattern is a **CSS grid**: 3 columns on desktop (9 videos = 3×3), 1 column on mobile (stacked, full-width). Each card is 16:9 aspect ratio with the video thumbnail, a purple play button overlay, and name+company overlaid at the bottom. Use `IntersectionObserver` with 200px rootMargin to lazy-load each video's metadata when it scrolls into view. Click a card to play/pause (pauses all others). No auto-rotate, no hover-to-focus, no fanned positioning — just a clean grid.
- **CRITICAL: name→video mapping must match the source funnel's index order EXACTLY.** When porting a video testimonial section from one funnel to another, the JS testimonials array order (index 0, 1, 2...) must match the video `<source data-src>` order in the HTML. If you copy the video elements in one order but write the JS array in a different order, every name will display on the wrong person's video. The FR funnel uses a specific order (index 0=Colo, 1=Audrey, 2=Jean-Philippe, 3=Danik, 4=Karine, 5=Philippe, 6=Charles, 7=Francis, 8=Bruno) — always copy that exact order. Verify the mapping programmatically after implementation: extract each `{name, video}` pair from the JS, check the video URL hash against the expected name.
- **Video thumbnails show as black boxes with `preload="none"`.** The FR funnel uses `preload="none"` on the `<video>` tags for performance, which means no frame loads until play — the cards render as solid black/dark rectangles with no visual content. Users see "broken videos." The fix is a 4-step `loadVideo()` function that forces a thumbnail frame to paint: (1) set `source.src = dataSrc + '#t=0.5'` (the `#t=0.5` media fragment tells the browser to load the frame at 0.5s); (2) set `video.preload = 'metadata'` then call `video.load()`; (3) add a `loadedmetadata` listener (once) that sets `video.currentTime = 0.5` to seek to that frame; (4) add a `seeked` listener (once) that calls `video.pause()` to hold the painted frame. For the grid layout, use `IntersectionObserver` with `rootMargin: '200px'` to lazy-load each video's metadata when its card scrolls into view — this replaces the old staggered `setTimeout` approach and is cleaner. After implementation, verify via browser console: all videos should show `readyState=4` and `currentTime=0.5` after scrolling to the section. The FR funnel's own `loadCardVideo()` does steps 1-2 but NOT the seek (steps 3-4) — that's why its side cards also look dark until hovered. The seek is the missing piece that makes thumbnails visible on first paint.
- **Replace lucide icons with the GS icon for key section headers.** Matt asked to replace `wand-sparkles` and `zap` icons with a specific Growthsquare icon image (`https://assets.cdn.filesafe.space/7ZO5K0hBF2arc7KuSZh0/media/698b2d8a01770735457d83d7.png`). Do NOT use the full GS wordmark logo with `filter: brightness(0) invert(1)` — Matt corrected this and provided the specific icon URL he wanted. Apply to proof-card icons and comparison-card winner icons.

### Quebec French copy corrections (standing)
- **"proprios" → "entrepreneurs"** — Matt finds "proprios" (short for propriétaires) sounds weird in marketing copy. Use "entrepreneurs" instead.
- **Remove "natif"** — "Français québécois natif" → just "Français québécois". The word "natif" is unnecessary and sounds stiff.
- **Rename English skill names to French.** "Swipe Library FR" → "Bibliothèque d'angles québécois". English product/feature names in a French funnel read as unfinished template text.
- **Remove technical jargon from user-facing copy.** "cma doctor" (a CLI health-check command) should not appear in guarantee copy or step descriptions. Most users won't touch a terminal — replace with "on est un call away", "on vérifie que tout roule", "on regarde ça ensemble".
- **Don't mention compliance frameworks you can't back up.** Matt asked to remove "Loi 25" from the hero trust bar because the product doesn't formally certify Loi 25 compliance in the background. Only mention legal/compliance claims if the product actually implements them.

### CTA button design (mobile-aware)
- **Arrow icon goes AFTER the text, not before.** `[→] Arrête l'hémorragie` looks broken on mobile (arrow floats to the left edge, disconnected from text). `Arrête l'hémorragie [→]` is the standard CTA pattern — text first, arrow pointing forward at the end. This applies to ALL `btn-primary` CTAs with an arrow icon.
- **Sometimes remove the arrow entirely.** Even after moving the arrow to the right side of the button text, Matt found it still looked "weird" on the calculator CTA ("remove the arrow and centered the text"). For long CTA text (3+ words like "Arrête l'hémorragie, réserve ton call"), the arrow adds visual noise and makes centering look off. When a CTA has long text, just use centered text with no icon — the `btn-primary` CSS already has `justify-content: center`. Short CTAs ("Je veux ma pub gratuite →") can keep the arrow; long CTAs should drop it.
- **Remove icons that render poorly rather than trying to fix them.** Matt flagged the lucide `gift` icon as "a little broken" on mobile — the fix was to remove it entirely, not debug the SVG rendering. If an icon looks off on mobile, drop it. Clean text > broken icon.
- **Matt strongly dislikes carousels and auto-rotating UI.** He rejected both a simple auto-rotating carousel ("the carousel ish is terrible") AND a fanned stacked-card design ("I don't want them in the carousel format"). When displaying multiple items (testimonials, features, proof), default to a **grid** — 3 columns desktop, 1 column mobile. No carousels, no auto-rotate, no hover-to-focus positioning.

### Booking widget (Growthsquare)
- FR white funnels: `https://booking.growthsquare.ai/embed/jeremy?theme=light&lang=fr`
- Use `/embed/` NOT `/book/` (the latter sends X-Frame-Options and blocks iframe)
- Include PostHog + Meta Pixel tracking (standard on all GS funnels)
- **No card wrapper around the iframe.** Matt explicitly asked to remove the bordered/shadowed card container around the booking widget ("it look weird just the widget will look better and the 1-2-3 closer from the text"). The `.booking-card` div should be a bare max-width container — NO border, NO padding, NO box-shadow, NO `::before` glow, NO background. Just `max-width: 700px; margin: 32px auto 0;` and the iframe sits directly on the page, closer to the heading text. The widget's own internal card/stepper styling is enough — wrapping it in another card creates a "card-in-a-card" look that reads as cluttered.

### Funnel structure — two-page, opt-in does NOT go straight to booking (Matt's preference, reinforced July 2026)
- **Two-page funnels.** Page 1 = video (or a hero section if no video exists) + an opt-in form. On page 1 the opt-in only needs first name + email — don't ask for phone/last name yet, that friction kills cold conversion. Page 2 = a LONG landing page with real content (problem agitation, mechanism explanation, modules / what's included, video testimonials, about the coach) and the **booking calendar at the VERY END**, after the prospect has been warmed up.
- **Do NOT send the page-1 opt-in directly to a bare booking page.** Matt explicitly dislikes the old pattern of "first page video + opt-in, second page is directly the booking." The booking must come AFTER a long sales page so the lead is sold before they see the calendar.
- **When no video exists** (e.g. a brand-new program), page 1 is hero + headline + opt-in only, then redirect to the long-landing page 2.
- Applies to all client funnels (Audrey Levasseur, etc.), not just Growthsquare's own pages. Reuse the client's existing webhook (GHL), booking iframe, logo/photo CDN URLs, and testimonial video URLs across both pages so the funnel stays self-consistent.

## Verification Checklist

**Single page:**
- [ ] Business, funnel, avatar, offer, and CTA confirmed
- [ ] Page type and traffic temperature identified
- [ ] Framework selected intentionally
- [ ] Header passes the grunt test
- [ ] Page has one primary CTA
- [ ] Offer links to a saved offer doc or clear source
- [ ] Proof and claims are sourced or flagged
- [ ] Main objections are answered
- [ ] Brand voice is followed
- [ ] Risky claims are softened or marked for review
- [ ] If wiki-backed, page is filed under the correct business/funnel and linked

**Full funnel:**
- [ ] Client wiki orientation completed when a wiki is available
- [ ] Business, business slug, avatar, offer, and traffic source confirmed
- [ ] Funnel archetype chosen and justified
- [ ] Golden thread defined (promise, mechanism, hook, CTA arc, voice, proof path)
- [ ] Full step map documented (every page, its job, its CTA, its hook variant)
- [ ] Every page written, every script delegated to the correct specialist skill
- [ ] Message-match audit passed (hook continuity, offer consistency, voice consistency, CTA escalation, proof sequencing)
- [ ] Hook continuity verified from ad opening through checkout confirmation
- [ ] Offer, price, guarantee, and scarcity stated identically wherever they appear
- [ ] CTA escalation is logical (no jarring jumps)
- [ ] Proof sequenced from relatable to aspirational without contradiction
- [ ] Brand voice consistent across every page
- [ ] Proof is real or flagged as missing
- [ ] Risky claims (income, health, financial, legal) flagged
- [ ] Funnel copy doc assembled and stored under `businesses/<business-slug>/funnels/`
- [ ] Confidence level and source list included
- [ ] Handoff to `funnel-html-builder` (deferred) is explicit and the doc is build-ready
