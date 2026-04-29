# 📓 WildChat Analytics Notebooks

> **From raw conversations to operational insights**  
> Three-stage analytical pipeline transforming 1M+ WildChat conversations into structured datasets, statistical findings, and Tableau-ready exports.

---

## 🎯 Overview

This directory contains the complete analytical workflow for the WildChat Analytics Platform:

```
Raw Data (HuggingFace)
    │
    ├──→ [01] ETL Pipeline
    │       Extract • Clean • Process • Feature Engineer
    │
    ├──→ [02] Exploratory Data Analysis
    │       Descriptive Statistics • Business Insights • KPIs
    │
    └──→ [03] Feature Engineering & Statistical Validation
            Hypothesis Testing • Predictive Modeling • Statistical Rigor
```

Each notebook is **independent and modular** — they can be executed in sequence, or specific stages can be re-run without reprocessing upstream data.

---

## 📂 Notebook Structure

### **[01] ETL Pipeline & Data Processing**

**File**: `01_etl_pipeline/WildChat_Notebook.ipynb`

**Purpose**: Foundation stage — converts 1M+ raw conversations into clean, structured, analysis-ready datasets.

**Pipeline Stages**:

1. **Extraction** — Stream from HuggingFace API in 50K-row batches
2. **Cleaning** — Deduplication, type normalization, null handling, timestamp standardization
3. **Text Preprocessing** — Language detection, sentiment scoring, token counting, text cleaning
4. **Feature Engineering** — Quality scores, toxicity detection, anomaly flagging, aggregation
5. **ML Analytics** — K-means prompt clustering (k=5), user segmentation, KPI aggregation
6. **Export** — 6 Tableau-ready CSVs with full schema documentation

**Key Outputs**:

- `conversations_clean.csv` — Deduplicated, normalized conversations
- `messages_sample.csv` — Individual message-level records
- `daily_kpis.csv` — Time-series performance metrics
- `geo_summary.csv` — Geographic distribution and toxicity heatmaps
- `prompt_categories.csv` — Clustered prompt archetypes
- `wildchat_combined_master.csv` — Master dataset with all engineered features

**Scale**: ~1M conversations processed in streaming mode (memory-efficient, ~2 hours runtime)

---

### **[02] Exploratory Data Analysis (EDA)**

**File**: `02_exploratory_data_analysis/02_eda.ipynb`

**Purpose**: Produces executive KPIs, operational insights, and safety metrics from processed data.

**3-Part Analysis Structure**:

#### Part 1: Executive Summary

- Global KPIs (Quality Score: 7.94/10, Tokens: 2.3M+, Conversations: 50,516)
- Geographic distribution (Top 5: China, USA, Russia, Germany, France)
- Trend analysis (volume vs. token complexity over time)

#### Part 2: Operational Intelligence

- **Model Performance**: GPT-4 (avg quality: 9.44) vs GPT-3.5-turbo (7.17) — 31.7% quality premium
- **Language Support**: Coverage across 50+ languages with quality variance analysis
- **User Segmentation**: Power users (top 8% = 41% of activity) vs. casual/at-risk cohorts
- **Conversation Depth**: Session abandonment (47% at turn 2), engagement drivers

#### Part 3: Safety & Trust

- Toxicity rate by geography (Germany: 16.97% vs platform avg: 3.2%)
- Temporal anomalies (Nocturnal window: 10 PM–2 AM = 2.8× elevated risk)
- Prompt category risk profiling (safety signals by content type)
- Demographic fairness analysis (language, geography equity gaps)

**Key Visualizations**: 18+ interactive plots (heatmaps, time-series, distributions, scatter plots)

---

### **[03] Feature Engineering & Statistical Validation**

**File**: `03_feature_engineering/03_features.ipynb`

**Purpose**: Statistical validation and predictive model development — transitions from descriptive analysis to actionable predictions.

**3-Part Analytical Structure**:

#### Part 1: Statistical Validations

- **Independent T-Tests** — GPT-4 vs GPT-3.5-turbo quality differences (p < 0.001, highly significant)
- **One-Way ANOVA** — Turn count variance across models (F-stat: 2567.97, p < 0.001)
- **Chi-Square Tests** — Toxicity independence across prompt categories (strong association detected)

