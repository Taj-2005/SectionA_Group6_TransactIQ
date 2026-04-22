# Processed Data Directory

This directory contains the cleaned, processed, and analytics-ready datasets generated from the WildChat-1M dataset through our comprehensive ETL pipeline.

## Dataset Overview

The WildChat Analytics Platform processes the AllenAI WildChat-1M dataset containing real-world ChatGPT conversations with metadata including geographic information, toxicity scores, and conversation structures. Our pipeline transforms raw conversational data into structured analytics-ready formats.

## Files Description

### Core Datasets

#### `conversations_clean.csv`
- **Description**: Cleaned conversation-level dataset with aggregated metrics
- **Rows**: ~100K unique conversations (sample) / ~1M (full dataset)
- **Key Columns**:
  - `conversation_id`: Unique identifier for each conversation
  - `turn_count`: Number of turns in the conversation
  - `start_time`, `end_time`: Conversation timestamps
  - `duration_seconds`: Length of conversation in seconds
  - `user_message_count`, `assistant_message_count`: Message counts by role
  - `avg_sentiment_score`: Average VADER sentiment for user messages
  - `toxicity_score`: Composite toxicity score from OpenAI moderation
  - `country`, `state`: Geographic information
  - `model`: AI model used (gpt-3.5-turbo, gpt-4, etc.)

#### `messages_sample.csv`
- **Description**: Individual message-level dataset with full text content
- **Rows**: ~500K+ individual messages (sample) / ~5M+ (full dataset)
- **Key Columns**:
  - `conversation_id`, `turn_id`: Message identifiers
  - `role`: User or assistant
  - `content`: Original message text
  - `content_clean`: Preprocessed text content
  - `token_count`: Number of tokens in message
  - `sentiment_score`: VADER sentiment score (user messages only)
  - `language`: Detected language code
  - `timestamp`: Message timestamp
  - `toxic`: Boolean toxicity flag

### Analytics Outputs

#### `user_segments.csv`
- **Description**: User segmentation analysis with behavioral metrics
- **Key Features**:
  - **Power Users**: Top 10% most active users by message count
  - **Casual Users**: Bottom 50% by activity
  - **Regular Users**: Middle 40% by activity
  - Metrics include: conversation frequency, average message length, sentiment patterns, model preferences

#### `prompt_categories.csv`
- **Description**: Categorized prompts using TF-IDF and K-means clustering
- **Categories**:
  - Coding and Technical
  - Factual Question Answering
  - Creative Writing
  - Emotional Support
  - Roleplay or Persona
  - Harmful or Policy Violating
  - Other
- **Columns**: Category labels, confidence scores, cluster centroids

#### `geo_summary.csv`
- **Description**: Geographic aggregation of conversation metrics
- **Granularity**: Country and state-level summaries
- **Metrics**: Conversation counts, average sentiment, toxicity rates, model usage patterns

#### `daily_kpis.csv`
- **Description**: Time-series key performance indicators
- **Metrics**: Daily conversation volumes, user engagement metrics, sentiment trends, toxicity incidents
- **Purpose**: Dashboard and reporting integration

#### `wildchat_combined.csv`
- **Description**: Master dataset combining all processed features
- **Usage**: Comprehensive analysis and machine learning model training
- **Size**: Largest consolidated dataset with all engineered features

## Data Processing Pipeline

### Stage 1: Extraction
- Source: AllenAI WildChat-1M dataset from HuggingFace Hub
- Method: Streaming extraction with configurable batch sizes
- Volume: 1M conversations, 5M+ message turns

### Stage 2: Cleaning
- Conversation explosion (list-of-dicts to structured format)
- Deduplication and quality checks
- Missing value handling and data type normalization
- Geographic and temporal validation

### Stage 3: Text Preprocessing
- Text normalization and PPI redaction removal
- Language detection (langdetect)
- Token counting and content length analysis
- VADER sentiment analysis (user messages only)

### Stage 4: Feature Engineering
- OpenAI moderation score parsing
- Composite toxicity scoring
- User behavior metrics
- Conversation-level aggregations
- Temporal and geographic features

### Stage 5: Analytics & ML
- User segmentation (power user identification)
- Prompt categorization (TF-IDF + K-means)
- Geographic clustering
- Time-series KPI generation

## Quality Assurance

### Data Validation
- Schema validation at each pipeline stage
- Referential integrity checks
- Outlier detection and handling
- Missing data impact assessment

### Privacy & Security
- IP address hashing (original IPs not stored)
- PII redaction placeholder removal
- Toxic content flagging and filtering
- GDPR-compliant data handling

## Usage Guidelines

### For Analytics
- Use `conversations_clean.csv` for conversation-level analysis
- Use `messages_sample.csv` for message-level insights
- Use `user_segments.csv` for user behavior studies
- Use `geo_summary.csv` for geographic analysis

### For Machine Learning
- Use `wildchat_combined.csv` for comprehensive model training
- Use `prompt_categories.csv` for classification tasks
- Use `user_segments.csv` for user prediction models

### For Reporting
- Use `daily_kpis.csv` for dashboard integration
- Use `geo_summary.csv` for geographic reporting
- All datasets include timestamp fields for time-series analysis

## Technical Specifications

### File Formats
- **Format**: CSV (UTF-8 encoded)
- **Compression**: Uncompressed for direct Tableau/BI tool integration
- **Size**: Varies by dataset (see individual file sizes)

### Schema Standards
- **Timestamps**: ISO 8601 format, UTC timezone
- **Identifiers**: SHA-256 hashes for conversation IDs
- **Scores**: Float values between 0.0 and 1.0
- **Categories**: String labels with consistent casing

### Performance Notes
- Optimized for pandas and SQL operations
- Indexed on conversation_id and timestamp fields
- Memory-efficient dtypes used throughout
- Suitable for both batch and streaming analytics

## Data Freshness

- **Last Updated**: Generated during pipeline execution
- **Update Frequency**: On-demand pipeline runs
- **Version Control**: Git-tracked with data versioning
- **Backup**: Original raw data preserved in `/data/raw/`

## Integration Points

### Tableau Dashboard
- Direct CSV connection support
- Geographic visualization ready
- Time-series dashboard compatible

### ML Pipeline
- Scikit-learn compatible formats
- Feature-engineered datasets ready
- Train/test split recommendations available

### API Integration
- RESTful data service endpoints
- Real-time analytics support
- Caching layer for performance

## Support & Documentation

For detailed pipeline code and methodology, refer to:
- Main notebook: `/notebooks/WildChat_Notebook.ipynb`
- Configuration: `/configs/`
- Documentation: `/docs/`

---

**Generated by**: WildChat Analytics Platform - Group G-6 (Section A)  
**Institution**: Rishihood University - Data Analytics Capstone 2025  
**Pipeline Version**: 1.0  
**Last Run**: See pipeline execution logs for timestamp