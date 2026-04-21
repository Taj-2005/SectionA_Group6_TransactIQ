# `data/`

Place data assets by lifecycle stage (raw → interim → processed → features → outputs).

- `raw/`: immutable source extracts (do not edit in-place)
- `interim/`: temporary, re-creatable working datasets
- `processed/`: cleaned, validated, analysis-ready tables
- `features/`: feature tables / embeddings (typically not committed)
- `outputs/`: dashboard- and report-ready exports
- `external/`: reference datasets (geo, language codes, taxonomies)

