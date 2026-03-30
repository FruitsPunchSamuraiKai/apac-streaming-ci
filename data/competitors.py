"""
Competitor and market data for Japan and Korea streaming markets.
All data sourced from public reports, IR filings, and press coverage.

Data vintage: 2024-2025 (latest available public data)
Each entry includes: source, source_date, data_tier, confidence
"""

# ── Japan Competitors ────────────────────────────────────────────────────────

JAPAN_PREMIUM_SVOD = [
    {
        "platform": "Netflix",
        "type": "Global SVOD",
        "pricing_usd_mo": 7.0,
        "pricing_local": "¥790–¥1,980/mo",
        "content_focus": "Global originals + Japanese anime/drama",
        "local_content_strength": 4,
        "mobile_access": "Full",
        "monetization": "Subscription (ad-tier available)",
        "data_tier": 1,
        "source": "Netflix IR, pricing page",
        "source_date": "2025 Q4",
        "confidence": "high",
        "notes": "Largest global SVOD; strong anime catalog; growing JP originals slate",
    },
    {
        "platform": "Amazon Prime Video",
        "type": "Global SVOD (bundled)",
        "pricing_usd_mo": 4.2,
        "pricing_local": "¥600/mo (Prime bundle)",
        "content_focus": "Global + Japanese variety/sports",
        "local_content_strength": 3,
        "mobile_access": "Full",
        "monetization": "Subscription (Prime bundle)",
        "data_tier": 1,
        "source": "Amazon JP pricing page, press coverage",
        "source_date": "2025 Q4",
        "confidence": "high",
        "notes": "Price advantage via Prime bundle; growing sports rights (J-League)",
    },
    {
        "platform": "Disney+",
        "type": "Global SVOD",
        "pricing_usd_mo": 7.0,
        "pricing_local": "¥990/mo",
        "content_focus": "Disney/Marvel/Star Wars + some JP content",
        "local_content_strength": 2,
        "mobile_access": "Full",
        "monetization": "Subscription",
        "data_tier": 1,
        "source": "Disney+ JP pricing page",
        "source_date": "2025 Q4",
        "confidence": "high",
        "notes": "Strong global IP; limited JP original investment vs Netflix",
    },
    {
        "platform": "U-NEXT",
        "type": "Local SVOD",
        "pricing_usd_mo": 14.5,
        "pricing_local": "¥2,189/mo",
        "content_focus": "Broadest JP library (drama/anime/film/adult)",
        "local_content_strength": 5,
        "mobile_access": "Full",
        "monetization": "Subscription + points system",
        "data_tier": 2,
        "source": "U-NEXT official site; subscriber est. from Nikkei/press",
        "source_date": "2025 H1",
        "confidence": "medium",
        "notes": "Largest JP content library; premium pricing; ~4M subscribers (est.)",
    },
    {
        "platform": "Hulu Japan",
        "type": "Local SVOD (Nippon TV)",
        "pricing_usd_mo": 7.4,
        "pricing_local": "¥1,026/mo",
        "content_focus": "Nippon TV dramas + catch-up",
        "local_content_strength": 3,
        "mobile_access": "Full",
        "monetization": "Subscription",
        "data_tier": 2,
        "source": "Hulu JP pricing page; Nippon TV annual report",
        "source_date": "2025 H1",
        "confidence": "medium",
        "notes": "Owned by Nippon TV; strong catch-up drama catalog",
    },
]

