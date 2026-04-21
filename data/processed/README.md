# Processed WildChat Data

This directory contains the cleaned and flattened WildChat conversation records prepared for visualization and analysis in Tableau.

## File Information

* **Filename:** `cleaned_wildchat_data.csv`
* **Source:** `allenai/WildChat-4.8M` (Hugging Face Dataset)
* **Cleaning Script:** `notebooks/02_cleaning.ipynb`

## Data Cleaning & Preprocessing Steps

The raw data underwent a series of cleaning, flattening, and formatting steps to ensure analytical reliability. Below are all the operations performed:

### 1. Data Flattening
- The original dataset contained nested conversation logs. These were flattened so each row represents a distinct turn. 

### 2. General Text Cleaning
- **Unicode Normalization:** Normalized text data using NFKC to ensure consistent encodings.
- **Whitespace Removal:** Removed excessive line breaks and multiple spaces.

### 3. Data Validation & Quality Checks
- Validated that the text is at least 3 characters long.
- Ensured the text contains at least one alphanumeric character.

### 4. Filtering
- Excluded any records where the text was determined to be invalid based on the above quality checks.

### 5. Feature Engineering
- Added several new columns useful for analysis:
  - `text_length`: The character count of the cleaned text.
  - `word_count`: The word count of the cleaned text.
  - `turn_id`: The ID of the turn within the conversation.
  - `conversation_length`: The total number of turns in the conversation.
- Structured the original nested dataset into easy-to-use columns such as `conversation_id`, `role`, `language`, and `timestamp`.

## Usage Configuration
The finalized CSV is structured and safely formatted without excessive whitespace or invalid characters. Each row corresponds to a single conversation turn with all relevant metadata attached, making it perfectly tailored for data modeling and dashboarding in platforms like Tableau.
