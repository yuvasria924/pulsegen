from play_loader import load_daily_batches
from trend_builder import build_trend_table
import os

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    TARGET_DATE = "2025-12-26"

    batches = load_daily_batches()
    trend_df = build_trend_table(batches, TARGET_DATE)

    trend_df.to_csv("output/trend_report.csv", index=False)

    print("\n--- Trend Report Generated ---")
    print(trend_df.head())
    print("\nSaved to: /output/trend_report.csv")
