import pandas as pd

performance = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

choice = input(
    "Risk Appetite (Low/Moderate/High): "
).strip().lower()

if choice == "low":

    result = (
        performance[
            performance["risk_grade"].str.contains(
                "Low",
                case=False,
                na=False
            )
        ]
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

elif choice == "moderate":

    result = (
        performance[
            performance["risk_grade"].str.contains(
                "Moderate",
                case=False,
                na=False
            )
        ]
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

elif choice == "high":

    result = (
        performance[
            performance["risk_grade"].str.contains(
                "High",
                case=False,
                na=False
            )
        ]
        .sort_values(
            "return_5yr_pct",
            ascending=False
        )
        .head(3)
    )

else:
    print("Please enter Low, Moderate, or High")
    exit()

print("\nTop Recommended Funds:\n")

print(
    result[
        [
            "scheme_name",
            "fund_house",
            "risk_grade",
            "sharpe_ratio",
            "return_5yr_pct"
        ]
    ]
)