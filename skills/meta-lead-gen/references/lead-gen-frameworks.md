# Lead Gen Frameworks Reference

This reference summarizes the Meta lead-gen frameworks used by the `meta-lead-gen` skill. It distills the lead-gen material from the Master Meta Ad knowledge base (Question 8: Instant Forms vs landing page, qualification questions, speed-to-lead, CRM connection) into operating patterns.

**Scope:** this reference covers the lead-gen-specific layer — capture path, form design, follow-up, CRM routing, quality scoring, compliance. For the underlying Meta Ads mechanics (objective selection, CBO vs ABO, audience strategy, bidding, Pixel/CAPI fundamentals), see `meta-ads-frameworks.md` in the `meta-ads-manager` skill. This file assumes that foundation.

**Conflict resolution rule:** Where sources conflict, the principle that serves the full path (capture → qualify → contact → convert) wins over the principle that optimizes any single stage in isolation. A cheaper lead that is never contacted is more expensive than a pricier lead that closes.

---

## Instant Forms vs Onsite Landing Page — Decision Matrix

The capture path is the most consequential structural decision in a lead-gen campaign. Instant Forms and onsite landing pages are not variations of the same tactic — they are different funnels with different economics.

### Instant Forms (on-platform capture)

The form opens natively inside the Facebook or Instagram app. The user never leaves the feed. Meta pre-fills name and email from the user's profile, reducing the submission to a few taps.

**Mechanics:**
- Conversion location: Instant Forms (under the Leads objective)
- Meta's algorithm optimizes for the form-submission event
- Highly optimized for mobile (where the majority of feed impressions occur)
- No page load, no navigation, no external site

**Strengths:**
- Dramatically higher lead volume — removing friction removes the drop-off that page loads and form-filling create
- Lower cost per lead — on-platform capture is cheaper than driving traffic to an external site
- Fast to launch — no landing page to build or optimize; ideal for validating offer quality and initial lead interest without technical blockers
- Pre-filled data reduces user effort and abandonment

**Tradeoffs:**
- Lower lead quality — the friction removed is also the friction that filtered low-intent submissions
- Less persuasion space — the form has room for an intro and questions, but not for a VSL, long copy, or a full sales argument
- Data lives in Meta first — must be pushed to the CRM via integration, not captured on a page you control

### Onsite Landing Page (off-platform capture)

The ad sends traffic to a proprietary landing page with a form, application, or booking widget.

**Mechanics:**
- Conversion location: Website (under the Leads or Sales objective)
- Pixel + CAPI track the form-submit or booking event
- The page is yours — full control over copy, proof, structure, and the form

**Strengths:**
- Higher lead quality — the extra step (page load, reading, form fill) filters for higher intent
- Richer persuasion — headline, body copy, testimonials, VSL, demo, objection handling all happen before the ask
- Leads convert to paying customers at a materially higher rate than Instant Form leads
- Data is captured on your property and flows directly into your CRM

**Tradeoffs:**
- Lower volume, higher CPL — every step in the path is a place a prospect can drop off
- The page must convert — a weak landing page makes the whole campaign fail, regardless of ad quality
- Requires a proven, high-converting page; launching traffic to an untested page burns budget

### Decision Matrix

| Situation | Recommended path | Rationale |
|---|---|---|
| No proven landing page exists yet | Instant Forms | Validate lead quality and offer demand without a page-building blocker |
| Offer is simple, low-friction, impulse-interest | Instant Forms | Persuasion isn't needed; volume is the goal |
| Offer needs a VSL, demo, or long proof before the ask | Landing page | The persuasion must happen before the form |
| High-ticket offer where qualification dominates | Instant Forms w/ strong questions, OR landing page + application | Quality matters more than volume; either can work if qualification is built in |
| Sales team is large, can work high volume fast | Instant Forms | Volume play; cheap leads + fast contact = scale |
| Sales team is small; every lead must count | Landing page or heavy qualification | Can't afford to work junk; filter hard up front |
| Lead value is high (close rate × ticket justifies CPL) | Landing page | The higher CPL pays for itself in close rate |
| Goal is list-building for a launch or nurture sequence | Instant Forms | Volume and cheap contacts feed the sequence |
| Goal is a scheduled call, not just a form submission | Landing page w/ calendar, OR Instant Form → instant calendar handoff | The booking must happen in the flow |
| B2B / enterprise with strict qualification | Landing page + application | Authority, budget, and fit are hard to gate on a short form |

