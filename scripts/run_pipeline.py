"""
Master Execution Script
Bluestock Mutual Fund Capstone
"""

import os

scripts = [
    "data_ingestion.py",
    "load_to_sqlite.py",
    "compute_metrics.py",
    "recommender.py"
]

for script in scripts:
    print(f"\nRunning {script}...")
    os.system(f"python scripts/{script}")

print("\nPipeline Completed Successfully")