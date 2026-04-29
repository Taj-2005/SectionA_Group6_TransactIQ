# WildChat Analytics Platform
<!-- Project Overview -->

> **Turning 1M+ real-world AI conversations into operational intelligence.**  
> End-to-end analytics platform — Python ETL · NLP · Tableau BI · Behavioral Segmentation · Safety Monitoring

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Tableau](https://img.shields.io/badge/Tableau-Dashboard-E97627?style=flat-square&logo=tableau&logoColor=white)](https://public.tableau.com/views/WildChat_Analytics_Platform/ExecutiveSummary)
[![Dataset](https://img.shields.io/badge/Dataset-WildChat--1M-FFD21F?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/datasets/allenai/WildChat-1M)
[![License](https://img.shields.io/badge/License-Apache_2.0-green?style=flat-square)](LICENSE)

---

## The Problem

Conversational AI platforms generate millions of interactions daily. Yet most operators cannot answer basic questions:

- **Why do 47% of users abandon after one reply?**
- **Which geographies are driving disproportionate safety risk?**
- **How does response quality vary across languages, models, and prompt types?**
- **Which 8% of users are driving 59% of all engagement?**

Without structured analytics, these decisions default to instinct — resulting in missed retention opportunities, under-resourced safety teams, and model investments that miss the highest-impact segments.

---

## The Solution

A **two-layer analytics system** built on the AllenAI WildChat-1M dataset:

```
Raw WildChat-1M (1M+ conversations)
         │
         ▼
┌─────────────────────────────────┐
│   Python ETL + NLP Pipeline     │
│  ─────────────────────────────  │
│  Extract → Clean → Enrich →     │
│  Feature Engineer → Export      │
└─────────────────────────────────┘
         │
         ▼
  6 analysis-ready CSV datasets
         │
         ▼
┌─────────────────────────────────┐
│   Tableau Dashboard Suite       │
│  ─────────────────────────────  │
│  Executive · Operational ·      │
│  Safety & Trust                 │
└─────────────────────────────────┘
```

**Output:** 26 interactive visualizations across 3 dashboard modules, surfacing KPIs, anomalies, user segments, and safety signals — ready for product, safety, and executive stakeholders.

---

## Impact at a Glance

| Outcome                       | Metric                                   | Source                        |
| ----------------------------- | ---------------------------------------- | ----------------------------- |
| Retention lift potential      | **+15–25%** via turn-2 intervention      | Drop-off analysis             |
| Moderation overhead reduction | **~30%** via geo-risk tiering            | Toxicity heatmap              |
| Power-user concentration      | **Top 8% → 59% of turns**                | Segmentation model            |
| Language quality gap          | **0.5× unanswered rate** for non-English | Quality distribution          |
| Nocturnal risk window         | **2.8× elevated toxicity** at 10 PM–2 AM | Time-series anomaly detection |

---

## Key Findings

**1. Half of all sessions never go deeper than one exchange.**  
47% of conversations end at turn 2. Sessions with 8+ turns show 35% higher quality scores — making turn-2 retention the single highest-leverage product intervention.

**2. Geography and toxicity are completely decoupled from volume.**  
Germany (ranked 4th by volume) records a 16.97% toxicity rate — 5.3× the platform average. China, the largest market at 24.5% of sessions, sits at 1.10%. Safety investment that follows headcount misses the actual risk.

**3. GPT-4 is more capable and more adversarially targeted.**  
GPT-4 conversations score 31.7% higher on quality — and attract 63.7% more toxic interactions. Model upgrades and safety calibration cannot be decoupled.

**4. Non-English users receive a structurally inferior experience.**  
Chinese-language quality scores average 57% below English. Chinese and Russian speakers represent 35% of all sessions. This is a retention and equity problem, not a niche edge case.

**5. Eight percent of users drive sixty percent of platform engagement.**  
The concentration ratio exceeds standard Pareto distributions. Platform health depends on a thin cohort — and has no resilience mechanism if that cohort churns.

---

<!-- Core Architecture Details -->
## Architecture

### Pipeline Stages

| Stage                       | What It Does                                                                                         | Key Output                                 |
| --------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **1 · Extraction**          | Streams WildChat-1M via HuggingFace in 50K-row batches                                               | Raw conversation frames                    |
| **2 · Cleaning**            | Deduplication, type normalisation, timestamp standardisation, geo validation                         | Zero-null structured schema                |
| **3 · Text Preprocessing**  | Language detection (langdetect), VADER sentiment scoring, token counting                             | `language`, `avg_sentiment`, `token_count` |
| **4 · Feature Engineering** | Composite toxicity scoring, drop-off flagging, quality score derivation, per-IP behavioral metrics   | 12 engineered features                     |
| **5 · ML Analytics**        | K-Means prompt clustering (k=5), user segmentation, Z-score anomaly detection, daily KPI aggregation | 3 user segments, 5 prompt categories       |
| **6 · Export**              | 6 Tableau-ready CSVs with schema documentation                                                       | Production-ready datasets                  |

### Data Outputs

```
data/processed/
├── conversations_clean.csv   # 49,550 rows — primary analytical dataset
├── messages_sample.csv       # Message-level text + sentiment + quality
├── daily_kpis.csv            # 22-day time-series KPIs
├── geo_summary.csv           # Country-level aggregations (148 countries)
├── prompt_categories.csv     # Category distribution (K-Means output)
└── user_segments.csv         # Power / Regular / Casual user classification
```

---

## Dashboard Suite

Three interlocked modules. Each answers a specific set of operational questions.

### Executive Summary

_For: Product leadership, C-Suite_

| Chart                                                                 | Decision It Supports                          |
| --------------------------------------------------------------------- | --------------------------------------------- |
| 5 KPI Cards (Engagement, Drop-off, Toxicity, Turn Count, Repeat Rate) | Platform health at a glance                   |
| Weekly Engagement & Drop-off Trend (dual-axis)                        | Where and when engagement is degrading        |
| Prompt Category Mix (donut)                                           | Shifting user intent over time                |
| Top Geographies Table (volume + toxicity)                             | Where to focus growth vs. safety resources    |
| Model Version Performance (grouped bar)                               | GPT-3.5 vs. GPT-4 quality and risk trade-offs |
| Platform Health Radar (6 dimensions vs. target)                       | Where the largest investment gaps sit         |

### Operational Intelligence

_For: Product managers, ML engineers_

| Chart                                     | Decision It Supports                             |
| ----------------------------------------- | ------------------------------------------------ |
| Activity Heatmap (day × hour)             | When to staff moderation; when demand peaks      |
| Prompt Length vs. Quality (scatter)       | Optimal input zone for response quality          |
| Quality Score by Language (box plot)      | Which language populations need model investment |
| Session Duration Distribution (histogram) | Whether engagement breadth is improving          |
| Response Quality by Language (bar)        | Language equity gap — ranked and quantified      |
| User Cluster Explorer (scatter)           | Behavioral segmentation for targeting            |

### Safety & Trust

_For: Trust & safety teams, policy_

| Chart                                                           | Decision It Supports                                    |
| --------------------------------------------------------------- | ------------------------------------------------------- |
| Toxicity Rate + Z-Score Anomaly Overlay                         | Automated spike detection with statistical significance |
| Toxicity Concentration Heatmap (country × language)             | Precise geo-linguistic risk profiling                   |
| Sentiment Distribution by Category (diverging bar)              | Which prompt types generate negative emotional signals  |
| Policy Violation Trends (line)                                  | Whether harmful content is increasing or stable         |
| Safety KPI Cards (Toxicity %, Risk Window, Adversarial Cluster) | Safety posture in three numbers                         |

> **Live Dashboard →** [View on Tableau Public](https://public.tableau.com/views/WildChat_Analytics_Platform/ExecutiveSummary?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

---

## KPI Framework

**12 production metrics across 4 tiers.**

### Engagement

| Metric                     | Formula                       | Current    | Signal                      |
| -------------------------- | ----------------------------- | ---------- | --------------------------- |
| User Engagement Rate       | % conversations with >2 turns | 53%        | Above 45% target            |
| Conversation Drop-off Rate | % ending at turn ≤2           | 47%        | Critical intervention point |
| Avg Conversation Length    | AVG(turn_count)               | 5.87 turns | On track                    |
| Repeat User Rate           | Conversations / Unique IPs    | 4.23×      | Healthy                     |

### Quality

| Metric                 | Formula                                 | Current     | Signal                       |
| ---------------------- | --------------------------------------- | ----------- | ---------------------------- |
| Response Quality Score | Derived: length + diversity + coherence | 7.94 / 16.2 | GPT-4 gap: +31.7%            |
| Avg Prompt Length      | AVG(token_count) per session            | 133 tokens  | Sweet spot: 300–1,500        |
| Long Session Uplift    | Quality delta for 8+ turn sessions      | +35%        | High-value engagement signal |
| Language Parity Score  | Non-EN quality / EN quality             | 0.57×       | Equity gap — action required |

### Safety

| Metric                    | Formula                             | Current           | Signal                        |
| ------------------------- | ----------------------------------- | ----------------- | ----------------------------- |
| Toxicity Rate             | AVG(toxicity_score)                 | 3.19%             | Within range; spikes flagged  |
| Anomaly Index             | Z-score vs. 30-day rolling mean     | 2 spikes detected | Apr 15, Apr 21                |
| Nocturnal Risk Multiplier | Toxicity rate 22:00–02:00 / daytime | 2.8×              | Automated escalation required |

### Concentration

| Metric                   | Formula                  | Current | Signal                               |
| ------------------------ | ------------------------ | ------- | ------------------------------------ |
| Power User Concentration | % turns from top 10% IPs | 59%     | Fragility risk — Pareto beyond 80/20 |

---

## Dataset

| Property           | Detail                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------- |
| **Source**         | [AllenAI WildChat-1M](https://huggingface.co/datasets/allenai/WildChat-1M) via HuggingFace Hub    |
| **Scale**          | 1,000,000+ real-world ChatGPT conversations                                                       |
| **Models**         | GPT-3.5-Turbo, GPT-4 (multiple versions)                                                          |
| **Metadata**       | Country, language, timestamps, OpenAI moderation scores, model version                            |
| **Sample Used**    | ~50,000 conversations (April 2023 snapshot, stratified)                                           |
| **Key Challenges** | Nested JSON, 1M+ scale, label sparsity (<5% toxic), geographic skew (China 24.5%), VPN distortion |

---

## Tech Stack

| Layer                    | Tools                                                       |
| ------------------------ | ----------------------------------------------------------- |
| Data Processing          | Python 3.9+, pandas, NumPy                                  |
| Large-Scale Loading      | HuggingFace `datasets` (streaming mode)                     |
| NLP & Text               | NLTK, langdetect, VADER Sentiment, HuggingFace Transformers |
| ML & Analytics           | scikit-learn — K-Means, Gradient Boosting, Isolation Forest |
| Feature Engineering      | TF-IDF vectorisation, custom LOD aggregations               |
| Visualisation (Analysis) | Matplotlib, Seaborn                                         |
| Visualisation (BI)       | Tableau Desktop / Tableau Public                            |
| Orchestration            | Jupyter Notebooks → Airflow-ready modular structure         |
| Future Layer             | LangChain + OpenAI API (natural language query interface)   |

---

## Repository Structure

```
SectionA_Group6_WildChat/
│
├── README.md
├── requirements.txt
├── LICENSE
│
├── notebooks/
│   ├── 01_etl_pipeline/
│   │   └── WildChat_Notebook.ipynb       # 6-stage production pipeline
│   ├── 02_exploratory_data_analysis/
│   │   └── 02_eda.ipynb
│   └── 03_feature_engineering/
│       └── 03_features.ipynb
│
├── data/
│   ├── raw/                              # Immutable source extracts
│   ├── processed/                        # 6 analysis-ready CSVs
│   └── dictionaries/
│       └── data_dictionary.md
│
├── dashboards/
│   └── tableau/
│       ├── workbooks/                    # .twbx packaged workbook
│       ├── screenshots/                  # Dashboard exports
│       └── links/
│           └── dashboard_links.md
│
├── docs/
│   ├── guides/                           # Setup, user, developer guides
│   ├── architecture/
│   │   └── ARCHITECTURE.md
│   └── PRD/
│       └── PRD.pdf
│
└── reports/                              # Final deliverables + slides
```

---

## Quick Start

### Requirements

- Python 3.9+, 8 GB RAM minimum
- Jupyter Notebook or JupyterLab
- Tableau Desktop (edit) or [Tableau Public](https://public.tableau.com) (view)

### Setup

```bash
git clone <repo-url>
cd SectionA_Group6_WildChat
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### Run the Pipeline

```bash
cd notebooks/01_etl_pipeline
jupyter notebook WildChat_Notebook.ipynb
# Execute cells Stage 1 → Stage 6
# Runtime: ~5 min (100K sample) | ~2–3 hrs (full 1M)
# Outputs land in data/processed/
```

### Open Dashboards

```bash
# Tableau Desktop
open dashboards/tableau/workbooks/WildChat_Analytics_Platform.twbx

# Tableau Public (read-only)
# → see dashboards/tableau/links/dashboard_links.md
```

### Configuration

```python
# notebooks/01_etl_pipeline/WildChat_Notebook.ipynb — top cell
CFG = {
    "batch_size":     50_000,
    "sample_batches": 2,      # quick test (100K rows)
    "max_batches":    20,     # full run (1M rows)
    "kmeans_k":       5,
    "tfidf_max_feat": 5_000,
    "power_user_pct": 0.90,
    "toxicity_thresh":0.10,
}
```

---

## Business Questions Answered

| Question                                             | Where to Look                           |
| ---------------------------------------------------- | --------------------------------------- |
| What % of users disengage after 1–2 messages?        | Operational → Engagement Funnel         |
| Which hours and geographies drive unsafe activity?   | Safety → Toxicity Heatmap + Time-Series |
| How does conversation length correlate with quality? | Operational → Prompt Length Scatter     |
| What are the dominant prompt categories and trends?  | Executive → Prompt Category Mix         |
| Who are power users vs. casual users?                | Operational → User Cluster Explorer     |
| Which languages and regions are underserved?         | Safety → Geographic Heatmap             |
| Are there statistically anomalous toxicity spikes?   | Safety → Z-Score Anomaly Overlay        |

---

## Why This Project Stands Out

**Full production pipeline, not a notebook exercise.**  
The codebase is structured for Airflow orchestration, modular stage execution, and reproducible outputs — not sequential cell execution for a grade.

**Insight-to-decision traceability.**  
Every chart in the Tableau suite maps directly to a stated business question. Nothing is decorative.

**Statistical rigor on safety signals.**  
Toxicity monitoring uses Z-score anomaly detection with rolling baselines — not a static threshold. The platform flags what is statistically unusual, not just what crosses an arbitrary line.

**Honest scope.**  
The analysis documents what cannot be concluded — VPN distortion in geographic data, derived quality scores vs. user-rated satisfaction, the limits of a 22-day KPI window. Real analytics work includes its own constraints.

**Built for multiple stakeholders.**  
Executive, Operational, and Safety dashboards serve different audiences with different questions — not one dashboard trying to serve everyone and satisfying no one.

---

## Team

| Name                        | Role                | Core Contribution                                             |
| --------------------------- | ------------------- | ------------------------------------------------------------- |
| **Shaik Tajuddin**          | Project Lead        | End-to-end architecture, KPI framework, stakeholder alignment |
| **Gaurav Meena**            | Visualisation Lead  | Tableau dashboard design and BI system build                  |
| **Dakarapu Hemamdhar Nath** | Data Lead           | Dataset sourcing, schema design, pipeline coordination        |
| **Sushant Guri**            | Data & Quality Lead | ETL validation, data quality assurance, QA documentation      |
| **Jivit Rana**              | ETL Lead            | Python pipeline engineering, feature extraction, exports      |
| **Parthraj Singh Bhati**    | Analytics Lead      | EDA, statistical analysis, segmentation and anomaly modelling |
| **Samarth Chaudhary**       | Delivery Lead       | Report writing, slide deck, submission coordination           |

---

<!-- Additional Resources Links -->
## Links

| Resource        | URL                                                                                                                                                                                      |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Live Dashboard  | [Tableau Public](https://public.tableau.com/views/WildChat_Analytics_Platform/ExecutiveSummary?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link) |
| Dataset         | [WildChat-1M on HuggingFace](https://huggingface.co/datasets/allenai/WildChat-1M)                                                                                                        |
| Documentation   | [/docs](docs/)                                                                                                                                                                           |
| Data Dictionary | [data/dictionaries/data_dictionary.md](data/dictionaries/data_dictionary.md)                                                                                                             |
| Portfolio       | [Team Portfolio & Case Study](portfolio/)                                                                                                                                                |

---

_Built on the [AllenAI WildChat-1M](https://huggingface.co/datasets/allenai/WildChat-1M) dataset. Apache 2.0 licensed._