JAPAN_FREE_ADSUPP = [
    {
        "platform": "TVer",
        "type": "Broadcaster catch-up (free)",
        "pricing_usd_mo": 0,
        "pricing_local": "Free (ad-supported)",
        "content_focus": "Major broadcaster dramas/variety (NHK/NTV/TBS/Fuji/TV Asahi)",
        "local_content_strength": 5,
        "mobile_access": "Full",
        "monetization": "Advertising",
        "data_tier": 2,
        "source": "TVer press releases; Nikkei reporting",
        "source_date": "2024 Q4",
        "confidence": "medium",
        "notes": "Joint venture of major JP broadcasters; ~30M MAU (2024 est.); fastest-growing free platform",
    },
    {
        "platform": "ABEMA",
        "type": "Free streaming + premium tier",
        "pricing_usd_mo": 0,
        "pricing_local": "Free / Premium ¥960/mo",
        "content_focus": "News, anime, reality, sports, originals",
        "local_content_strength": 4,
        "mobile_access": "Full (mobile-first design)",
        "monetization": "Advertising + subscription tier",
        "data_tier": 2,
        "source": "CyberAgent IR (quarterly earnings); ABEMA official",
        "source_date": "2025 Q3",
        "confidence": "medium",
        "notes": "CyberAgent-owned; mobile-first; strong in younger demographics; World Cup rights",
    },
    {
        "platform": "NHK Plus",
        "type": "Public broadcaster streaming",
        "pricing_usd_mo": 0,
        "pricing_local": "Free (with NHK subscription)",
        "content_focus": "NHK programming (news, documentary, drama)",
        "local_content_strength": 3,
        "mobile_access": "Full",
        "monetization": "Public broadcasting fee",
        "data_tier": 1,
        "source": "NHK official",
        "source_date": "2025",
        "confidence": "high",
        "notes": "Public broadcaster digital arm; limited but high-quality content",
    },
]

JAPAN_UGC = [
    {
        "platform": "YouTube",
        "type": "UGC + creator economy",
        "pricing_usd_mo": 0,
        "pricing_local": "Free / Premium ¥1,280/mo",
        "content_focus": "Everything — entertainment, education, music, vlogs",
        "local_content_strength": 5,
        "mobile_access": "Full",
        "monetization": "Advertising + subscription",
        "data_tier": 2,
        "source": "Google/Alphabet earnings; Statista Japan digital usage",
        "source_date": "2025 H1",
        "confidence": "medium",
        "notes": "Dominant video platform in Japan; ~70M+ monthly users; key attention competitor",
    },
    {
        "platform": "TikTok",
        "type": "Short-form UGC",
        "pricing_usd_mo": 0,
        "pricing_local": "Free",
        "content_focus": "Short-form entertainment, trends, music",
        "local_content_strength": 3,
        "mobile_access": "Mobile-native",
        "monetization": "Advertising",
        "data_tier": 3,
        "source": "Industry estimates; DataReportal Japan",
        "source_date": "2024",
        "confidence": "low",
        "notes": "Growing rapidly in Japan; ~28M MAU (est.); mobile-first attention competitor",
    },
]

# ── Korea Competitors ────────────────────────────────────────────────────────

KOREA_PREMIUM_SVOD = [
    {
        "platform": "Netflix",
        "type": "Global SVOD",
        "pricing_usd_mo": 5.5,
        "pricing_local": "₩5,500–₩17,000/mo",
        "content_focus": "Global originals + Korean originals (strongest pipeline)",
        "local_content_strength": 5,
        "mobile_access": "Full",
        "monetization": "Subscription (ad-tier available)",
        "data_tier": 1,
        "source": "Netflix IR, Korea pricing page",
        "source_date": "2025 Q4",
        "confidence": "high",
        "notes": "Market leader in Korea; massive K-drama/film investment; Squid Game effect",
    },
    {
        "platform": "Tving",
        "type": "Local SVOD (CJ ENM)",
        "pricing_usd_mo": 5.5,
        "pricing_local": "₩5,500–₩13,900/mo",
        "content_focus": "CJ ENM content (tvN, OCN) + originals + sports",
        "local_content_strength": 5,
        "mobile_access": "Full",
        "monetization": "Subscription",
        "data_tier": 2,
        "source": "CJ ENM IR; Korea Herald; subscriber est. from press",
        "source_date": "2025 H1",
        "confidence": "medium",
        "notes": "Strongest local competitor; CJ ENM content pipeline; ~8M subscribers (est.)",
    },
    {
        "platform": "Wavve",
        "type": "Local SVOD (KBS/MBC/SBS + SK Telecom)",
        "pricing_usd_mo": 5.5,
        "pricing_local": "₩5,500–₩13,900/mo",
        "content_focus": "Broadcaster content + originals + live TV",
        "local_content_strength": 4,
        "mobile_access": "Full",
        "monetization": "Subscription + live TV",
        "data_tier": 2,
        "source": "SK Telecom IR; Korea JoongAng Daily",
        "source_date": "2025 H1",
        "confidence": "medium",
        "notes": "Joint venture of 3 major broadcasters + SK Telecom; ~5M subscribers (est.)",
    },
    {
        "platform": "Coupang Play",
        "type": "Local SVOD (bundled with Rocket WOW)",
        "pricing_usd_mo": 6.0,
        "pricing_local": "₩7,890/mo (Rocket WOW)",
        "content_focus": "Sports (K-League, international football) + originals",
        "local_content_strength": 3,
        "mobile_access": "Full",
        "monetization": "Subscription (e-commerce bundle)",
        "data_tier": 2,
        "source": "Coupang SEC filings; Korea press coverage",
        "source_date": "2025 H1",
        "confidence": "medium",
        "notes": "Coupang bundle strategy; aggressive sports rights; growing rapidly",
    },
    {
        "platform": "Disney+",
        "type": "Global SVOD",
        "pricing_usd_mo": 6.0,
        "pricing_local": "₩9,900/mo",
        "content_focus": "Disney/Marvel/Star Wars + some Korean content",
        "local_content_strength": 2,
        "mobile_access": "Full",
        "monetization": "Subscription",
        "data_tier": 1,
        "source": "Disney+ Korea pricing page",
        "source_date": "2025 Q4",
        "confidence": "high",
        "notes": "Some Korean originals but struggling vs local competitors",
    },
    {
        "platform": "Amazon Prime Video",
        "type": "Global SVOD (bundled)",
        "pricing_usd_mo": 3.5,
        "pricing_local": "₩5,900/mo (Prime bundle)",
        "content_focus": "Global content + limited Korean content",
        "local_content_strength": 1,
        "mobile_access": "Full",
        "monetization": "Subscription (Prime bundle)",
        "data_tier": 1,
        "source": "Amazon Korea pricing page",
        "source_date": "2025 Q4",
        "confidence": "high",
        "notes": "Limited Korean content investment; Prime bundle value play",
    },
]

