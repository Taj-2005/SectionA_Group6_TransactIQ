# System Architecture & Technical Design

## Overview

The WildChat Analytics Platform is a **two-layer data architecture** designed to transform 1M+ raw AI conversations into decision-ready business intelligence.

---

## 🏗️ Architecture Layers

### Layer 1: Data Processing Pipeline (Python ETL + NLP)

```
┌──────────────────────────────────────────────────────────┐
│           WildChat-1M Dataset (HuggingFace)              │
│         1,000,000+ Real User Conversations               │
└──────────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────┐
│  STAGE 1: EXTRACTION                                     │
│  • Stream dataset from HuggingFace Hub                   │
│  • Parse JSON/HuggingFace format                         │
│  • Validate structure                                    │
└──────────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────┐
│  STAGE 2: CLEANING & NORMALIZATION                       │
│  • Handle missing values (nulls, incomplete records)     │
│  • Normalize timestamps (UTC, ISO 8601)                  │
│  • Standardize text encoding (UTF-8)                     │
│  • Filter invalid records (< 2 messages = drop)          │
│  • Geographic enrichment (IP → Country)                  │
└──────────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────┐
│  STAGE 3: TEXT PREPROCESSING                             │
│  • Tokenization (NLTK)                                   │
│  • Lemmatization (spaCy)                                 │
│  • Language detection (langdetect)                       │
│  • URL/email removal                                     │
│  • Special character normalization                       │
└──────────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────┐
│  STAGE 4: FEATURE ENGINEERING                            │
│  • Engagement metrics (turn count, drop-off)             │
│  • NLP features (sentiment, toxicity, intent)            │
│  • User clustering (K-Means, k=5)                        │
│  • Anomaly detection (Isolation Forest)                  │
│  • Dropout prediction (Gradient Boost, AUC=0.74)         │
└──────────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────┐
│  STAGE 5: OUTPUT GENERATION                              │
│  • Write processed datasets (CSV)                        │
│  • Export by category: engagement, safety, geography     │
│  • Aggregate daily KPIs                                  │
│  • Prepare Tableau data extracts                         │
└──────────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────┐
│  PROCESSED DATA ARTIFACTS (data/processed/)              │
│  ├── conversations_clean.csv (full dataset)              │
│  ├── messages_sample.csv (stratified sample)             │
│  ├── daily_kpis.csv (aggregated metrics)                 │
│  ├── geo_summary.csv (geographic breakdown)              │
│  ├── prompt_categories.csv (intent distribution)         │
│  └── user_segments.csv (cluster assignments)             │
└──────────────────────────────────────────────────────────┘
```

**Key Technologies**:

- **Data Processing**: Pandas, NumPy
- **NLP**: NLTK, spaCy, Transformers
- **ML**: scikit-learn (clustering, classification, anomaly detection)
- **Data Source**: HuggingFace Hub streaming API

---

### Layer 2: Business Intelligence (Tableau Dashboards)

```
┌──────────────────────────────────────────────────────────┐
│         PROCESSED DATA (data/processed/*.csv)            │
└──────────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────┐
│         TABLEAU DASHBOARD SUITE                          │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  ┌───────────────────────────────────────────────────┐   │
│  │  EXECUTIVE DASHBOARD                              │   │
│  │  Audience: C-Suite, VPs                           │   │
│  │  KPIs: Engagement, Drop-off, Toxicity             │   │
│  │  Trends, Risks, Geographic Performance            │   │
│  │  Refresh: Daily                                   │   │
│  └───────────────────────────────────────────────────┘   │
│                                                          │
│  ┌───────────────────────────────────────────────────┐   │
│  │  OPERATIONAL DASHBOARD                            │   │
│  │  Audience: Product, ML, Data teams                │   │
│  │  Filters: Date, Model, Country, Category          │   │
│  │  Funnels, Heatmaps, User Segments                 │   │
│  │  Refresh: Hourly (near-real-time)                 │   │
│  └───────────────────────────────────────────────────┘   │
│                                                          │
│  ┌───────────────────────────────────────────────────┐   │
│  │  SAFETY DASHBOARD                                 │   │
│  │  Audience: Trust & Safety, Legal                  │   │
│  │  Toxicity Monitoring, Anomaly Detection           │   │
│  │  Compliance Audit Trail                           │   │
│  │  Refresh: Real-time                               │   │
│  └───────────────────────────────────────────────────┘   │
│                                                          │
└──────────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────┐
│  STAKEHOLDERS & DECISION-MAKERS                          │
│  • Product Strategy & Roadmap                            │
│  • Safety Policy & Compliance                            │
│  • Model Performance & Optimization                      │
│  • User Experience Improvements                          │
└──────────────────────────────────────────────────────────┘
```

