# Processed Financial Transactions Data

This directory contains the cleaned and preprocessed financial transaction records prepared for visualization and analysis in Tableau.

## File Information

* **Filename:** `cleaned_financial_transactions.csv`
* **Source:** `dirty_financial_transactions.csv`
* **Cleaning Script:** `notebooks/Cleaned_financial_transactions.ipynb`

## Data Cleaning & Preprocessing Steps

The raw data underwent a series of cleaning and formatting steps to ensure analytical reliability. Below are all the operations performed:

### 1. Handling Duplicates
- Removed exact duplicate rows from the dataset to prevent skewed distributions.

### 2. General Text Cleaning
- Converted text columns specifically `Payment_Method` and `Transaction_Status` to lowercase.
- Stripped leading and trailing whitespaces.

### 3. Categorical Standardization
- **`Payment_Method`**: Standardized values to `paypal`, `creditcard`, and `cash`. Instances like "pay pal" and "credit card" were mapped properly.
- **`Transaction_Status`**: Unified instances of "complete" to standard "completed". 

### 4. Date and Time Processing
- **`Transaction_Date`**: Converted the text format into robust Python `datetime` objects.
- **Dropping Bad Dates**: Removed records where dates couldn't be parsed (converted to `NaT`).

### 5. Numerical Data Validation and Imputation
- **`Price`**:
  - Removed all non-numeric currency characters like `$` and `,`.
  - Parsed into float values.
  - Formatted negative price numbers into positive numbers using absolute values (assuming they were typos for refund magnitudes but should be strictly positive for this dataset).
  - Imputed missing values with the median.
- **`Quantity`**:
  - Converted negative quantities into their absolute values.
  - Imputed missing values with the median.

### 6. Managing Missing Critical Identifiers
- Dropped any records without a `Transaction_ID` or `Customer_ID`, as imputing unique identifiers could cause duplication or bad links downstream.

### 7. Managing Missing Transaction Statuses
- Populated missing rows for `Transaction_Status` with string `'unknown'`.

### 8. Feature Engineering
- Extracted multiple date parts from `Transaction_Date` into standalone columns to boost temporal analysis and plotting in Tableau:
  - `Transaction_Year`
  - `Transaction_Month`
  - `Transaction_Day`
  - `Transaction_DayOfWeek` (0 = Monday, 6 = Sunday)
  - `Transaction_Hour`

## Usage Configuration
The finalized CSV is standardized safely without non-numeric clutter, missing values, duplicates, and with properly assigned temporal variables, hence ready for data modeling and dashboarding in platforms like Tableau without requiring any further alterations.
