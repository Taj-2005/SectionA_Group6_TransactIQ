# Data dictionary (template)

Update this file after finalizing your dataset. The goal is to make the data understandable to **non-technical stakeholders** and ensure consistent KPI computation.

## Dataset metadata

- **Source**: [Kaggle — Dirty Financial Transactions Dataset](https://www.kaggle.com/datasets/alfarisbachmid/dirty-financial-transactions-dataset)
- **Raw file (repo)**: `data/raw/dirty_financial_transactions.csv`
- **Refresh**: one-time download (as of project start)
- **Grain (row-level meaning)**: (e.g., one row = one transaction, one customer-month, one ticket)
- **Primary keys**: (e.g., `customer_id`, `order_id`)
- **Time window**: (start date → end date)

---

## Column definitions (starter example)

Replace with your actual schema.

| Column             | Type        | Example      | Business meaning              | Notes / validation                     |
| ------------------ | ----------- | ------------ | ----------------------------- | -------------------------------------- |
| `customer_id`      | string      | `C_10293`    | Unique customer identifier    | Must be non-null                       |
| `transaction_id`   | string      | `T_883712`   | Unique transaction identifier | Used for de-duplication                |
| `transaction_date` | datetime    | `2025-03-18` | When the transaction occurred | Normalize timezone/date formats        |
| `segment`          | category    | `SMB`        | Customer segment              | Standardize casing/spelling            |
| `region`           | category    | `South`      | Geography/market region       | Map inconsistent values                |
| `product_category` | category    | `Add-on`     | Product grouping              | Optional if dataset lacks product data |
| `revenue`          | float       | `129.99`     | Gross revenue amount          | Currency normalization                 |
| `refund_amount`    | float       | `0.00`       | Refund/chargeback amount      | Set missing to 0 if appropriate        |
| `is_active`        | boolean/int | `1`          | Whether customer is active    | Define consistent logic                |
| `tenure_days`      | int         | `210`        | Days since first seen / signup| Feature engineered                     |

---

## KPI mapping (example)

Define the exact columns used in each KPI.

- **Net Revenue** = `revenue - refund_amount`
- **Retention Rate** = based on active customers in consecutive periods (`is_active`)
- **ARPU** = `net_revenue / active_customers`
