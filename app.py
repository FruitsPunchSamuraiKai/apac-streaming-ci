"""
APAC Streaming Competitive Intelligence Dashboard
MVP: Japan + Korea
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from data.competitors import (
    JAPAN_PREMIUM_SVOD, JAPAN_FREE_ADSUPP, JAPAN_UGC,
    KOREA_PREMIUM_SVOD, KOREA_FREE_ADSUPP, KOREA_UGC,
    PRESSURE_SCORES, APAC_NUANCE, MARKET_SUMMARY,
)

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="APAC Streaming Competitive Intelligence",
    page_icon="📊",
    layout="wide",
)

st.title("APAC Streaming Competitive Intelligence")
st.caption(
    "External-data-based competitive analysis framework | "
    "MVP: Japan + Korea | Three-layer competition model"
)

# ── Data helpers ─────────────────────────────────────────────────────────────
MARKETS = {
    "Japan": {
        "premium": JAPAN_PREMIUM_SVOD,
        "free": JAPAN_FREE_ADSUPP,
        "ugc": JAPAN_UGC,
        "pressures": PRESSURE_SCORES["japan"],
        "nuance": APAC_NUANCE["japan"],
        "summary": MARKET_SUMMARY["japan"],
    },
    "Korea": {
        "premium": KOREA_PREMIUM_SVOD,
        "free": KOREA_FREE_ADSUPP,
        "ugc": KOREA_UGC,
        "pressures": PRESSURE_SCORES["korea"],
        "nuance": APAC_NUANCE["korea"],
        "summary": MARKET_SUMMARY["korea"],
    },
}

PRESSURE_LABELS = {
    "premium_svod": "Direct Paid Streaming Competition",
    "free_substitution": "Free Substitution Pressure",
    "ugc_attention": "UGC / Attention Fragmentation",
}

PRESSURE_COLORS = {
    "premium_svod": "#1f77b4",
    "free_substitution": "#ff7f0e",
    "ugc_attention": "#2ca02c",
}


def competitors_to_df(competitors: list) -> pd.DataFrame:
    return pd.DataFrame(competitors)


# ── Tabs ─────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "Executive Summary",
    "Market Structure & Competitors",
    "APAC Nuance",
    "Strategic Implications",
])

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 1: EXECUTIVE SUMMARY
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab1:
    st.header("Executive Summary")
    st.markdown("*Understand the competitive landscape in 60 seconds*")

    # Market selector
    market = st.selectbox("Select Market", ["Japan", "Korea"], key="exec_market")
    m = MARKETS[market]
    pressures = m["pressures"]
    summary = m["summary"]

    # KPI cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(
            "Paid Streaming Intensity",
            f"{pressures['premium_svod']['score']}/5",
            pressures["premium_svod"]["label"],
        )
    with col2:
        st.metric(
            "Free Substitution Pressure",
            f"{pressures['free_substitution']['score']}/5",
            pressures["free_substitution"]["label"],
        )
    with col3:
        st.metric(
            "UGC Attention Pressure",
            f"{pressures['ugc_attention']['score']}/5",
            pressures["ugc_attention"]["label"],
        )
    with col4:
        n_competitors = len(m["premium"]) + len(m["free"]) + len(m["ugc"])
        st.metric(
            "Platforms Tracked",
            n_competitors,
            "across 3 layers",
        )

    st.divider()

    # Competitive pressure radar
    st.subheader("Competitive Pressure Profile")
    col_radar, col_text = st.columns([1, 1])

    with col_radar:
        categories = list(PRESSURE_LABELS.values())
        jp_scores = [PRESSURE_SCORES["japan"][k]["score"] for k in PRESSURE_LABELS]
        kr_scores = [PRESSURE_SCORES["korea"][k]["score"] for k in PRESSURE_LABELS]

        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=jp_scores + [jp_scores[0]],
            theta=categories + [categories[0]],
            fill="toself",
            name="Japan",
            fillcolor="rgba(31, 119, 180, 0.15)",
            line=dict(color="#1f77b4"),
        ))
        fig_radar.add_trace(go.Scatterpolar(
            r=kr_scores + [kr_scores[0]],
            theta=categories + [categories[0]],
            fill="toself",
            name="Korea",
            fillcolor="rgba(255, 127, 14, 0.15)",
            line=dict(color="#ff7f0e"),
        ))
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
            height=380,
            legend=dict(orientation="h", y=-0.1),
            margin=dict(t=30, b=30),
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    with col_text:
        st.markdown(f"**{market}: {summary['headline']}**")
        st.markdown(summary["takeaway"])

    st.divider()

    # Top competitive pressures with sub-signal decomposition
    st.subheader("Competitive Pressure Scoring")
    sorted_pressures = sorted(
        pressures.items(), key=lambda x: x[1]["score"], reverse=True
    )
    for key, p in sorted_pressures:
        label = PRESSURE_LABELS[key]
        st.markdown(f"**{label}** — {p['label']} ({p['score']}/5)")
        # Sub-signals
        subs = p.get("sub_signals", {})
        if subs:
            sub_rows = []
            for sub_name, sub_data in subs.items():
                sub_rows.append({
                    "Sub-signal": sub_name.replace("_", " ").title(),
                    "Score": f"{sub_data['score']}/5",
                    "Note": sub_data["note"],
                })
            with st.expander("View sub-signal breakdown"):
                st.dataframe(pd.DataFrame(sub_rows), use_container_width=True, hide_index=True)
        st.caption(p["rationale"])

    st.divider()
    st.caption(
        "Note: All data is from public sources. Pressure scores are semi-quantitative "
        "assessments decomposed into sub-signals with documented rationale. "
        "This is an external-data planning framework, not an internal market model."
    )

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 2: MARKET STRUCTURE & COMPETITORS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab2:
    st.header("Market Structure & Competitor Landscape")

    market2 = st.selectbox("Select Market", ["Japan", "Korea"], key="struct_market")
    m2 = MARKETS[market2]

    # Competitor map visualization
    st.subheader("Competition Landscape by Layer")

    all_competitors = []
    for comp in m2["premium"]:
        all_competitors.append({**comp, "layer": "Premium SVOD"})
    for comp in m2["free"]:
        all_competitors.append({**comp, "layer": "Free / Ad-supported"})
    for comp in m2["ugc"]:
        all_competitors.append({**comp, "layer": "YouTube / UGC"})

    df_comp = pd.DataFrame(all_competitors)

    layer_colors = {
        "Premium SVOD": "#1f77b4",
        "Free / Ad-supported": "#ff7f0e",
        "YouTube / UGC": "#2ca02c",
    }

    fig_landscape = px.scatter(
        df_comp,
        x="local_content_strength",
        y="pricing_usd_mo",
        color="layer",
        size=[30] * len(df_comp),
        text="platform",
        color_discrete_map=layer_colors,
        labels={
            "local_content_strength": "Local Content Strength (1–5)",
            "pricing_usd_mo": "Monthly Price (USD equivalent)",
            "layer": "Competition Layer",
        },
    )
    fig_landscape.update_traces(textposition="top center", textfont_size=11)
    fig_landscape.update_layout(
        height=450,
        xaxis=dict(range=[0, 6]),
        yaxis=dict(range=[-1, 16]),
        legend=dict(orientation="h", y=1.12),
    )
    st.plotly_chart(fig_landscape, use_container_width=True)
    st.caption(
        "Bubble position: x = local content strength (1–5 qualitative), "
        "y = monthly price in USD equivalent. Free platforms at $0."
    )

    # Competitor comparison tables by layer
    st.subheader("Layer 1 — Premium SVOD")
    df_premium = competitors_to_df(m2["premium"])
    display_cols = ["platform", "type", "pricing_local", "content_focus",
                    "local_content_strength", "monetization", "source", "confidence", "notes"]
    st.dataframe(
        df_premium[display_cols].rename(columns={
            "platform": "Platform",
            "type": "Type",
            "pricing_local": "Pricing",
            "content_focus": "Content Focus",
            "local_content_strength": "Local Strength (1–5)",
            "monetization": "Model",
            "source": "Source",
            "confidence": "Confidence",
            "notes": "Notes",
        }),
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Layer 2 — Free / Ad-supported Streaming")
    df_free = competitors_to_df(m2["free"])
    st.dataframe(
        df_free[display_cols].rename(columns={
            "platform": "Platform",
            "type": "Type",
            "pricing_local": "Pricing",
            "content_focus": "Content Focus",
            "local_content_strength": "Local Strength (1–5)",
            "monetization": "Model",
            "source": "Source",
            "confidence": "Confidence",
            "notes": "Notes",
        }),
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Layer 3 — YouTube / UGC / Short-form")
    df_ugc = competitors_to_df(m2["ugc"])
    st.dataframe(
        df_ugc[display_cols].rename(columns={
            "platform": "Platform",
            "type": "Type",
            "pricing_local": "Pricing",
            "content_focus": "Content Focus",
            "local_content_strength": "Local Strength (1–5)",
            "monetization": "Model",
            "source": "Source",
            "confidence": "Confidence",
            "notes": "Notes",
        }),
        use_container_width=True,
        hide_index=True,
    )

    # Pricing comparison bar chart
    st.subheader("Pricing Comparison — Paid Platforms")
    paid_platforms = [c for c in all_competitors
                      if c["pricing_usd_mo"] > 0 and c["layer"] == "Premium SVOD"]
    if paid_platforms:
        df_pricing = pd.DataFrame(paid_platforms).sort_values("pricing_usd_mo")
        fig_price = px.bar(
            df_pricing,
            x="platform",
            y="pricing_usd_mo",
            color="layer",
            color_discrete_map=layer_colors,
            labels={"pricing_usd_mo": "Monthly Price (USD)", "platform": ""},
        )
        fig_price.update_layout(height=350, showlegend=False)
        st.plotly_chart(fig_price, use_container_width=True)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 3: APAC NUANCE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab3:
    st.header("APAC Nuance — Why Global Frameworks Need Local Adjustment")
    st.markdown(
        "Standard North American streaming analysis assumes paid SVOD is the "
        "primary video consumption mode. In APAC, this assumption breaks down. "
        "This page explains why."
    )

    # Side-by-side comparison
    st.subheader("Japan vs Korea — Structural Comparison")

    jp_n = APAC_NUANCE["japan"]
    kr_n = APAC_NUANCE["korea"]

    compare_data = {
        "Dimension": [
            "Mobile video viewing share",
            "Smartphone penetration",
            "Average commute (one-way)",
            "Free streaming ecosystem",
            "Broadcast TV culture",
            "UGC creator ecosystem",
            "Paid content willingness",
        ],
        "Japan": [
            f"{jp_n['mobile_video_share_pct']}%",
            f"{jp_n['smartphone_penetration_pct']}%",
            f"{jp_n['avg_commute_minutes']} min",
            jp_n["free_streaming_penetration"],
            jp_n["broadcast_tv_culture"],
            jp_n["ugc_creator_ecosystem"],
            jp_n["paid_content_willingness"],
        ],
        "Korea": [
            f"{kr_n['mobile_video_share_pct']}%",
            f"{kr_n['smartphone_penetration_pct']}%",
            f"{kr_n['avg_commute_minutes']} min",
            kr_n["free_streaming_penetration"],
            kr_n["broadcast_tv_culture"],
            kr_n["ugc_creator_ecosystem"],
            kr_n["paid_content_willingness"],
        ],
    }
    st.dataframe(
        pd.DataFrame(compare_data),
        use_container_width=True,
        hide_index=True,
    )

    # Mobile-first visualization
    st.subheader("Mobile-First Viewing: APAC vs Global Context")

    mobile_data = pd.DataFrame({
        "Market": ["Japan", "Korea", "US (reference)", "UK (reference)"],
        "Mobile Video Share (%)": [65, 72, 42, 38],
        "Region": ["APAC", "APAC", "North America", "Europe"],
    })

    fig_mobile = px.bar(
        mobile_data,
        x="Market",
        y="Mobile Video Share (%)",
        color="Region",
        color_discrete_map={"APAC": "#ff7f0e", "North America": "#aec7e8", "Europe": "#c7c7c7"},
    )
    fig_mobile.update_layout(height=350, showlegend=True)
    st.plotly_chart(fig_mobile, use_container_width=True)
    st.caption(
        "US/UK figures are approximate reference points from industry reports. "
        "APAC mobile-first behavior has implications for content format, "
        "session length, and discovery UX."
    )

    # Free streaming ecosystem comparison
    st.subheader("Free Streaming Ecosystem Strength")

    col_jp, col_kr = st.columns(2)
    with col_jp:
        st.markdown("**Japan — High free ecosystem strength**")
        st.markdown(
            "- **TVer:** Joint venture of all major broadcasters; 30M+ MAU; "
            "free access to primetime drama, variety, news\n"
            "- **ABEMA:** CyberAgent-owned; mobile-first; free anime, reality, "
            "sports, news; younger demographics\n"
            "- **NHK Plus:** Public broadcaster digital arm\n\n"
            "Combined effect: Casual viewers have strong free alternatives. "
            "Paid streaming must offer content that free platforms *cannot* — "
            "originals, exclusive anime, and premium library."
        )
    with col_kr:
        st.markdown("**Korea — Lower free ecosystem strength**")
        st.markdown(
            "- **Broadcaster apps:** KBS/MBC/SBS offer partial free catch-up, "
            "but content increasingly funneled to Wavve (paid)\n"
            "- **Samsung TV Plus:** Limited local content; device-dependent\n"
            "- No unified free platform equivalent to Japan's TVer\n\n"
            "Combined effect: Korean consumers are more accustomed to paying "
            "for content. Competition is premium-vs-premium, not paid-vs-free."
        )

    st.divider()

    # Framework adjustment recommendations
    st.subheader("Which Metrics Need Local Adjustment?")
    adjustments = pd.DataFrame({
        "Global Metric / Assumption": [
            "SVOD market share = competitive position",
            "Subscriber growth = market health",
            "Price comparison among paid platforms",
            "Content investment ROI = viewing hours / cost",
            "Competitive set = other paid platforms",
        ],
        "APAC Adjustment Needed": [
            "Must include free platform share of viewing time",
            "Must account for attention absorbed by free + UGC",
            "Must include $0 alternatives in value perception",
            "Must account for export value (especially K-content)",
            "Must include free streaming + YouTube as competitors",
        ],
        "Strongest Impact": [
            "Japan",
            "Both",
            "Japan",
            "Korea",
            "Japan",
        ],
    })
    st.dataframe(adjustments, use_container_width=True, hide_index=True)

    st.divider()
    for market_key, nuance in APAC_NUANCE.items():
        st.caption(f"**{market_key.title()}:** {nuance['notes']}")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TAB 4: STRATEGIC IMPLICATIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
with tab4:
    st.header("Strategic Implications")
    st.markdown(
        "What should Netflix think differently about in Japan vs Korea?"
    )

    # Pressure comparison table
    st.subheader("Competitive Pressure Comparison")
    pressure_compare = pd.DataFrame({
        "Competitive Pressure": [
            PRESSURE_LABELS[k] for k in PRESSURE_LABELS
        ],
        "Japan": [
            f"{PRESSURE_SCORES['japan'][k]['score']}/5 — {PRESSURE_SCORES['japan'][k]['label']}"
            for k in PRESSURE_LABELS
        ],
        "Korea": [
            f"{PRESSURE_SCORES['korea'][k]['score']}/5 — {PRESSURE_SCORES['korea'][k]['label']}"
            for k in PRESSURE_LABELS
        ],
        "What Matters Most": [
            "Korea — intense local SVOD rivalry for content and subscribers",
            "Japan — strong free broadcaster ecosystem absorbs casual viewing",
            "Japan — YouTube/VTuber culture fragments attention from long-form",
        ],
    })
    st.dataframe(pressure_compare, use_container_width=True, hide_index=True)

    # Market-specific implications
    st.subheader("Japan — Strategic Implications")
    jp_summary = MARKET_SUMMARY["japan"]
    st.info(jp_summary["takeaway"])
    for impl in jp_summary["strategic_implications"]:
        st.markdown(f"- {impl}")

    st.subheader("Korea — Strategic Implications")
    kr_summary = MARKET_SUMMARY["korea"]
    st.info(kr_summary["takeaway"])
    for impl in kr_summary["strategic_implications"]:
        st.markdown(f"- {impl}")

    # Cross-market insights
    st.divider()
    st.subheader("Cross-Market Insights — Global Framework Adjustments")

    st.markdown("""