**Key Technologies**:

- **BI Platform**: Tableau Desktop + Tableau Public
- **Data Source**: CSV and Tableau Data Extracts (.hyper)
- **Visualizations**: KPI cards, trend charts, maps, heatmaps, scatter plots
- **Interactivity**: Filters, drill-downs, cross-filtering

---

## 📊 Data Pipeline Details

### Stage 1: Extraction

**Input**: HuggingFace `allenai/WildChat-1M` dataset

- Streaming format (not downloaded locally by default)
- JSON structure with nested messages

**Processing**:

```python
from datasets import load_dataset
dataset = load_dataset('allenai/WildChat-1M', split='train', streaming=True)
```

**Output**: Raw records in memory/staged for cleaning

---

### Stage 2: Cleaning & Normalization

**Tasks**:

- **Handle Nulls**: Drop records with missing core fields
- **Normalize Timestamps**: Convert to UTC, ISO 8601 format
- **Text Encoding**: Ensure UTF-8 (handle multi-language)
- **Filter Invalid**: Remove conversations with < 2 messages
- **Enrich Geography**: Map IP to country (when available)

**Example Rules**:

```python
# Drop if core fields missing
df = df.dropna(subset=['conversation_id', 'messages', 'user_id'])

# Normalize timestamp
df['timestamp'] = pd.to_datetime(df['timestamp']).dt.tz_convert('UTC')

# Ensure text encoding
df['text'] = df['text'].str.encode('utf-8').str.decode('utf-8', errors='ignore')

# Filter by conversation length
df = df[df['messages'].apply(len) >= 2]
```

**Output**: `data/raw/conversations_normalized.csv` (temporary)

---

### Stage 3: Text Preprocessing

**Tasks**:

- **Tokenization**: Split text into words
- **Lemmatization**: Reduce words to base form
- **Language Detection**: Identify language of each message
- **Cleaning**: Remove URLs, emails, special characters

**Libraries**:

- NLTK: Stop word removal, POS tagging
- spaCy: Lemmatization, NER
- langdetect: Language identification

**Example Pipeline**:

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def preprocess_text(text):
    # Tokenize
    tokens = word_tokenize(text.lower())

    # Remove stopwords
    tokens = [t for t in tokens if t not in stopwords.words('english')]

    # Keep only alphanumeric
    tokens = [t for t in tokens if t.isalnum()]

    return ' '.join(tokens)

df['text_clean'] = df['text'].apply(preprocess_text)
```

**Output**: Cleaned text in `text_clean` column

---

### Stage 4: Feature Engineering

#### Engagement Metrics

```python
# Turn count (conversation depth)
df['turn_count'] = df['messages'].apply(len)

# Engagement flag (threshold: 3+ turns)
df['engagement_flag'] = df['turn_count'] >= 3

# Drop-off (first turn quit)
df['dropped_at_turn_1'] = df['turn_count'] == 1
```

#### NLP Features

**Sentiment Analysis** (VADER):

```python
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

df['sentiment_score'] = df['text_clean'].apply(
    lambda x: sia.polarity_scores(x)['compound']
)
```

**Toxicity Detection** (Multi-model ensemble):

- OpenAI Moderation API
- HuggingFace toxic-bert
- PERSPECTIVE API
- Composite score: mean of all models

```python
def compute_toxicity(text):
    scores = [
        openai_moderation(text),
        huggingface_toxic(text),
        perspective_api(text)
    ]
    return np.mean(scores)

df['toxicity_score'] = df['text'].apply(compute_toxicity)
```

**Intent Classification**:

- Multi-class classification (8 categories)
- Using fine-tuned DISTILBERT
- Confidence score per category

#### User Clustering

**K-Means Clustering** (k=5):

```python
from sklearn.cluster import KMeans

# Feature matrix: engagement, turn count, toxicity, sentiment
X = df[['engagement_rate', 'turn_count', 'toxicity_score', 'sentiment_score']]

# Standardize
from sklearn.preprocessing import StandardScaler
X_scaled = StandardScaler().fit_transform(X)