KOREA_FREE_ADSUPP = [
    {
        "platform": "Samsung TV Plus",
        "type": "FAST (free ad-supported TV)",
        "pricing_usd_mo": 0,
        "pricing_local": "Free",
        "content_focus": "Linear channels, news, entertainment",
        "local_content_strength": 2,
        "mobile_access": "Samsung devices",
        "monetization": "Advertising",
        "data_tier": 3,
        "source": "Samsung press; industry commentary",
        "source_date": "2024",
        "confidence": "low",
        "notes": "Pre-installed on Samsung TVs; limited but growing in Korea",
    },
    {
        "platform": "Broadcaster apps (KBS/MBC/SBS)",
        "type": "Broadcaster catch-up (partial free)",
        "pricing_usd_mo": 0,
        "pricing_local": "Free (recent episodes) / paid archive",
        "content_focus": "Broadcaster dramas, variety, news",
        "local_content_strength": 4,
        "mobile_access": "Full",
        "monetization": "Advertising + partial paywall",
        "data_tier": 3,
        "source": "App store listings; Korea press",
        "source_date": "2024",
        "confidence": "low",
        "notes": "Less unified than Japan's TVer; content increasingly funneled to Wavve",
    },
]

KOREA_UGC = [
    {
        "platform": "YouTube",
        "type": "UGC + creator economy",
        "pricing_usd_mo": 0,
        "pricing_local": "Free / Premium ₩14,900/mo",
        "content_focus": "Entertainment, K-pop, gaming, education",
        "local_content_strength": 5,
        "mobile_access": "Full",
        "monetization": "Advertising + subscription",
        "data_tier": 2,
        "source": "Google/Alphabet earnings; DataReportal Korea",
        "source_date": "2025 H1",
        "confidence": "medium",
        "notes": "Extremely dominant in Korea; ~45M monthly users; top video app by time spent",
    },
    {
        "platform": "TikTok",
        "type": "Short-form UGC",
        "pricing_usd_mo": 0,
        "pricing_local": "Free",
        "content_focus": "Short-form entertainment, K-pop, trends",
        "local_content_strength": 3,
        "mobile_access": "Mobile-native",
        "monetization": "Advertising",
        "data_tier": 3,
        "source": "Industry estimates; DataReportal Korea",
        "source_date": "2024",
        "confidence": "low",
        "notes": "Strong growth in Korea; particularly popular with younger demographics",
    },
]

# ── Competitive Pressure Scores (with sub-signal decomposition) ──────────────

