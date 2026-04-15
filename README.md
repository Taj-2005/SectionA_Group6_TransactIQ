# SectionA_Group16_DVA — Data Visualization & Analytics Capstone (Production-Grade)

## Overview
This repository is a **2-week, industry-style Data Visualization & Analytics (DVA) capstone** where the team acts as a **data consulting unit**:

**Raw dataset → Python ETL → EDA + statistical analysis → KPI framework → Tableau dashboard → business recommendations**

The project is designed to be **decision-centric** (insights and actions), not visualization-centric.

---

## Problem statement (template — tailor to your dataset)
**Goal**: Identify the key drivers of business performance and quantify actionable levers (pricing, retention, operational efficiency, marketing ROI) using a messy real-world dataset.

**Primary outputs**:
- Clean, reproducible ETL pipeline
- KPI definitions + computation
- Statistical evidence (tests/models) that supports decisions
- Tableau dashboard(s) with executive + operational views
- Final report + presentation

---

## Dataset requirements (strict)
- **Raw** dataset with **≥ 5000 rows** and **≥ 8 columns**
- **Messy** attributes expected (missing values, inconsistent categories, mixed date formats, duplicates, outliers)
- Stored in `data/raw/` (or downloaded reproducibly by notebook/script)

This repo includes **placeholders** and a full pipeline skeleton. Replace the dataset in `data/raw/` with your chosen source and update the data dictionary.

---

## Architecture
- **Extraction**: load raw file(s), inspect schema, validate assumptions (`notebooks/01_extraction.ipynb`)
- **Cleaning/ETL**: dedupe, type normalization, missing value policy, feature engineering, export to `data/processed/` (`notebooks/02_cleaning.ipynb`)
- **EDA**: distributions, trends, segment comparisons, business insights (`notebooks/03_eda.ipynb`)
- **Statistical analysis**: hypothesis tests + regression/segmentation and interpretation in decision terms (`notebooks/04_statistical_analysis.ipynb`)
- **Final load prep**: KPI dataset shaped for Tableau, stable grain, dimensions/measures (`notebooks/05_final_load_prep.ipynb`)
- **Automation**: `scripts/etl_pipeline.py` for reproducible ETL and exports

---

## KPIs (starter framework — adjust to your business context)
Define **3–5 KPIs** that map to decisions. This starter set assumes a customer + transactions dataset; rename as needed.

- **Net Revenue**: \( \sum \text{revenue} - \sum \text{refunds} \)
  - **Decision link**: pricing & discount policy, refund management
- **Revenue Growth (MoM)**: \( \frac{R_t - R_{t-1}}{R_{t-1}} \)
  - **Decision link**: marketing allocation, demand planning
- **Retention Rate**: \( \frac{\#\text{customers active in }t \cap t-1}{\#\text{customers active in }t-1} \)
  - **Decision link**: lifecycle campaigns, onboarding improvements
- **Churn Rate**: \(1 - \text{Retention Rate}\)
  - **Decision link**: churn prevention, product roadmap
- **ARPU**: \( \frac{\text{Net Revenue}}{\#\text{active customers}} \)
  - **Decision link**: upsell/cross-sell strategy, pricing tiers

All KPI formulas + computation live in notebooks and are exported for Tableau.

---

## Tableau integration
- `tableau/dashboard_links.md` includes placeholder Tableau Public URLs.
- `tableau/screenshots/` contains placeholders for dashboard screenshots.

Dashboards should include:
- **Executive view**: KPI tiles, trends, top drivers, headline insights
- **Operational drill-down**: segment views, cohorts, categories, regions
- **Interactivity**: filters (date, segment, region/product), parameter controls

---

## Folder structure
```
SectionA_Group16_DVA/
  README.md
  data/
    raw/
    processed/
  notebooks/
    01_extraction.ipynb
    02_cleaning.ipynb
    03_eda.ipynb
    04_statistical_analysis.ipynb
    05_final_load_prep.ipynb
  scripts/
    etl_pipeline.py
  tableau/
    screenshots/
    dashboard_links.md
  reports/
    project_report.pdf
    presentation.pdf
  docs/
    data_dictionary.md
  .github/
    workflows/
      ci.yml
  .gitignore
  LICENSE
  requirements.txt
```

---

## Setup instructions
### Prerequisites
- Python 3.10+
- Jupyter (or VSCode notebooks)

### Create environment and install deps
From the repo root:
```bash
cd SectionA_Group16_DVA
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run notebooks
```bash
jupyter lab
```
Run notebooks in order: `01 → 05`.

### Run ETL pipeline (CLI)
```bash
python scripts/etl_pipeline.py --raw data/raw/dataset.csv --outdir data/processed
```

---

## Sample insight style (what “good” looks like)
- ❌ “Revenue dropped in Q3.”
- ✅ “Revenue dropped in Q3 primarily due to a **15% decline in repeat-customer orders** in Segment B; **targeted win-back campaigns** for Segment B could recover an estimated **$X** monthly net revenue, based on baseline ARPU and historical response rates.”

---

## Contribution guidelines (PR-based workflow)

### Branching model (simulate industry workflow)
- `main`: protected (only via PR)
- Feature branches:
  - `feature/extraction`
  - `feature/cleaning-etl`
  - `feature/eda`
  - `feature/stats-analysis`
  - `feature/tableau`
  - `docs/report-and-ppt`

### Commit message style
- Use meaningful, scoped messages:
  - `feat(etl): add schema validation and cleaning rules`
  - `docs: add data dictionary and KPI definitions`
  - `chore(ci): add lint workflow`

### Module ownership (starter)
- **Extraction**: `notebooks/01_extraction.ipynb`
- **Cleaning/ETL**: `notebooks/02_cleaning.ipynb`, `scripts/etl_pipeline.py`
- **EDA**: `notebooks/03_eda.ipynb`
- **Statistical analysis**: `notebooks/04_statistical_analysis.ipynb`
- **Final KPI + Tableau prep**: `notebooks/05_final_load_prep.ipynb`, `tableau/`
- **Docs & deliverables**: `docs/`, `reports/`

---

## Deliverables checklist
- [ ] Raw dataset added to `data/raw/` (or reproducible download)
- [ ] Cleaned dataset generated to `data/processed/`
- [ ] KPI dataset generated to `data/processed/tableau_kpi_dataset.csv`
- [ ] Tableau dashboard published and linked
- [ ] `docs/data_dictionary.md` finalized
- [ ] `reports/project_report.pdf` and `reports/presentation.pdf` replaced with final exports

