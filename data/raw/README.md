# Raw Data Folder

This folder stores raw source extracts for the WildChat Analytics project.

## Source Dataset

- Source: WildChat-1M (AllenAI, Hugging Face)
- URL: https://huggingface.co/datasets/allenai/WildChat-1M
- Dataset variant: WildChat-1M

## Raw Data Format

- Expected raw formats: parquet and/or JSON from Hugging Face streaming extraction.
- Row grain: one row represents one conversation containing a list of message turns.
- Primary key: conversation_id

## Handling Rules

- Store raw files here as downloaded or extracted from the source.
- Do not clean or transform files in this folder.
- Perform all cleaning, feature engineering, and KPI dataset creation in data/processed.

## Current Repository State

- This folder currently includes a placeholder file (.gitkeep) so the directory is tracked in version control.