**Where global streaming frameworks most likely misread APAC:**

1. **Japan:** Overweighting premium SVOD rivalry, underweighting free substitution.
   The biggest competitive threat to paid streaming growth in Japan is not Disney+
   or Prime — it's TVer and ABEMA offering good-enough content for free.

2. **Korea:** Underweighting local premium competition. Global frameworks
   that treat Netflix as the dominant SVOD may miss that Tving and Wavve
   are legitimate, well-funded competitors with strong local content pipelines.

3. **Both markets:** Ignoring UGC attention share. YouTube and TikTok do not
   appear in traditional SVOD competitive analyses, but they absorb significant
   daily viewing time — especially on mobile, which is the primary screen in APAC.

**Implication for APAC content strategy:**

Content investment decisions in APAC should be evaluated not just against other
paid platforms, but against the full spectrum of attention competition. A title
that wins subscribers away from Tving in Korea serves a different strategic purpose
than a title that pulls viewers from TVer in Japan — even if both generate similar
viewing hours.
    """)

    st.divider()
    st.caption(
        "These implications are based on external data analysis and publicly available "
        "market information. Internal Netflix data would enable more precise "
        "competitive positioning assessment."
    )

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### About This Dashboard")
    st.markdown(
        "**APAC Streaming Competitive Intelligence**\n\n"
        "External-data-based framework analyzing three layers of "
        "competition in Japan and Korea:\n"
        "1. Premium SVOD\n"
        "2. Free / ad-supported streaming\n"
        "3. YouTube / UGC / short-form\n\n"
        "Built to demonstrate competitive intelligence and "
        "strategy analytics capability for APAC content markets."
    )
    st.markdown("---")
    st.markdown("### Framework")
    st.markdown(
        "Each market scored on three competitive pressure dimensions (1–5) "
        "with documented rationale. Scores are qualitative assessments, "
        "not statistical outputs."
    )
    st.markdown("---")
    st.markdown("### Data")
    st.markdown(
        "- Public sources only\n"
        "- Tier 1: Official disclosures\n"
        "- Tier 2: Market estimates\n"
        "- Tier 3: Proxy indicators\n"
        "- See assumptions.md for details"
    )
    st.markdown("---")
    st.markdown("### Limitations")
    st.markdown(
        "- No internal Netflix data\n"
        "- Qualitative pressure scoring\n"
        "- Japan + Korea only (MVP)\n"
        "- Point-in-time analysis\n"
        "- See README §7"
    )
