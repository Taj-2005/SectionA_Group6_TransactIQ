# Dashboard User Guide

## Overview

The **WildChat Analytics Platform** consists of three complementary Tableau dashboards, each designed for a specific audience and use case:

1. **Executive Dashboard** — Strategic overview for leadership
2. **Operational Dashboard** — Detailed analytics for product and ML teams
3. **Safety Dashboard** — Monitoring for trust and safety teams

All dashboards are **updated daily** and accessible online via [Tableau Public](https://public.tableau.com/views/WildChat_Analytics_Platform/ExecutiveSummary?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link).

<!-- Tableau Link -->
---

## 📊 Executive Dashboard

**Audience**: C-Suite, VP Product, VP Safety  
**Refresh**: Daily | **Primary Purpose**: Strategic decision-making

### Key Sections

#### KPI Summary Cards

- **Engagement Rate**: % of conversations with 3+ turns
- **Drop-off Rate**: % ending at turn 1–2
- **Toxicity Rate**: % conversations with unsafe content
- **Avg Turn Count**: Mean conversation length
- **Repeat User Rate**: % users returning for 2+ sessions

**How to Use**: Monitor trend badges (↑ ↓) to identify weekly performance changes.

#### Engagement Trend Chart

- Weekly engagement rate over past 6 months
- Target performance band (reference baseline)
- **Action**: Click a data point to drill into that week's details

#### Risk Indicator Panel

- **Anomaly Index**: Gauge showing current toxicity vs. 30-day baseline
- **Top 3 Anomalous Dates**: Dates requiring investigation
- **Action**: Click a date to view the Safety Dashboard for that date

#### Prompt Category Distribution

- Current month breakdown vs. prior month
- Side-by-side comparison
- **Action**: Identify which categories are trending up/down

#### Top-10 Geographies

- Country-level volume, engagement, toxicity
- Sortable by any metric
- **Action**: Click a country to drill into operational details

---

## 🔧 Operational Dashboard

**Audience**: Product Managers, ML Engineers, Data Analysts  
**Refresh**: Hourly (near-real-time) | **Primary Purpose**: Troubleshooting and optimization

### Key Features

#### Interactive Filters (Top of Dashboard)

- **Date Range**: Select any period (default: last 30 days)
- **Model Version**: Compare different model releases
- **Country**: Filter by geography
- **Language**: Multi-language analysis
- **Toxicity Level**: Focus on specific risk bands
- **Prompt Category**: Drill into specific intent types
- **User Segment**: Analyze user behavioral clusters

**Pro Tip**: Filters are linked — changing one updates all visualizations below.

#### Engagement Funnel

- Waterfall showing drop-off by conversation turn number
- Segment by category or cohort
- **Action**: Identify which turn has highest drop-off; target that turn for improvements

#### Geographic Heat Map

- World choropleth colored by engagement rate
- **Action**: Click a country to drill down into regional details
- Darker color = higher engagement

#### Hourly Activity Heatmap

- 7 days × 24 hours grid
- Color intensity = toxicity spike risk
- **Action**: Identify high-risk time windows for proactive moderation

#### User Segment Explorer

- 2D scatter plot from K-Means clustering (k=5)
- Each dot = user cluster
- Size = cluster volume; color = avg engagement
- **Action**: Hover over clusters to see demographic insights

#### Model Version Comparison

- Quality score, drop-off, toxicity by model release
- Side-by-side line chart
- **Action**: Identify which model performs best by metric

---

## 🛡️ Safety Dashboard

**Audience**: Safety & Trust Team, Policy & Legal  
**Refresh**: Real-time | **Primary Purpose**: Risk monitoring and compliance

### Key Sections

#### Toxicity Time-Series

- Daily toxicity rate over 90 days
- Anomaly bands (red = Z-score > 2.5)
- **Alert Trigger**: Red band = investigate immediately
- **Action**: Click anomalous date to drill into conversation-level details

#### Top Unsafe Prompt Categories

- Ranking of intent categories by flagged frequency
- **Action**: Identify categories requiring policy updates

#### Geographic Safety Map

- Country-level toxicity concentration
- Color intensity = toxicity risk level
- **Action**: Identify regions needing localized moderation policies

#### Anomaly Detector

- Automated flagging of unusual daily spikes
- **Alert Types**: Sudden increase, sustained elevation, unusual pattern
- **Action**: Review each flagged day in detail

#### Compliance Audit Trail

- Historical log of moderation flags
- Timestamp, conversation ID, toxicity score, resolution status
- **Action**: Export for regulatory compliance review

---

## 🎯 Common Use Cases

### "Why did engagement drop this week?"

1. Open **Executive Dashboard**
2. Click the drop in **Engagement Trend**
3. Note the date range
4. Switch to **Operational Dashboard**
5. Set Date Range filter to that week
6. Review **Engagement Funnel** — which turn has highest drop?
7. Check **Prompt Category Distribution** — did a category change?
8. Filter by Model Version — was a new model deployed?

### "Is there a toxicity issue?"

1. Open **Safety Dashboard**
2. Check **Toxicity Time-Series** for red anomaly bands
3. If red band detected, note the date
4. Click the date to drill into conversation-level analysis
5. Review **Top Unsafe Prompt Categories** — which types are flagged?
6. Use **Geographic Safety Map** to identify affected regions
7. Document findings in Compliance Audit Trail

### "How do I compare two model versions?"

1. Open **Operational Dashboard**
2. Use **Model Version Comparison** chart
3. Set Date Range to overlapping deployment period
4. Compare metrics: Quality, Drop-off, Toxicity
5. Filter by Prompt Category to identify category-specific performance

### "Which user segment should I focus on?"

1. Open **Operational Dashboard**
2. Scroll to **User Segment Explorer** (2D scatter plot)
3. Hover over clusters to see demographics
4. Click a cluster to filter all other visualizations
5. Review engagement and quality metrics for that segment
6. Drill into **Engagement Funnel** for segment-specific insights

---

## 📱 Mobile Access

Tableau dashboards are mobile-responsive. To view on phone/tablet:

1. Go to [Tableau Public](https://public.tableau.com/views/WildChat_Analytics_Platform/ExecutiveSummary?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
2. Tap the **Mobile** view option
3. Dashboard reflows for small screens

---

## 📋 Metric Definitions

For detailed KPI definitions, formulas, and data types:

- See: [KPI Framework](../../README.md#-kpi-framework-12-production-metrics)
- Reference: [Data Dictionary](../../data/dictionaries/data_dictionary.md)

---

## ❓ FAQ

**Q: How often are dashboards updated?**  
A: Executive and Safety dashboards update daily. Operational dashboard updates hourly for near-real-time insights.

**Q: Can I download the data?**  
A: Yes. Tableau allows exporting filtered views as CSV/PDF. Right-click any visualization and select "Download".

**Q: Can I share a filtered dashboard?**  
A: Yes. Set your filters, then copy the URL from your browser. The URL encodes all filter settings. Recipients will see your exact view.

**Q: How do I report a bug or request a feature?**  
A: Open a GitHub issue or contact the data team via [Contributors](../../README.md#-contributors--roles).

**Q: Is historical data available?**  
A: Yes. Use the Date Range filter to access any date from launch (see [data/README.md](../../data/README.md) for dataset dates).

---

## Next Steps

- Setup: [Installation Guide](SETUP.md)
- Development: [Developer Guide](DEVELOPER_GUIDE.md)
- Architecture: [System Design](../architecture/ARCHITECTURE.md)
