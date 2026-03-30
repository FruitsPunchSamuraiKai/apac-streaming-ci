# Data Assumptions & Methodology

## Data Reliability Tiers

All data points are classified into one of three tiers:

| Tier | Label | Meaning | Example |
|---|---|---|---|
| 1 | Reported | Official company disclosure or government data | Platform pricing, IR filings |
| 2 | Market Estimate | Third-party research firm estimate | Statista market size, app rankings |
| 3 | Proxy Indicator | Indirect measure used as directional signal | YouTube trending as UGC pressure proxy |

## Competitive Pressure Scoring

Each market is scored 1–5 on three competitive pressure dimensions.
Scores are **semi-quantitative**: each top-level score is decomposed into
**3 sub-signals**, each scored independently with a documented note.

| Score | Meaning |
|---|---|
| 1 | Minimal pressure — few or weak competitors |
| 2 | Low pressure — competitors exist but limited impact |
| 3 | Moderate pressure — meaningful competition present |
| 4 | High pressure — strong competitive forces |
| 5 | Very high pressure — dominant competitive dynamic |

### Sub-signal structure (per pressure dimension)

| Pressure | Sub-signals |
|---|---|
| Direct Paid Streaming | Local premium strength, Bundle advantage, Local originals depth |
| Free Substitution | Broadcaster catch-up strength, FAST/free penetration, Free content expectation |
| UGC/Attention | Mobile video share, YouTube dominance, Short-form intensity |

Every score includes written rationale and sub-signal breakdown.

### Platform data fields

Each competitor entry includes:
- **source:** Where the data comes from (e.g., "Netflix IR", "CyberAgent IR")
- **source_date:** When the data was current (e.g., "2025 Q4")
- **confidence:** high / medium / low
- **data_tier:** 1 (reported), 2 (market estimate), 3 (proxy)

## Key Assumptions

1. **App store rankings and download volumes** are directional proxies for
   platform reach, not precise MAU measures.

2. **YouTube trending data** reflects UGC attention competition but does not
   capture total YouTube consumption.

3. **Pricing data** reflects list prices; actual effective prices may differ
   due to bundles, carrier deals, and promotions.

4. **Market size estimates** from Statista and similar sources carry ±15-20%
   uncertainty; we use them for relative comparison, not absolute values.

5. **"Free streaming penetration"** is approximated through platform availability,
   ad-supported model presence, and broadcaster digital strategy — not measured
   directly.

## What This Data Cannot Tell Us

- Netflix's actual market share or subscriber count by country
- Individual platform's real MAU or engagement metrics
- Content licensing costs or production budgets
- Churn rates or subscriber lifetime value
- Causal relationships between competitive pressure and Netflix performance
