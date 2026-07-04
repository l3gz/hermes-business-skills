# Funnel Copy Frameworks Reference

This reference distills the funnel archetypes, the message-match framework, the golden-thread principle, the delegation matrix, and the common funnel disconnects used by the `funnel-copy-writer` skill. It is a field guide distilled from the indexed sources (ad-to-funnel mapping, VSL structure, offer psychology, and conversion principles). Use it to plan the funnel architecture and enforce continuity, then verify all claims, proof, prices, and guarantees against the client's real offer.

## The Golden Thread

The golden thread is the single promise, mechanism, and CTA that runs through every step of the funnel. Without it, a funnel is a collection of pages. With it, a funnel is one continuous conversation.

The thread has six strands. Define all six before any page is planned:

1. **The one promise** — the specific, quantifiable outcome the avatar gets (from the offer doc). Example: "Add 30-50 high-ticket consulting clients per month."
2. **The one mechanism** — the unique method or vehicle that makes the result achievable and differentiates from alternatives. Example: "The Attention Economy Funnel system."
3. **The one hook** — the scroll-stopping idea that opens the ad and carries through every page as the headline or opener. The hook is chosen from the hook bank and expressed as a variant at each step.
4. **The one CTA arc** — how the ask escalates: ad sells the click → opt-in sells the email → VSL sells the watch → checkout sells the buy. Same destination, escalating commitment. Never jump levels.
5. **The one voice** — the brand voice and attractive character signature (tone, phrases, polarity) that every page shares.
6. **The one proof path** — the testimonials and results, sequenced from relatable (early, similar avatar) to aspirational (late, best result) to consensus (checkout, many people like you).

**One-sentence test:** "[Avatar] gets [promise] through [mechanism], and every step of this funnel says exactly that." If any step cannot be traced back to this sentence, it is off-thread.

## The Message-Match Framework

Message match is the principle that every transition between funnel steps must be seamless. When a prospect clicks an ad, three elements must carry over perfectly to the destination — and carry through every subsequent step.

### The Three Pillars of Message Match

1. **Promise match** — the outcome promised in the ad is the outcome delivered on the landing page, expanded in the VSL, and confirmed at checkout. No new promises appear mid-funnel. If the ad promises "30-50 high-ticket clients," the landing page headline leads with exactly that.
2. **Language match** — the terminology, key phrases, and tone carry through every step. The avatar hears the same words from the brand at every touchpoint. If the ad calls the problem "the murdered budget," the landing page and VSL use the same phrase.
3. **Aesthetic-direction match** — while this skill is copy-only, the copy implies a visual and tone direction. Flag anywhere the copy implies a shift that would break visual continuity for the design team (the deferred `funnel-html-builder`).

### Why message match breaks funnels

A disconnect between what a user sees in the ad and what they experience on the landing page is one of the primary reasons funnels fail to convert. The click is a micro-commitment built on an expectation; if the destination breaks that expectation, the prospect bounces. Every page must validate the click that brought the prospect there.

## The Message-Match Audit Checklist

Run this five-point audit across every step-to-step transition in the funnel:

1. **Hook continuity** — does the hook from the ad reappear as the headline on the landing page and the opening line of the VSL? The hook is expressed as a variant (shorter, longer, visual, verbal) but it is the same idea. If the ad hooks with "the real reason your ads are failing isn't your creative," the landing page headline and VSL opener say the same thing.

2. **Offer consistency** — is the same offer, price, guarantee, and scarcity stated identically across the VSL, sales page, order bump, and checkout? Price, guarantee terms, bonus list, and deadline must match word for word wherever they appear. A buyer who sees "$997" on the VSL and "$1,097" at checkout abandons.

3. **Voice consistency** — does every page sound like the same brand and the same attractive character? Tone, signature phrases, polarity, and the founder's voice must be uniform. A landing page in casual voice followed by a stiff corporate checkout breaks trust.

4. **CTA escalation** — does the ask escalate logically from micro-commitment to purchase?
   - Ad: sell the click (indirect CTA — "click to see the breakdown")
   - Opt-in: sell the email (low-friction — "enter your email for the free guide")
   - VSL: sell the watch (commitment of attention — "give me 15 minutes")
   - Sales page: sell the buy (direct — "click the button to claim your spot")
   - Checkout: confirm the buy (reassurance — "you're protected by the guarantee")
   
   A jump from "learn more" to "buy now for $997" breaks the arc.

5. **Proof sequencing** — is proof deployed in the right order without repetition or contradiction?
   - Early funnel (ad, opt-in): relatable proof — a similar avatar with a modest result.
   - Mid funnel (VSL, sales page): aspirational proof — the best result, the transformation story.
   - Late funnel (checkout, thank-you): consensus proof — many people like you, social validation, risk reversal.
   
   Never quote a testimonial differently on two pages. Source it once, quote it consistently.

