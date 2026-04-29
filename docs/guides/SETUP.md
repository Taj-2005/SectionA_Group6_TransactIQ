# Project Setup Guide

## Environment Prerequisites

- **Python**: 3.9+
- **Package Manager**: pip (or conda)
- **Storage**: 50GB+ free disk space (for dataset download and processing)

## Installation Steps

### 1. Clone Repository

```bash
git clone https://github.com/Taj-2005/SectionA_Group6_WildChat.git
cd SectionA_Group6_WildChat
```

### 2. Create Virtual Environment

**Using venv** (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate  # On Windows
```

**Using conda**:

```bash
conda create -n wildchat python=3.9
conda activate wildchat
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
python -c "import pandas; import nltk; print('✓ All dependencies installed')"
```

---

## Running the ETL Pipeline

### Quick Start

```bash
cd notebooks/01_etl_pipeline
jupyter notebook WildChat_Notebook.ipynb
```

### Full Pipeline Execution

The ETL pipeline is split into 3 stages:

1. **ETL Pipeline** (`notebooks/01_etl_pipeline/WildChat_Notebook.ipynb`)
   - Downloads WildChat-1M dataset from HuggingFace
   - Cleans and normalizes raw data
   - Outputs: `data/processed/conversations_clean.csv`

2. **Exploratory Data Analysis** (`notebooks/02_exploratory_data_analysis/02_eda.ipynb`)
   - Analyzes distributions, correlations, anomalies
   - Validates data quality
   - Generates preliminary insights

3. **Feature Engineering** (`notebooks/03_feature_engineering/03_features.ipynb`)
   - Creates engineered features for ML models
   - Applies clustering, anomaly detection, predictive scoring
   - Outputs: `data/processed/` (daily_kpis.csv, geo_summary.csv, etc.)

---

## Tableau Dashboard Setup

### View Dashboards (No Installation Required)

Published dashboards are available online:

- **Link**: [WildChat Analytics Platform on Tableau Public](https://public.tableau.com/views/WildChat_Analytics_Platform/ExecutiveSummary?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

### Work with Local Workbook (Requires Tableau Desktop)

1. Open **Tableau Desktop**
2. File → Open
3. Navigate to: `dashboards/tableau/workbooks/WildChat_Analytics_Platform (1).twbx`
4. Connect to local or cloud data sources as needed

---

## Data Dictionary Reference

For column definitions, data types, and transformation logic:

- See: [Data Dictionary](../../data/dictionaries/data_dictionary.md)

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'pandas'"

```bash
pip install pandas numpy scikit-learn
```

### Dataset Download Fails

The WildChat-1M dataset (~20GB) is streamed from HuggingFace. Ensure:

- Active internet connection
- Sufficient disk space (50GB+)
- HuggingFace API accessible

### Tableau Connection Issues

If Tableau can't connect to data files:

1. Verify file paths are absolute (not relative)
2. Check file permissions (read access required)
3. Restart Tableau and reload the workbook

---

## Next Steps

- Read: [Architecture Overview](../architecture/ARCHITECTURE.md)
- Review: [Dashboard User Guide](USER_GUIDE.md)
- Explore: [Developer Guide](DEVELOPER_GUIDE.md)
