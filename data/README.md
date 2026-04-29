# `data/` — Dataset Lifecycle Management

This directory manages all data assets across the project lifecycle, from raw ingestion to Tableau-ready exports. Organized by processing stage to maintain clear separation of concerns and enable reproducible analysis.

---

## 📁 Folder Structure

### `raw/`

**Immutable source extracts** — Never edit in-place.

- Original dataset as received or streamed from HuggingFace
- Read-only archive for audit trail and reproducibility
- Backup of data before any transformation
- **Files**: `.parquet`, `.json`, or HuggingFace streaming (stored as metadata)

### `interim/`

**Temporary, re-creatable working datasets**

- Intermediate outputs between stages (e.g., after cleaning but before feature engineering)
- Snapshots during exploratory analysis
- Can be safely deleted and regenerated from pipeline
- Used for debugging and stage-by-stage validation

### `processed/`

**Cleaned, validated, analysis-ready tables** — Primary analytical layer

| File                      | Description                                      | Rows  | Purpose                                   |
| ------------------------- | ------------------------------------------------ | ----- | ----------------------------------------- |
| `conversations_clean.csv` | One row per conversation with aggregate features | ~50K  | Primary Tableau data source               |
| `messages_sample.csv`     | Stratified 10% sample of individual messages     | ~290K | Drill-down views, detailed analysis       |
| `daily_kpis.csv`          | Pre-aggregated daily KPIs                        | ~365  | Time-series trends (engagement, toxicity) |
| `geo_summary.csv`         | Country-level rollup metrics                     | ~100  | Geographic analysis, heatmaps             |
| `prompt_categories.csv`   | Distribution by category, week, country, model   | ~500  | Category trends, dashboard slicing        |
| `user_segments.csv`       | User cluster assignments from K-Means            | ~50K  | Behavioral segmentation                   |

### `features/`

**Feature tables & embeddings** (typically not committed to git)

- TF-IDF vectors for text similarity analysis
- PCA 2D projections for user cluster visualization
- Embedding vectors (future: BERT embeddings for semantic search)
- Pre-computed distance matrices
- **.gitignore**: These files are regenerated during pipeline runs

### `outputs/`

**Dashboard- and report-ready exports**

#### `outputs/tableau/`

- Processed CSVs directly connected to Tableau workbooks
- Mirrors `processed/` structure but optimized for BI consumption
- Includes pre-calculated KPI cards, drill-down tables, and filter lists

#### `outputs/ml/`

- Model predictions and scoring outputs
- Drop-off probability scores
- Anomaly detection flags
- Cluster assignments

---

## 🔄 Data Pipeline Flow

```
┌──────────────────────┐
│  WildChat-1M (Raw)   │  HuggingFace streaming
│  1,000,000+ records  │
└──────────┬───────────┘
           ↓
    [STAGE 1: EXTRACTION]
    Load in 50K batches
           ↓
┌──────────────────────────┐
│  raw/                    │
│  (Immutable backup)      │
└──────────┬───────────────┘
           ↓
    [STAGE 2: CLEANING]
    • Remove duplicates
    • Fill nulls
    • Normalize types
           ↓
┌──────────────────────────┐
│  interim/                │
│  (Checkpoint)            │
└──────────┬───────────────┘
           ↓
    [STAGE 3: PREPROCESSING]
    • Flatten nested JSON
    • Clean text
    • Language detection
           ↓
┌──────────────────────────┐
│  interim/                │
│  (Message-level data)    │
└──────────┬───────────────┘
           ↓
    [STAGE 4: FEATURE ENGINEERING]
    • Aggregate to conversation level
    • Extract quality scores
    • Classify prompts (zero-shot)
    • Detect anomalies
           ↓
┌──────────────────────────┐
│  processed/              │
│  ✅ Analysis-Ready       │
└──────────┬───────────────┘
           ├─→ conversations_clean.csv
           ├─→ messages_sample.csv
           ├─→ daily_kpis.csv
           ├─→ geo_summary.csv
           ├─→ prompt_categories.csv
           └─→ user_segments.csv
           ↓
    [STAGE 5: OUTPUT EXPORT]
    • Copy to outputs/tableau/
    • Package for BI tools
           ↓
┌──────────────────────────┐
│  outputs/tableau/        │
│  📊 Tableau-Ready        │
└──────────────────────────┘
```

---

## 📊 Dataset Details

### Primary Source: WildChat-1M (AllenAI)

