# 04 - Feature Engineering & Statistical Validation

This directory contains the statistical modeling and feature preparation phase. We transition from descriptive EDA to predictive insights, focusing on user retention, model performance disparities, and interaction quality.

## Contents

- **[04_features.ipynb](04_features.ipynb)**: A notebook performing rigorous statistical testing and predictive modeling:
    1.  **Statistical Validations**:
        - **Independent T-Tests**: Comparing response quality between models. Result: `gpt-4` (avg quality 9.44) significantly outperforms `gpt-3.5-turbo` (avg quality 7.17) with a p-value of 0.0.
        - **One-Way ANOVA**: Assessing how turn count varies across models. Result: Highly significant difference (F-statistic: 2567.97, p-value: 0.0).
        - **Independence Testing**: Chi-Square tests to validate if toxicity rates are independent of prompt categories.
    2.  **Operational Drivers**:
        - Correlation analysis between user sentiment and session depth.
        - Box-plot distributions identifying quality variance across languages.
    3.  **Predictive Modeling (User Drop-Off)**:
        - **Logistic Regression**: Developed a model to predict the probability of a user "dropping off" (ending a session prematurely).
        - **Key Coefficients**: Session duration emerged as the strongest predictor (coefficient: -42.26), suggesting that extremely short sessions are the primary indicator of churn/dissatisfaction.

## Key Methodology

- **Hypothesis Testing**: Moving beyond averages to confirm that observed differences in model performance and user behavior are statistically significant and not due to chance.
- **Model Comparison**: Quantifying the "quality premium" of GPT-4 over GPT-3.5 to justify higher token costs.
- **Predictive Drivers**: Identifying actionable features (like session duration and sentiment) that can be used to trigger proactive engagement or quality interventions.

## Requirements

The feature engineering process utilizes `scipy.stats` and `scikit-learn` on data from:
- `data/processed/conversations_clean.csv`
- `data/processed/prompt_categories.csv`
