# `dashboards/` — BI & Analytics Visualizations

Business Intelligence and stakeholder-facing artifacts for the WildChat Analytics Platform. Contains Tableau workbooks, published links, screenshots, and supporting design assets.

---

## 📊 Overview

The dashboard suite translates raw analytics into **decision-ready visual intelligence** for three distinct audiences:

- **Executive Dashboard**: C-Suite, Product VP, Safety VP → KPIs, trends, risk overview
- **Operational Dashboard**: Product Managers, ML Engineers, Data Analysts → Detailed insights, filters, drill-downs
- **Safety Dashboard**: Safety & Trust Team, Policy & Legal, Compliance → Real-time toxicity monitoring, anomaly alerts

---

## 📁 Folder Structure

### `tableau/`

**Primary Tableau BI artifacts**

#### `tableau/workbooks/`

- **`WildChat_Analytics_Platform (1).twbx`** — Main Tableau workbook file
  - Contains all three dashboards (Executive, Operational, Safety)
  - Published data source connections to `data/processed/` CSVs
  - Optimized for Tableau Desktop (2022.1+) and Tableau Server

#### `tableau/links/`

- **[dashboard_links.md](tableau/links/dashboard_links.md)** — Published Tableau Public/Server URLs
  - Direct links for stakeholders without Tableau Desktop access
  - QR codes for mobile access
  - Update frequency and refresh schedules

#### `tableau/screenshots/`

- **`executive_dashboard.png`** — Executive dashboard export
- **`operational_dashboard.png`** — Operational dashboard export
- **`safety_dashboard.png`** — Safety dashboard export
- Used for README documentation, reports, and presentations

#### `tableau/assets/`

- **Color Palette**: WildChat brand colors (RGB/HEX)
- **Fonts**: Consistent typography across dashboards
- **Icons**: Custom safety, engagement, and KPI icons
- **Templates**: Reusable Tableau design components

---

## 📺 Dashboard Specifications

### Dashboard 1: Executive Overview

**Audience**: C-Suite, VPs | **Refresh**: Daily | **Default Time Range**: Last 90 days

#### Layout

```
┌─────────────────────────────────────────────────────────┐
│            KPI SUMMARY CARDS (Top Row)                  │
├──────────┬──────────┬──────────┬──────────┬──────────────┤
│Engagement│ Drop-off │Toxicity │ Avg Turn │Repeat Users │
│  Rate %  │  Rate %  │  Rate % │  Count   │    Rate %   │
└──────────┴──────────┴──────────┴──────────┴──────────────┘
│
├─────────────────────────────────────────────────────────┐
│ ENGAGEMENT TREND (Line Chart)                           │
│ • Weekly engagement rate over 6 months                  │
│ • Reference band for target threshold                   │
│ • Annotations: model changes, product launches          │
└─────────────────────────────────────────────────────────┘
│
├──────────────────────────┬────────────────────────────────┤
│ PROMPT CATEGORY DONUT    │ TOP-10 GEOGRAPHIES TABLE      │
│ • Current month split    │ • Country, volume, engagement │
│ • % change vs last month │ • Toxicity rate by country    │
└──────────────────────────┴────────────────────────────────┘
│
├─────────────────────────────────────────────────────────┐
│ RISK INDICATOR PANEL (Anomaly Dashboard)                │
│ • Gauge: Anomaly Index (Z-score vs 30-day rolling avg)  │
│ • Red = Z-score > 2.5 (investigation required)          │
│ • Top 3 anomalous dates with drill-down links           │
└─────────────────────────────────────────────────────────┘
```

#### KPI Cards

| Card                 | Metric                        | Formula                                          | Target | Meaning                                           |
| -------------------- | ----------------------------- | ------------------------------------------------ | ------ | ------------------------------------------------- |
| **Engagement Rate**  | % conversations with 3+ turns | (Conv ≥ 3 turns / Total Conv) × 100              | >70%   | Conversations sustaining meaningful interaction   |
| **Drop-off Rate**    | % ending at turn 1–2          | (Conv ≤ 2 turns / Total Conv) × 100              | <35%   | Early abandonment signal; highest-leverage metric |
| **Toxicity Rate**    | % with unsafe content         | (Conv flagged toxic / Total Conv) × 100          | <5%    | Safety compliance; automatic alert if >6%         |
| **Avg Turn Count**   | Mean conversation depth       | SUM(turns) / COUNT(conversations)                | >3.5   | Indicates response quality & user trust           |
| **Repeat User Rate** | % returning users             | (Users with 2+ session days / Total Users) × 100 | >60%   | Retention signal; product stickiness              |