PRESSURE_SCORES = {
    "japan": {
        "premium_svod": {
            "score": 3,
            "label": "Moderate",
            "sub_signals": {
                "local_premium_strength": {"score": 3, "note": "U-NEXT strong but niche; Hulu JP limited"},
                "bundle_advantage": {"score": 3, "note": "Prime bundle pricing is competitive"},
                "local_originals_depth": {"score": 2, "note": "No local SVOD matches Netflix JP originals"},
            },
            "rationale": (
                "Several premium SVOD options exist (Netflix, Prime, Disney+, U-NEXT, Hulu), "
                "but the market does not appear as intensely contested as Korea within this comparison. "
                "U-NEXT serves a niche (broadest library, premium price). Prime benefits from bundle pricing. "
                "No single local SVOD directly challenges Netflix's original content strategy."
            ),
        },
        "free_substitution": {
            "score": 4,
            "label": "High",
            "sub_signals": {
                "broadcaster_catchup_strength": {"score": 5, "note": "TVer ~30M MAU, all major broadcasters"},
                "fast_free_penetration": {"score": 4, "note": "ABEMA strong in younger demographics"},
                "free_content_expectation": {"score": 4, "note": "Decades of dominant broadcast TV culture"},
            },
            "rationale": (
                "TVer (~30M MAU est.) provides free access to content from all major broadcasters, "
                "creating strong substitution for casual viewing. ABEMA adds free anime, reality, "
                "and sports. Japanese consumers have strong free-content expectations from decades "
                "of dominant broadcast TV culture. This appears to be the most underweighted competitive "
                "force in Japan if using a North American-style framework."
            ),
        },
        "ugc_attention": {
            "score": 4,
            "label": "High",
            "sub_signals": {
                "mobile_video_share": {"score": 4, "note": "~65% video on mobile (est.)"},
                "youtube_dominance": {"score": 5, "note": "~70M+ monthly users"},
                "shortform_intensity": {"score": 3, "note": "TikTok growing but not yet dominant"},
            },
            "rationale": (
                "YouTube reaches an estimated 70M+ monthly users in Japan — more than any single streaming "
                "platform. Japanese YouTube culture is strong (VTubers, variety content, music). TikTok growing "
                "rapidly in younger demographics. Mobile-first consumption patterns amplify short-form "
                "and UGC content accessibility. Significant attention fragmentation away from "
                "long-form paid content."
            ),
        },
    },
    "korea": {
        "premium_svod": {
            "score": 5,
            "label": "Very High",
            "sub_signals": {
                "local_premium_strength": {"score": 5, "note": "Tving ~8M, Wavve ~5M, Coupang Play growing"},
                "bundle_advantage": {"score": 4, "note": "Coupang Rocket WOW bundle, telco bundles"},
                "local_originals_depth": {"score": 5, "note": "Tving/Wavve invest heavily in K-originals"},
            },
            "rationale": (
                "Korea appears to have among the most intense premium SVOD competition in APAC "
                "within the JP/KR comparison. Tving (CJ ENM, ~8M subs est.), Wavve (broadcaster JV, "
                "~5M subs est.), and Coupang Play (e-commerce bundle) all invest heavily in Korean originals. "
                "Netflix faces direct competition for talent, content rights, and subscriber attention "
                "from well-funded local platforms with deep content pipelines."
            ),
        },
        "free_substitution": {
            "score": 2,
            "label": "Low",
            "sub_signals": {
                "broadcaster_catchup_strength": {"score": 2, "note": "Fragmented apps, content shifting to Wavve"},
                "fast_free_penetration": {"score": 2, "note": "Samsung TV Plus limited"},
                "free_content_expectation": {"score": 2, "note": "Korean consumers more accustomed to paying"},
            },
            "rationale": (
                "Korea lacks a unified free streaming platform equivalent to Japan's TVer. "
                "Broadcaster apps offer partial free access but content is increasingly funneled "
                "to paid platforms (Wavve). Samsung TV Plus exists but has limited local content. "
                "Korean consumers appear more accustomed to paying for premium content, partly driven "
                "by strong K-drama/film culture and willingness to pay for quality originals."
            ),
        },
        "ugc_attention": {
            "score": 3,
            "label": "Moderate",
            "sub_signals": {
                "mobile_video_share": {"score": 5, "note": "~72% video on mobile (est.)"},
                "youtube_dominance": {"score": 4, "note": "~45M monthly users"},
                "shortform_intensity": {"score": 3, "note": "K-pop clip culture complements rather than substitutes"},
            },
            "rationale": (
                "YouTube is dominant in Korea (~45M monthly users est.) and K-pop content drives massive "
                "engagement. However, YouTube in Korea appears to function more as a complement to premium "
                "streaming (clip culture, behind-the-scenes, fan content) rather than a direct "
                "substitute for long-form drama viewing. TikTok is growing but appears less disruptive "
                "to paid streaming than in Japan."
            ),
        },
    },
}

