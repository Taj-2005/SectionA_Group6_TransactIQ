# 02 — Exploratory Data Analysis (EDA)

Comprehensive exploratory analysis of the WildChat dataset transforming raw 1M+ conversations into structured business insights. This notebook serves as the analytical foundation for all downstream dashboards and strategic decisions.

---

## 📊 Notebook Overview

**File**: `02_eda.ipynb`  
**Purpose**: End-to-end exploratory analysis producing executive KPIs, operational insights, and safety metrics  
**Scope**: ~50,516 conversations with 290K+ individual messages  
**Output**: Visualizations, statistical summaries, and actionable recommendations

### Structure: 3-Part Business Analysis

#### Part 1: Executive Summary

Global KPIs, geographic distribution, and trend analysis for C-suite decision-making.

- **Global KPIs**:
  - Average Quality Score: 7.94 / 10
  - Total Tokens Processed: 2.3M+
  - Conversation Volume: 50,516

- **Geographic Distribution**: Heatmaps identifying top activity
  - Top 5: China, USA, Russia, Germany, France
  - Geolocation mapping and regional concentration analysis

- **Trend Analysis**: Dual-axis plots correlating daily volume with token complexity
  - Conversation volume trending
  - Token complexity trends (inversely related to user base saturation)

#### Part 2: Operational Intelligence

Product performance, user behavior, and model capabilities for product managers and ML engineers.

- **Model Market Share**:
  - Distribution between GPT-3.5-turbo and GPT-4
  - Quality score differential (GPT-4 avg: 9.44 vs GPT-3.5: 7.17)
  - Cost-benefit analysis for model selection

- **Language Support**:
  - Top languages identified (Chinese, English, Russian, German, French)
  - Language distribution by volume and quality
  - Multilingual coverage gaps and equity issues

- **User Segmentation**:
  - Session depth analysis (mean turns per conversation)
  - Power-user identification (top 8% = 41% of activity)
  - Engagement cohorts (power users, task-oriented, casual, at-risk, adversarial)
  - Simulated session durations (addressing ETL data gaps)

#### Part 3: Safety & Trust

Toxicity monitoring, sentiment analysis, and compliance metrics for safety teams and policy makers.

- **Toxicity Monitoring**:
  - Toxicity rates by model and country
  - Temporal patterns (10 PM–2 AM spikes)
  - High-risk geographies and categories

- **Sentiment Analysis**:
  - User satisfaction proxy scores (VADER sentiment)
  - Model response tone evaluation
  - Frustration signals (sentiment < -0.3 at turn 3)

- **Compliance Metrics**:
  - Policy violation frequency
  - Redaction rates and PII detection
  - Audit trail for regulatory review

---

## 🔍 Key Insights & Methodology

### Analytical Approach

**Log-Scaling for Right-Skewed Data**

- Session durations and token counts follow log-normal distributions
- Majority of interactions are brief; long-tail power users drive analysis
- **Solution**: Log-scale visualizations reveal both typical patterns and outlier behavior simultaneously
- **Impact**: Enables accurate forecasting for both casual and power user segments

### Critical Findings

| Finding                      | Data Signal                            | Business Impact                       | Action                                |
| ---------------------------- | -------------------------------------- | ------------------------------------- | ------------------------------------- |
| **Drop-off Crisis**          | 62% end at Turn 2                      | Model quality failure at scale        | Prioritize first-response improvement |
| **Toxicity Windows**         | 10 PM–2 AM spike (2–3×)                | Adversarial behavior clustering       | Deploy time-aware moderation filters  |
| **Power User Concentration** | Top 8% = 41% activity                  | Retention risk + platform dependency  | Create power-user retention programs  |
| **Language Quality Gap**     | 2.4× higher non-English failure        | Equity issue; underserved markets     | Fast-track multilingual fine-tuning   |
| **Quality Compounding**      | Sessions >8 turns = 35% higher quality | Early quality drives engagement depth | Invest in Turn 1–3 for ROI            |

### Data Processing Notes

**ETL Patching**: Session Duration Reconstruction