## Selling the Click vs. Selling the Offer

The most common funnel mapping mistake is trying to sell the entire product inside the ad. The ad's sole job is to sell the click — to treat the click as a low-resistance micro-commitment.

- **The ad sells the click.** It hooks curiosity, establishes authority, validates the pain, and primes the core belief — then directs the prospect to click for the full explanation. It does not reveal price, the full stack, or the mechanism in detail.
- **The landing page or VSL sells the offer.** That is where the deep explanation, the mechanism, the stack, the price, and the risk reversal belong.

If the ad tries to do the VSL's job, the prospect has no reason to click. If the VSL tries to do the ad's job, it loses the warmed prospect who already clicked for the deep content.

## Funnel Archetypes

Each archetype has a step map. Choose the archetype that matches the business model, offer price, and traffic temperature.

### 1. Opt-In Funnel

**Goal:** capture the lead (email, phone, or opt-in).
**Best for:** lead magnets, low-friction entry, warming cold traffic, building a list before a launch.
**Traffic:** typically cold or warm.

| Step | Page / asset | One job | Primary CTA | Awareness arriving |
|---|---|---|---|---|
| 1 | Cold traffic ad | Stop the scroll, promise the lead magnet | Click to get the free resource | Unaware / problem-aware |
| 2 | Opt-in page | Sell the lead magnet value, capture contact | Enter email / phone | Problem-aware |
| 3 | Thank-you / delivery page | Deliver the asset, set the next expectation | Watch / read / join the list | Solution-aware |
| 4 | Nurture email sequence | Build trust, agitate the deeper problem, introduce the core offer | Click to the core offer | Solution-aware |

**Golden-thread note:** the lead magnet must solve a narrow, specific obstacle and naturally reveal a deeper problem that only the core offer solves. The opt-in is not a dead end; it is the first step of the CTA arc.

### 2. VSL Funnel

**Goal:** direct purchase from a video sales letter.
**Best for:** info-products, courses, mid-to-high-ticket offers, cold-to-warm traffic.
**Traffic:** cold or warm.

| Step | Page / asset | One job | Primary CTA | Awareness arriving |
|---|---|---|---|---|
| 1 | Cold / warm traffic ad | Hook, promise the payoff, sell the click | Click to watch | Unaware / problem-aware |
| 2 | VSL page (opt-in gated or open) | Capture the lead (if gated), host the VSL | Watch the video | Problem-aware |
| 3 | VSL script | Take the viewer from hook to buy | Click to buy / claim | Solution-aware → product-aware |
| 4 | Checkout page | Confirm the offer, handle final objections, close | Complete purchase | Product-aware |
| 5 | (Optional) Upsell / order bump | Add value, increase AOV | Add to order | Buyer |
| 6 | Thank-you page | Confirm, deliver, start onboarding, set next step | Access / begin | Buyer |

**Golden-thread note:** the ad hook must be the VSL opener. The VSL's big promise must be the checkout's confirmation. The price, guarantee, and bonus stack must be identical on the VSL and checkout.

### 3. Webinar Funnel

**Goal:** register, show up, buy.
**Best for:** high-ticket coaching, complex transformations, launches, offers needing live demonstration.
**Traffic:** cold or warm, problem-aware to solution-aware.

| Step | Page / asset | One job | Primary CTA | Awareness arriving |
|---|---|---|---|---|
| 1 | Cold / warm traffic ad | Promote the webinar, promise the training outcome | Click to register | Unaware / problem-aware |
| 2 | Registration page | Sell the webinar, set the time expectation, capture details | Register | Problem-aware |
| 3 | Confirmation / reminder sequence | Maximize show-up rate, reassign attention (email/SMS/private group) | Add to calendar / join group | Solution-aware |
| 4 | Webinar (live or evergreen) | Deliver value, build belief, reveal the offer | Stay to the end | Solution-aware → product-aware |
| 5 | Offer page / sales page | Present the offer, stack, price, guarantee | Buy now | Product-aware |
| 6 | Checkout page | Confirm and close | Complete purchase | Product-aware / buyer |
| 7 | Thank-you page | Confirm, deliver, onboard | Access / begin | Buyer |

**Golden-thread note:** the webinar must set an honest time expectation at registration (e.g., "block off 2 hours"). The offer reveal happens only after value is delivered. The same offer terms carry to the checkout.

### 4. Application Funnel

**Goal:** qualify and book a sales conversation.
**Best for:** high-ticket services, done-for-you, coaching with capacity limits, offers requiring fit assessment.
**Traffic:** warm or hot, solution-aware.