### The Hybrid Approach

Run both paths in parallel, as separate campaigns (never the same ad set):
- **Instant Forms campaign** for volume — feeds a nurture sequence, builds the list, captures the market that won't click through to a page
- **Landing page campaign** for quality — captures the higher-intent segment that will engage with persuasion and book a call

Measure them separately. Their CPL, lead quality, and cost-per-sale will differ significantly; blending them hides the economics of each.

**Rule:** never run Instant Forms and onsite capture in the same ad set. They are different funnels with different conversion events, optimization signals, and expected outcomes.

---

## Instant Form Question Design

A default Instant Form (name, email, phone) generates volume but no qualification signal. The custom questions are what turn a form submission into a qualified lead. Design them deliberately.

### Core Rules

1. **1-3 questions maximum.** Every additional question reduces completion rate. Only add a question if its answer changes how sales will treat the lead. If the answer doesn't change the sales action, don't ask it.
2. **Multiple choice over open text.** Multiple choice is faster to answer (a tap vs typing), produces clean structured data, and lets you gate on specific answers. Open-text questions get skipped, filled with junk, or produce unstructured data sales can't act on quickly.
3. **Gate on the qualification criteria.** Every question maps to one criterion (budget, authority, need, timing, fit). If a question doesn't map to a criterion, it's decoration — cut it.
4. **Use conditional logic where available.** Show follow-up questions only to relevant respondents. If they say "Under 1 year in business," don't ask a question that only matters for established businesses. This reduces friction for the majority.
5. **Justify sensitive questions.** Revenue, budget, company size, and role can feel invasive. Add a one-line explanation of *why* you're asking, placed immediately under the question. Without justification, respondents assume you're price-discriminating and answer dishonestly or abandon.
6. **Monitor drop-off per question.** Meta reports form-completion and per-question drop-off. A question with high abandonment is too rigid, too personal, or poorly worded. Rewrite or remove it.

### Qualification Question Patterns

Map each question to the qualification criterion it serves:

| Criterion | What it gates | Example question (multiple choice) |
|---|---|---|
| **Budget** | Can they afford the offer? | "What's your monthly budget for [solution]?" — Under $1k / $1k–$5k / $5k–$10k / $10k+ |
| **Authority** | Are they the decision-maker? | "What's your role?" — Owner / Founder / Marketing lead / Employee / Other |
| **Need** | Do they have the problem? | "What's the main challenge you're facing right now?" (problem-specific options) |
| **Timing** | Are they ready to act? | "When are you looking to start?" — Immediately / 1–3 months / 3–6 months / Just researching |
| **Fit (business stage)** | Do they match the offer's requirements? | "How long has your business been active?" — Under 1 year / 1–3 years / 3+ years |
| **Fit (scale)** | Is the volume right for the offer? | "How many [customers/projects/jobs] per month?" — ranges |
| **Fit (industry)** | Is this the right vertical? | "What industry are you in?" (industry list) |

### The Pre-Sale Questionnaire Pattern

For high-intent, high-ticket funnels, structure the questions to make the prospect *feel* the problem before qualifying them. This agitates the pain and raises perceived urgency, improving both qualification accuracy and conversion on the subsequent sales call.

Sequence:
1. "What's the main problem you're facing today?"
2. "How long have you been dealing with it?"
3. "If you had to put a number on it, what has it cost you so far?"
4. "If this continued for another 5 years, how much worse would it get?"

This pattern does double duty: it qualifies (the answers reveal severity and timeline) and it pre-sells (the prospect arrives at the sales call already feeling the cost of inaction).

### Justifying Sensitive Questions — Examples

- **Budget question:** "What's your monthly budget? *(This helps us match you with the right plan and avoid wasting your time if we're not a fit.)*"
- **Revenue question:** "What's your approximate annual revenue? *(We use this to tailor our recommendations to businesses at your stage.)*"
- **Role question:** "What's your role at the company? *(So we connect you with the right person on our team.)*"

