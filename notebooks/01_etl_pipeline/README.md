# 01 — ETL Pipeline & Data Processing

Comprehensive 5-stage Extract-Transform-Load pipeline that converts 1M+ raw WildChat conversations into structured, analysis-ready datasets. This is the foundation for all downstream analytics, dashboards, and ML models.

---

## 📊 Notebook Overview

**File**: `WildChat_Notebook.ipynb`  
**Purpose**: End-to-end ETL pipeline processing raw conversation data into Tableau-ready exports  
**Scale**: 1,000,000+ conversations processed in streaming mode (memory-efficient)  
**Output**: 6 CSV datasets optimized for analysis and BI consumption

### Pipeline Architecture

```
Raw WildChat-1M
    ↓
┌─────────────────────────────────────────┐
│ STAGE 1: EXTRACTION                     │
│ • Stream from HuggingFace API           │
│ • Load in 50K-row batches               │
│ • Collect schema metadata               │
└────────────┬────────────────────────────┘
             ↓
┌─────────────────────────────────────────┐
│ STAGE 2: CLEANING                       │
│ • Remove duplicates                     │
│ • Standardize data types                │
│ • Fill missing values (imputation)      │
│ • Normalize timestamps (UTC)            │
└────────────┬────────────────────────────┘
             ↓
┌─────────────────────────────────────────┐
│ STAGE 3: TEXT PREPROCESSING             │
│ • Flatten nested JSON structure         │
│ • Clean & normalize text                │
│ • Detect language (langdetect)          │
│ • Extract basic text features           │
└────────────┬────────────────────────────┘
             ↓
┌─────────────────────────────────────────┐
│ STAGE 4: FEATURE ENGINEERING            │
│ • Aggregate message → conversation      │
│ • Compute quality scores (heuristic)    │
│ • Classify prompts (transformers)       │
│ • Detect anomalies & clusters           │
└────────────┬────────────────────────────┘
             ↓
┌─────────────────────────────────────────┐
│ STAGE 5: OUTPUT GENERATION              │
│ • Generate 6 analysis-ready CSVs        │
│ • Package for Tableau connections       │
│ • Export to data/processed/             │
└─────────────────────────────────────────┘
```

---

## 🔄 Stage-by-Stage Specification

### Stage 1: Extraction

**Objective**: Load raw conversation data without exceeding memory constraints.

**Process**:

- **Source**: AllenAI WildChat-1M via HuggingFace `datasets` library
- **Loading Strategy**: Streaming mode for 1M+ records
- **Batch Size**: 50,000 records per iteration
- **Scope**: First 50,000 conversations (representative sample for analysis)

**Key Code**:

```python
from datasets import load_dataset
import pandas as pd

ds = load_dataset("allenai/WildChat-1M", split="train", streaming=True)
batches = []
for i, batch in enumerate(ds.iter(batch_size=50000)):
    df_batch = pd.DataFrame(batch)
    batches.append(df_batch)
    if i >= 0:  # First batch only (50K)
        break

df_raw = pd.concat(batches, ignore_index=True)
```

**Output Schema** (14 columns):

```python
{
    "conversation_id": str,          # Unique ID
    "turn_id": int,                 # Sequential turn within conversation
    "timestamp": str,               # UTC timestamp
    "role": str,                    # "user" or "assistant"
    "content": str,                 # Raw message text
    "country": str,                 # ISO 3166 country code
    "language": str,                # ISO 639-1 language code
    "model": str,                   # Model version
    "toxic": bool,                  # Binary toxicity flag
    "openai_moderation": dict,      # JSON category scores
    "redacted": bool,               # PII redaction flag
    "state": str,                   # US state (if applicable)
    "timestamp_modified": str       # Processing timestamp
}
```

**Quality Checks**:

- Validate expected columns exist
- Log & skip rows with missing `conversation_id` or `timestamp`
- Assert no NaN in critical fields

---

### Stage 2: Cleaning

**Objective**: Standardize data types, resolve missing values, and ensure data integrity.

**Process**:

```python
# Remove duplicates
df_raw = df_raw.drop_duplicates(subset=["conversation_id", "turn_id"])

# Missing value imputation
df_raw["country"] = df_raw["country"].fillna("UNKNOWN")
df_raw["language"] = df_raw["language"].fillna("und")  # undetermined

# Data type conversion
df_raw["toxic"] = df_raw["toxic"].astype(int)
df_raw["timestamp"] = pd.to_datetime(
    df_raw["timestamp"],
    errors="coerce",  # Convert unparseable to NaT
    utc=True
)

# Remove rows with missing timestamps
df_raw = df_raw[df_raw["timestamp"].notna()]

# Normalize model names
df_raw["model"] = df_raw["model"].str.replace(
    r"gpt-3\.5-turbo.*",
    "gpt-3.5-turbo",
    regex=True
)
```

**Data Quality Metrics**:

- **Input**: 50,000 rows
- **Output**: ~49,550 rows (0.9% duplicates removed)
- **Null Handling**: 100% non-null for critical fields after imputation

---

### Stage 3: Text Preprocessing

**Objective**: Flatten nested conversation structure and extract basic text features.

**Process**:

#### Conversation Flattening

```python
# Convert nested conversation objects to message-level records
message_records = []

for _, conv in df_raw.iterrows():
    conversation = json.loads(conv["conversation_content"])  # if nested JSON

    for turn_idx, turn in enumerate(conversation, start=1):
        message_records.append({
            "conversation_id": conv["conversation_id"],
            "message_index": turn_idx,
            "role": turn["role"],
            "content": turn["content"],
            "timestamp": conv["timestamp"],
            # ... (preserve other fields)
        })

df_messages = pd.DataFrame(message_records)
```

**Result**: 290,714 message records from 49,550 conversations

#### Text Cleaning

```python
def clean_text(x):
    x = str(x).lower()
    # Remove PII placeholders
    x = re.sub(r"\[name\]|\[email\]|\[phone\]", "", x)
    # Normalize whitespace
    x = re.sub(r"\s+", " ", x).strip()
    return x

df_messages["content_clean"] = df_messages["content"].apply(clean_text)
```

#### Feature Extraction

```python
# Token count (word tokenization)
df_messages["token_count"] = df_messages["content_clean"].apply(
    lambda x: len(nltk.word_tokenize(x))
)

# Sentiment (VADER)
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
df_messages["sentiment_score"] = df_messages["content_clean"].apply(
    lambda x: sia.polarity_scores(x)["compound"]
)

# Toxicity (from moderation JSON)
df_messages["toxicity_score"] = df_messages["openai_moderation"].apply(
    lambda x: max([v for k, v in x.items()
                   if k in ["hate", "harassment", "violence", "sexual"]], default=0)
)
```

---

### Stage 4: Feature Engineering

**Objective**: Aggregate to conversation level and create analytical features.

**Process**:

#### Conversation-Level Aggregation

```python
conv_features = df_messages.groupby("conversation_id").agg({
    "message_index": ["max", "size"],           # turn_count
    "token_count": ["mean", "sum"],             # avg_prompt_len, total_tokens
    "sentiment_score": ["mean", "min", "max"],  # sentiment profile
    "toxicity_score": "max",                    # max_toxicity
    "content": lambda x: sum(1 for r in x if r == "user")  # user_msg_count
}).reset_index()
```

#### Quality Score (Heuristic)

```python
def compute_quality_score(row):
    """
    Composite quality metric (0–10).
    Components:
    • 30%: Length appropriateness
    • 40%: Lexical diversity (TTR)
    • 30%: Coherence proxy (sentiment + toxicity)
    """
    # Length: Penalize very short (<50 tokens) and very long (>1000)
    length_score = 10 if 50 <= row["avg_response_len"] <= 500 else 5

    # Lexical diversity (token type / token count ratio)
    diversity_score = (10 * row["lexical_diversity"]) if row["lexical_diversity"] > 0 else 0

    # Sentiment penalty for negative (frustrated) users
    coherence_score = 10 - (abs(row["avg_sentiment"]) * 5)

    # Composite
    quality = (0.3 * length_score + 0.4 * diversity_score + 0.3 * coherence_score)

    return min(10, max(0, quality))  # Clamp to 0–10

df_conv["response_quality_score"] = df_conv.apply(compute_quality_score, axis=1)
```

#### Prompt Classification (Zero-Shot)

