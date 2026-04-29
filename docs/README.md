# `docs/` — Project Documentation

Central repository for setup guides, architecture documentation, and source materials. Everything you need to understand, deploy, and contribute to the WildChat Analytics Platform.

---

## 📁 Folder Structure

```
docs/
├── guides/                ← How-to guides and setup instructions
│   ├── SETUP.md          ← Installation & environment setup
│   ├── USER_GUIDE.md     ← How to use Tableau dashboards
│   ├── DEVELOPER_GUIDE.md ← How to contribute to the pipeline
│   └── tableau_guide.pdf ← Tableau platform reference guide
├── architecture/         ← Technical design and system architecture
│   └── ARCHITECTURE.md   ← End-to-end pipeline design
└── PRD/                  ← Product requirements and project brief
    └── PRD.pdf          ← Original capstone brief document
```

---

## 🚀 Quick Start by Role

### 👤 **New Team Member?**

Start here → [SETUP.md](guides/SETUP.md)

1. Clone repo and create virtual environment
2. Install dependencies
3. Run your first notebook
4. ✅ You're ready to contribute

---

### 📊 **Using the Dashboards?**

Start here → [USER_GUIDE.md](guides/USER_GUIDE.md)

- All 3 dashboards explained (Executive, Operational, Safety)
- Common use cases and troubleshooting
- KPI definitions and metric references
- Mobile access guide

---

### 💻 **Contributing to Code?**

Start here → [DEVELOPER_GUIDE.md](guides/DEVELOPER_GUIDE.md)

- Development workflow
- Adding features and models
- Making changes to the ETL pipeline
- Code style and standards
- Debugging tips

---

### 🏗️ **Understanding the Architecture?**

Start here → [ARCHITECTURE.md](architecture/ARCHITECTURE.md)

- Complete data pipeline flow (5 stages)
- Data schema and transformations
- Feature engineering methods
- Dashboard design
- Performance and scalability

---

## 📚 Complete Documentation Map

| Role           | Document                                                   | Purpose                         |
| -------------- | ---------------------------------------------------------- | ------------------------------- |
| **All**        | [SETUP.md](guides/SETUP.md)                                | Environment setup, dependencies |
| **Analysts**   | [USER_GUIDE.md](guides/USER_GUIDE.md)                      | Dashboard usage, KPIs, insights |
| **Developers** | [DEVELOPER_GUIDE.md](guides/DEVELOPER_GUIDE.md)            | Code contribution, debugging    |
| **Engineers**  | [ARCHITECTURE.md](architecture/ARCHITECTURE.md)            | System design, data flow        |
| **All**        | [Root README](../README.md)                                | Project overview, team, roadmap |
| **All**        | [Data Dictionary](../data/dictionaries/data_dictionary.md) | Column definitions, formulas    |
| **All**        | [Dashboards Guide](../dashboards/README.md)                | BI platform overview            |

---

## 🔧 Essential Reference Files

### Data & Schema

- **[Data Dictionary](../data/dictionaries/data_dictionary.md)** — Column definitions, transformations, KPI formulas
- Used by: Everyone (analysts, engineers, analysts)

### Notebooks & Code

- **[ETL Pipeline](../notebooks/01_etl_pipeline/README.md)** — Data extraction, cleaning, preprocessing
- **[EDA Analysis](../notebooks/02_exploratory_data_analysis/README.md)** — Exploratory insights and validation
- **[Feature Engineering](../notebooks/03_feature_engineering/README.md)** — ML models and metrics

### Source Materials

- **[Product Requirements](PRD/PRD.pdf)** — Original project brief
- **[Tableau Guide](guides/tableau_guide.pdf)** — Platform reference

---

## 🔄 Common Tasks

### "I want to set up my environment"

→ [SETUP.md](guides/SETUP.md)

### "I need to understand a dashboard"

→ [USER_GUIDE.md](guides/USER_GUIDE.md)

### "I want to add a new feature"

→ [DEVELOPER_GUIDE.md](guides/DEVELOPER_GUIDE.md) + [ARCHITECTURE.md](architecture/ARCHITECTURE.md)

### "I need to understand the data pipeline"

→ [ARCHITECTURE.md](architecture/ARCHITECTURE.md)

### "I need column definitions"

→ [Data Dictionary](../data/dictionaries/data_dictionary.md)

### "I want to run a notebook"

→ [SETUP.md](guides/SETUP.md) + relevant notebook README

---

## 📝 Maintenance & Updates

### When to update documentation

- **SETUP.md**: When dependencies or installation process changes
- **USER_GUIDE.md**: When dashboards or filters change
- **DEVELOPER_GUIDE.md**: When code patterns or workflow changes
- **ARCHITECTURE.md**: When pipeline stages or feature engineering changes
- **Data Dictionary**: When schema or KPI definitions change (EVERY TIME)

### How to update

1. Edit the relevant `.md` file in this folder
2. Test all links and code snippets
3. Commit with message: `docs: update [filename]`
4. Verify links work from the root README

---

## 🔗 Navigation

**Going deeper?**

- [Data Processing Details](architecture/ARCHITECTURE.md#-data-pipeline-details)
- [Dashboard KPI Definitions](guides/USER_GUIDE.md#-kpi-summary-cards)
- [Feature Engineering Methods](guides/DEVELOPER_GUIDE.md#stage-4-feature-engineering)
- [Contributing Guidelines](guides/DEVELOPER_GUIDE.md#-contributing)

**Need help?**

- Check the [FAQ](guides/USER_GUIDE.md#-faq)
- Review [Common Issues](guides/DEVELOPER_GUIDE.md#-debugging)
- Open a GitHub issue

---

## 📞 Questions?

Reach out to the team or open a GitHub issue.

- **Setup help**: See [SETUP.md](guides/SETUP.md#troubleshooting)
- **Dashboard questions**: See [USER_GUIDE.md](guides/USER_GUIDE.md#-faq)
- **Code/development**: See [DEVELOPER_GUIDE.md](guides/DEVELOPER_GUIDE.md#-debugging)
- **Architecture/design**: See [ARCHITECTURE.md](architecture/ARCHITECTURE.md)
