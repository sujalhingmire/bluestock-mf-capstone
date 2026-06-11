# 📊 Mutual Fund Analytics Platform
### Bluestock Fintech Pvt. Ltd. — Data Analytics Capstone (June 2026)

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=flat&logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Star%20Schema-003B57?style=flat&logo=sqlite&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=flat&logo=powerbi&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

> An end-to-end financial data engineering and analytics platform covering the full lifecycle from raw data ingestion to quantitative risk modelling and interactive BI dashboards — built in 7 days for the Indian mutual fund ecosystem.

---

## 🔍 Project Summary

This capstone delivers a **production-grade Mutual Fund Analytics Platform** integrating:

- **Data Engineering** — ETL pipeline across 10 datasets, 5M+ records, SQLite star schema
- **Quantitative Analytics** — 14 financial metrics: CAGR, Sharpe, Sortino, Alpha, Beta, Max Drawdown, VaR, CVaR, Rolling Sharpe, HHI
- **Business Intelligence** — 4-page interactive Power BI dashboard with drill-through
- **Advanced Analytics** — Portfolio concentration analysis, investor cohort analysis, SIP continuity, rule-based fund recommender
- **Live Data Integration** — Real-time NAV fetch via [mfapi.in](https://www.mfapi.in) REST API

**Author:** Sujal Hingmire
**Organization:** Bluestock Fintech Pvt. Ltd.
**Duration:** 7 Days | June 2–11, 2026

---

## 📁 Repository Structure

```
bluestock_mf_capstone/
│
├── data/
│   ├── raw/                        # Original unprocessed datasets (10 CSVs)
│   ├── processed/                  # Cleaned, validated datasets
│   └── db/
│       └── bluestock_mf.db         # SQLite star-schema database
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb     # Day 1 — API integration & data loading
│   ├── 02_data_cleaning.ipynb      # Day 2 — ETL, cleaning, DB creation
│   ├── 03_eda_analysis.ipynb       # Day 3 — Exploratory analysis & visualization
│   ├── 04_performance_analytics.ipynb  # Day 4 — Quantitative metrics & scorecards
│   └── 05_advanced_analytics.ipynb # Day 6 — VaR, CVaR, HHI, Cohort, Recommender
│
├── scripts/
│   ├── etl_pipeline.py             # Full ETL orchestration
│   ├── live_nav_fetch.py           # mfapi.in real-time NAV fetcher
│   ├── compute_metrics.py          # Financial metric computation engine
│   ├── recommender.py              # Rule-based fund recommendation engine
│   └── run_pipeline.py             # End-to-end pipeline runner
│
├── sql/
│   ├── schema.sql                  # Star schema DDL
│   └── queries.sql                 # 10 analytical SQL queries
│
├── dashboard/
│   └── bluestock_mf_dashboard.pbix # Power BI 4-page interactive dashboard
│
├── reports/
│   ├── var_cvar_report.csv         # VaR & CVaR results for all funds
│   ├── hhi_report.csv              # Portfolio concentration (HHI) scores
│   ├── rolling_sharpe_chart.png    # 90-day rolling Sharpe visualization
│   ├── top5_funds.csv              # Top 5 composite scorecard results
│   └── data_dictionary.md          # Field-level data definitions
│
├── requirements.txt
└── README.md
```

---

## 📊 Datasets Used

| # | Dataset | Records | Description |
|---|---------|---------|-------------|
| 1 | `fund_master_clean.csv` | ~50 funds | Fund metadata: scheme name, category, expense ratio, benchmark |
| 2 | `nav_history_clean.csv` | ~95,000 | Daily NAV prices across all schemes (5-year window) |
| 3 | `scheme_performance_clean.csv` | ~50 funds | 1/3/5-yr returns, Sharpe, Sortino, Alpha, Beta, AUM |
| 4 | `portfolio_holdings_clean.csv` | ~500 rows | Sector and stock-level portfolio weights |
| 5 | `investor_transactions_clean.csv` | ~50,000 | Transaction log with investor demographics |
| 6 | `monthly_sip_inflows_clean.csv` | 36 months | Industry-level monthly SIP inflow amounts |
| 7 | `category_inflows_clean.csv` | ~15 categories | Net and gross inflows by fund category |
| 8 | `aum_by_fund_house_clean.csv` | ~40 houses | AUM distribution across AMCs |
| 9 | `benchmark_indices_clean.csv` | ~25,000 | NIFTY50, NIFTY100, Sensex daily close values |
| 10 | `industry_folio_count_clean.csv` | 36 months | Total industry folio (investor account) counts |

---

## 🧮 Analytics & Metrics Implemented

### Performance Metrics (Day 4 — `compute_metrics.py`)

```python
# Risk-free rate: 6.5% p.a. (Indian 10-yr G-Sec proxy)
RISK_FREE_RATE = 0.065

# Metrics computed per fund:
# ✅ Daily Returns            → nav.pct_change()
# ✅ CAGR (1Y, 3Y, 5Y)       → (end/start)^(1/n) - 1
# ✅ Sharpe Ratio             → (μ - Rf) / σ * √252
# ✅ Sortino Ratio            → (μ - Rf) / σ_downside * √252
# ✅ Alpha & Beta             → OLS regression vs. NIFTY100 (SciPy linregress)
# ✅ Maximum Drawdown         → min(NAV / cummax(NAV) - 1)
```

### Risk Analytics (Day 6 — `05_advanced_analytics.ipynb`)

```python
# ✅ VaR (95%)                → np.percentile(returns, 5)
# ✅ CVaR (95%)               → returns[returns < VaR].mean()
# ✅ Rolling 90-Day Sharpe    → rolling(90).apply(sharpe_fn)
# ✅ HHI Concentration        → Σ(weight_i²) across holdings
```

### Fund Scorecard — Top 5 Results

| Rank | Fund | Score | CAGR 3Y | Sharpe | Alpha | Max DD |
|------|------|-------|---------|--------|-------|--------|
| 🥇 | ICICI Pru Midcap Fund — Regular | **100.0** | 31.78% | 1.18 | 0.293 | −18.19% |
| 🥈 | Mirae Asset Large Cap Fund — Regular | 97.72 | 34.00% | 1.45 | 0.270 | −11.27% |
| 🥉 | Mirae Asset Tax Saver Fund — Regular | 96.20 | 29.18% | 1.23 | 0.283 | −16.40% |
| 4 | Axis Midcap Fund — Regular | 95.44 | 35.11% | 1.00 | 0.261 | −20.96% |
| 5 | HDFC Mid-Cap Opportunities — Regular | 95.06 | 32.44% | 1.09 | 0.272 | −16.22% |

---

## 🗄️ Database Schema (Star Schema)

```sql
-- Dimension Tables
dim_fund    (fund_id PK, scheme_name, category, fund_house)
dim_date    (date_id PK, full_date, year, month, quarter)

-- Fact Tables
fact_nav           (nav_id PK, fund_id FK, date_id FK, nav)
fact_transactions  (transaction_id PK, fund_id FK, date_id FK, type, amount)
fact_performance   (performance_id PK, fund_id FK, return_1y, return_3y, return_5y, expense_ratio)
fact_aum           (aum_id PK, fund_id FK, date_id FK, aum)
```

---

## ⚡ Quick Start

### Prerequisites
```bash
Python 3.9+  |  pip  |  Jupyter Notebook  |  Power BI Desktop (for dashboard)
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/sujal-hingmire/bluestock-mf-capstone.git
cd bluestock-mf-capstone

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the full ETL pipeline
python scripts/run_pipeline.py

# 4. Launch notebooks sequentially
jupyter notebook notebooks/
```

### Run Individual Components

```bash
# Fetch live NAV for a specific fund (HDFC Top 100 → AMFI: 100016)
python scripts/live_nav_fetch.py

# Compute all performance metrics and generate scorecard
python scripts/compute_metrics.py

# Get fund recommendations by risk appetite
python scripts/recommender.py
# → Prompts: Enter risk appetite [Low / Moderate / High]
```

---

## 📈 Power BI Dashboard

Open `dashboard/bluestock_mf_dashboard.pbix` in Power BI Desktop.

| Page | Description |
|------|-------------|
| **Industry Overview** | AUM trends, folio growth, SIP inflows, category net flows |
| **Fund Performance** | Scorecard matrix, CAGR comparison, benchmark overlay |
| **Investor Analytics** | Demographics, geographic distribution, investment patterns |
| **SIP & Market Trends** | Monthly SIP trends, NAV time series, rolling performance |

---

## 🔬 Key Insights

1. **Mid-cap funds dominate the risk-adjusted return leaderboard** — 4 of 5 top-ranked funds are mid-cap or large-cap blends with Sharpe Ratios above 1.0.
2. **Two funds flagged for concentration risk** — Axis Bluechip (HHI: 2,064) and ABSL Small Cap (HHI: 2,007) exceed moderate concentration thresholds.
3. **Geographic concentration risk** — Top 5 states account for >70% of AUM; Tier 2/3 cities show high folio growth but low average ticket size.
4. **SIP continuity is counter-cyclical** — Investors starting SIPs during market downturns show significantly higher 12-month retention rates.

---

## 🏗️ Technology Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.11 |
| Data Processing | Pandas, NumPy |
| Statistical Analysis | SciPy (linregress, percentile) |
| Database | SQLite + SQLAlchemy ORM |
| Notebooks | Jupyter Notebook |
| Visualization | Plotly, Matplotlib, Seaborn |
| Business Intelligence | Microsoft Power BI Desktop |
| API Integration | mfapi.in (REST) |
| Version Control | Git + GitHub |

---

## 📋 Requirements

See [`requirements.txt`](requirements.txt) for the full dependency list. Key packages:

```
pandas>=2.0.0
numpy>=1.24.0
scipy>=1.10.0
sqlalchemy>=2.0.0
plotly>=5.14.0
matplotlib>=3.7.0
seaborn>=0.12.0
requests>=2.28.0
jupyter>=1.0.0
```

---

## 📄 License

This project is submitted as a capstone deliverable for Bluestock Fintech Pvt. Ltd. and is intended for educational and portfolio demonstration purposes.

---

## 👤 Author

**Sujal Hingmire**
Data Analytics Intern | Bluestock Fintech Pvt. Ltd.
📧 [sujalhingmire@gmail.com]
🔗 [www.linkedin.com/in/sujal-hingmire-0476052b8]
💻 [[github.com/sujal-hingmire](https://github.com/sujalhingmire)]

---

*Built with ❤️ during a 7-day capstone at Bluestock Fintech Pvt. Ltd. | June 2026*
