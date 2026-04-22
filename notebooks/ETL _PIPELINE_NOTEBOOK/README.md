# Notebooks Directory

This directory contains the complete analytical workspace for the WildChat Analytics Platform, organized by pipeline stages for systematic data processing and analysis.

## Project Overview

The WildChat Analytics Platform is a comprehensive ETL and analytics pipeline built to process the AllenAI WildChat-1M dataset. This platform transforms raw ChatGPT conversation data into actionable insights through advanced NLP techniques, machine learning, and statistical analysis.

**Team**: Group G-6 (Section A) | Rishihood University | Data Analytics Capstone 2025

---

## Main Pipeline Notebook

### `WildChat_Notebook.ipynb`
**Primary analytical pipeline and comprehensive data processing notebook**

This is the main executable notebook that orchestrates the entire data processing pipeline from raw data extraction to final analytics outputs.

#### Key Features:
- **Google Colab Optimized**: Ready-to-run with GPU acceleration
- **Streaming Data Processing**: Handles 1M+ conversations efficiently
- **Modular Architecture**: 6 distinct processing stages
- **Progress Tracking**: Real-time progress bars and status updates
- **Configurable Parameters**: Easy adjustment for testing vs. production runs

#### Pipeline Stages:

1. **STAGE 1 - EXTRACTION**
   - Streaming download from HuggingFace Hub
   - Configurable batch processing (50K rows per batch)
   - Memory-efficient handling of large datasets
   - Progress tracking with tqdm

2. **STAGE 2 - CLEANING**
   - Conversation explosion (nested list to structured format)
   - Deduplication and quality validation
   - Missing value handling and data type normalization
   - Geographic and temporal data validation
   - Model name standardization

3. **STAGE 3 - TEXT PREPROCESSING**
   - Text normalization and cleaning
   - PII redaction placeholder removal
   - Language detection using langdetect
   - Token counting and content analysis
   - VADER sentiment analysis (user messages only)

4. **STAGE 4 - FEATURE ENGINEERING**
   - OpenAI moderation score parsing
   - Composite toxicity scoring
   - User behavior metrics calculation
   - Conversation-level aggregations
   - Temporal and geographic feature extraction

5. **STAGE 5 - ANALYTICS & ML**
   - User segmentation analysis
   - Prompt categorization using TF-IDF + K-means
   - Geographic clustering and analysis
   - Time-series KPI generation

6. **STAGE 6 - EXPORTS**
   - Tableau-ready CSV generation
   - Analytics output files
   - Summary statistics and reports

#### Configuration Options:
```python
CFG = {
    "dataset_name": "allenai/WildChat-1M",
    "batch_size": 50_000,
    "max_batches": 20,          # Full dataset: 20 × 50k = 1M rows
    "sample_batches": 2,        # Quick test: 2 × 50k = 100k rows
    "min_content_len": 3,
    "power_user_pct": 0.90,
    "kmeans_k": 5,
    "tfidf_max_feat": 5_000,
}
```

#### Dependencies:
- **Core**: pandas, numpy, scikit-learn
- **NLP**: nltk, vaderSentiment, langdetect, transformers
- **ML**: datasets, accelerate
- **Visualization**: matplotlib, seaborn
- **Utilities**: tqdm, openpyxl

---

## Modular Notebook Structure

### `01_ingest/` - Data Ingestion & Schema Validation
**Purpose**: Raw data extraction and initial quality checks

**Expected Contents**:
- Data source connection testing
- Schema validation scripts
- Initial data quality reports
- Sampling strategies for testing

**Key Functions**:
- HuggingFace dataset streaming
- Batch processing optimization
- Memory usage monitoring
- Data integrity validation

### `02_clean/` - Data Cleaning & Normalization
**Purpose**: Transform raw data into clean, structured format

**Expected Contents**:
- Conversation explosion logic
- Missing value handling strategies
- Data type standardization
- Deduplication algorithms

**Key Functions**:
- Nested JSON flattening
- Geographic data validation
- Timestamp normalization
- Model name standardization

### `03_eda/` - Exploratory Data Analysis
**Purpose**: Understand data patterns and generate hypotheses

**Expected Contents**:
- Statistical summaries
- Distribution analysis
- Correlation matrices
- Anomaly detection

**Key Analyses**:
- Conversation length distributions
- User activity patterns
- Geographic usage patterns
- Temporal trend analysis
- Toxicity prevalence studies

### `04_features/` - Feature Engineering for Analytics & ML
**Purpose**: Create predictive and analytical features

**Expected Contents**:
- Sentiment analysis implementations
- Toxicity scoring algorithms
- User behavior metrics
- Conversation-level features