---

### Dashboard 2: Operational Intelligence

**Audience**: PMs, ML Engineers, Analysts | **Refresh**: Hourly (near-real-time) | **Default Time Range**: Last 7 days

#### Interactive Filters (Always Visible)

- **Date Range**: Picker or preset (Today, Last 7 days, Last 30 days, Custom)
- **Model Version**: Single-select (gpt-3.5-turbo, gpt-4)
- **Country**: Multi-select by ISO code or region
- **Language**: Multi-select (Top 10 languages)
- **Toxicity Level**: Slider (0.0–1.0)
- **Prompt Category**: Multi-select (Coding, Factual, Creative, Emotional, Roleplay, Harmful, Other)
- **User Segment**: Single-select (Power Users, Task-Oriented, Casual, At-Risk, Adversarial)

#### Charts & Components

| Chart                                | Specification                                                                                                                                  |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Engagement Funnel**                | Bar chart: % conversations surviving each turn (1→10+). Stacked by prompt category. Filterable.                                                |
| **Geographic Heatmap**               | Choropleth world map colored by engagement rate. Click-through to country-level drill-down. Toggle: Engagement / Toxicity / Volume.            |
| **Activity Heatmap**                 | 7 days (rows) × 24 hours (columns). Dual heatmaps: volume & toxicity rate. Identifies high-risk time windows.                                  |
| **User Segment Scatter**             | X: avg session duration, Y: avg quality score. Points = user clusters. Color: cluster ID. Size: user volume. Tooltip: cluster characteristics. |
| **Model Version Comparison**         | Side-by-side bar chart: quality score, drop-off rate, toxicity rate by model.                                                                  |
| **Prompt Length vs Quality**         | Scatter plot: X = avg prompt length (tokens), Y = response quality score. Color: prompt category. Identifies optimal length ranges.            |
| **Quality Distribution by Language** | Box plot: response quality score distribution for top 10 languages. Shows quality variance & language gaps.                                    |
| **Category Trends**                  | Stacked area chart: weekly volume of each prompt category. Shows emerging use-case shifts.                                                     |

---

### Dashboard 3: Safety & Compliance Monitoring

**Audience**: Safety Team, Policy & Legal, Compliance | **Refresh**: Real-time (1-hour cache) | **Default Time Range**: Last 30 days

#### Layout & Components

| Component                  | Description                                                                                                              |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Toxicity Time-Series**   | Line chart: daily toxicity rate with anomaly bands. Red band = Z-score > 2.5. Clicking band shows anomaly detail.        |
| **Unsafe Prompt Top-10**   | Horizontal bar chart: top 10 prompt categories by unsafe flag frequency. Sortable, filterable by date range.             |
| **Geographic Safety Map**  | Choropleth: country-level toxicity concentration. Identifies high-risk regions.                                          |
| **Anomaly Detector**       | Table: flagged dates, anomaly score, contributing factors (e.g., spike in politics category, unusual hour pattern).      |
| **Compliance Audit Trail** | Sortable table: conversation_id, flag type, timestamp, category, reason, status (reviewed/pending/resolved). Exportable. |
| **Moderation Workload**    | KPI cards: flagged conversations (today/week/month), avg review time, backlog size.                                      |

---

## 🔧 Dashboard Configuration

### Data Connections

**Primary Data Source**: `data/processed/conversations_clean.csv`

```
Source:    Local file (update path: /data/processed/)
Format:    CSV
Update:    Manual refresh after ETL pipeline run
Location:  Right-click data source → Edit connection
```

**Supporting Data Sources**:

- `daily_kpis.csv` — Time-series KPI trends
- `geo_summary.csv` — Geographic aggregates
- `prompt_categories.csv` — Category breakdowns
- `user_segments.csv` — Cluster assignments

### Filter Relationships

```
All filters apply to:
  ├─ Engagement Trend
  ├─ Engagement Funnel
  ├─ Geographic Heatmap
  ├─ Activity Heatmap
  ├─ User Segment Scatter
  ├─ Model Comparison
  └─ All other charts
```

### Refresh Schedules