| Property         | Value                                                              |
| ---------------- | ------------------------------------------------------------------ |
| **Dataset**      | [WildChat-1M](https://huggingface.co/datasets/allenai/WildChat-1M) |
| **Scale**        | 1,000,000+ real conversations                                      |
| **Interactions** | ChatGPT (GPT-3.5 / GPT-4)                                          |
| **Collection**   | Consent-based opt-in web interface                                 |
| **Language**     | Multi-lingual (primarily English, Chinese, Russian, German)        |

### Raw Schema (14 columns)

```python
{
    "conversation_id": str,           # Unique identifier
    "turn_id": int,                  # Sequential turn within conversation
    "timestamp": str,                # UTC timestamp
    "role": str,                     # "user" or "assistant"
    "content": str,                  # Raw message text
    "country": str,                  # ISO 3166 country code
    "language": str,                 # ISO 639-1 language code
    "model": str,                    # Model version (gpt-3.5-turbo, gpt-4)
    "toxic": bool,                   # Binary toxicity flag
    "openai_moderation": dict,       # JSON with category scores
    "redacted": bool,                # PII redaction flag
    "state": str,                    # US state (if applicable)
    "timestamp_modified": str,       # Processing timestamp
}
```

### Processed Schema (conversations_clean.csv)

```python
{
    # Original fields
    "conversation_id": str,
    "country": str,
    "language": str,
    "model": str,

    # Aggregated features
    "turn_count": int,                        # Conversation depth
    "user_msg_count": int,                    # User messages only
    "assistant_msg_count": int,               # AI responses only
    "avg_prompt_len_tokens": float,           # Mean user message length
    "avg_response_len_tokens": float,         # Mean AI response length
    "avg_prompt_len_chars": float,            # Character count

    # Quality & Sentiment
    "response_quality_score": float,          # 0–10 heuristic
    "avg_sentiment_score": float,             # -1 to +1 (VADER)
    "max_sentiment_score": float,
    "min_sentiment_score": float,

    # Safety
    "max_toxicity_score": float,              # 0–1
    "has_toxic_flag": bool,
    "toxicity_categories": str,               # JSON list

    # Temporal
    "hour_of_day": int,
    "day_of_week": str,
    "week_num": int,
    "session_duration_min": float,

    # Classification
    "prompt_category": str,                   # Coding | Factual | Creative | Emotional | Roleplay | Harmful | Other
    "drop_off_flag": bool,                    # 1 if turn_count <= 2

    # Engagement
    "is_power_user": bool,                    # 1 if > 90th percentile
    "repeat_user": bool,                      # 2+ distinct calendar days
}
```

---

## 🔍 Data Quality Notes

### Known Data Challenges

- **Unstructured Text**: Free-form prompts require NLP processing; includes code, documents, and multi-language content
- **Scale**: 1M+ rows demand batch processing and memory-efficient ETL
- **Noise**: Test conversations, bot interactions, and automated probing inflate raw counts
- **Temporal Gaps**: Uneven timestamp distribution — some periods over-represented, others sparse
- **Label Sparsity**: Toxicity flags are binary; nuanced scoring requires additional modeling
- **PII Redaction**: Redacted fields break entity extraction and some NLP analyses
- **Class Imbalance**: Unsafe conversations <5% — standard classifiers underperform without resampling

### Data Validation Checkpoints

1. **Extraction**: Assert schema; log & drop rows with missing conversation_id or timestamp
2. **Cleaning**: Validate 100% non-null for key fields after imputation
3. **Processing**: Cross-check message-level → conversation-level aggregations
4. **Export**: Verify no NaNs in primary Tableau datasets; spot-check KPI calculations

---

## 🛠️ Python Libraries Used

| Library                      | Purpose                                       |
| ---------------------------- | --------------------------------------------- |
| `pandas`                     | DataFrames, aggregations, CSV I/O             |
| `NumPy`                      | Numerical operations, array handling          |
| `datasets` (HuggingFace)     | Streaming large parquet files                 |
| `nltk`                       | Tokenization, VADER sentiment                 |
| `spaCy`                      | Named entity recognition, language detection  |
| `transformers` (HuggingFace) | Zero-shot prompt classification               |
| `scikit-learn`               | TF-IDF, K-Means clustering, anomaly detection |
| `pyarrow`                    | Parquet file handling                         |

---

## 📝 Usage Examples

### Load Processed Data for Analysis

```python
import pandas as pd

# Main conversation dataset
df = pd.read_csv("processed/conversations_clean.csv")

# KPI time-series
kpis = pd.read_csv("processed/daily_kpis.csv")

# Geographic breakdown
geo = pd.read_csv("processed/geo_summary.csv")
```

### Connect to Tableau

1. Open Tableau Desktop
2. **Connect** → **Text File** → `processed/conversations_clean.csv`
3. Drag tables into canvas; create relationships as needed
4. Save as `.twbx` workbook

### Re-run ETL Pipeline

```bash
cd ../notebooks/ETL\ _PIPELINE_NOTEBOOK
jupyter notebook WildChat_Notebook.ipynb
# Execute all cells: outputs to data/processed/
```

---

## 🔐 Security & Compliance

- **PII**: Dataset has PII pre-redacted; no sensitive customer data
- **GDPR**: Conversation data is from opt-in users; compliant with GDPR consent requirements
- **Retention**: No personally identifiable information stored in processed outputs
- **Access**: `.gitignore` excludes `features/` (large embeddings); `raw/` is read-only

---

## 📚 Related Documentation

- [Data Dictionary](dictionaries/data_dictionary.md) — Column definitions & formulas
- [ETL Pipeline](../notebooks/01_etl_pipeline/README.md) — Detailed processing stages
- [EDA Notebook](../notebooks/02_exploratory_data_analysis/README.md) — Analysis patterns & distributions

---

## ✅ Checklist for New Analysts

- [ ] Read this README
- [ ] Explore `processed/conversations_clean.csv` structure
- [ ] Run `02_eda.ipynb` to see analysis workflow
- [ ] Review [Data Dictionary](dictionaries/data_dictionary.md)
- [ ] Connect Tableau to `processed/` datasets
- [ ] Review dashboards for KPI logic

**Questions?** See [Root README](../README.md) or open a GitHub issue.