# Cluster
kmeans = KMeans(n_clusters=5, random_state=42)
df['user_segment'] = kmeans.fit_predict(X_scaled)
```

**Segments** (Inferred):

- Segment 0: Power users (high engagement, high quality)
- Segment 1: Casual users (moderate engagement)
- Segment 2: Safety-risk users (high toxicity)
- Segment 3: Low-engagement users (1–2 turns)
- Segment 4: Niche interest users (category-specific)

#### Anomaly Detection

**Isolation Forest** (daily KPI level):

```python
from sklearn.ensemble import IsolationForest

# Aggregate daily KPIs
daily_kpis = df.groupby('date').agg({
    'engagement_rate': 'mean',
    'toxicity_score': 'mean',
    'turn_count': 'mean'
})

# Train anomaly detector
iso_forest = IsolationForest(contamination=0.05)
daily_kpis['anomaly'] = iso_forest.fit_predict(daily_kpis)

# Flag anomalous days
daily_kpis['is_anomaly'] = daily_kpis['anomaly'] == -1
```

**Alert Trigger**: Z-score > 2.5 on toxicity (standard deviation from 30-day mean)

#### Predictive Modeling

**Drop-off Prediction** (Gradient Boosting Classifier):

```python
from sklearn.ensemble import GradientBoostingClassifier

# Features: turn_count, sentiment, toxicity, user_segment, language, country
X_train = df[['turn_count', 'sentiment_score', 'toxicity_score', 'user_segment']]
y_train = df['engagement_flag']  # 1 = 3+ turns (engaged), 0 = dropped

# Train model
gbc = GradientBoostingClassifier(n_estimators=100, max_depth=5, random_state=42)
gbc.fit(X_train, y_train)

# Performance: AUC ~ 0.74 (validation set)
df['dropout_probability'] = gbc.predict_proba(X_train)[:, 0]
```

---

### Stage 5: Output Generation

**Output Files** (CSV format):

| File                      | Rows | Purpose                                    |
| ------------------------- | ---- | ------------------------------------------ |
| `conversations_clean.csv` | 1M   | Full cleaned dataset with all features     |
| `messages_sample.csv`     | 10K  | Stratified random sample for manual review |
| `daily_kpis.csv`          | ~500 | Aggregated daily metrics (time-series)     |
| `geo_summary.csv`         | ~200 | Geographic breakdown (country level)       |
| `prompt_categories.csv`   | 8    | Intent distribution by category            |
| `user_segments.csv`       | 5    | User cluster statistics                    |

**Tableau Data Extract** (.hyper format):

- Compressed columnar format
- Faster query performance in Tableau
- Refreshed daily as part of ETL run

---

## 🔄 Data Flow & Refresh Schedule

```
┌─────────────────────────────────────┐
│  ETL Pipeline Runs (Daily 2 AM UTC) │
└─────────────────────────────────────┘
         ↓
[1] New raw data ingested
[2] Cleaning & preprocessing
[3] Feature engineering
[4] Anomaly detection
[5] Output generation
         ↓
┌─────────────────────────────────────┐
│  Tableau Extracts Updated (3 AM UTC)│
└─────────────────────────────────────┘
         ↓
┌─────────────────────────────────────┐
│  Dashboards Refreshed & Available   │
│  Executive: 4 AM UTC (Daily)        │
│  Operational: Hourly (12 AM – 11 PM)│
│  Safety: Real-time monitoring       │
└─────────────────────────────────────┘
```

---

## 🔐 Data Security & Privacy

- **Raw Data**: Deleted after processing (not persisted)
- **Processed Datasets**: Anonymized (no PII)
- **Access Control**: Team-only GitHub; Tableau Public dashboards (anonymized aggregates only)
- **Audit Trail**: All transformations documented in notebooks

---

## 📈 Performance & Scalability

### Current Performance

- **ETL Runtime**: ~45 minutes (1M records)
- **Memory Usage**: ~12 GB (peak)
- **Storage**: ~5 GB (processed data)
- **Query Latency** (Tableau): < 2 seconds (95th percentile)

### Scalability Improvements (Future)

- **Apache Spark**: Distributed ETL for 10M+ records
- **Cloud Data Warehouse**: Snowflake, BigQuery (replace CSV storage)
- **Orchestration**: Apache Airflow for automated daily runs
- **GPU Acceleration**: RAPIDS for NLP feature extraction

---

## 🔗 Related Documentation

- Setup: [Installation Guide](../guides/SETUP.md)
- Usage: [Dashboard User Guide](../guides/USER_GUIDE.md)
- Development: [Developer Guide](../guides/DEVELOPER_GUIDE.md)
- Data: [Data Dictionary](../../data/dictionaries/data_dictionary.md)
- Project: [Root README](../../README.md)
