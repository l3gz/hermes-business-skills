---
name: product-market-fit
description: >
  Validate whether a startup/product idea has real market fit through market +
  customer-sentiment research, then score it out of 100 against a weighted rubric
  and return a pursue / refine / kill verdict with cited evidence. Use when the user
  asks to "validate an idea", "do PMF research", "is there a market for X", "should
  we pursue this idea", "market research on X", or wants a go/no-go on a concept.
  Research and confirmation only — NEVER builds the application.
version: 2.0.0
author: Growthsquare
license: Private workspace context
---

# Product-Market Fit — Research & Validation Engine

Take an idea and answer one question with evidence: **is there a real, reachable, paying market for this — yes or no?**

This skill does **research and confirmation only**. It does NOT plan, design, or build the product. The deliverable is a scored, cited verdict.

---

## Core principles (read first)

1. **Facts, not opinions.** Every score must be backed by cited evidence (URL or named source). No claim without a source.
2. **Hunt for disconfirming evidence.** Actively search for *why this idea fails* — saturated market, no willingness to pay, "vitamin not painkiller." A skill that only finds reasons to say yes is broken. Spend real effort on red flags.
3. **Honest unknowns.** If evidence is thin, say so and lower the **confidence** rating — do not invent numbers or inflate the score to please.
4. **No score inflation.** A mediocre idea gets a mediocre score. The point is to kill bad ideas cheaply.
5. **Sentiment is approximated, not measured.** We infer demand/pain from public discussions and reviews. Label it as inference, never as a survey.

---

## Tool routing (mandatory)

This skill uses **two complementary research engines**. Use both — they serve different purposes.

### Engine 1 — Firecrawl (primary: web search + structured extraction)

Firecrawl is the primary web research tool. It searches the web, scrapes pages to clean markdown, and extracts structured data from URLs via LLM prompts + JSON schemas. The `firecrawl` Python module and `FIRECRAWL_API_KEY` are available in the environment.

Run Firecrawl via `terminal` (the `execute_code` sandbox lacks system site-packages). Always load the API key from the environment — never inline it.

```python
import os, json
from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key=os.environ["FIRECRAWL_API_KEY"])

# 1. Web search — returns list of results (url, title, description, markdown)
results = app.search(
    query="<problem> reddit complaints OR forum",
    limit=10,
    scrape_options={"formats": ["markdown"], "onlyMainContent": True},
)
for r in results.get("data", []):
    print(r.get("url"), r.get("title"))

# 2. Scrape a single page to clean markdown (competitor pricing, review pages)
doc = app.scrape(
    url="https://competitor.com/pricing",
    formats=["markdown"],
    only_main_content=True,
)
print(doc.get("markdown", ""))

# 3. Structured extraction — pull specific fields from a set of URLs
data = app.extract(
    urls=["https://competitor.com/pricing", "https://competitor2.com/pricing"],
    prompt="Extract the product name, all plan names, and their prices (monthly and annual).",
    schema={
        "type": "object",
        "properties": {
            "competitors": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "url": {"type": "string"},
                        "product": {"type": "string"},
                        "plans": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"},
                                    "price_monthly": {"type": "string"},
                                    "price_annual": {"type": "string"},
                                },
                            },
                        },
                    },
                },
            }
        },
    },
    show_sources=True,
)

# 4. Map a site's URL structure (find all pages on a competitor's docs/pricing section)
sitemap = app.map_url(url="https://competitor.com")
```

**Firecrawl decision guide:**
| Need | Method |
|------|--------|
| Broad web search for problem evidence, sentiment, trends | `app.search(query, limit=10, scrape_options={...})` |
| Read one specific page (pricing, review thread, blog post) | `app.scrape(url, formats=["markdown"], only_main_content=True)` |
| Pull structured fields from several pages at once (competitor pricing matrix) | `app.extract(urls=[...], prompt=..., schema={...})` |
| Discover all URLs on a competitor site (docs, features, case studies) | `app.map_url(url)` |

**Pitfalls:**
- `app.search()` with `scrape_options` returns markdown for each result — expensive but rich. For a quick scan, omit `scrape_options` and just use the `description` field, then `scrape()` only the 2–3 most promising URLs.
- `app.extract()` is async and polls — it can take 30–60s for multiple URLs. Use it for batch competitor pricing, not for single quick lookups.
- Large markdown outputs will flood context. Print only the fields you need (title, url, first 500 chars of markdown). Write full output to a temp file if needed.

### Engine 2 — Agent-Reach platform CLIs (sentiment & community signal)

For customer sentiment and demand signals, generic web search misses the highest-density sources: Reddit threads, Twitter/X discussions, YouTube tutorials/reviews. Agent-Reach provides one-command access to these platforms via CLI tools.

**First-time setup:** tell the user to run in their agent:
```
Install Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```
Then verify with `agent-reach doctor` (run via terminal). If Agent-Reach is not installed, fall back to Firecrawl `search()` with `include_domains` for the relevant platforms (see fallback below).

**Platform tools for PMF (run via terminal):**

