# `dashboards/tableau/` — Tableau BI Workbooks & Assets

Tableau deliverables for Executive, Operational, and Safety stakeholders. Contains workbooks, published URLs, screenshots, and supporting design assets.

---

## 📁 Folder Contents

### `workbooks/`

**Tableau workbook files**

- **`WildChat_Analytics_Platform (1).twbx`**
  - Primary Tableau workbook
  - Contains all three dashboards (Executive, Operational, Safety)
  - Data source: `data/processed/conversations_clean.csv` + supporting CSVs
  - Tableau version: 2022.1+ (Desktop & Server compatible)
  - Size: ~50 MB (includes embedded data snapshots)
  - Last updated: [Maintenance date]

**File Management**:

- Regular backups stored in version control
- `.twbx` = Packaged workbook (workbook + data sources + images)
- `.twb` = Workbook only (requires separate live connections)
- For publishing: Export to `.twbx` for server deployment

---

### `links/`

**Published dashboard URLs and access information**

#### [dashboard_links.md](links/dashboard_links.md)

Links to published dashboards on Tableau Public / Tableau Server:

```markdown
## Executive Dashboard

- **Tableau Public**: https://public.tableau.com/views/WildChat_Analytics_Platform/ExecutiveSummary?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link
- **Tableau Server**: https://[server]/views/WildChat_Executive/
- **Last Updated**: [Date]
- **Refresh Cadence**: Daily

## Operational Dashboard

- **Tableau Public**: https://public.tableau.com/views/WildChat_Analytics_Platform/ExecutiveSummary?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link
- **Tableau Server**: https://[server]/views/WildChat_Operational/
- **Last Updated**: [Date]
- **Refresh Cadence**: Hourly

## Safety Dashboard

- **Tableau Public**: https://public.tableau.com/views/WildChat_Analytics_Platform/ExecutiveSummary?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link
- **Tableau Server**: https://[server]/views/WildChat_Safety/
- **Last Updated**: [Date]
- **Refresh Cadence**: Real-time (1h cache)
```

---

### `screenshots/`

**Dashboard exports for documentation & presentations**

- **`executive_dashboard.png`**
  - Full Executive dashboard export
  - Used in: README, project reports, stakeholder emails
  - Resolution: 1920×1080 (16:9)

- **`operational_dashboard.png`**
  - Full Operational dashboard (filters collapsed)
  - Used in: Documentation, onboarding materials

- **`safety_dashboard.png`**
  - Full Safety dashboard with example anomaly flags
  - Used in: Compliance reports, incident reviews

**How to Update**:

```
In Tableau:
  1. Open dashboard
  2. Ctrl+Alt+I (or Dashboard → Download Image)
  3. Save to screenshots/ with timestamp
  4. Commit to git
```

---

### `assets/`

**Design resources and supporting files**

#### `assets/colors/`

**WildChat Brand Color Palette**

```
Primary Colors:
  • Success (Engagement):  #28A745 | RGB(40, 167, 69)
  • Risk (Toxicity):       #DC3545 | RGB(220, 53, 69)
  • Neutral (Background):  #6C757D | RGB(108, 117, 125)
  • Accent (Highlights):   #007BFF | RGB(0, 123, 255)
  • Warning (Anomaly):     #FFC107 | RGB(255, 193, 7)

Secondary:
  • Light Gray:            #E9ECEF | RGB(233, 236, 239)
  • Dark Gray:             #495057 | RGB(73, 80, 87)
```

#### `assets/fonts/`

- **Header Font**: San Francisco (macOS) / Segoe UI (Windows)
- **Body Font**: San Francisco (macOS) / Segoe UI (Windows)
- **Monospace (Data)**: Monaco (macOS) / Courier New (Windows)

#### `assets/icons/`

- **engagement.svg** — Upward trend, conversation bubbles
- **toxicity.svg** — Alert, hazard symbol
- **quality.svg** — Star, checkmark
- **geography.svg** — Globe, pins
- **anomaly.svg** — Red flag, exclamation

#### `assets/templates/`

- **kpi_card_template.twbx** — Reusable KPI card design
- **heatmap_template.twbx** — Heatmap layout
- **funnel_template.twbx** — Conversion funnel structure

---

## 🔌 Data Source Connections

### Primary Connection

```
File: data/processed/conversations_clean.csv
Type: CSV (local file)
Refresh: Manual (after ETL pipeline run)
Location in Tableau: Data → [Right-click] → Edit Connection
Update Path: /data/processed/conversations_clean.csv
```

### Secondary Connections (Supporting Data)

| CSV                     | Purpose                  | Update Frequency |
| ----------------------- | ------------------------ | ---------------- |
| `daily_kpis.csv`        | KPI time-series trends   | Daily            |
| `geo_summary.csv`       | Geographic aggregates    | Daily            |
| `prompt_categories.csv` | Category breakdowns      | Daily            |
| `user_segments.csv`     | User cluster assignments | Weekly           |

### Connection Steps (First-Time Setup)

1. **Open Tableau Desktop**

   ```
   File → Open → dashboards/tableau/workbooks/WildChat_Analytics_Platform.twbx
   ```

2. **Update Data Connection** (if needed)

   ```
   Data menu → [Right-click CSV source] → Edit Connection
   Path: /data/processed/conversations_clean.csv
   ```

3. **Refresh Data**

   ```
   Data menu → [Right-click CSV source] → Refresh
   ```

4. **Verify Dashboards Load**
   - Executive, Operational, Safety dashboards appear in sheet tabs
   - All KPI cards show values
   - Filters respond to selection