| Step | Page / asset | One job | Primary CTA | Awareness arriving |
|---|---|---|---|---|
| 1 | Warm / hot traffic ad | Hook, qualify the avatar, promise the outcome | Click to apply | Solution-aware |
| 2 | Application page | Qualify fit, set expectations, filter tire-kickers | Submit application | Solution-aware |
| 3 | Booking / calendar page | Confirm the call, reduce no-shows | Book the call | Product-aware |
| 4 | Sales call (script / deck) | Diagnose, present the offer, close | Enroll / sign | Product-aware |
| 5 | (Optional) Post-call checkout / proposal page | Close the committed buyer | Complete purchase | Buyer |
| 6 | Thank-you / onboarding | Confirm, deliver, onboard | Access / begin | Buyer |

**Golden-thread note:** the application must filter for fit, not gather everyone. The ad, application, and call must share the same avatar call-out and the same promise. The sales call is where the offer is personalized, not reinvented.

### 5. Ecommerce Funnel

**Goal:** direct purchase of a physical or digital product.
**Best for:** physical products, low-to-mid ticket, impulse or comparison buys.
**Traffic:** cold or warm.

| Step | Page / asset | One job | Primary CTA | Awareness arriving |
|---|---|---|---|---|
| 1 | Cold / warm traffic ad | Demo the product, hook the desire | Click to view / shop | Unaware / product-aware |
| 2 | Product / landing page | Show the product, handle objections, frame value | Add to cart | Product-aware |
| 3 | Cart page | Confirm the order, add order bump (optional) | Checkout | Buyer-intent |
| 4 | Checkout page | Close with minimal friction, free shipping / returns | Complete purchase | Buyer |
| 5 | (Optional) Post-purchase upsell | Increase AOV with a relevant add-on | Add to order | Buyer |
| 6 | Thank-you / order confirmation | Confirm, set delivery expectations, start retention | Track order | Buyer |

**Golden-thread note:** the product is the star, not the founder. The ad demo must match the product page experience. Price comparison is handled honestly. Risk reversal (returns, guarantees) is the primary conversion lever.

## The Delegation Matrix

This skill delegates page copy to specialist skills. It does not write the copy itself.

| Funnel step | Skill | Notes |
|---|---|---|
| Cold / warm / hot traffic ad (video, image, carousel) | `ad-script-writer` | Pass the hook, the avatar, the traffic temperature, and the CTA (sell the click). |
| Opt-in page, lead magnet page | `funnel-page-writer` | Pass the lead magnet, the hook variant, and the next step. |
| Landing page (pre-VSL or direct-to-offer) | `funnel-page-writer` | Pass the hook, the offer summary, and the CTA. |
| VSL page (the wrapper that hosts the video) | `funnel-page-writer` | The page around the video; not the script. |
| VSL script | `vsl-writer` | Pass the offer, avatar, hook, industry variant, and CTA destination. |
| Sales page (long-form) | `funnel-page-writer` | Pass the full offer doc, the hook, the proof, and the objections. |
| Webinar registration page | `funnel-page-writer` | Pass the webinar promise, time expectation, and hook. |
| Webinar script / deck script | `vsl-writer` (webinar variant) | Long-form; pass the three pillars and the offer reveal plan. |
| Application page | `funnel-page-writer` | Pass the qualification criteria and the avatar call-out. |
| Booking / calendar page copy | `funnel-page-writer` | Pass the call promise and the no-show reducer. |
| Checkout page copy | `funnel-page-writer` | Pass the exact offer terms (price, guarantee, bonus stack) to match the VSL/sales page verbatim. |
| Order bump / upsell / downsell page | `funnel-page-writer` (offer from `offer-builder`) | Pass the bump offer and the objection it removes. |
| Thank-you / delivery page | `funnel-page-writer` | Pass the delivery steps and the next action (onboarding, nurture, upsell). |
| Nurture / follow-up email sequence | `nurture-email-writer` / `launch-email-writer` | Pass the golden thread, the offer, and the sequence goal. |

When delegating, always pass: the golden thread (promise, mechanism, hook, voice, proof path), the step context (traffic temperature, awareness level, previous step, next step), and the specific CTA. Each skill owns its output quality; this skill owns the continuity.

## Common Funnel Disconnects and Fixes

### Disconnect 1: The ad hook does not match the landing page headline
**Symptom:** the ad hooks with one idea, the landing page opens with another. The prospect feels disoriented and bounces.
**Fix:** choose one hook from the hook bank. The ad hook, the landing page headline, and the VSL opener are all variants of that one hook. Align the downstream page to the hook — do not change the hook to fit a page.

### Disconnect 2: The offer is stated differently on the VSL and the checkout
**Symptom:** price, guarantee, or bonus list differs between the VSL and checkout. The buyer loses trust at the moment of highest friction.
**Fix:** source the offer terms once from the offer doc. Quote them identically on the VSL, sales page, order bump, and checkout. Verify word for word.

