# PMF Research Playbook — 5 Lanes

Run each lane **inline by default** (call Firecrawl and Agent-Reach tools directly, one lane at a time) — NOT in a subagent. Subagents add approval friction and lose context. Each lane returns a **short cited mini-report** (bullets + sources), not raw pages. Summarize each lane into ~5–8 bullets before moving to the next.

For each lane: run the searches, then explicitly run **one disconfirming search** ("why X fails", "X waste of money", "stopped using X") so red flags surface.

**Tool pairing:** Firecrawl `search()` + `scrape()` + `extract()` for web-wide research and structured competitor data. Agent-Reach CLIs (`rdt-cli`, `twitter`, `yt-dlp`) for deep platform sentiment. See SKILL.md "Tool routing" for exact commands.

---

## Lane A — Problem evidence & severity → feeds rubric #1
**Goal:** prove the problem is real, painful, and frequent.

Firecrawl search patterns:
- `"<problem>" reddit OR forum complaints`
- `how do people currently solve <problem>` / `<problem> workaround spreadsheet`
- `<audience> biggest frustrations with <domain>`

Agent-Reach (if installed) — deeper Reddit signal:
- `rdt-cli search "<problem> worst experience"`
- `rdt-cli search "is there a tool for <job to be done>"`

Disconfirm: `is <problem> actually a problem` / `<problem> not worth solving`

Report: severity (painkiller vs vitamin), frequency, evidence people already pay/hack to solve it.

## Lane B — Customer sentiment & demand → feeds rubric #2
**Goal:** infer demand and emotional intensity from public voice.

Agent-Reach (primary for this lane — highest density signal):
- `rdt-cli search "<existing solution> complaints"` (Reddit: G2/Trustpilot-style reviews + raw threads)
- `rdt-cli search "<domain> subreddit recommendations"`
- `twitter search "<existing solution> frustrating"` (real-time pain language)
- YouTube: `yt-dlp --write-auto-sub --skip-download "<tutorial/review url>"` → extract pain points from transcript

Firecrawl (structured review extraction):
- `app.search(query="<existing solution> reviews complaints", include_domains=["g2.com","trustpilot.com","reddit.com"], limit=10)`
- `app.extract(urls=[<review page urls>], prompt="Extract sentiment polarity, recurring complaints (as a list), and any willingness-to-pay signals.", schema={...})`

Trend check: Google Trends direction for the core search term (via Firecrawl `search("google trends <term>")` or `scrape` the trends page).

Disconfirm: `<category> overrated` / `why I stopped using <category>`

Report: sentiment polarity, recurring pain language (quote 2–3), demand signals, willingness-to-pay hints. Label all as **inferred**.

## Lane C — Competitive landscape → feeds rubric #4
**Goal:** map who already serves this and find the wedge.

Firecrawl search patterns:
- `app.search(query="<solution> alternatives", limit=10)` / `app.search("best <category> tools 2026", limit=10)`
- For each top 3–5 competitor: `app.scrape(url="<competitor>/pricing", formats=["markdown"], only_main_content=True)`
- **Batch pricing extraction** (high-value Firecrawl feature): `app.extract(urls=[<all competitor pricing pages>], prompt="Extract product name, all plan names, prices (monthly + annual), and key feature limits.", schema={...})` — produces a clean pricing matrix in one call.
- `app.map_url(url="<competitor>")` → discover case studies, feature pages, docs for deeper positioning analysis.

Search for indirect substitutes (incl. "doing nothing" / spreadsheets): `app.search("how to do <job> without software", limit=5)`

Report: table of direct + indirect competitors (name, positioning, price), saturation level, and the specific gap/underserved segment. Flag if **zero competitors** (likely no market) or **entrenched free default**.

## Lane D — Market size & growth → feeds rubric #3
**Goal:** order-of-magnitude TAM/SAM/SOM and trend direction.

Firecrawl search patterns:
- `app.search(query="<market> market size 2026 CAGR forecast", limit=10, scrape_options={"formats":["markdown"],"onlyMainContent":True})`
- `app.search("number of <target customers> in <geography>", limit=5)`
- Bottom-up sanity check: ICP count × plausible price (compute yourself, cite the ICP count source)

Report: rough TAM/SAM/SOM with sources, growth direction. State assumptions; flag if only top-down or only one source (lowers confidence).

## Lane E — Timing & tailwinds → feeds rubric #7
**Goal:** answer "why now?"

Firecrawl search patterns:
- `app.search("<domain> trends 2026 recent changes", limit=10)`
- `app.search("<market> disruption OR regulation 2025 2026", limit=5)`

Agent-Reach (real-time signal):
- `twitter search "<domain> trend"` — early-adopter chatter about shifts
- `rdt-cli search "<domain> new in 2026"` — community-sensed changes

Disconfirm: headwinds, market fatigue, failed predecessors: `app.search("<idea> failed startups", limit=5)`

Report: tailwinds vs headwinds, and whether the window is opening or closing.

---

## Cross-lane notes
- **Willingness to pay (#5)** and **ICP reachability (#6)** are synthesized from Lanes B + C (paid comparables, price anchors) and B + D (channel concentration) — no separate lane needed.
- Prefer **recent** sources (last ~18 months) for sentiment and trends; older is fine for fundamentals.
- If lanes conflict, surface the conflict in the report rather than averaging it away.
- Keep each mini-report tight: ~5–8 bullets + a Sources list. The synthesis step (Phase 2) does the scoring.
- **Firecrawl cost awareness:** `search()` with `scrape_options` and `extract()` consume more credits than bare `search()`. For exploration, use bare `search()` first (just titles + descriptions), then `scrape()`/`extract()` only the 2–5 most promising URLs.