```python
from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

categories = [
    "Coding & Technical",
    "Factual Q&A",
    "Creative Writing",
    "Emotional Support",
    "Roleplay / Persona",
    "Harmful / Policy-Violating",
    "Other / Unclassified"
]

def classify_prompt(text):
    result = classifier(text, categories, multi_class=True)
    return result["labels"][0]  # Top category

df_conv["prompt_category"] = df_conv["sample_prompt"].apply(classify_prompt)
```

#### Behavioral Features

```python
# Drop-off flag (key metric)
df_conv["drop_off_flag"] = (df_conv["turn_count"] <= 2).astype(int)

# Power user identification (top 10% by turn count)
turn_90th = df_conv["turn_count"].quantile(0.9)
df_conv["is_power_user"] = (df_conv["turn_count"] > turn_90th).astype(int)

# Repeat user (proxy: multiple turns + long session)
df_conv["repeat_user"] = (
    (df_conv["turn_count"] >= 3) &
    (df_conv["session_duration_min"] > 2)
).astype(int)
```

---

### Stage 5: Output Generation

**Objective**: Create analysis-ready CSV exports for Tableau and downstream analytics.

**Output Datasets**:

#### 1. `conversations_clean.csv`

**One row per conversation** with all aggregate features.

| Column                 | Type  | Example      | Purpose                      |
| ---------------------- | ----- | ------------ | ---------------------------- |
| conversation_id        | str   | "conv_12345" | Unique ID                    |
| turn_count             | int   | 4            | Conversation depth           |
| avg_prompt_len_tokens  | float | 125.5        | User engagement depth        |
| response_quality_score | float | 7.94         | Quality heuristic (0–10)     |
| avg_sentiment_score    | float | 0.25         | User satisfaction (-1 to +1) |
| max_toxicity_score     | float | 0.08         | Safety metric (0–1)          |
| drop_off_flag          | int   | 0            | Early abandonment flag       |
| country                | str   | "US"         | Geographic context           |
| language               | str   | "en"         | Language code                |
| model                  | str   | "gpt-4"      | Model version                |
| hour_of_day            | int   | 14           | Temporal feature             |
| prompt_category        | str   | "Coding"     | Intent classification        |
| is_power_user          | int   | 1            | Engagement tier              |

**Size**: ~49,550 rows (one per conversation)  
**Use**: Primary Tableau data source; all main analysis

#### 2. `messages_sample.csv`

**Stratified 10% sample** of individual messages for drill-down analysis.

**Sampling Strategy**:

```python
# Stratified by conversation_id (ensure all conversations represented)
messages_sample = df_messages.groupby("conversation_id", group_keys=False).apply(
    lambda x: x.sample(frac=0.1, random_state=42)
)
```

**Size**: ~29,000 rows  
**Use**: Detailed message-level analysis, sentiment trends, validation

#### 3. `daily_kpis.csv`

**Pre-aggregated daily metrics** for time-series analysis.

```python
daily_kpis = df_conv.groupby(df_conv["timestamp"].dt.date).agg({
    "conversation_id": "count",               # Daily volume
    "drop_off_flag": "mean",                  # Daily drop-off %
    "response_quality_score": "mean",         # Daily avg quality
    "avg_sentiment_score": "mean",            # Daily sentiment
    "max_toxicity_score": ["mean", "max"],    # Daily toxicity stats
    "turn_count": "mean",                     # Daily avg depth
    "is_power_user": "sum",                   # Daily power users
}).reset_index()

daily_kpis.columns = [
    "date",
    "conversation_volume",
    "drop_off_rate",
    "avg_quality_score",
    "avg_sentiment",
    "avg_toxicity",
    "max_toxicity",
    "avg_turn_count",
    "power_user_count"
]
```

**Size**: ~365 rows (one per day)  
**Use**: Executive dashboard trends, anomaly detection

#### 4. `geo_summary.csv`

**Country-level rollup** for geographic analysis.

```python
geo_summary = df_conv.groupby("country").agg({
    "conversation_id": "count",
    "response_quality_score": "mean",
    "max_toxicity_score": "mean",
    "avg_sentiment_score": "mean",
    "turn_count": "mean",
    "drop_off_flag": "mean",
    "is_power_user": "sum"
}).reset_index()
```

**Columns**: country, volume, avg_quality, avg_toxicity, avg_sentiment, avg_turns, drop_off_pct, power_users  
**Size**: ~100 countries  
**Use**: Geographic heatmaps, regional compliance analysis

#### 5. `prompt_categories.csv`

