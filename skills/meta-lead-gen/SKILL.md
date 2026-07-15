---
name: meta-lead-gen
description: Use when planning a Meta lead generation campaign for a business — lead form (Instant Forms) vs onsite landing page decision, Instant Form and qualification-question design, speed-to-lead follow-up workflow, CRM routing, and lead-quality scoring. Produces a complete lead-gen campaign blueprint a media buyer and sales team can execute. Covers B2B, services, coaching, and high-ticket info-product lead gen.
version: 1.0.0
author: Matt
license: MIT
metadata:
  hermes:
    tags: [marketing, meta-ads, lead-gen, facebook-ads, paid-social, instant-forms, crm, sales-funnel]
    related_skills: [meta-ads-manager, meta-creative-tester, meta-audience-builder, funnel-writer, offer-builder, avatar-builder]
---

# Meta Lead Gen

## Overview

Plan and structure Meta lead generation campaigns that turn ad spend into qualified, sales-ready contacts. This skill produces a complete lead-gen blueprint — lead definition, capture path (Instant Form vs onsite landing page), form and qualification-question design, speed-to-lead follow-up SLA, CRM routing, and lead-quality scoring — that a media buyer and sales team can execute against.

Lead gen is not ecommerce with a different conversion event. It is a fundamentally different funnel: the ad buys an opt-in, the opt-in is only valuable if it is qualified, and a qualified lead is only valuable if it is contacted before it goes cold. A campaign that generates cheap form submissions that sales never reaches, or reaches too late, is a campaign that wasted its budget. Every decision in a lead-gen plan must serve the full path: capture → qualify → contact → convert.

Use `references/lead-gen-frameworks.md` for the detailed framework reference (Instant Form vs landing page decision matrix, question design patterns, follow-up speed benchmarks, CRM integration patterns, lead-quality scoring, compliance flags). This file is the operating process.

The core discipline: a lead is not a form submission. A lead is a person who can be reached, qualifies for the offer, and is contacted fast enough to still be in a buying state of mind. Optimize for that outcome — deep events like "Qualified Lead" and "Scheduled Call" — not for raw form volume.

## When to Use

Use this skill when the client asks for:

- a Meta lead generation campaign from scratch (Leads objective)
- the lead form vs onsite landing page decision for a specific offer
- an Instant Form design (questions, qualification gates, question order)
- a speed-to-lead follow-up workflow and SLA
- a CRM routing plan (Zapier, Make, native integration, lead assignment)
- a lead-quality scoring model (what makes a lead sales-ready vs nurture-ready)
- a lead-gen campaign audit (why leads are cheap but unqualified, or qualified but never contacted)
- a shift from a generic "Lead" optimization event to a deeper "Qualified Lead" or "Schedule" event
- a qualification-question set for a B2B, services, coaching, or high-ticket info-product offer

Do not use this skill for:

- general Meta campaign structure, objective selection, CBO vs ABO, or budget strategy — use `meta-ads-manager`
- creative production (ad images, video, copy) — use `ad-creative-brief-writer`, `ad-script-writer`, `hook-angle-writer`
- audience research at the avatar level — use `avatar-builder`
- offer construction — use `offer-builder`
- the landing page or funnel copy the ads point to — use `funnel-writer` or `vsl-writer`
- the sales script or close itself — out of scope for this skill
- ecommerce purchase campaigns — use `meta-ads-manager` with the Sales objective (this skill covers lead capture, not online transactions)

## Multi-Business Rule

A client can run several businesses, and each business can have many lead-gen campaigns. Never blend lead definitions, offers, qualification criteria, or CRM routing across businesses. Before planning, confirm the business, business slug, Meta ad account ID, the offer the campaign will promote, and the CRM or sales process the leads will route into.

Store lead-gen plans inside the client wiki under the correct business:

```text
businesses/<business-slug>/
├── brand.md
├── brand-voice.md
├── offers/
│   └── <offer-slug>.md
├── avatars/
│   └── <avatar-slug>.md
└── meta-ads/
    └── lead-gen/
        └── <campaign-slug>.md
```

