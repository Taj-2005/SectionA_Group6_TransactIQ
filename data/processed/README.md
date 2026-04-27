# WildChat Processed Data Repository

This directory contains the processed and cleaned datasets derived from the WildChat-1M dataset, generated through a comprehensive ETL pipeline and analytical workflows.

## Overview

The processed data is the result of a multi-stage data processing pipeline that transforms raw WildChat conversation data into analysis-ready datasets. The pipeline includes data extraction, cleaning, text preprocessing, feature engineering, and statistical analysis to support comprehensive analytics and dashboard visualization.

## Data Processing Pipeline

### Stage 1: Extraction
- **Source**: AllenAI WildChat-1M dataset
- **Sample Size**: 50,000 conversations (streaming mode for efficiency)
- **Raw Fields**: 14 columns including conversation metadata, timestamps, and moderation data

### Stage 2: Cleaning
- **Duplicate Removal**: Eliminated duplicate conversations based on `conversation_hash`
- **Missing Value Handling**: 
  - `country` → "UNKNOWN"
  - `language` → "und" (undetermined)
- **Data Type Conversion**: 
  - `toxic` → integer
  - `timestamp` → datetime (UTC)
- **Final Cleaned Dataset**: 49,550 unique conversations

### Stage 3: Text Preprocessing
- **Conversation Flattening**: Transformed nested conversation structure into message-level records (290,714 messages)
- **Text Cleaning**: 
  - Lowercase conversion
  - Placeholder removal ([name], [email])
  - Whitespace normalization
- **Feature Extraction**:
  - Token count (word count)
  - Sentiment analysis using VADER
  - Toxicity scoring from OpenAI moderation data

### Stage 4: Feature Engineering
- **Conversation-Level Aggregates**:
  - Turn count per conversation
  - Average prompt length
  - Average sentiment score
  - Response quality scoring
  - Drop-off flags (≤2 turns)
- **User Classification**: Prompt categorization (Coding, Factual, Creative, Casual, Other)
- **Geographic Processing**: Country-based aggregation and toxicity rates
- **Temporal Analysis**: Daily KPIs and trends

### Stage 5: Output Generation
Multiple processed datasets generated for different analytical perspectives:

## Dataset Files

### Core Datasets

#### `conversations_clean.csv`
**Primary analysis dataset with conversation-level features**
- **Records**: 49,550 conversations
- **Key Features**:
  - `conversation_id`: Unique conversation identifier
  - `conv_turn_count`: Number of message turns
  - `avg_prompt_len`: Average prompt length in tokens
  - `avg_sentiment`: Average sentiment score (-1 to 1)
  - `country`, `language`, `model`: Geographic and technical metadata
  - `toxicity_score`: Moderation-based toxicity score
  - `toxic_flag`: Binary toxicity indicator (>0.30 threshold)
  - `drop_off_flag`: Early conversation termination flag
  - `response_quality_score`: Composite quality metric
  - `prompt_category`: User intent classification

#### `wildchat_combined_master.csv`
**Comprehensive master dataset with all features and daily KPIs**
- **Records**: 49,550 conversations
- **Features**: All conversation-level features plus daily aggregates
- **Additional Fields**:
  - `date`: Processing date
  - `conversation_count`: Daily conversation volume
  - `avg_tokens`: Daily average token usage
  - `toxicity_rate`: Daily toxicity percentage

### Analytical Datasets

#### `daily_kpis.csv`
**Time-series data for trend analysis**
- **Records**: 22 days of data
- **Metrics**:
  - `timestamp`: Date
  - `conversation_count`: Daily conversation volume
  - `avg_tokens`: Average token usage per day
  - `toxicity_rate`: Daily toxicity percentage

#### `geo_summary.csv`
**Geographic aggregation for regional analysis**
- **Records**: Countries with conversation activity
- **Metrics**:
  - `country`: Country name
  - `conversation_count`: Total conversations per country
  - `toxicity_rate`: Country-specific toxicity rate

#### `messages_sample.csv`
**Message-level data for detailed conversation analysis**
- **Records**: Sample of flattened message data
- **Features**:
  - Individual message content and metadata
  - Role-based analysis (user vs assistant)
  - Message-level sentiment and toxicity

#### `prompt_categories.csv`
**User intent classification data**
- **Categories**: Coding, Factual, Creative, Casual, Other
- **Usage**: Understanding user behavior patterns

