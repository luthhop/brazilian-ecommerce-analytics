from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"
DATABASE_DIR = PROJECT_ROOT / "data" / "database"


def main() -> None:
    input_path = PROCESSED_DATA_DIR / "orders_analytics.csv"
    output_path = DATABASE_DIR / "olist_analytics.sqlite"

    if not input_path.exists():
        raise FileNotFoundError(
            f"Processed dataset not found: {input_path}. "
            "Run notebooks/03_feature_engineering_and_dataset.ipynb first."
        )

    DATABASE_DIR.mkdir(parents=True, exist_ok=True)

    orders = pd.read_csv(input_path)

    with sqlite3.connect(output_path) as connection:
        orders.to_sql("orders_analytics", connection, if_exists="replace", index=False)

        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_orders_order_id "
            "ON orders_analytics(order_id)"
        )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_orders_status "
            "ON orders_analytics(order_status)"
        )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_orders_year_month "
            "ON orders_analytics(order_year_month)"
        )
        connection.execute(
            "CREATE INDEX IF NOT EXISTS idx_orders_customer_state "
            "ON orders_analytics(customer_state)"
        )

    print(f"SQLite database created at: {output_path}")
    print(f"Rows loaded: {len(orders):,}")
    print(f"Columns loaded: {len(orders.columns):,}")


if __name__ == "__main__":
    main()

