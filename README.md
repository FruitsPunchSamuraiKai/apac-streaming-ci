# APAC Streaming Competitive Intelligence — Japan + Korea

*Part of a two-project analytical series. This project maps the competitive
environment; the companion project
([Japan Content Investment Efficiency](../japan-content-efficiency/README.md))
provides a framework for content investment discussion within that environment.*

## 1. Problem

Global streaming competitive analysis typically focuses on paid SVOD rivalry.
In APAC, this framework misses two structurally important competitive forces:
strong free/ad-supported streaming ecosystems and YouTube/UGC attention
fragmentation. Understanding all three layers is essential for content strategy,
growth planning, and investment prioritization — especially in markets like
Japan and Korea where these pressures differ fundamentally.

## 2. Scope

- **Markets:** Japan and Korea (MVP)
- **Competition layers:** Premium SVOD, Free/Ad-supported streaming, YouTube/UGC
- **NOT in scope:** Subscriber forecasting, revenue modeling, internal Netflix metrics

## 3. Data Sources

| Category | Sources | Type |
|---|---|---|
| Market structure | Statista, company IR/earnings, press releases | Reported + estimates |
| App/usage proxy | App store rankings, SimilarWeb public data | Proxy indicators |
| Content positioning | Platform official sites, press coverage | Qualitative |
| UGC/attention | YouTube trending public data, digital usage surveys | Proxy indicators |
| Pricing/model | Platform pricing pages, news coverage | Reported |

All data is public, transparent, and labeled by reliability tier.
Every platform entry includes source, source date, and confidence level.

## 4. Approach

Three-layer competitive pressure framework:
1. **Direct paid streaming competition** — premium SVOD rivalry intensity
2. **Free substitution pressure** — demand absorbed by free/ad-supported platforms
3. **UGC/attention fragmentation** — attention diverted from long-form paid content

Each market is scored 1–5 per pressure dimension. Scores are **decomposed into
3 sub-signals** each (e.g., local premium strength, bundle advantage, originals depth)
with documented rationale. This is semi-quantitative scoring, not pure expert judgment.

## 5. Key Findings

Japan and Korea appear to have fundamentally different competitive structures
within this comparison:
- **Japan:** Moderate premium SVOD rivalry, but high free substitution pressure
  (TVer, ABEMA) and significant UGC attention fragmentation
- **Korea:** Strong premium local competition (Tving, Wavve, Coupang Play),
  lower free substitution, moderate UGC pressure

Global frameworks that only measure SVOD-vs-SVOD rivalry will understate
competitive pressure in Japan and overweight it in Korea.

## 6. Deliverables

- 4-tab Streamlit dashboard (Executive Summary, Market Structure, APAC Nuance, Strategic Implications)
- Competitive pressure framework (reusable for additional APAC markets)
- Market-specific strategic implications

## 7. Limitations

- External data only — no internal Netflix metrics
- Proxy indicators, not precise measurements
- Qualitative scoring requires judgment calls (documented)
- Two markets only — framework designed to extend but not yet validated beyond JP/KR
- Point-in-time analysis; market dynamics shift quickly

## 8. How This Would Improve with Internal Data

With Netflix internal data, this framework could incorporate:
- Actual subscriber acquisition/churn by market and content type
- Viewing hours and engagement by competitor content category
- Content cost and efficiency metrics
- A/B test results on pricing and positioning
- Real-time competitive response tracking

## 9. Connection to Companion Project

This project provides the **market context** — which competitive pressures
matter most in each market, and why global frameworks need local adjustment.

The companion project, *Japan Content Investment Efficiency & Export Value
Framework*, builds on this context by asking: given the competitive environment,
how should content investment be discussed? It evaluates Japanese content types
on viewing efficiency, export value, and portfolio role.

Together: **competitive landscape → content investment framework → strategic implications.**