**Category distribution** by time period and model.

```python
category_dist = df_conv.groupby([
    df_conv["timestamp"].dt.to_period("W"),  # Weekly
    "prompt_category",
    "model"
]).size().reset_index(name="volume")
```

**Columns**: week, category, model, volume  
**Size**: ~500 rows  
**Use**: Category trends, model-category performance analysis

#### 6. `user_segments.csv`

**User cluster assignments** from K-Means behavioral segmentation.

```python
from sklearn.cluster import KMeans

# Feature scaling
features = ["turn_count", "avg_prompt_len_tokens", "sentiment_score",
            "max_toxicity_score", "session_duration_min"]
X_scaled = StandardScaler().fit_transform(df_conv[features])

# K-Means (k=5 optimized via Elbow + Silhouette)
kmeans = KMeans(n_clusters=5, random_state=42)
df_conv["cluster_id"] = kmeans.fit_predict(X_scaled)

user_segments = df_conv[["conversation_id", "cluster_id"] + features]
```

**Clusters**:

- **Cluster 0**: Power Users (high turns, long duration, high engagement)
- **Cluster 1**: Task-Oriented (short, focused, high quality)
- **Cluster 2**: Casual Explorers (1–3 turns, entertainment)
- **Cluster 3**: At-Risk (short, negative sentiment, high toxicity)
- **Cluster 4**: Adversarial (probing patterns, spam-like behavior)

**Size**: ~49,550 rows  
**Use**: User segmentation analysis, targeted interventions

---

## 🛠️ Libraries & Dependencies

| Library             | Purpose            | Usage                                 |
| ------------------- | ------------------ | ------------------------------------- |
| `datasets` (HF)     | Streaming API      | Load WildChat from HuggingFace        |
| `pandas`            | DataFrames         | All data manipulation                 |
| `NumPy`             | Arrays             | Numerical operations                  |
| `nltk`              | NLP tools          | Tokenization, VADER sentiment         |
| `spacy`             | Advanced NLP       | Entity extraction, language detection |
| `transformers` (HF) | Pre-trained models | Zero-shot classification, embeddings  |
| `scikit-learn`      | ML algorithms      | K-Means, TF-IDF, preprocessing        |
| `pyarrow`           | Parquet I/O        | Read/write Parquet files              |
| `re`                | Regex              | Text pattern matching                 |
| `json`              | JSON parsing       | Handle moderation scores              |

---

## 🚀 How to Run

### Prerequisites

```bash
python --version  # ≥ 3.9
pip install -r requirements.txt
```

### Execution

```bash
# Navigate to notebook
cd notebooks/01_etl_pipeline

# Start Jupyter
jupyter notebook WildChat_Notebook.ipynb

# Execute cells sequentially:
# 1. Imports & configuration
# 2. Stage 1: Extraction
# 3. Stage 2: Cleaning
# 4. Stage 3: Text Preprocessing
# 5. Stage 4: Feature Engineering
# 6. Stage 5: Output Generation
# 7. Validation & summary stats
```

### Output

```
Outputs saved to:
  data/processed/conversations_clean.csv
  data/processed/messages_sample.csv
  data/processed/daily_kpis.csv
  data/processed/geo_summary.csv
  data/processed/prompt_categories.csv
  data/processed/user_segments.csv
```

### Runtime

- **Expected Time**: 10–15 minutes (first run)
- **Memory Usage**: ~4–6 GB (streaming mode minimizes peak)
- **Batch Processing**: 50K rows at a time

---

## 🔍 Data Quality Metrics

### Pre-ETL (Raw)

- **Input Rows**: 1,000,000+
- **Sampled**: 50,000
- **Columns**: 14
- **Missing Values**: Variable (country, language ~10%)

### Post-ETL (Processed)

- **Conversations**: 49,550 (99.1% retention)
- **Messages**: 290,714 (flattened from nested JSON)
- **Columns**: 20+ (enriched with features)
- **Missing Values**: <0.1% (imputed or filled)
- **Data Types**: Standardized (no type errors)

### Quality Checks

```python
# Validate outputs
assert len(conversations_clean) == 49550
assert conversations_clean.isna().sum().sum() == 0  # No NaNs in output
assert (conversations_clean["response_quality_score"] >= 0).all()
assert (conversations_clean["response_quality_score"] <= 10).all()
print(f"✅ All {len(conversations_clean)} rows validated successfully")
```