### Disconnect 3: The CTA jumps from "learn more" to "buy now"
**Symptom:** the ad says "click to learn more," the landing page says "buy now for $997." The commitment arc is broken.
**Fix:** map the CTA arc: click → email → watch → buy. Each step asks for one logical level more commitment than the last. Never skip a level.

### Disconnect 4: Proof contradicts itself across steps
**Symptom:** a testimonial is quoted one way on the sales page and another way on the checkout, or the result number changes between the VSL and the ad.
**Fix:** source every testimonial and result once. Quote it consistently wherever it appears. Use the exact wording from the source material.

### Disconnect 5: The thank-you page is a dead end
**Symptom:** the thank-you page says "thanks for your purchase" and nothing else. Retention and upsell opportunities are lost.
**Fix:** the thank-you page has a job: confirm the purchase, deliver the access, start onboarding, and set the next step (upsell, nurture, community, or first action).

### Disconnect 6: The funnel speaks to cold traffic the whole way through
**Symptom:** the checkout page still uses curiosity hooks and problem agitation as if the buyer is unaware. The buyer is product-aware and ready; they need confirmation, not re-persuasion.
**Fix:** match the copy to the awareness level arriving at each step. Cold copy at the ad, solution-aware copy at the VSL, confirmation copy at the checkout.

### Disconnect 7: The ad tries to sell the offer
**Symptom:** the ad reveals the price, the full stack, and the mechanism. The prospect has no reason to click.
**Fix:** the ad sells the click. It hooks, promises, validates, and directs to the landing page or VSL for the deep content. Move any offer detail out of the ad and into the destination page.

### Disconnect 8: The lead magnet does not lead anywhere
**Symptom:** the opt-in delivers a resource but does not reveal the deeper problem the core offer solves. The lead goes cold.
**Fix:** the lead magnet solves a narrow obstacle and naturally surfaces the next problem. The thank-you page and nurture sequence bridge to the core offer using the same golden thread.

## Behavioral Filtering and Identity Transition

A high-converting funnel does not just deliver information; it systematically shifts the prospect's identity as they move toward the purchase.

- **The narrow lead magnet** solves a specific obstacle and reveals the deeper problem only the core offer solves.
- **Low-ticket qualification** (a $7-$97 offer or paid application) separates active buyers from browsers. Once a prospect makes a small financial commitment, their identity shifts from passive viewer to active participant, lowering friction for the backend offer.
- **The CTA arc is an identity arc:** clicker → subscriber → watcher → buyer. Each step's copy speaks to the identity the prospect holds at that step.

## CTA Escalation Map

The ask escalates one logical level at a time. Same destination, escalating commitment.

| Step | Ask | Friction | Copy job |
|---|---|---|---|
| Ad | Click | Near-zero | Sell the click — hook, promise, curiosity |
| Opt-in | Email / phone | Low | Sell the lead magnet value |
| VSL / webinar | Watch time | Medium | Sell the attention — deliver value, build belief |
| Sales page / offer page | Buy | High | Sell the offer — stack, price, guarantee, urgency |
| Checkout | Complete purchase | Highest | Confirm — reassure, remove final friction, state the guarantee |
| Thank-you | Next action | Low (buyer) | Deliver, onboard, set the next step |

A jump of more than one level breaks the arc. A drop in the CTA (e.g., a "learn more" on the sales page) signals the prospect is not yet ready for the ask and the upstream steps need to do more work.

## Proof Sequencing Map

Proof is deployed in a specific order across the funnel. Never repeat the same proof at the same intensity; never contradict a result across pages.

| Funnel stage | Proof type | Purpose |
|---|---|---|
| Ad / opt-in (early) | Relatable — a similar avatar, modest result | "This is for someone like me" |
| VSL / sales page (mid) | Aspirational — the best result, the transformation story | "This can really work / I want this" |
| Checkout / thank-you (late) | Consensus — many people like you, social validation | "I'm making the right choice / others did too" |

Source each proof point once. Quote it consistently. Flag any proof that is not from real source material.

## Safety Rules

- Do not invent proof, testimonials, results, or claims.
- Do not fake scarcity or urgency. Use only real deadlines, capacity limits, or cost-of-delay framing.
- Do not make health, income, legal, financial, or credential claims without a source.
- Do not state a price, guarantee, or bonus that is not in the offer document.
- Do not blend copy, proof, or voice across businesses or offers.
- Keep the avatar as the hero and the brand as the guide at every step.
- Keep the CTA direct and escalating at every step.
- Use the client's offer docs, avatar profiles, and voice guides as the source of truth.
- Flag every risky claim for legal or compliance review before the funnel goes live.