| Dashboard   | Refresh Frequency    | Trigger               |
| ----------- | -------------------- | --------------------- |
| Executive   | Daily (6 AM UTC)     | Manual ETL completion |
| Operational | Hourly               | Automated scheduler   |
| Safety      | Real-time (1h cache) | Continuous monitoring |

---

## 📈 KPI Definitions (Dashboard Reference)

All KPIs calculated in ETL pipeline; defined in detail in [Data Dictionary](../data/dictionaries/data_dictionary.md).

- **Engagement Rate**: % conversations with ≥3 turns (active interaction)
- **Drop-off Rate**: % ending at turn 1–2 (abandonment)
- **Toxicity Rate**: % flagged as containing unsafe content
- **Response Quality Score**: 0–10 heuristic (length + diversity + coherence)
- **Repeat User Rate**: % users returning on 2+ calendar days
- **Power User Concentration**: % conversation turns from top-10% users
- **Anomaly Index**: Z-score of daily toxicity vs. 30-day rolling mean

---

## 🎨 Visual Standards

### Color Palette (WildChat Brand)

| Element         | HEX       | RGB             | Usage                       |
| --------------- | --------- | --------------- | --------------------------- |
| Primary Success | `#28A745` | (40, 167, 69)   | Engagement, positive trends |
| Primary Risk    | `#DC3545` | (220, 53, 69)   | Drop-off, toxicity, alerts  |
| Neutral         | `#6C757D` | (108, 117, 125) | Background, neutral data    |
| Accent          | `#007BFF` | (0, 123, 255)   | KPI highlights, CTAs        |
| Warning         | `#FFC107` | (255, 193, 7)   | Anomalies, attention needed |

### Typography

- **Header**: San Francisco / Segoe UI, 20px, bold
- **Body**: San Francisco / Segoe UI, 12px, regular
- **Data**: Monaco / Courier New, 11px, monospace (numbers)

### Layout Standards

- **Margin**: 16px (all edges)
- **Dashboard Grid**: 12-column responsive
- **Card Spacing**: 8px between components
- **KPI Cards**: 140px height, rounded corners (8px)

---

## 🚀 How to Use

### View in Tableau Desktop

```bash
1. Open dashboards/tableau/workbooks/WildChat_Analytics_Platform.twbx
2. Select dashboard tab (Executive / Operational / Safety)
3. Use filters to explore data
4. Hover for tooltips; click for drill-downs
5. Refresh data: Data Source → Refresh
```

### View Online (Tableau Public)

See [dashboard_links.md](tableau/links/dashboard_links.md) for published URLs.

### Edit Dashboards

```bash
1. Install Tableau Desktop (2022.1+)
2. Open .twbx file
3. Edit sheets & dashboards
4. Update data connections if needed
5. Republish to Tableau Server/Public
```

### Update Data

```bash
# After running ETL pipeline
1. Run: notebooks/ETL\ _PIPELINE_NOTEBOOK/WildChat_Notebook.ipynb
2. Outputs: data/processed/conversations_clean.csv (+ others)
3. In Tableau: Data Source → Refresh
4. Dashboards auto-update
```

---

## 📋 Maintenance Checklist

- [ ] **Weekly**: Review Executive dashboard KPI trends
- [ ] **Daily**: Check Safety dashboard for anomalies
- [ ] **Monthly**: Validate data connections; compare Tableau vs. source CSVs
- [ ] **Quarterly**: Review KPI targets; adjust thresholds if needed
- [ ] **As Needed**: Update data sources after schema changes

---

## 🔗 Related Resources

- [Dashboard Design Specifications](tableau/README.md)
- [Data Dictionary](../data/dictionaries/data_dictionary.md)
- [ETL Pipeline](../notebooks/ETL%20_PIPELINE_NOTEBOOK/README.md)
- [Root README](../README.md)

---

## 📞 Support

**Dashboard Issues?**

- Check [Tableau troubleshooting guide](https://www.tableau.com/support/)
- Verify data source connections in `Data` menu
- Review server logs (if using Tableau Server)
- Open a GitHub issue for data-related questions

**Data Updates?**

- Re-run ETL notebook: `notebooks/ETL\ _PIPELINE_NOTEBOOK/WildChat_Notebook.ipynb`
- Refresh data source in Tableau
- Contact data lead for large-scale changes

**Questions?** See [Root README](../README.md) or contact the Visualization Lead.