The justification should be honest, brief, and benefit-framed (what's in it for them), not sales-framed (what's in it for you).

### Question Anti-Patterns

- **More than 3 custom questions** — completion rate collapses; cut to the essential
- **Open-text where multiple choice works** — "Tell us about your business" produces unstructured data; use "What industry?" with options instead
- **Asking for data sales doesn't use** — if the rep won't change their approach based on the answer, don't ask the question
- **No justification on sensitive fields** — bare revenue/budget questions get dishonest answers
- **Questions that don't map to a qualification criterion** — decoration that adds friction without signal

---

## Speed-to-Lead — Follow-Up Benchmarks

Lead value decays fast. The single most important factor in whether a lead converts is how quickly they are contacted after submitting the form. This is the most under-respected rule in lead gen.

### The Decay Curve

| Time to first contact | Lead state | Conversion impact |
|---|---|---|
| Under 5 minutes (ideally seconds) | Hot — still on their phone, still in a buying frame of mind | Best conversion |
| 5 minutes – 1 hour | Warm — still reachable, intent fading | Acceptable; conversion drops but remains workable |
| 1 – 4 hours | Cooling — the prospect has moved on to other things | Conversion drops sharply |
| 4 – 24 hours | Cold — the moment has passed | Conversion is a fraction of the 5-minute window |
| Over 24 hours | Effectively dead for an immediate-sale offer | May still work for long nurture, not for a close |

**The booking decay specifically:** if a lead submits a form but leaves the screen without booking a call, the probability of ever booking them drops from roughly **70% to roughly 20%**. The window to capture the booking is minutes, not hours.

### The Target SLA

- **Gold standard:** first contact within 5 minutes of form submission (ideally the phone rings within seconds)
- **Acceptable:** within 1 hour
- **Minimum viable:** within 4 hours (same business day)
- **Unacceptable for a direct-sale offer:** over 24 hours

### The Follow-Up Cadence

If the first contact attempt misses, apply a tight sequence immediately — do not wait and "try again tomorrow":

1. **Minute 0:** double-dial (call, hang up, immediately call again) + a personalized SMS
2. **Within the hour:** a value email with a testimonial or case study + a booking link
3. **Same day or next morning:** a second call attempt
4. **If still unreachable:** a DM on the same platform the lead submitted on (Facebook/Instagram Messenger)
5. **Ongoing:** move to a nurture sequence, but the lead is no longer "hot"

### The "Open Season" Protocol

To prevent leads from dying in one rep's queue:

- When a lead submits a form but isn't booked or claimed within a defined window, it becomes **open season** — available to any setter on the team to claim
- The setter who claims it has a defined window (e.g., 7 days) to work it, provided they log a contact attempt daily
- If they don't work it within the window, the lead returns to the pool for others

This eliminates the "I'll get to it" delay that kills lead value.

### The "Call Now" Option

On the Instant Form's thank-you screen, offer a **"Call Now"** button for the highest-intent prospects. This lets a prospect who is ready to talk reach sales instantly, bypassing the follow-up window entirely. It captures the segment that would otherwise cool while waiting for a callback.

### Automation to Hit the SLA

Human discipline alone will not hit a 5-minute SLA at scale. Automate the routing and the first touch:

- **Instant CRM push:** the form submission triggers a webhook (Zapier, Make, native integration) that creates the CRM record and assigns it to a rep within seconds — not via manual export from Ads Manager
- **Auto-SMS:** an automated SMS fires immediately on submission — "Hi [name], this is [rep] from [company]. Saw you requested info on [offer]. Do you have 5 minutes now?"
- **Auto-email:** an automated welcome email sends value + a booking link as a fallback if the call isn't answered
- **Rep notification:** the assigned rep gets a real-time alert (Slack, Teams, SMS, CRM push notification) so they call within the window
- **Calendar handoff:** if a calendar is in place, the thank-you screen surfaces the booking link so the prospect self-schedules, bypassing the need for a first call entirely

**Rule:** if leads are being exported manually from Ads Manager, the SLA is already broken. Automate the push before launching the campaign.

---

## CRM Integration Patterns