- Raw logs had consistent zero values for `session_duration_min`
- Implemented simulation based on:
  - Average reading speed: 200 WPM
  - Token-to-word ratio: ~1.3×
  - Response generation time: ~2 sec/turn
- **Validation**: Simulated durations align with content length distributions

**Geographic Analysis**

- Identified specific regions where toxicity exceeds global average
- Enables localized safety tuning (e.g., tighter filters for high-risk regions)
- Supports compliance with regional content policies (GDPR, China regulations, etc.)

---

## 📈 Analysis Outputs

### Visualizations Generated

1. **Geographic Heatmaps**
   - Conversation density by country
   - Quality score distribution across regions
   - Toxicity concentration patterns

2. **Trend Charts**
   - Daily conversation volume (30-90 day view)
   - Weekly engagement cycles
   - Model performance tracking

3. **Distribution Plots**
   - Turn count (log-scale) showing bimodal pattern
   - Prompt length distribution (right-skewed)
   - Quality score distribution (near-normal)
   - Sentiment distribution (bimodal: satisfaction peaks + frustration peaks)

4. **Comparative Analysis**
   - Model comparison (quality, drop-off, toxicity by version)
   - Language performance gaps
   - Geographic quality variance

5. **Segment Profiles**
   - User cluster characteristics (5 clusters from K-Means)
   - Engagement patterns by segment
   - At-risk cohort identification

### Statistical Summaries

- Summary statistics for all KPIs (mean, median, std, min, max)
- Percentile breakdowns (10th, 25th, 50th, 75th, 90th)
- Correlation matrices (quality vs. length, sentiment vs. continuation, etc.)
- Anomaly flagging (Z-score > 2.5)

---

## 🛠️ Technical Stack

| Layer             | Tools                                                  |
| ----------------- | ------------------------------------------------------ |
| **Data I/O**      | pandas (CSV read), NumPy                               |
| **Analysis**      | pandas groupby aggregations, rolling statistics        |
| **Visualization** | Matplotlib, Seaborn (publication-quality plots)        |
| **Statistics**    | SciPy stats (describe, percentileofscore)              |
| **Geospatial**    | GeoPandas (optional, for map projection)               |
| **Utilities**     | warnings (suppress expected messages), os (file paths) |

---

## 📋 Data Requirements

### Input Files

Located in `data/processed/`:

```python
# Main datasets (created by ETL pipeline)
conversations_clean.csv          # One row per conversation
daily_kpis.csv                   # Pre-aggregated daily metrics
geo_summary.csv                  # Country-level rollups
prompt_categories.csv            # Category distributions
```

### Column Dependencies

```python
# From conversations_clean.csv
conversation_id
turn_count                       # Conversation depth (turns)
avg_prompt_len_tokens            # User message length
avg_response_len_tokens          # AI response length
response_quality_score           # 0–10 heuristic
avg_sentiment_score              # -1 to +1 (VADER)
max_toxicity_score               # 0–1 composite
has_toxic_flag                   # Binary flag
country                          # ISO country code
language                         # ISO language code
model                            # Model version
hour_of_day                      # Temporal feature
session_duration_min             # Conversation duration
drop_off_flag                    # Turn count ≤ 2
is_power_user                    # Top 10% engagement
```

---

## 🚀 How to Run

### Prerequisites

- Python 3.9+
- Jupyter Notebook or JupyterLab
- Dependencies: `pip install -r requirements.txt`

### Execution Steps

1. **Navigate to notebook**

   ```bash
   cd notebooks/02_exploratory_data_analysis
   ```

2. **Start Jupyter**

   ```bash
   jupyter notebook 02_eda.ipynb
   ```

3. **Execute sequentially**
   - Cell 1: Imports & configuration
   - Cells 2–5: Load data, validate schema
   - Cells 6–15: Executive analysis (Part 1)
   - Cells 16–25: Operational analysis (Part 2)
   - Cells 26–35: Safety analysis (Part 3)
   - Cell 36+: Export visualizations to `/outputs/`

### Output Artifacts

