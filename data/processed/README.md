# Processed Financial Transactions Data

This directory contains the cleaned and preprocessed financial transaction records prepared for visualization and analysis in Tableau.

## File Information

* **Filename:** `cleaned_financial_transactions.csv`
* **Source:** `dirty_financial_transactions.csv`
* **Cleaning Script:** `notebooks/02_cleaning.ipynb`

## Data Cleaning & Preprocessing Steps

The raw data underwent a series of cleaning and formatting steps to ensure analytical reliability. Below are all the operations performed:

### 1. Handling Duplicates
- Removed exact duplicate rows from the dataset to prevent skewed distributions.

### 2. General Text Cleaning
- Converted text columns specifically `Payment_Method` and `Transaction_Status` to lowercase.
- Stripped leading and trailing whitespaces.

### 3. Product Name Standardization
- **`Product_Name`** was standardized into these 6 canonical categories:
  - `Tablet`
  - `Coffee Machine`
  - `Laptop`
  - `Smartphone`
  - `Headphones`
  - `Coffee`
- Fixed common truncations/typos such as:
  - `Tab`, `T`, `Ta`, `Tabl`, `Table` → `Tablet`
  - `Cof`, `Coff`, `Coffe`, `C`, `Co` → `Coffee`
  - `Coffee M`, `Coffee Ma`, `Coffee Mach*`, `Coffee Mac*` → `Coffee Machine`
  - Similar short forms for Laptop/Smartphone/Headphones were mapped back to their full names.

### 4. Categorical Standardization
- **`Payment_Method`**: Standardized values to `paypal`, `creditcard`, and `cash`. Instances like "pay pal" and "credit card" were mapped properly.
- **`Transaction_Status`**: Unified instances of "complete" to standard "completed". 

### 5. Date and Time Processing
- **`Transaction_Date`**: Converted the text format into robust Python `datetime` objects.
- **Dropping Bad Dates**: Removed records where dates couldn't be parsed (converted to `NaT`).

### 6. Numerical Data Validation and Imputation
- **`Price`**:
  - Removed all non-numeric currency characters like `$` and `,`.
  - Parsed into float values.
  - Formatted negative price numbers into positive numbers using absolute values (assuming they were typos for refund magnitudes but should be strictly positive for this dataset).
  - Imputed missing values with the median.
- **`Quantity`**:
  - Converted negative quantities into their absolute values.
  - Imputed missing values with the median.

### 7. Managing Missing Critical Identifiers
- Dropped any records without a `Transaction_ID` or `Customer_ID`, as imputing unique identifiers could cause duplication or bad links downstream.

### 8. Managing Missing Transaction Statuses
- Populated missing rows for `Transaction_Status` with string `'unknown'`.

### 9. Feature Engineering
- Extracted multiple date parts from `Transaction_Date` into standalone columns to boost temporal analysis and plotting in Tableau:
  - `Transaction_Year`
  - `Transaction_Month`
  - `Transaction_Day`
  - `Transaction_DayOfWeek` (0 = Monday, 6 = Sunday)
  - `Transaction_Hour`

## Usage Configuration
The finalized CSV is standardized safely without non-numeric clutter, missing values, duplicates, and with properly assigned temporal variables, hence ready for data modeling and dashboarding in platforms like Tableau without requiring any further alterations.
