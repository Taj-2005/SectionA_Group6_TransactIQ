# SectionA_Group6_DVA — Data Visualization & Analytics Capstone

## Overview

This repository is a **2-week, industry-style Data Visualization & Analytics (DVA) capstone** where the team acts as a **data consulting unit**:

Raw dataset → Python ETL → EDA + statistical analysis → KPI framework → Tableau dashboard → business recommendations

The project is designed to be **decision-centric** (insights and actions), not visualization-centric.

---

## Team members (roles)

- **Project Lead**: Shaik Tajuddin (`@Taj-2005`)
- **Visualization Lead**: Gaurav Meena (`@Gaurav-meena95`)
- **Data Lead**: Dakarapu Hemamdhar Nath (`@Hemamdhar`), Sushant Guri (`@sushantguri`)
- **ETL Lead**: Jivit Rana (`@Jivit87`)
- **Analysis Lead**: Parthraj Singh Bhati (`@parthrajsinghbhati`)
- **PPT & Quality Lead**: Samarth Chaudhary (`@iamsamarth1011`),  Sushant Guri(`@sushantguri`)
 

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

### Selected dataset (raw source)

- **Name**: Dirty Financial Transactions Dataset
- **Source**: [Kaggle — Dirty Financial Transactions Dataset](https://www.kaggle.com/datasets/alfarisbachmid/dirty-financial-transactions-dataset)
- **Raw-data rule**: download the dataset from Kaggle and place the file(s) into `data/raw/` **without modifying them** (no edits/cleaning to the source file). All transformations must happen in `data/processed/` via notebooks/scripts.

This repo includes **placeholders** and a full pipeline skeleton. Add the Kaggle dataset into `data/raw/` and update `docs/data_dictionary.md` once you confirm the raw schema.

---

## Architecture

- **Notebooks (workbooks)**: the primary analysis lives in `notebooks/01_extraction.ipynb` → `notebooks/05_final_load_prep.ipynb`
- **Root notebook wrappers**: `01_extraction.ipynb` → `05_final_load_prep.ipynb` exist only to satisfy the required repo shape; they point you to the real notebooks in `notebooks/`
- **Automation**: `scripts/etl_pipeline.py` runs a reproducible **raw → cleaned → Tableau export** pipeline

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

```text
SectionA_Group6_DVA/
  README.md
  01_extraction.ipynb
  02_cleaning.ipynb
  03_eda.ipynb
  04_statistical_analysis.ipynb
  05_final_load_prep.ipynb
  data/
    raw/
      dirty_financial_transactions.csv
    processed/
      (generated cleaned + Tableau-ready files go here; currently placeholders)
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
      (add dashboard screenshots here)
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

## What each folder/file contains

- **`data/raw/`**: the original dataset files (or a reproducible download script/notebook). Keep these **unchanged** once selected. This repo tracks `data/raw/dirty_financial_transactions.csv`.
- **`data/processed/`**: outputs generated by cleaning/ETL (e.g., `cleaned.csv`, `tableau_fact.csv`). These should be reproducible from `data/raw/`.
- **`docs/data_dictionary.md`**: dataset metadata + column definitions + KPI mappings (update this after finalizing schema).
- **`notebooks/`**: the real project notebooks, in the required order:
  - **`01_extraction.ipynb`**: loading + schema inspection + grain definition
  - **`02_cleaning.ipynb`**: cleaning policy + feature engineering + write `data/processed/`
  - **`03_eda.ipynb`**: exploration + visuals + insight hypotheses
  - **`04_statistical_analysis.ipynb`**: tests/models to support decisions
  - **`05_final_load_prep.ipynb`**: Tableau-friendly datasets (stable grain, dims/measures)
- **`01_extraction.ipynb` → `05_final_load_prep.ipynb` (repo root)**: lightweight wrappers (required by the submission checklist). Use the notebooks in `notebooks/` for actual work.
- **`scripts/etl_pipeline.py`**: CLI ETL skeleton to regenerate processed outputs from raw inputs.
- **`tableau/dashboard_links.md`**: Tableau Public URLs (replace placeholders with published links).
- **`tableau/screenshots/`**: dashboard screenshots (export from Tableau Public and add here).
- **`reports/`**: final submission PDFs (report + presentation).

---

## Setup instructions

### Prerequisites

- Python 3.10+
- Jupyter (or VSCode notebooks)

### Create environment and install deps

From the repo root:

```bash
cd SectionA_Group6_DVA
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
