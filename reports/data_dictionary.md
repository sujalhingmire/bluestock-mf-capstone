# Data Dictionary

## fund_master

| Column | Type | Description |
|----------|---------|------------|
| amfi_code | INTEGER | Unique AMFI scheme code |
| scheme_name | TEXT | Mutual fund scheme name |
| category | TEXT | Fund category |
| fund_house | TEXT | AMC name |

## nav_history

| Column | Type | Description |
|----------|---------|------------|
| amfi_code | INTEGER | Scheme code |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

## investor_transactions

| Column | Type | Description |
|----------|---------|------------|
| transaction_id | INTEGER | Unique transaction |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount | REAL | Transaction amount |
| transaction_date | DATE | Transaction date |

...
