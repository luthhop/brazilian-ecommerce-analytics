from __future__ import annotations

import csv
from pathlib import Path


RAW_DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"


def inspect_csv(path: Path) -> dict[str, object]:
    with path.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = sum(1 for _ in reader)

    return {
        "file": path.name,
        "rows": rows,
        "columns": len(header),
        "column_names": header,
    }


def main() -> None:
    csv_files = sorted(RAW_DATA_DIR.glob("*.csv"))

    if not csv_files:
        print(f"No CSV files found in {RAW_DATA_DIR}")
        return

    for csv_file in csv_files:
        info = inspect_csv(csv_file)
        print(f"{info['file']}: {info['rows']} rows, {info['columns']} columns")
        print("  " + ", ".join(info["column_names"]))


if __name__ == "__main__":
    main()