Leads are only valuable if they reach the right person, with the right context, fast, and with source attribution intact. Define the integration before launch.

### Integration Methods

| Method | How it works | Best for |
|---|---|---|
| **Native CRM integration** | The CRM has a direct Meta Lead Ads integration (many modern CRMs do) | Most reliable, least setup; use when available |
| **Zapier** | Meta Lead Ads → Zapier → CRM. Triggers on new lead, creates/updates the CRM record | Flexibility, quick setup, multi-step routing |
| **Make (Integromat)** | Similar to Zapier, with a visual flow builder and more complex routing | Complex multi-step workflows, conditional routing |
| **Custom webhook** | A developer builds a direct webhook from the form to the CRM API | Full control, custom logic, high-volume or regulated setups |

### Field Mapping

Every field on the form must map to a field in the CRM:
- **Contact fields:** name → first/last name, email → email, phone → phone
- **Qualification answers:** each custom question → a custom CRM field used for scoring and routing
- **Source attribution:** capture the UTM parameters

### UTM Mapping (Critical for Attribution)

Map every UTM parameter from the ad's URL to the lead record so each lead is traceable back to the campaign, ad set, and creative that produced it:

| UTM parameter | Maps to | Purpose |
|---|---|---|
| `utm_source` | Lead source (e.g., "facebook") | Platform attribution |
| `utm_medium` | Medium (e.g., "paid") | Channel attribution |
| `utm_campaign` | Campaign name | Campaign attribution |
| `utm_content` | Ad creative / variant | Creative attribution |
| `utm_term` | Audience / ad set | Audience attribution |

Without UTM mapping, you cannot answer "which creative produced our qualified leads?" — you can only answer "how many leads did we get?" The first question is the one that improves the campaign; the second is vanity.

### Lead Assignment Rules

Define how a lead gets assigned to a rep:
- **Round-robin:** even distribution across the team (simple, fair)
- **Territory / rep-based:** leads routed by geography, industry, or deal size to specialists
- **Skills-based:** high-intent / SQL leads to closers; MQL / nurture leads to SDRs
- **Open-season (claim-based):** leads go to a pool; the first rep to claim it owns it (drives speed)

### Notification

Define who gets alerted and how:
- The assigned rep (CRM notification, Slack/Teams, SMS)
- Optionally a manager (for SLA monitoring)
- The channel should be one the rep monitors in real time, not email

### Duplicate Handling

Define how to treat a lead who submits twice or already exists:
- **Merge:** update the existing record with new info, don't create a duplicate
- **Update:** refresh the lead's qualification answers and timestamp
- **Skip:** ignore if already in the CRM and recently contacted

Decide the rule before launch; duplicate leads create confusion and double-contacting.

---

## Lead-Quality Scoring

Not every form submission is sales-ready. Define the scoring that separates SQLs from MQLs from junk — and use that signal to improve the campaign.

### Quality Tiers

- **SQL (Sales-Qualified Lead):** meets all qualification criteria, ready for a sales conversation now. Route to a closer immediately.
- **MQL (Marketing-Qualified Lead):** meets some criteria, interested but not ready to buy now. Route to nurture (email sequence, retargeting) until they qualify.
- **Unqualified / Junk:** does not meet minimum criteria (wrong industry, no budget, fake data, out of geography). Exclude from sales follow-up; do not count as a successful conversion.

### Scoring Model

Assign points per qualification field and set thresholds:

| Criterion | Answer | Points |
|---|---|---|
| Budget | $10k+ | 40 |
| Budget | $5k–$10k | 30 |
| Budget | $1k–$5k | 15 |
| Budget | Under $1k | 0 |
| Authority | Owner / Founder | 30 |
| Authority | Marketing lead | 15 |
| Authority | Employee | 0 |
| Timing | Immediately | 20 |
| Timing | 1–3 months | 10 |
| Timing | Just researching | 0 |
| Fit | 3+ years in business | 10 |
| Fit | Under 1 year | 0 |

Set the thresholds:
- **SQL:** 70+ points (meets budget + authority + ready timing)
- **MQL:** 40–69 points (interested, missing one criterion)
- **Unqualified:** under 40 points (fails budget or authority)

