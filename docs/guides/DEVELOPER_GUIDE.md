# Developer Guide

## Overview

This guide is for developers contributing to the WildChat Analytics pipeline, maintaining data infrastructure, or extending functionality.

---

## 🏗️ Project Architecture

### High-Level Data Flow

```
WildChat-1M Dataset (HuggingFace)
    ↓
[Stage 1: Extraction]
    ↓
[Stage 2: Cleaning & Normalization]
    ↓
[Stage 3: Text Preprocessing]
    ↓
[Stage 4: Feature Engineering]
    ↓
[Stage 5: Output Generation]
    ↓
Processed Data Files
    ↓
Tableau Dashboards
```

For detailed architecture, see: [System Design](../architecture/ARCHITECTURE.md)

---

## 🔧 Development Workflow

### 1. Setup Environment

```bash
# Clone repository
git clone https://github.com/Taj-2005/SectionA_Group6_WildChat.git
cd SectionA_Group6_WildChat

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Understanding the Pipeline

The ETL pipeline is organized into 3 Jupyter notebooks:

#### Stage 1–3: ETL Pipeline

**File**: `notebooks/01_etl_pipeline/WildChat_Notebook.ipynb`

**Responsibilities**:

- Download WildChat-1M from HuggingFace
- Clean raw data (handle nulls, normalize text)
- Preprocess text (tokenization, lemmatization)
- Output: `data/processed/conversations_clean.csv`

**Key Functions**:

- `load_dataset()` — Streams dataset from HuggingFace
- `clean_conversations()` — Data validation and normalization
- `preprocess_text()` — NLP preprocessing (NLTK, spaCy)
- `generate_outputs()` — Write clean data to CSV

#### Stage 4: Feature Engineering

**File**: `notebooks/03_feature_engineering/03_features.ipynb`

**Responsibilities**:

- Compute engagement metrics (turn count, drop-off)
- Create NLP features (sentiment, toxicity, intent)
- Apply clustering and anomaly detection
- Build predictive models

**Key Functions**:

- `compute_engagement_metrics()` — Engagement stats
- `compute_nlp_features()` — Sentiment, toxicity, entities
- `cluster_users()` — K-Means clustering (k=5)
- `detect_anomalies()` — Isolation Forest on KPIs
- `train_dropout_predictor()` — Gradient Boost classifier

#### Stage 2: EDA & Validation

**File**: `notebooks/02_exploratory_data_analysis/02_eda.ipynb`

**Responsibilities**:

- Exploratory analysis (distributions, correlations)
- Data quality checks
- Validate feature engineering outputs
- Generate insights and recommendations

---

## 📊 Data Schema

For complete schema definitions:

- See: [Data Dictionary](../../data/dictionaries/data_dictionary.md)

### Input Schema (WildChat-1M)

| Column            | Type       | Example                                  |
| ----------------- | ---------- | ---------------------------------------- |
| `conversation_id` | String     | "abc123"                                 |
| `user_id`         | String     | "user_456"                               |
| `messages`        | List[Dict] | `[{"role": "user", "content": "Hello"}]` |
| `language`        | String     | "en"                                     |
| `timestamp`       | DateTime   | "2023-01-15T10:30:00Z"                   |

### Output Schema (conversations_clean.csv)

| Column            | Type   | Computation           |
| ----------------- | ------ | --------------------- |
| `conversation_id` | String | From input            |
| `turn_count`      | Int    | Len(messages)         |
| `engagement_flag` | Bool   | turn_count ≥ 3        |
| `toxicity_score`  | Float  | Multi-model ensemble  |
| `language`        | String | langdetect prediction |
| `country`         | String | IP geolocation        |

---

## 🔄 Making Changes

### Adding a New Feature

1. **Edit the feature engineering notebook**:

   ```
   notebooks/03_feature_engineering/03_features.ipynb
   ```

2. **Define your computation**:

   ```python
   def compute_my_feature(df):
       """
       Args:
           df: DataFrame with columns [...]
       Returns:
           Series with feature values
       """
       # Your logic here
       return result
   ```

3. **Apply to dataset**:

   ```python
   df['my_feature'] = compute_my_feature(df)
   ```

4. **Validate output**:

   ```python
   # Check for nulls, outliers, type consistency
   assert df['my_feature'].dtype == 'float64'
   assert df['my_feature'].isna().sum() == 0
   ```

5. **Update Data Dictionary**:
   - Add row to [data/dictionaries/data_dictionary.md](../../data/dictionaries/data_dictionary.md)
   - Document: name, type, computation, example values

6. **Test**: Run the notebook end-to-end
   ```bash
   cd notebooks/03_feature_engineering
   jupyter nbconvert --to notebook --execute 03_features.ipynb
   ```

### Adding a New Dashboard

1. **Create workbook in Tableau Desktop**
   - Data source: Connect to `data/processed/conversations_clean.csv` or specific CSV

2. **Save to** `dashboards/tableau/workbooks/`

3. **Create associated README** in `dashboards/tableau/`
   - Document filters, visualizations, audience, refresh rate

4. **Publish to Tableau Public**
   - File → Publish to Tableau Public
   - Get share URL

5. **Update** [dashboards/README.md](../../dashboards/README.md)
   - Add entry to dashboard index
   - Link to published dashboard

### Running Tests

Currently, the project uses notebook-based validation. For future improvements:

```bash
# Validate all notebooks run without error
pytest notebooks/ --nbval