**Feature Categories**:
- Text-based features (sentiment, complexity)
- Temporal features (response times, session duration)
- Behavioral features (message patterns, model preferences)
- Geographic features (regional usage patterns)

### `05_ml/` - Machine Learning Experiments
**Purpose**: Build predictive models and advanced analytics

**Expected Contents**:
- User segmentation models
- Prompt classification systems
- Anomaly detection algorithms
- Predictive analytics experiments

**Model Types**:
- **Clustering**: K-means for prompt categorization
- **Classification**: User behavior prediction
- **Anomaly Detection**: Isolation Forest for unusual patterns
- **Time Series**: Trend analysis and forecasting

### `06_exports/` - Data Exports & Reporting
**Purpose**: Generate production-ready outputs

**Expected Contents**:
- Tableau-compatible CSV exports
- Summary statistics reports
- Data dictionaries
- Quality assurance reports

**Export Formats**:
- **Analytics Ready**: Cleaned CSV files
- **ML Ready**: Feature-engineered datasets
- **Reporting Ready**: Aggregated summaries
- **Dashboard Ready**: KPI datasets

---

## Usage Guidelines

### Quick Start (Testing)
1. Open `WildChat_Notebook.ipynb` in Google Colab
2. Set `sample_batches = 2` in configuration
3. Run cells sequentially (top to bottom)
4. Expected runtime: ~5 minutes for 100K rows

### Production Run (Full Dataset)
1. Set `sample_batches = max_batches = 20`
2. Ensure GPU runtime in Colab
3. Expected runtime: ~2-3 hours for 1M rows
4. Monitor memory usage and batch processing

### Development Workflow
1. Use modular notebooks for feature development
2. Test in `01_ingest/` → `02_clean/` → `03_eda/` sequence
3. Integrate proven features into main pipeline
4. Update configuration parameters as needed

---

## Performance Considerations

### Memory Management
- Streaming data loading to avoid memory overflow
- Batch processing for large datasets
- Efficient data type usage (category, int32, float32)
- Garbage collection between stages

### Computational Efficiency
- GPU acceleration for NLP tasks
- Vectorized operations with pandas/numpy
- Parallel processing where possible
- Progress tracking for long-running operations

### Scalability
- Configurable batch sizes
- Modular architecture for distributed processing
- Cloud-ready implementation
- API integration capabilities

---

## Quality Assurance

### Data Validation
- Schema validation at each stage
- Referential integrity checks
- Statistical validation of outputs
- Cross-validation of ML models

### Code Quality
- Comprehensive documentation
- Error handling and logging
- Progress tracking and status updates
- Modular, reusable functions

### Reproducibility
- Fixed random seeds for ML models
- Configuration-driven pipeline
- Version-controlled notebooks
- Detailed execution logs

---

## Integration Points

### Tableau Dashboard
- Direct CSV output from `06_exports/`
- Geographic data ready for mapping
- Time-series data for trend analysis
- Pre-calculated KPIs for dashboards

### ML Pipeline
- Scikit-learn compatible outputs
- Feature-engineered datasets
- Train/test split recommendations
- Model performance metrics

### API Integration
- RESTful service ready outputs
- Real-time processing capabilities
- Caching layer support
- Monitoring and alerting integration

---

## Technical Requirements

### Minimum Specifications (Testing)
- **RAM**: 8GB
- **Storage**: 2GB free space
- **Runtime**: CPU-only acceptable
- **Time**: 5-10 minutes

### Recommended Specifications (Production)
- **RAM**: 16GB+
- **GPU**: T4 or better (Colab)
- **Storage**: 10GB+ free space
- **Time**: 2-3 hours for full dataset

### Software Dependencies
- Python 3.8+
- Jupyter Notebook/Google Colab
- All packages listed in requirements.txt
- HuggingFace account for dataset access

---

## Troubleshooting

### Common Issues
- **Memory Errors**: Reduce batch_size or sample_batches
- **GPU Not Available**: Switch to CPU runtime (slower)
- **Dataset Access**: Verify HuggingFace authentication
- **Slow Processing**: Check internet connection and Colab resources

### Performance Tips
- Use GPU runtime for faster NLP processing
- Monitor memory usage during extraction
- Save intermediate results for debugging
- Use smaller sample sizes for development

---

## Project Documentation

For additional information:
- **Main README**: `/README.md` (project overview)
- **Configuration**: `/configs/` (pipeline settings)
- **Data Dictionary**: `/docs/data-dictionary.md`
- **API Documentation**: `/docs/api-reference.md`
- **Dashboard Guide**: `/docs/dashboard-guide.md`

---

**Last Updated**: Pipeline execution timestamp  
**Version**: 1.0  
**Environment**: Google Colab (GPU recommended)  
**Support**: Group G-6, Rishihood University

