import pandas as pd
import os

folder_path = "data/raw"

files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

for file in files:
    print("=" * 50)
    print("File:", file)

    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\n")