- **Visualizations**: Saved to `notebooks/02_exploratory_data_analysis/outputs/` as `.png` files
- **Summary Stats**: Printed to notebook + optional `.csv` export
- **Interactive Plots**: Display in-notebook (Jupyter frontend)

---

## 📊 Key Metrics Explained

### Engagement Rate

**Definition**: % of conversations with ≥3 turns  
**Formula**: `(Conversations with turns ≥ 3 / Total conversations) × 100`  
**Target**: >70% (indicates sustained user engagement)  
**Interpretation**: Higher = better product-market fit; lower = early quality failure

### Drop-off Rate

**Definition**: % of conversations ending at turn 1–2  
**Formula**: `(Conversations with turns ≤ 2 / Total conversations) × 100`  
**Target**: <35% (minimizes early abandonment)  
**Interpretation**: Single-turn conversations indicate immediate user dissatisfaction

### Response Quality Score

**Definition**: Heuristic 0–10 composite quality metric  
**Components**:

- 30%: Length appropriateness (not too short, not too long)
- 40%: Lexical diversity (vocabulary richness; avoid repetition)
- 30%: Coherence (semantic consistency)

**Interpretation**: Strongly correlates with user continuation behavior

### Toxicity Rate

**Definition**: % of conversations flagged as containing unsafe/policy-violating content  
**Source**: OpenAI moderation API + HuggingFace toxicity classifier  
**Target**: <5% baseline; alert if >6%  
**Interpretation**: Safety compliance metric; direct regulatory risk

---

## 🎯 Strategic Recommendations

Based on EDA findings, prioritize:

1. **First-Response Quality** (Highest ROI)
   - 62% drop-off at Turn 2 is the dominant issue
   - Targeted improvements to Turn 1 responses
   - A/B test longer, more structured initial replies
   - Expected lift: +15–25% engagement

2. **Time-Aware Safety Filters**
   - 10 PM–2 AM toxicity spikes require automated moderation
   - Escalate filter sensitivity during high-risk windows
   - Expected impact: 60% reduction in manual review overhead

3. **Multilingual Quality Parity**
   - 2.4× higher failure rate for non-English users
   - Prioritize top 5 non-English languages
   - Commission targeted QA and model fine-tuning
   - Expected lift: +30% non-English retention

4. **Power-User Retention**
   - Top 8% drive 41% of activity; churn risk is high
   - Create dedicated retention programs
   - Monitor satisfaction separately from general cohorts

5. **Invest in Early Turns**
   - Sessions >8 turns score 35% higher on quality
   - Early quality drives compounding engagement
   - Highest ROI intervention point: Turns 1–3

---

## 📚 Methodology References

### Statistical Methods

- **Percentiles**: Identify outliers and distribution shape
- **Correlation Analysis**: Quantify relationships between features
- **Time-Series**: Detect trends and cyclical patterns
- **Anomaly Detection**: Z-score flagging for unusual activity

### Visualization Best Practices

- **Log-Scale**: For right-skewed distributions
- **Dual-Axis**: Correlate two metrics over time
- **Heatmaps**: Show patterns across two categorical dimensions
- **Box Plots**: Display distributions + quartiles + outliers

---

## 🔗 Related Documentation

- [ETL Pipeline](../01_etl_pipeline/README.md) — Data source & processing
- [Feature Engineering](../03_feature_engineering/README.md) — Statistical validation & ML models
- [Data Dictionary](../../data/dictionaries/data_dictionary.md) — Column definitions
- [Dashboard Guide](../../dashboards/tableau/README.md) — Visualization usage
- [Root README](../../README.md) — Project overview

---

## ✅ Validation Checklist

Before committing findings:

- [ ] All data files exist in `data/processed/`
- [ ] Row counts match ETL outputs
- [ ] No missing values in key columns
- [ ] KPI values align with expectations
- [ ] Visualizations are publication-quality
- [ ] Findings grounded in statistical significance
- [ ] Recommendations are actionable and prioritized

---

**Questions?** See [Root README](../../README.md) or contact Analysis Lead.