| Platform | Command | PMF use |
|----------|---------|---------|
| Reddit | `rdt-cli search "<query>"` or `rdt-cli subreddit <sub> --sort top` | Lane A & B: raw complaints, "is there a tool for X", workaround threads |
| Twitter/X | `twitter search "<query>"` or `twitter timeline <user>` | Lane B: real-time sentiment, pain language, influencer takes |
| YouTube | `yt-dlp --write-auto-sub --skip-download "<url>"` | Lane B & E: tutorial comments, "why I switched from X" videos |
| Web (any URL) | Jina Reader (zero-config in Agent-Reach) | Lane C: competitor pages, review sites |

**If Agent-Reach is NOT installed** — Firecrawl fallback with domain targeting:
```python
# Reddit sentiment via Firecrawl
app.search(
    query="<problem> worst experience OR switched from OR waste of money",
    include_domains=["reddit.com"],
    limit=10,
    scrape_options={"formats": ["markdown"], "onlyMainContent": True},
)

# Twitter/X via Firecrawl (public pages)
app.search(
    query="<problem> site:x.com OR site:twitter.com",
    limit=10,
)
```
The fallback is weaker (no API auth, rate-limited, less structured) — recommend the user install Agent-Reach for repeat PMF work.

### Quick fallback search
`web_search` (Hermes built-in) for quick lookups when Firecrawl is rate-limited or you need a fast sanity check. Not for primary research.

---

## Workflow

### Phase 0 — Idea intake
Capture a structured brief. If the user gave a one-liner, infer what you can and ask **at most 2–3** clarifying questions only for genuinely blocking gaps (don't interrogate):

```
IDEA BRIEF
- Problem:        what pain, for whom, how often
- Target customer (ICP): who specifically pays
- Proposed solution: one sentence
- Business model:  how it makes money + rough price point
- Geography/market: where
```

Write the brief into the report so the verdict is traceable to what was actually asked.

### Phase 1 — Research (5 lanes, inline by default)
Run the 5 research lanes from `references/research-playbook.md` one at a time. Each lane produces a short **cited** mini-report:

- **A. Problem evidence & severity** — are people actively complaining / hacking workarounds / paying to solve this *today*?
- **B. Customer sentiment & demand** — pain language, frustration with existing options, willingness-to-pay signals (Reddit, reviews, forums, social).
- **C. Competitive landscape** — direct + indirect competitors, pricing, positioning, gaps. (Zero competitors = usually no market, not a green field.)
- **D. Market size & growth** — TAM/SAM/SOM order-of-magnitude, trend direction (Google Trends / Statista / industry reports).
- **E. Timing & tailwinds** — tech enablers, regulation, cultural/behavioral shifts that make *now* the moment (or not).

**Run inline by default** — call Firecrawl and Agent-Reach tools directly from the main thread. Do NOT default to spawning subagents; they add approval friction and lose context. Subagents are an optional speed-up only when the user explicitly asks for parallel execution.

Large Firecrawl/Agent-Reach outputs are persisted or truncated — summarize each lane into ~5–8 cited bullets before moving to the next so context stays clean.

### Phase 2 — Score & verdict
Apply `references/scoring-rubric.md`: score each of the 7 dimensions, multiply by weight, sum to **/100**, map to a verdict band, and assign a **confidence** level based on evidence quality.

### Phase 3 — Deliver the report
Write the report to a file (see Output) and give the user a tight in-chat summary: **score, band, verdict, top 3 green flags, top 3 red flags, 2–3 recommended next validation steps.**

---

## Scoring at a glance

Full rubric in `references/scoring-rubric.md`. Seven weighted dimensions:

| # | Dimension | Weight |
|---|-----------|--------|
| 1 | Problem severity & frequency | 20 |
| 2 | Demand & customer sentiment | 20 |
| 3 | Market size & growth | 15 |
| 4 | Competitive gap / differentiation | 15 |
| 5 | Willingness to pay / monetization | 10 |
| 6 | ICP reachability (distribution) | 10 |
| 7 | Timing / tailwinds | 10 |

**Verdict bands:**
- **80–100 — Strong fit. Pursue.**
- **65–79 — Promising. Pursue with the named refinements.**
- **50–64 — Mixed. Reframe / narrow the ICP and re-test before committing.**
- **35–49 — Weak. Pivot the angle.**
- **<35 — Kill.**

Always pair the score with a **confidence** (High / Medium / Low). A high score at low confidence means "promising but under-researched," not "go."

---

## Output

Write the full report to a markdown file. Default location:
`wiki/product-market-fit/<idea-slug>.md`
If the idea is tied to a specific client, write to the client's folder instead.

Report structure: Idea Brief → Score table (dimension, score, weight, evidence + citations) → **Total /100 + Verdict + Confidence** → Green flags (top 3) → Red flags / risks (top 3) → Recommended next validation experiments → Sources list.

Return only the file path + the tight summary in chat (per workspace output rules). Do not paste the full report inline.

## Modes
- **Full PMF (default):** all phases → scored verdict.
- **Research-only:** if the user says "just research, no score," stop after Phase 1 and deliver the cited findings without the rubric.