## Data Quality and Validation

### Statistical Validation
- **Model Performance Comparison**: T-tests confirm significant differences between GPT-3.5 and GPT-4 quality scores
- **User Segmentation**: ANOVA tests validate distinct behavioral clusters
- **Feature Independence**: Chi-square tests analyze categorical relationships

### Quality Metrics
- **Response Quality Score**: Composite metric considering prompt length and toxicity
- **Sentiment Analysis**: VADER-based sentiment scoring (-1 to 1 scale)
- **Toxicity Detection**: Multi-category moderation analysis with configurable thresholds

### Known Issues and Patches
- **Session Duration**: Applied simulation patch for realistic session duration based on turn count
- **Data Completeness**: Handled missing values through imputation strategies

## Usage Guidelines

### For Executive Summary Analysis
- Use `conversations_clean.csv` for high-level KPIs
- Reference `daily_kpis.csv` for temporal trends
- Leverage `geo_summary.csv` for geographic insights

### For Operational Intelligence
- Analyze user segments in `conversations_clean.csv`
- Examine session patterns and drop-off predictors
- Use `messages_sample.csv` for detailed interaction analysis

### For Safety and Trust Analysis
- Focus on toxicity metrics across all datasets
- Analyze sentiment patterns by prompt category
- Cross-reference moderation data with user behavior

## Data Schema

### Conversation-Level Features
```python
{
    "conversation_id": "string",           # Unique identifier
    "conv_turn_count": "integer",          # Number of message exchanges
    "avg_prompt_len": "float",             # Average prompt length
    "avg_sentiment": "float",              # Sentiment score (-1 to 1)
    "country": "string",                   # Country code/name
    "language": "string",                  # Language code
    "model": "string",                     # AI model used
    "toxicity_score": "float",             # Toxicity probability
    "toxic_flag": "integer",               # Binary toxicity indicator
    "drop_off_flag": "integer",            # Early termination flag
    "response_quality_score": "float",     # Composite quality metric
    "prompt_category": "string"            # User intent classification
}
```

### Daily KPI Features
```python
{
    "timestamp": "date",                   # Date
    "conversation_count": "integer",       # Daily volume
    "avg_tokens": "float",                 # Average token usage
    "toxicity_rate": "float"               # Toxicity percentage
}
```

## Analytical Insights Available

### User Behavior Patterns
- **Segmentation**: Power Users, Casual Explorers, Task-Oriented, At-Risk Users, Adversarial/Abuse
- **Engagement Metrics**: Session duration, turn count, prompt complexity
- **Drop-off Predictors**: Logistic regression identifies key churn factors

### Content Analysis
- **Prompt Categories**: Classification across coding, factual, creative, and casual intents
- **Sentiment Trends**: Emotional tone analysis across user segments
- **Quality Assessment**: Response quality scoring by model and user type

### Safety and Trust
- **Toxicity Monitoring**: Multi-dimensional toxicity detection and trending
- **Geographic Risk**: Country-specific toxicity patterns
- **Model Safety**: Comparative safety analysis across AI models

## Technical Specifications

### Processing Environment
- **Primary Language**: Python 3.x
- **Core Libraries**: pandas, numpy, scikit-learn, nltk, vaderSentiment
- **Data Sources**: AllenAI WildChat-1M dataset via HuggingFace datasets

### Performance Metrics
- **Processing Volume**: 50,000 conversations → 290,714 messages
- **Memory Usage**: Optimized streaming for large dataset handling
- **Output Size**: ~20MB of processed data across all files

## Data Freshness

- **Last Updated**: April 2026
- **Processing Date**: Current timestamp embedded in master dataset
- **Version Control**: Git-tracked with CI/CD pipeline validation

## Contact and Support

For questions about the processed data, methodology, or analytical insights:
- Reference the source notebooks in `/notebooks/` directory
- Consult the ETL pipeline in `ETL _PIPELINE_NOTEBOOK/WildChat_Notebook.ipynb`
- Review analytical notebooks for detailed methodology

## Data Usage Ethics

This processed dataset maintains user privacy through:
- IP address hashing
- Content redaction where applicable
- Aggregated geographic data
- Anonymized user identifiers

Users should adhere to the original WildChat dataset terms of service and applicable data protection regulations.