# Check code style
pylint notebooks/*.py

# Type checking (if type hints added)
mypy --strict notebooks/
```

---

## 🐛 Debugging

### Common Issues

#### Dataset Download Fails

```python
# Check HuggingFace API connectivity
import huggingface_hub
print(huggingface_hub.list_repo_files('allenai/WildChat-1M'))
```

#### Memory Error (Dataset Too Large)

```python
# Stream smaller batches instead of loading all
dataset = load_dataset('allenai/WildChat-1M', split='train', streaming=True)
```

#### Null Values in Output

```python
# Check for nulls
print(df.isna().sum())

# Identify source
print(df[df['column'].isna()].head())
```

#### Model Training Fails

```python
# Verify feature types and shapes
print(X.shape, y.shape)
print(X.dtypes)
print(y.value_counts())  # Check class balance
```

---

## 📚 Dependencies

For complete dependency list:

- See: [requirements.txt](../../requirements.txt)

**Key Libraries**:

- **pandas** — Data manipulation
- **scikit-learn** — ML models (clustering, anomaly detection)
- **nltk** — Text preprocessing
- **spacy** — NLP features
- **transformers** — Pre-trained language models
- **datasets** — HuggingFace streaming
- **jupyter** — Notebook environment

To add a dependency:

```bash
pip install <package>
pip freeze > requirements.txt
```

---

## 🚀 Performance Optimization

### Notebook Execution Time

**Current bottlenecks**:

- Dataset download (first run): ~20 minutes
- Toxicity scoring (multi-model ensemble): ~5 minutes
- Clustering & anomaly detection: ~2 minutes

**Optimization strategies**:

- Cache datasets locally after first download
- Batch inference for toxicity models
- Use GPU for transformer models (if available)

### Memory Management

```python
# Release memory after large computations
del df_temp
import gc
gc.collect()

# Use chunking for large datasets
for chunk in pd.read_csv('file.csv', chunksize=10000):
    process(chunk)
```

---

## 📋 Code Style & Standards

**Python Style**: PEP 8

- Line length: 88 characters (Black formatter)
- Use type hints where possible
- Docstrings: Google format

**Notebook Standards**:

- Clear cell organization (markdown headers)
- Comments for complex logic
- Cell output cleared before commit
- No hardcoded file paths (use relative paths or `os.path.join`)

---

## 🔗 Contributing

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/my-feature`
3. **Make changes** and test thoroughly
4. **Update** [data/dictionaries/data_dictionary.md](../../data/dictionaries/data_dictionary.md) if schema changes
5. **Commit** with clear messages: `git commit -m "Add my feature: description"`
6. **Push** and create a Pull Request

---

## Next Steps

- Setup: [Installation Guide](SETUP.md)
- Architecture: [System Design](../architecture/ARCHITECTURE.md)
- Dashboard: [User Guide](USER_GUIDE.md)
- Dataset: [Data Dictionary](../../data/dictionaries/data_dictionary.md)

---

## Questions?

Contact the development team or open a GitHub issue.
