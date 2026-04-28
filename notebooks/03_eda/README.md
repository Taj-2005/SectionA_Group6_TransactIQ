# 03 - Exploratory Data Analysis (EDA)

This directory contains the primary exploratory analysis of the WildChat dataset (~50,516 conversations). The analysis aims to provide high-level business KPIs, understand user personas, and evaluate AI safety metrics.

## Contents

- **[03_eda.ipynb](03_eda.ipynb)**: A deep-dive analytical notebook structured as a three-part business dashboard:
    1.  **Executive Summary**:
        - Global KPIs: Average Quality Score (7.94), Total Tokens, and Volume.
        - Geographic Distribution: Heatmaps showing top activity in China, USA, Russia, Germany, and France.
        - Trend Analysis: Dual-axis plots correlating daily conversation volume with average token complexity.
    2.  **Operational Intelligence**:
        - Model Market Share: Distribution between `gpt-3.5-turbo` and `gpt-4`.
        - Language Support: Top languages identified (Chinese, English, Russian, German).
        - User Segmentation: Analysis of session depth (turns) and simulated session durations.
    3.  **Safety & Trust**:
        - Toxicity Monitoring: Rates by model and country.
        - Sentiment Analysis: Evaluating user satisfaction vs. model response tone.

## Key Insights & Methodology

- **Analytical Rationale (Log-Scaling)**: Session durations and token counts are highly right-skewed. The analysis employs log-scale distributions to visualize patterns across both typical short interactions and extreme power-user outliers.
- **Geographic Toxicity**: Identified specific regions where toxicity rates exceed the global average, aiding in localized safety tuning.
- **ETL Patching**: Addressed a known data gap where `session_duration_min` was consistently zero in raw logs. The notebook implements a simulation based on average reading speeds and response lengths to provide realistic operational estimates.
- **Visual Correlations**: Used heatmaps to identify the strongest relationships between prompt length and response quality.

## Requirements

The analysis relies on the following processed files in `data/processed/`:
- `conversations_clean.csv`
- `daily_kpis.csv`
- `geo_summary.csv`
- `prompt_categories.csv`