#### Part 2: Operational Drivers

- **Sentiment → Session Depth** correlation (frustration threshold: sentiment < -0.3 by turn 3 = 78% drop-off)
- **Quality by Language** box-plots identifying underperforming languages
- **Prompt Length → Quality** relationship analysis (optimal range identification)

#### Part 3: Predictive Modeling

- Regression models predicting conversation quality from input features
- Feature importance ranking and coefficient analysis
- Model performance metrics (R², RMSE, MAE)

**Key Outputs**: Statistical findings, model coefficients, predictive scores, actionable recommendations

---

## 🚀 Quick Start

### Prerequisites

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Running the Notebooks

**Option 1: Sequential Execution (Recommended for first run)**

```bash
# Run all three notebooks in order
jupyter notebook 01_etl_pipeline/WildChat_Notebook.ipynb
jupyter notebook 02_exploratory_data_analysis/02_eda.ipynb
jupyter notebook 03_feature_engineering/03_features.ipynb
```

**Option 2: Using processed data (skip ETL)**

```bash
# If ETL has already been run, jump to analysis
jupyter notebook 02_exploratory_data_analysis/02_eda.ipynb
```

**Option 3: Programmatic execution**

```python
import subprocess
notebooks = [
    "01_etl_pipeline/WildChat_Notebook.ipynb",
    "02_exploratory_data_analysis/02_eda.ipynb",
    "03_feature_engineering/03_features.ipynb"
]
for nb in notebooks:
    subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", nb])
```

---

## 📊 Data Flow Diagram

```
HuggingFace WildChat-1M
         │
         ├─→ [NOTEBOOK 01: ETL]
         │   ├─ Extract raw conversations
         │   ├─ Clean & normalize
         │   ├─ Engineer features
         │   └─ Export 6 CSVs
         │
         └─→ data/processed/
             ├─ conversations_clean.csv
             ├─ messages_sample.csv
             ├─ daily_kpis.csv
             ├─ geo_summary.csv
             ├─ prompt_categories.csv
             └─ wildchat_combined_master.csv
                      │
                      ├─→ [NOTEBOOK 02: EDA]
                      │   ├─ Descriptive statistics
                      │   ├─ Executive KPIs
                      │   ├─ 18+ visualizations
                      │   └─ Business insights
                      │
                      └─→ [NOTEBOOK 03: Feature Engineering]
                          ├─ Statistical tests
                          ├─ Hypothesis validation
                          ├─ Predictive models
                          └─ Actionable recommendations
```

---

## 🔑 Key Insights Across Notebooks

| Finding                                   | Notebook      | Impact                                       |
| ----------------------------------------- | ------------- | -------------------------------------------- |
| **47% session drop-off at turn 2**        | [02] EDA      | Highest-leverage retention intervention      |
| **GPT-4 quality premium: +31.7%**         | [03] Features | Model cost-benefit justification             |
| **Germany toxicity: 5.3× platform avg**   | [02] EDA      | Geographic safety risk tiering               |
| **Top 8% of users = 59% of engagement**   | [02] EDA      | Platform concentration risk                  |
| **Chinese users: -57% quality scores**    | [02] EDA      | Language equity & retention gap              |
| **t-statistic (GPT-4 vs 3.5): p < 0.001** | [03] Features | Statistically significant quality difference |

---

## 📦 Output Artifacts

### Processed Data (Generated by Notebook 01)

All files located in `data/processed/`:

| File                           | Records | Purpose                                        |
| ------------------------------ | ------- | ---------------------------------------------- |
| `conversations_clean.csv`      | ~50K    | Deduplicated conversations with all features   |
| `messages_sample.csv`          | ~290K   | Individual messages for message-level analysis |
| `daily_kpis.csv`               | 365+    | Time-series KPIs (volume, quality, toxicity)   |
| `geo_summary.csv`              | 130+    | Geographic metrics (country-level aggregates)  |
| `prompt_categories.csv`        | ~50K    | Clustered prompts with category labels         |
| `wildchat_combined_master.csv` | ~50K    | Master dataset with all engineered features    |