# ── APAC Nuance Data ─────────────────────────────────────────────────────────

APAC_NUANCE = {
    "japan": {
        "mobile_video_share_pct": 65,
        "smartphone_penetration_pct": 85,
        "avg_commute_minutes": 48,
        "free_streaming_penetration": "High — TVer, ABEMA widely used",
        "broadcast_tv_culture": "Very strong — decades of dominant broadcast habit",
        "ugc_creator_ecosystem": "Strong — VTubers, variety YouTubers, music",
        "paid_content_willingness": "Moderate — strong free expectations",
        "data_tier": "Mix of Tier 1-2",
        "source": "MIC Japan telecom surveys; Statista; DataReportal",
        "notes": (
            "Japan's streaming market cannot be understood without accounting for "
            "the strength of free broadcast/digital content and mobile-first viewing. "
            "Global frameworks that assume paid SVOD is the primary video consumption "
            "mode may significantly understate competitive pressure in Japan."
        ),
    },
    "korea": {
        "mobile_video_share_pct": 72,
        "smartphone_penetration_pct": 97,
        "avg_commute_minutes": 58,
        "free_streaming_penetration": "Low-Moderate — less unified free ecosystem",
        "broadcast_tv_culture": "Moderate — younger audiences shifted to streaming",
        "ugc_creator_ecosystem": "Strong — K-pop, gaming, lifestyle",
        "paid_content_willingness": "High — strong K-content premium culture",
        "data_tier": "Mix of Tier 2-3",
        "source": "KISDI Korea media surveys; Statista; DataReportal",
        "notes": (
            "Korea appears to be among the most premium-competitive SVOD markets in APAC "
            "within this comparison. The real competitive challenge appears to be direct "
            "rivalry from well-funded local platforms with strong content pipelines. "
            "Mobile-first behavior is even more pronounced than Japan due to higher "
            "smartphone penetration and longer commute times."
        ),
    },
}

# ── Market Summary ───────────────────────────────────────────────────────────

MARKET_SUMMARY = {
    "japan": {
        "headline": "Free + UGC pressure appears to outweigh premium SVOD rivalry",
        "takeaway": (
            "In Japan, competitive pressure appears not primarily premium SVOD rivalry "
            "but structural substitution from strong free viewing ecosystems (TVer, ABEMA) "
            "and attention fragmentation (YouTube, TikTok). Global paid-streaming frameworks "
            "that focus only on Netflix vs. Disney+ vs. Prime may miss the most important "
            "competitive dynamic in this market."
        ),
        "strategic_implications": [
            "Content strategy must compete not just with other paid platforms but with free broadcaster content — especially for casual drama/variety viewing",
            "Anime remains a key differentiator in Japan; it is harder for free platforms to match exclusive anime originals investment",
            "Mobile-optimized content discovery matters more than in Western markets given mobile-first viewing patterns",
            "Marketing and positioning should emphasize exclusive value that free platforms cannot replicate",
        ],
    },
    "korea": {
        "headline": "Intense premium local competition appears to define the market",
        "takeaway": (
            "In Korea, the primary competitive challenge appears to be direct rivalry from well-funded "
            "local SVOD platforms (Tving, Wavve, Coupang Play) that compete aggressively "
            "for Korean original content, talent, and IP. Free substitution appears less of a factor. "
            "Netflix's competitive advantage may lie in global distribution reach for Korean content "
            "(export value) and global original content that local platforms cannot offer."
        ),
        "strategic_implications": [
            "Content investment efficiency matters more in Korea — local competitors can match or exceed spending on Korean originals",
            "Netflix's unique value proposition may be bi-directional: bringing global content to Korea AND giving Korean content global distribution",
            "Sports rights (K-League, football) are an emerging battleground — Coupang Play and Tving are investing aggressively",
            "Talent and IP acquisition competition appears fiercer than in Japan; relationship management is strategic",
        ],
    },
}