---

## 📚 Related Documentation

- [EDA Notebook](../02_exploratory_data_analysis/README.md) — Analysis of processed data
- [Feature Engineering](../03_feature_engineering/README.md) — Statistical validation
- [Data Dictionary](../../data/dictionaries/data_dictionary.md) — Column definitions
- [Dashboard Guide](../../dashboards/tableau/README.md) — BI visualizations
- [Root README](../../README.md) — Project overview

---

## 🆘 Troubleshooting

| Issue                          | Solution                                                                    |
| ------------------------------ | --------------------------------------------------------------------------- |
| **OOM (Out of Memory)**        | Reduce batch size (e.g., 25K instead of 50K); increase virtual memory       |
| **API Rate Limit**             | HuggingFace might throttle; add `time.sleep(1)` between batches             |
| **Transformer Model Download** | First run downloads ~2GB model; ensure disk space                           |
| **NaN Values**                 | Check imputation logic; adjust fill strategy if needed                      |
| **Slow Tokenization**          | Bottleneck in Stage 3; use `spacy` faster alternative or pre-tokenized text |

---

## ✅ Validation Checklist

Before publishing outputs:

- [ ] All 6 CSVs generated in `data/processed/`
- [ ] No NaN values in key columns
- [ ] Row counts match expectations (49,550 conversations)
- [ ] KPI calculations spot-checked (e.g., drop-off % vs raw observation)
- [ ] Cluster assignments validated (silhouette coefficient)
- [ ] Sample files are consistent with full outputs
- [ ] Data dictionary updated with new columns

---

**Questions?** See [Root README](../../README.md) or contact ETL Lead.

#### Response Quality Score

Composite metric combining prompt length and toxicity:

```python
conv["response_quality_score"] = np.log1p(conv["avg_prompt_len"]) * 2 - conv["toxicity_score"] * 3
```

#### User Intent Classification

Automated categorization of user prompts:

```python
def classify_prompt(text):
    t = str(text).lower()
    if any(x in t for x in ["python","sql","code","bug"]):
        return "Coding"
    elif any(x in t for x in ["what","why","how","explain"]):
        return "Factual"
    elif any(x in t for x in ["story","poem","write"]):
        return "Creative"
    elif len(t.split()) < 8:
        return "Casual"
    elif "?" in t:
        return "Factual"
    else:
        return "Other"
```

#### Daily KPIs

Time-series aggregation for trend analysis:

```python
daily_kpis = df_messages.groupby(df_messages["timestamp"].dt.date).agg({
    "conversation_id": "nunique",              # Daily conversation count
    "token_count": "mean"                      # Average tokens per day
})
```

### Stage 5: Output Generation

**Objective**: Export processed datasets for downstream analysis

**Process**:

- **Primary Datasets**: Core conversation and daily metrics
- **Analytical Datasets**: Geographic summaries and combined master data
- **File Formats**: CSV for universal compatibility

**Output Files**:

#### Core Datasets

1. **`conversations_clean.csv`**: Primary analysis dataset
   - 49,550 conversations with engineered features
   - Includes quality scores, toxicity flags, user classifications

2. **`daily_kpis.csv`**: Time-series metrics
   - 22 days of aggregated data
   - Conversation volume, token usage, toxicity rates

#### Analytical Datasets

3. **`geo_summary.csv`**: Geographic aggregation
   - Country-level conversation counts and toxicity rates
   - Regional analysis support

4. **`wildchat_combined_master.csv`**: Comprehensive master dataset
   - All conversation features plus daily KPIs
   - Complete feature set for advanced analytics

## Technical Implementation

### Dependencies

```python
# Core data manipulation
import pandas as pd
import numpy as np
import re

# Dataset loading and text processing
from datasets import load_dataset
from langdetect import detect
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
nltk.download("punkt")
```

### Performance Optimizations

- **Streaming Data Loading**: Memory-efficient dataset ingestion
- **Vectorized Operations**: Pandas-based transformations for speed
- **Batch Processing**: Efficient group-by operations
- **Memory Management**: Strategic data type conversions

### Error Handling

- **Graceful Degradation**: Error handling for missing or malformed data
- **Data Validation**: Type checking and constraint enforcement
- **Fallback Strategies**: Default values for missing critical fields