### Documentation

- `data/dictionaries/DATA_DICTIONARY.md` — Complete schema documentation
- `docs/guides/DEVELOPER_GUIDE.md` — Technical implementation details
- `docs/guides/USER_GUIDE.md` — End-user documentation

### Tableau Dashboards (Generated from processed data)

- **Executive Summary** — C-suite KPIs and trends
- **Operational Intelligence** — Model performance, user segments, language coverage
- **Safety & Trust** — Toxicity heatmaps, anomaly detection, temporal patterns

---

## 🛠️ Configuration & Customization

### Environment Variables (Optional)

Create a `.env` file to customize pipeline behavior:

```bash
# Data extraction
BATCH_SIZE=50000              # HuggingFace extraction batch size
SAMPLE_SIZE=50516             # Limit dataset size (omit for full 1M)

# Processing
MIN_TOKEN_COUNT=5             # Minimum tokens per conversation
LANGUAGE_THRESHOLD=0.95       # Language detection confidence

# Feature engineering
QUALITY_MODEL="heuristic"     # Quality scoring approach
CLUSTERING_K=5                # K-means clusters for prompts
ANOMALY_THRESHOLD=3.0         # Z-score threshold for outliers

# Output
EXPORT_FORMAT="csv"           # Output format (csv, parquet)
COMPRESS_OUTPUT=false         # Gzip output files
```

### Reducing Runtime

**Skip full ETL (use pre-processed data)**:

```python
# In Notebook 02, load directly from CSV
import pandas as pd
df = pd.read_csv('data/processed/conversations_clean.csv')
# Skip Notebooks 01 and 03, proceed with analysis
```

**Parallel processing**:

```python
# Enable parallel feature engineering in Notebook 01
import multiprocessing
n_jobs = multiprocessing.cpu_count() - 1
```

---

## 📋 Troubleshooting

### "Memory Error" during extraction

→ Reduce `BATCH_SIZE` in `.env` or subsample data:

```python
# Notebook 01, Stage 1
df = df.sample(frac=0.1)  # Use 10% sample
```

### Missing language detection

→ Install langdetect:

```bash
pip install langdetect
```

### Tableau connection issues

→ Verify CSV paths in Tableau data source settings match `data/processed/` directory structure.

---

## 🔗 Related Documentation

- [**Architecture Guide**](../docs/architecture/ARCHITECTURE.md) — System design and component relationships
- [**Developer Guide**](../docs/guides/DEVELOPER_GUIDE.md) — Detailed technical implementation
- [**Setup Guide**](../docs/guides/SETUP.md) — Environment configuration and dependencies
- [**Data Dictionary**](../data/dictionaries/DATA_DICTIONARY.md) — Complete schema reference
- [**Tableau Dashboards**](../dashboards/tableau) — Interactive BI visualizations

---

## 📈 Performance Metrics

| Metric                         | Benchmark                |
| ------------------------------ | ------------------------ |
| **Extraction time**            | ~45 minutes (1M records) |
| **Cleaning time**              | ~15 minutes              |
| **Feature engineering**        | ~30 minutes              |
| **Total ETL runtime**          | ~90–120 minutes          |
| **EDA runtime**                | ~20 minutes              |
| **Feature validation runtime** | ~15 minutes              |
| **Output file size**           | ~1.2 GB (all CSVs)       |

---

## 📝 License

This project is licensed under the **Apache License 2.0**. See [LICENSE](../LICENSE) for details.

---

## 📞 Support

For questions or issues:

1. Check the [Troubleshooting](#troubleshooting) section above
2. Review [DEVELOPER_GUIDE.md](../docs/guides/DEVELOPER_GUIDE.md) for implementation details
3. Refer to [DATA_DICTIONARY.md](../data/dictionaries/DATA_DICTIONARY.md) for schema questions
4. Open an issue with reproduction steps and environment details

---

**Last Updated**: April 2026  
**Dataset**: [WildChat-1M](https://huggingface.co/datasets/allenai/WildChat-1M) (AllenAI)  
**Platform**: WildChat Analytics Platform