If the wiki uses another structure, follow it while keeping every lead-gen plan grouped by business and linked to its offer, avatar, and the sales process it feeds.

## Source Hierarchy

Orient from the client wiki first. Read `SCHEMA.md`, `index.md`, recent `log.md`, and the target business pages before claiming facts. Then prioritize:

1. The offer document: dream outcome, price, mechanism, proof, objections, and what qualifies a prospect to buy (budget, authority, need, timing).
2. The avatar profile: demographics, awareness level, and the exact problem language that belongs in qualification questions.
3. The sales process: who contacts leads, how, how fast, and what tools (CRM, dialer, SMS, email) are in place.
4. The CRM or lead-handling stack: what CRM is used, whether Zapier/Make/native integrations exist, whether Conversions API (CAPI) is installed for lead postback.
5. Existing assets: past lead-gen performance (CPL, lead quality, contact rate, show rate, close rate), known qualification thresholds.
6. Real proof and approved claims for any ad copy or form intro that will be shown to prospects.
7. Agent inference for structure, question sequencing, and workflow design only — never for facts, proof, lead-quality claims, or qualification thresholds.

Completion: the offer, avatar, lead definition, sales process, and CRM/CAPI status are known or marked unknown.

## Required Inputs

Minimum useful inputs:

- the business or brand
- the offer or product being promoted (dream outcome and price at minimum)
- the target avatar
- the lead definition: what counts as a qualified lead for this offer (the qualification criteria)
- the daily or lifetime budget range
- whether the Pixel and Conversions API are installed and firing
- whether leads will be contacted by a human sales process, an automated sequence, or both

Best inputs:

- a completed offer document from `offer-builder`
- a completed avatar profile
- a documented sales process: who contacts, the expected response time, the cadence
- the CRM in use and whether it can receive leads via webhook/Zapier/Make/native integration
- whether CAPI is installed and whether the CRM can post quality updates (MQL/SQL) back to Meta
- past lead-gen performance data (CPL, contact rate, qualification rate, show rate, close rate)
- the landing page or funnel URL if onsite capture is being considered
- the call-booking or scheduling tool in use (Calendly, Cal.com, etc.)

Completion: there is enough source material to design a lead-gen plan without guessing at the lead definition, the sales process, or how leads will be reached.

## Core Workflow

### 1. Orient to the wiki

If working inside a client wiki, read:

- `SCHEMA.md`, `index.md`, recent `log.md`
- the target business's brand, offer, avatar, character, voice, and any existing `meta-ads/` plans
- the sales process documentation, if it exists

Completion: the lead-gen context, source assets, and save path are known.

### 2. Confirm lead-gen scope

Define before structuring:

- business and business slug
- Meta ad account ID (or a note that one needs to be created)
- offer and offer slug
- primary avatar
- the lead definition (see step 3 — what makes a lead qualified for this offer)
- daily or lifetime budget
- Pixel/CAPI status
- CRM and lead-handling stack
- who contacts leads and the target response time
- confidence level and source list

Completion: the campaign is tied to one business, one offer, one avatar, one lead definition, and one sales process.

### 3. Confirm the lead definition

Before any capture-path or form design, define exactly what counts as a qualified lead for this offer. A vague lead definition ("anyone who submits the form") produces a campaign optimized for volume, not value.

Define the qualification criteria:

