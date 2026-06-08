import pandas as pd
import numpy as np
from scipy.stats import linregress

# Load data
nav = pd.read_csv("data/processed/nav_history_clean.csv")
benchmark = pd.read_csv("data/processed/benchmark_indices_clean.csv")

# Convert dates
nav["date"] = pd.to_datetime(nav["date"])
benchmark["date"] = pd.to_datetime(benchmark["date"])

# Sort NAV data
nav = nav.sort_values(
    ["amfi_code", "date"]
)

# --------------------------
# DAILY RETURNS
# --------------------------

nav["daily_return"] = (
    nav.groupby("amfi_code")["nav"]
       .pct_change()
)

# --------------------------
# CAGR
# --------------------------

def calculate_cagr(df, years):

    latest_date = df["date"].max()

    start_date = latest_date - pd.DateOffset(years=years)

    temp = df[df["date"] >= start_date]

    if len(temp) < 2:
        return np.nan

    start_nav = temp.iloc[0]["nav"]
    end_nav = temp.iloc[-1]["nav"]

    return (
        (end_nav / start_nav)
        ** (1 / years)
        - 1
    )

cagr_data = []

for fund in nav["amfi_code"].unique():

    df = nav[
        nav["amfi_code"] == fund
    ]

    cagr_data.append([
        fund,
        calculate_cagr(df, 1),
        calculate_cagr(df, 3),
        calculate_cagr(df, 5)
    ])

cagr_table = pd.DataFrame(
    cagr_data,
    columns=[
        "amfi_code",
        "cagr_1y",
        "cagr_3y",
        "cagr_5y"
    ]
)

# --------------------------
# SHARPE
# --------------------------

risk_free = 0.065

sharpe_results = []

for fund in nav["amfi_code"].unique():

    returns = nav[
        nav["amfi_code"] == fund
    ]["daily_return"].dropna()

    if len(returns) > 0:

        sharpe = (
            (
                returns.mean()
                -
                risk_free / 252
            )
            /
            returns.std()
        ) * np.sqrt(252)

        sharpe_results.append(
            [fund, sharpe]
        )

sharpe_df = pd.DataFrame(
    sharpe_results,
    columns=[
        "amfi_code",
        "sharpe_ratio"
    ]
)

# --------------------------
# SORTINO
# --------------------------

sortino_results = []

for fund in nav["amfi_code"].unique():

    returns = nav[
        nav["amfi_code"] == fund
    ]["daily_return"].dropna()

    downside = returns[
        returns < 0
    ]

    if len(downside) > 1:

        sortino = (
            (
                returns.mean()
                -
                risk_free / 252
            )
            /
            downside.std()
        ) * np.sqrt(252)

        sortino_results.append(
            [fund, sortino]
        )

sortino_df = pd.DataFrame(
    sortino_results,
    columns=[
        "amfi_code",
        "sortino_ratio"
    ]
)

# --------------------------
# ALPHA BETA
# --------------------------

benchmark_nifty = benchmark[
    benchmark["index_name"] == "NIFTY100"
].copy()

benchmark_nifty["benchmark_return"] = (
    benchmark_nifty["close_value"]
    .pct_change()
)

alpha_beta = []

for fund in nav["amfi_code"].unique():

    fund_df = nav[
        nav["amfi_code"] == fund
    ][["date", "daily_return"]]

    merged = pd.merge(
        fund_df,
        benchmark_nifty[
            ["date", "benchmark_return"]
        ],
        on="date"
    ).dropna()

    if len(merged) > 50:

        slope, intercept, r, p, se = linregress(
            merged["benchmark_return"],
            merged["daily_return"]
        )

        alpha_beta.append([
            fund,
            intercept * 252,
            slope
        ])

alpha_beta_df = pd.DataFrame(
    alpha_beta,
    columns=[
        "amfi_code",
        "alpha",
        "beta"
    ]
)

# --------------------------
# MAX DRAWDOWN
# --------------------------

drawdowns = []

for fund in nav["amfi_code"].unique():

    temp = nav[
        nav["amfi_code"] == fund
    ].copy()

    temp["running_max"] = (
        temp["nav"].cummax()
    )

    temp["drawdown"] = (
        temp["nav"]
        /
        temp["running_max"]
        -
        1
    )

    drawdowns.append([
        fund,
        temp["drawdown"].min()
    ])

drawdown_df = pd.DataFrame(
    drawdowns,
    columns=[
        "amfi_code",
        "max_drawdown"
    ]
)

# --------------------------
# SCORECARD
# --------------------------

scorecard = (
    cagr_table
    .merge(sharpe_df, on="amfi_code")
    .merge(alpha_beta_df, on="amfi_code")
    .merge(drawdown_df, on="amfi_code")
)

scorecard.to_csv(
    "../reports/fund_scorecard.csv",
    index=False
)

print("Metrics computed successfully!")