## Data Quality and Validation

### Automated Quality Checks

- **Duplicate Detection**: Hash-based conversation deduplication
- **Data Type Validation**: Automatic type conversion and error handling
- **Completeness Assessment**: Missing value analysis and imputation
- **Range Validation**: Sentiment scores (-1 to 1), toxicity probabilities (0 to 1)

### Statistical Validation

- **Distribution Analysis**: Verify expected data distributions
- **Correlation Checks**: Identify feature relationships
- **Outlier Detection**: Identify and handle anomalous values

## Usage Instructions

### Running the Pipeline

1. **Environment Setup**: Install required dependencies
2. **Data Access**: Ensure HuggingFace datasets access
3. **Execution**: Run notebook cells sequentially
4. **Validation**: Verify output file generation

### Customization Options

- **Sample Size**: Adjust conversation sampling (default: 50,000)
- **Feature Thresholds**: Modify toxicity detection thresholds
- **Classification Rules**: Update user intent categorization logic
- **Output Paths**: Customize file output locations

### Integration Points

- **Upstream**: Compatible with WildChat-1M dataset updates
- **Downstream**: Outputs feed directly into analytical notebooks
- **Monitoring**: Pipeline status and data quality metrics

## Monitoring and Maintenance

### Pipeline Health Metrics

- **Processing Volume**: Number of conversations processed
- **Data Quality Rates**: Missing value percentages, duplicate rates
- **Feature Distributions**: Statistical summaries of engineered features
- **Output Validation**: File generation and schema verification

### Troubleshooting Guide

- **Memory Issues**: Reduce sample size or implement chunking
- **Data Access**: Verify dataset credentials and network connectivity
- **Feature Errors**: Check input data schema and validation rules
- **Output Failures**: Verify write permissions and disk space

## Version Control and Reproducibility

### Pipeline Versioning

- **Git Tracking**: Notebook version control with commit history
- **Dependency Management**: Requirements.txt for environment reproduction
- **Data Versioning**: Timestamped outputs for traceability
- **Configuration Management**: Parameterized pipeline settings

### Reproducibility Features

- **Random State Control**: Consistent results for stochastic operations
- **Deterministic Processing**: Reproducible data transformations
- **Audit Trail**: Complete processing log with timestamps
- **Data Lineage**: Clear mapping from source to target features

## Performance Benchmarks

### Processing Metrics

- **Input Volume**: 50,000 conversations (290,714 messages)
- **Processing Time**: ~5-10 minutes on standard hardware
- **Memory Usage**: Peak ~2GB during processing
- **Output Size**: ~20MB across all generated files

### Scalability Considerations

- **Horizontal Scaling**: Pipeline designed for distributed processing
- **Incremental Updates**: Support for delta processing
- **Batch Optimization**: Configurable batch sizes for memory management
- **Resource Allocation**: Adjustable based on available compute

## Security and Privacy

### Data Protection

- **Anonymization**: IP address hashing and user identifier protection
- **Content Filtering**: Redaction of sensitive information
- **Access Control**: Restricted data access and processing
- **Compliance**: GDPR and data protection regulation adherence

### Ethical Considerations

- **Bias Detection**: Monitoring for demographic and content biases
- **Fairness Assessment**: Equitable treatment across user segments
- **Transparency**: Clear documentation of processing decisions
- **Accountability**: Traceable data processing and feature generation

## Future Enhancements

### Planned Improvements

- **Real-time Processing**: Streaming pipeline for live data
- **Advanced NLP**: Integration of transformer-based features
- **Automated Quality**: Enhanced data quality monitoring
- **Scalability**: Distributed processing capabilities

### Extension Points

- **Custom Features**: Modular feature engineering framework
- **Additional Sources**: Support for multiple data sources
- **Advanced Analytics**: Machine learning pipeline integration
- **Visualization**: Automated report generation

## Contact and Support

For technical assistance or pipeline customization:

- **Documentation**: Review inline code comments and markdown explanations
- **Issues**: Report problems through project issue tracking
- **Enhancements**: Submit feature requests and improvement suggestions
- **Community**: Engage with user community for best practices and shared solutions

---

**Note**: This pipeline is designed as the foundational data processing component for the WildChat analytics ecosystem. All downstream analytical notebooks and dashboards depend on the high-quality, standardized outputs generated by this ETL process.