---

## 🎨 Design Standards

### Layout Grid

- **Dashboard Canvas**: 12-column responsive grid
- **Margin**: 16px (all edges)
- **Component Spacing**: 8px between elements
- **Card Height**: 140px (KPI cards), variable (charts)

### Typography

| Usage           | Font           | Size | Weight  | Color   |
| --------------- | -------------- | ---- | ------- | ------- |
| Dashboard Title | SF Pro Display | 28px | Bold    | #000000 |
| Section Header  | SF Pro Display | 18px | Bold    | #495057 |
| KPI Label       | SF Pro Text    | 12px | Regular | #6C757D |
| KPI Value       | SF Mono        | 24px | Bold    | #000000 |
| Chart Axis      | SF Pro Text    | 11px | Regular | #6C757D |

### Visual Hierarchy

- **KPI Cards**: Bold, large numbers with trend arrows
- **Line Charts**: Prominent lines, subtle reference bands
- **Heatmaps**: Color intensity represents magnitude
- **Tables**: Alternating row colors for readability

---

## 🚀 Publishing & Deployment

### To Tableau Desktop (Local)

```bash
1. Edit workbook: dashboards/tableau/workbooks/WildChat_Analytics_Platform.twbx
2. Data → Refresh all
3. File → Save
4. Commit to git
```

### To Tableau Server

```bash
1. Open workbook in Tableau Desktop
2. Server → Publish as → [Select Project]
3. Check "Include external files" (for data sources)
4. Publish
5. Share URLs: dashboards/tableau/links/dashboard_links.md
```

### To Tableau Public

```bash
1. File → Export to Tableau Public
2. Create account (if needed)
3. Set visibility: Public or Private
4. Copy share URL
5. Update: dashboards/tableau/links/dashboard_links.md
```

---

## 🔄 Refresh & Maintenance Workflow

### Daily Refresh (Scheduled)

**Time**: 6 AM UTC daily

```bash
# On server or automation platform (e.g., cron, airflow):

1. Run ETL pipeline:
   python notebooks/ETL_PIPELINE_NOTEBOOK/WildChat_Notebook.ipynb

2. Update CSVs:
   cp data/processed/*.csv dashboards/tableau/data/

3. Refresh Tableau:
   tabcmd refreshextracts -s [server] -u [user] -p [password] \
     'WildChat Analytics Platform' \
     'Executive Dashboard' \
     'Operational Dashboard' \
     'Safety Dashboard'

4. Log completion & notify stakeholders
```

### Data Source Validation

```bash
# Weekly check (manual)

1. Compare row counts:
   wc -l data/processed/*.csv

2. Spot-check KPI values vs. ETL logs

3. Validate Tableau reflects current data:
   Last Refreshed timestamp in Data menu
```

### Quarterly Maintenance

- [ ] Review KPI thresholds vs. actual performance
- [ ] Audit data connections (redundant, slow, unused)
- [ ] Backup workbooks (git pull)
- [ ] Update screenshots for documentation

---

## 📚 Dashboard User Guides

### For Executives

```
1. Open Executive Dashboard
2. Review KPI cards (top row):
   - Engagement Rate: Should trend upward month-over-month
   - Drop-off Rate: Lower is better (target <35%)
   - Toxicity Rate: Should stay <5% (red alert if >6%)
3. Review trend line: Look for breakpoints or inflection points
4. Check Risk Indicator: Any red bands? Investigate with ops team
5. Drill-down to geographies: Click country for context
```

### For Analysts

```
1. Open Operational Dashboard
2. Set filters: Date range, model, country, category
3. View Engagement Funnel: Where is drop-off worst?
4. Check Geographic Heatmap: Any anomalies by region?
5. Review Model Comparison: Is GPT-4 outperforming GPT-3.5?
6. Export filtered data: Data → Export All
```

### For Safety Team

```
1. Open Safety Dashboard
2. Check Toxicity Time-Series: Any red anomaly bands?
3. Review Top-10 Unsafe Categories: What needs attention?
4. View Geographic Map: High-risk regions identified?
5. Export Compliance Trail: For regulatory review
```

---

## 🆘 Troubleshooting

| Issue                      | Solution                                                    |
| -------------------------- | ----------------------------------------------------------- |
| **Data not updating**      | Data → Refresh / Check file path / Re-run ETL pipeline      |
| **Filters not working**    | Dashboard → Edit Filter / Check field names match data      |
| **Slow dashboard**         | Data → Optimize Data Source / Reduce aggregation complexity |
| **Missing KPI cards**      | Verify calculated fields exist / Re-add formula             |
| **Charts appearing blank** | Data → Show Data / Check filters aren't too restrictive     |

---

## 📞 Support & Contact

**Dashboard Changes?**

- Contact: Visualization Lead (Gaurav Meena, `@Gaurav-meena95`)

**Data Issues?**

- Contact: Data Lead (`@Hemamdhar`, `@sushantguri`)

**Access Issues?**

- Contact: Project Lead (Shaik Tajuddin, `@Taj-2005`)

---

## 🔗 Related Resources

- [Dashboard Overview](../README.md)
- [Data Dictionary](../../data/dictionaries/data_dictionary.md)
- [ETL Pipeline](../../notebooks/ETL%20_PIPELINE_NOTEBOOK/README.md)
- [Root README](../../README.md)

---

**Last Updated**: [Maintenance date]
**Maintained By**: Visualization Lead
**Version**: 1.0