Adapt the model, points, and thresholds to the specific offer. The scoring can be automated in the CRM based on the form answers.

### Feeding Quality Back to Meta (The Highest-Leverage Move)

This is what separates basic lead gen from advanced lead gen:

1. **Don't stop at the Lead event.** A generic "Lead" event tells Meta "find me people who submit forms." That includes junk.
2. **Post quality events back via CAPI.** When a lead is marked MQL or SQL in the CRM, trigger a Conversions API postback to Meta with that deeper event — "Qualified Lead," "Scheduled Call," or "Closed Won."
3. **Optimize for the deepest event you have volume for.** Shift the campaign's optimization event from "Lead" to "Qualified Lead" or "Schedule" once you have enough of those events (50+ per week per ad set for the algorithm to learn).

**Why this works:** Meta's algorithm optimizes against the events it receives. If it receives only "Lead" events, it finds form-submitters — including the ones with no budget and fake emails. If it receives "Qualified Lead" events, it learns the profile of people who actually qualify and books calls, and it finds more of them. CPA per raw lead may rise, but **cost per qualified lead and cost per sale fall** because the algorithm stops spending on junk.

**The progression:**
- Start: optimize for Lead (to gather initial volume and data)
- Once you have qualification data: post MQL/SQL via CAPI, optimize for Qualified Lead
- At scale: optimize for Schedule or Sale (the deepest event with enough volume)

---

## Compliance Flags

Lead data is personally identifiable information (PII). Collecting, storing, and using it triggers privacy obligations depending on the jurisdiction.

### What Counts as PII in a Lead Form

- Name, email, phone (always PII)
- Company name + role (can identify an individual, especially in small companies)
- Revenue, budget, or financial data (sensitive — higher obligation)
- Any custom field that could identify or profile an individual

### Jurisdiction Flags

- **Quebec (Loi 25):** collecting PII requires a lawful basis, a privacy policy, transparency about the purpose, and in some cases consent. Data must be stored securely, with a documented retention period. **Flag any Quebec-targeted lead-gen campaign for Loi 25 review.**
- **EU / UK (GDPR / UK GDPR):** collecting PII requires a lawful basis (often consent or legitimate interest), a privacy policy link on the form, data subject rights (access, deletion), and documented data processing. **Flag any EU/UK-targeted campaign for GDPR review.**
- **California (CCPA / CPRA):** privacy notice, right to know and delete, opt-out of sale/sharing. Relevant if collecting data from California residents.
- **Other jurisdictions:** check the client's local privacy law; default to treating all lead data as regulated PII unless confirmed otherwise.

### Form-Level Compliance Checklist

- [ ] Privacy policy link present on the form or thank-you screen
- [ ] Consent checkbox if the jurisdiction requires opt-in consent (e.g., GDPR for EU leads)
- [ ] Clear statement of what the data will be used for (e.g., "We'll use this to contact you about [offer]")
- [ ] Documented retention period (how long leads are kept)
- [ ] Data stored in a compliant CRM / system
- [ ] No collection of data beyond what's needed for qualification and contact

**Rule:** this skill flags compliance concerns for review; it does not provide legal advice. Route compliance questions to the client's legal or ops team. Do not launch a PII-collecting campaign in a regulated jurisdiction without confirming the privacy basis.

---

## Hormozi / Direct-Response Principles Applied to Lead Gen

- **The offer is the ceiling.** No form design or follow-up speed fixes an offer the market doesn't want. If leads aren't qualifying, the offer or the avatar may be wrong before the form is.
- **Specificity converts.** "We help [specific avatar] doing [specific thing] get [specific result]" in the form intro outperforms generic "Get a free consultation."
- **Cost of delay framing.** In the form intro and follow-up, frame what they lose by waiting, not just what they gain by acting. This raises the perceived urgency that makes them answer the sales call.
- **The form sells the next step, not the product.** An Instant Form's job is to earn the contact and the qualification, not to close. Don't overload the form with the pitch — that's the landing page or sales call's job.
- **Qualification is a service, not a gate.** Framed well, qualification questions make the prospect feel heard and matched ("This helps us send you to the right person"). Framed poorly, they feel like an interrogation. Design for the first.