- **Budget:** can they afford the offer? (monthly revenue, project size, ticket they can approve)
- **Authority:** are they the decision-maker? (job title, role, owner vs employee)
- **Need:** do they have the problem the offer solves? (current problem, pain severity)
- **Timing:** are they ready to act now? (deadline, buying window, how long they've had the problem)
- **Fit:** do they match the offer's requirements? (industry, business age, geography, team size)

The lead definition is the contract between marketing and sales. Marketing captures what sales needs to prioritize; sales contacts what marketing has qualified. If these two are not aligned, leads die in the handoff.

Completion: the qualification criteria are explicit and agreed — every field and question in the form maps back to one of them.

### 4. Choose the lead capture path

This is the most consequential structural decision in a lead-gen campaign: capture leads on-platform via Meta Instant Forms, or off-platform via an onsite landing page. Each path has a distinct tradeoff. See `references/lead-gen-frameworks.md` for the full decision matrix.

**Instant Forms (on-platform capture):**
- The form opens inside the Facebook or Instagram app — no page load, no leaving the feed
- Meta pre-fills the user's name and email, reducing friction to two taps
- Highly optimized for mobile (where the vast majority of feed impressions happen)
- The algorithm optimizes specifically for the form-submission action
- **Result:** dramatically higher lead volume, much lower cost per lead
- **Tradeoff:** lower lead quality. The friction that is removed is also the friction that filtered out low-intent submissions. Form abandonment is lower, but so is real intent.

**Onsite landing page (off-platform capture):**
- The ad sends traffic to a proprietary landing page with a form, application, or booking widget
- Allows richer persuasion before the ask (headline, copy, proof, VSL, demo)
- Adds a step (page load, navigation, form fill), which filters for higher intent
- **Result:** lower lead volume, but leads convert to paying customers at a materially higher rate
- **Tradeoff:** CPL is higher and volume is lower; the page itself must convert or the whole campaign fails

**The decision rule:**

| Situation | Use |
|---|---|
| No proven landing page yet; validating offer / lead quality | Instant Forms |
| B2B or high-ticket offer where qualification matters more than volume | Instant Forms with strong qualification questions, or landing page + application |
| Offer needs persuasion, proof, or a VSL before the ask | Onsite landing page |
| Sales team is large and can work high volume fast | Instant Forms (volume play) |
| Sales team is small; every lead must count | Landing page or heavy qualification |
| Lead value is high (close rate × ticket justifies higher CPL) | Landing page (quality play) |
| Goal is to build a list fast for a launch or nurture sequence | Instant Forms |
| Need a scheduled call, not just a form submission | Landing page with calendar, or Instant Form → instant calendar handoff |

**The hybrid:** run both. Use Instant Forms for volume and to feed a nurture sequence; use a landing page for the qualified, sales-ready path. Never run them in the same ad set — they are different funnels and must be measured separately.

Completion: the capture path is chosen and justified by the lead definition, the sales capacity, and whether a converting landing page exists.

### 5. Design the Instant Form (if using Instant Forms)

If the capture path is an Instant Form, design every element deliberately. A default Instant Form with only name and email will generate volume but not qualified leads.

**Form structure:**

1. **Intro/Heading:** a short, benefit-framed headline that reinforces why they should share their details. Not the ad creative repeated — the value of submitting the form.
2. **Contact fields:** name, email, phone (pre-filled by Meta where possible). Phone is non-negotiable for speed-to-lead — you cannot call a lead with only an email.
3. **Qualification questions:** 1-3 custom questions (see question design rules below).
4. **Thank-you screen:** the immediate next step. If a calendar is in place, surface a "Schedule your call" button here. If not, tell them exactly what happens next ("You'll get a call within the hour") so they are ready to answer.

**Question design rules:**

- **1-3 questions maximum.** Every additional question reduces completion rate. Only add a question if it changes how sales will treat the lead.
- **Multiple choice over open text.** Multiple choice is faster to answer, produces clean data, and lets you gate on specific answers. Open-text questions get skipped or filled with junk.
- **Gate on the qualification criteria from step 3.** If budget qualifies the lead, ask a budget question. If authority qualifies, ask the role. If fit qualifies, ask industry or business stage.
- **Use conditional logic where available** to show follow-up questions only to relevant respondents (reduces friction for the majority).
- **Justify sensitive questions.** If you ask about revenue, budget, or company size, add a one-line explanation of *why* you're asking ("This helps us match you with the right advisor"). Without the justification, respondents assume you're price-discriminating and answer dishonestly or abandon.
- **The pre-sale questionnaire pattern:** for high-intent funnels, structure questions to make the prospect *feel* the problem before qualifying them — "What's the main problem you're facing today?", "How long have you been dealing with it?", "What has it cost you so far?", "If it continued for 5 more years, how much worse would it get?". This agitates the problem and raises perceived urgency, improving both qualification and conversion on the sales call.
- **Monitor drop-off per question.** If a specific question has a high abandonment rate, it is too rigid or poorly worded. Rewrite or remove it.

**Qualification question examples** (adapt to the offer):

| Qualifies on | Example question |
|---|---|
| Budget | "What's your monthly budget for this?" (ranges: Under $1k / $1k–$5k / $5k–$10k / $10k+) |
| Authority | "What's your role?" (Owner / Founder / Marketing lead / Employee) |
| Need / timing | "When are you looking to start?" (Immediately / 1–3 months / Just researching) |
| Fit | "How long has your business been active?" (Under 1 year / 1–3 years / 3+ years) |
| Volume / scale | "How many [jobs/customers/projects] per month?" (ranges) |

Completion: the form captures every qualification field sales needs, and every field maps to a qualification criterion.

### 6. Define the follow-up speed SLA

Lead value decays fast. The single most important factor in lead conversion is **speed to contact**. This is non-negotiable — a lead-gen plan without a follow-up SLA is a plan to waste the leads it generates.

**The speed benchmarks** (see `references/lead-gen-frameworks.md` for the data):

| Time to contact | Lead state |
|---|---|
| Under 5 minutes (ideally seconds) | Best conversion. The prospect is still on their phone, still in a buying frame of mind. |
| Under 1 hour | Acceptable. Conversion drops but remains workable. |
| 4–24 hours | Cold. Conversion drops sharply; the lead has moved on. |
| Over 24 hours | Effectively dead for an immediate-sale offer. May still work for a long nurture. |

**The decay curve:** if a lead submits a form but leaves the screen without booking a call, the probability of ever booking them drops from roughly 70% to roughly 20%. The window is minutes, not hours.

**The follow-up SLA to define:**

- **Target first-contact time:** the standard (5 minutes) or what the sales process can realistically sustain
- **The cadence if the first contact misses:** double-dial + SMS immediately → value email with a testimonial → second call same day or next morning → a DM on the same platform the lead submitted on
- **The "open season" rule:** if a lead is not booked or claimed within a set window, it becomes available to any setter on the team to claim and work — this prevents leads from dying in one rep's queue
- **The "Call Now" option:** offer a "Call Now" button on the form's thank-you screen for the highest-intent prospects to reach sales instantly

**Automation to hit the SLA:**

- Instant CRM push: the form submission triggers a webhook (Zapier, Make, native) that creates the CRM record and assigns it within seconds
- Auto-SMS: an automated SMS fires to the lead immediately on submission ("Hi [name], this is [rep] from [company] — saw you requested info on [offer]. Do you have 5 minutes now?")
- Auto-email: an automated welcome email sends value + a booking link as a fallback if the call isn't answered
- Slack/Teams notification: the assigned rep gets a real-time alert so they can call within the window

Completion: the SLA is defined, the automation that enforces it is specified, and every lead has an owner and a first-contact target.

### 7. Plan CRM routing

Leads are only valuable if they reach the right person, with the right context, fast. Define the routing before launch — not after the first 200 leads land in an unowned inbox.

**Routing decisions:**

- **Integration method:** native Meta-to-CRM integration (if the CRM supports it), Zapier, Make, or a custom webhook. Native is most reliable; Zapier/Make are most flexible.
- **Field mapping:** every form field maps to a CRM field, and every UTM parameter (`utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`) maps to the lead record so each lead is traceable back to the creative and campaign that produced it.
- **Lead assignment:** round-robin (even distribution), territory/rep-based, or skills-based (high-intent leads to closers, nurture leads to SDRs). Define the rule.
- **Notification:** who gets alerted (rep, rep + manager) and how (CRM notification, Slack, SMS, email).
- **Duplicate handling:** how to treat a lead who submits twice or already exists in the CRM (merge, update, skip).

Completion: the path from form submission to an assigned, notified rep with full source attribution is defined and testable.

### 8. Set the qualification threshold and quality scoring

Not every form submission is a sales-ready lead. Define the scoring that separates sales-ready leads from nurture leads from junk — and feed that signal back to Meta.

**Lead-quality tiers:**

- **SQL (Sales-Qualified Lead):** meets all qualification criteria, ready for a sales conversation. Route to a closer immediately.
- **MQL (Marketing-Qualified Lead):** meets some criteria, interested but not ready to buy now. Route to nurture (email sequence, retargeting) until they qualify.
- **Unqualified / Junk:** does not meet minimum criteria (wrong industry, no budget, fake data). Exclude from sales follow-up; do not count as a conversion for optimization.

**Scoring model:** assign points per qualification field (budget range, authority, timing, fit) and set the threshold for SQL vs MQL vs unqualified. The scoring can live in the CRM and be automated.

**The optimization signal — feed quality back to Meta:**

This is the highest-leverage move in advanced lead gen. Do not optimize the campaign for a generic "Lead" event. Instead:

1. When a lead is marked MQL or SQL in the CRM, trigger a CAPI postback to Meta with that deeper event ("Qualified Lead", "Scheduled Call", "Closed Won").
2. Shift the campaign's optimization event from "Lead" to the deepest event you have enough volume for (Qualified Lead, Schedule, or Sale).
3. This teaches Meta's algorithm to find people who *qualify and convert*, not just people who *submit forms*. CPA may rise, but cost per qualified lead and cost per sale fall.

Completion: the scoring model is defined, the tiers are mapped to sales actions, and the CAPI postback path for quality events is specified (or flagged as a setup gap).

### 9. Verify the conversion signal

Same discipline as any Meta campaign: the algorithm optimizes against the events it receives.

- [ ] Pixel installed and firing on the lead-capture event (form submission or onsite form complete)
- [ ] CAPI installed server-side (reduces iOS 14.5+ attribution loss for lead events too)
- [ ] For Instant Forms: the lead is captured natively; ensure the CRM receives it via integration, not manual export
- [ ] For onsite capture: Pixel + CAPI firing on the form-submit or booking event
- [ ] Event Match Quality above 6/10 (ideally 8+)
- [ ] Domain verified (for onsite capture)
- [ ] If optimizing for a deep event (Qualified Lead, Schedule): the CAPI postback from the CRM is firing and the event is available in Events Manager

If the conversion signal is broken or shallow (generic Lead only), flag it. Optimizing for the wrong event is the most common cause of cheap-but-useless leads.

Completion: the conversion signal is verified or the gaps are documented as blocking.

### 10. Assemble the lead-gen campaign document

Use this output shape:

```markdown
# Meta Lead Gen Campaign Plan: [Offer] for [Avatar]

## Scope
- Business:
- Business slug:
- Meta ad account ID:
- Offer:
- Primary avatar:
- Lead definition (what qualifies a lead for this offer):
- Daily / lifetime budget:
- Pixel/CAPI status:
- CRM / lead-handling stack:
- Confidence:
- Sources used:

## Lead Definition
- Budget criteria:
- Authority criteria:
- Need criteria:
- Timing criteria:
- Fit criteria:
- A qualified lead is:

## Capture Path Decision
- Chosen path: Instant Forms / onsite landing page / hybrid
- Rationale:
- Landing page URL (if onsite):
- Form type (if Instant Forms):

## Instant Form Design (if applicable)
- Intro / heading:
- Contact fields: name, email, phone
- Qualification questions (1-3):
  1. Question: [text] — Type: [multiple choice / text] — Qualifies on: [criterion] — Options:
  2. Question: [text] — Type: — Qualifies on: — Options:
  3. Question: [text] — Type: — Qualifies on: — Options:
- Conditional logic:
- Thank-you screen next step: [calendar link / "expect a call within X min"]
- Call Now button: yes / no

## Follow-Up SLA
- Target first-contact time:
- Cadence if first contact misses:
  - Minute 0: double-dial + SMS
  - Minute X: value email
  - Same day / next morning: second call
  - Day X: DM on platform
- Open-season rule:
- Sales owner / assignment rule:

## CRM Routing
- Integration method:
- Field mapping (form field → CRM field):
- UTM mapping:
- Lead assignment rule:
- Notification:
- Duplicate handling:

## Lead-Quality Scoring
- Scoring model:
- SQL threshold:
- MQL threshold:
- Unqualified / junk criteria:
- CRM action per tier:
- CAPI postback events: [Qualified Lead / Schedule / Sale]
- Optimization event for the campaign: [Lead / Qualified Lead / Schedule]

## Conversion Signal Readiness
- [ ] Pixel firing on lead event
- [ ] CAPI installed
- [ ] Deep event postback configured (if optimizing past Lead)
- [ ] EMQ:
- Gaps blocking launch:

## Campaign Structure Summary
- Objective: Leads
- Capture location: Instant Forms / Website
- Optimization event:
- Budget strategy: (see meta-ads-manager for full CBO/ABO and audience plan)
- Note: full campaign hierarchy, audience, creative testing, and budget plan live in the meta-ads-manager campaign plan; this document covers the lead-gen-specific layer

## Compliance Flags
- PII collected: [list — name, email, phone, + any custom fields]
- Consent / privacy policy link on form:
- Loi 25 (Quebec) review needed: yes / no
- GDPR review needed: yes / no
- Data retention / purpose documented:

## Needs Confirmation
- [unverified CRM integration, missing CAPI setup, unconfirmed sales capacity, unconfirmed qualification thresholds, missing privacy review]
```

Completion: the document can be handed to a media buyer and a sales team to execute without reconstructing the lead-gen strategy.

### 11. Update the wiki when appropriate

If working inside an LLM wiki:

- save the lead-gen plan under `businesses/<business-slug>/meta-ads/lead-gen/<campaign-slug>.md`
- link it to the offer, avatar, and the meta-ads-manager campaign plan it sits beneath
- update `index.md` if appropriate
- append to `log.md`
- run `qmd update` if configured

Completion: the plan is filed under the correct business and reusable in later sessions.

## Missing Information Handling

Do not invent missing facts. Use these labels:

- `Unknown`: no source material supports the answer
- `Needs confirmation`: likely but not verified
- `Client to provide`: requires CRM access, sales process details, qualification thresholds, or CAPI setup confirmation
- `Risk flag`: a privacy, compliance, consent, or data-handling concern needing legal or ops review
- `Out of scope`: a sales-process change, CRM migration, or offer redesign this plan cannot drive

If the offer, avatar, or lead definition is missing, stop and route to `offer-builder` or `avatar-builder` first, or confirm the lead definition with the client. A lead-gen plan built without a clear lead definition is a plan to generate unqualified volume.

If the sales process or CRM is unknown, flag it as blocking the follow-up SLA. You cannot define speed-to-lead without knowing who will contact the leads and how.

## Quality Bar

A strong lead-gen plan has:

- one business, one offer, one avatar, one lead definition, and one sales process
- an explicit lead definition tied to qualification criteria (budget, authority, need, timing, fit)
- a capture-path decision (Instant Forms vs landing page) justified by the lead definition, sales capacity, and whether a converting page exists
- an Instant Form (if used) with 1-3 multiple-choice questions, each mapping to a qualification criterion, with sensitive questions justified
- a follow-up SLA with a target first-contact time and a defined cadence if the first contact misses
- CRM routing defined (integration, field mapping, assignment, notification)
- a lead-quality scoring model with SQL / MQL / unqualified tiers
- a plan to feed quality signals back to Meta via CAPI postback on deep events
- a verified or gap-documented conversion signal
- PII and compliance flagged for privacy review (Loi 25, GDPR)
- risky claims and unknowns flagged
- a confidence level and source list

A weak lead-gen plan has:

- no lead definition ("a lead is anyone who fills the form")
- a capture path chosen by default (Instant Forms everywhere) without considering quality
- an Instant Form with only name and email, no qualification questions
- no follow-up SLA — leads land in a CRM with no owner and no target response time
- optimization for a generic "Lead" event with no quality postback
- no CRM routing plan (leads exported manually from Ads Manager days later)
- no privacy/compliance consideration despite collecting PII
- a sales process assumed but not confirmed with the client

## Common Pitfalls

1. **Optimizing for Lead, not Qualified Lead.** A generic Lead event optimizes for form submissions, including junk. Feed MQL/SQL/Schedule back via CAPI and optimize for the deepest event you have volume for.
2. **No follow-up SLA.** The leads are cheap and the contact rate is zero because no one calls them within the window. Speed to lead is the #1 conversion factor — define it before launch.
3. **Instant Forms with no qualification questions.** Pre-filled name and email generate volume but no signal. Add 1-3 multiple-choice questions that gate on the qualification criteria.
4. **Too many questions.** More than 3 custom questions tanks completion rate. Every question must earn its place by changing how sales treats the lead.
5. **Open-text questions.** Open-text is slow to answer and produces unstructured data. Use multiple choice unless the answer truly needs free text.
6. **Asking for sensitive data without justification.** A bare "What's your revenue?" gets dishonest answers or abandonment. Add a one-line reason.
7. **No phone field.** You cannot call a lead with only an email. Speed-to-lead requires a phone number.
8. **Leads dying in one rep's queue.** Without an open-season rule, unworked leads rot. Define when a lead becomes claimable by the team.
9. **Manual lead export.** Exporting leads from Ads Manager by hand means hours of delay. The form must push to the CRM automatically via integration.
10. **No UTM mapping.** If leads arrive in the CRM without source attribution, you cannot tell which creative or campaign produced the qualified leads. Map every UTM.
11. **Choosing Instant Forms when the offer needs persuasion.** If the offer needs a VSL, proof, or a demo before the ask, Instant Forms is the wrong path — use a landing page.
12. **Ignoring compliance.** Lead data is PII. In Quebec (Loi 25) and the EU (GDPR), collecting contact data requires a lawful basis, a privacy policy link, and a documented retention purpose. Flag for review; do not assume it's handled.
13. **Treating lead gen as a media-buying-only problem.** The campaign is one input; the sales process is the other. A great campaign into a broken sales process produces nothing.

## Verification Checklist

- [ ] Business, ad account, offer, avatar, and sales process confirmed
- [ ] Lead definition explicit and tied to qualification criteria (budget, authority, need, timing, fit)
- [ ] Capture path (Instant Forms vs landing page) chosen and justified
- [ ] Instant Form (if used) has 1-3 multiple-choice questions, each mapping to a criterion, with sensitive questions justified
- [ ] Phone field included (speed-to-lead requires it)
- [ ] Thank-you screen defines the immediate next step (calendar link or "expect a call")
- [ ] Follow-up SLA defined: target first-contact time + cadence if missed + open-season rule
- [ ] CRM routing defined: integration, field mapping, UTM mapping, assignment, notification
- [ ] Lead-quality scoring model defined with SQL / MQL / unqualified tiers
- [ ] CAPI postback on deep events (Qualified Lead, Schedule) specified or flagged as a gap
- [ ] Optimization event chosen (deepest available, not generic Lead if possible)
- [ ] Conversion signal verified (Pixel + CAPI + deep event)
- [ ] PII and compliance flagged for privacy review (Loi 25, GDPR)
- [ ] Risky claims and unknowns flagged
- [ ] Confidence level and source list included
- [ ] If wiki-backed, plan filed under `businesses/<business-slug>/meta-ads/lead-gen/` and linked
- [ ] Final output follows the lead-gen document shape

## Output Shape

The lead-gen campaign document (step 10) is the deliverable. It must be self-contained: a media buyer and a sales team should be able to execute the capture path, form design, follow-up SLA, CRM routing, and quality scoring without reconstructing the strategy. The full campaign hierarchy, audience plan, creative testing matrix, and budget strategy live in the companion `meta-ads-manager` campaign plan — this document covers the lead-gen-specific layer and links to that plan.
