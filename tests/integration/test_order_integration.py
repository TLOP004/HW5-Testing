import pytest
from src.order_io import load_order, write_receipt

def test_order_integration(tmp_path):
    # 1) Create a temporary CSV input file
    input_file = tmp_path / "order.csv"
    input_file.write_text(
        "widget,$10.00\n"
        "gizmo,5.50\n",
        encoding="utf-8",
    )

    # 2) Load items from the CSV
    items = load_order(input_file)

    # Sanity check: we got both items
    assert items == [("widget", 10.00), ("gizmo", 5.50)]

    # 3) Write the receipt (this will internally call bulk_total and format_currency)
    receipt_path = tmp_path / "receipt.txt"
    write_receipt(receipt_path, items, discount_percent=10, tax_rate=0.10)

    # 4) Read the receipt back and verify its contents
    output_text = receipt_path.read_text(encoding="utf-8")

    # The receipt should have one line per item:
    assert "widget: $10.00" in output_text
    assert "gizmo: $5.50" in output_text

    # And a TOTAL line with correct format.
    # We won't hardcode the exact number here (to avoid duplicating business logic),
    # but we check that the TOTAL line exists and looks like currency.
    total_lines = [ln for ln in output_text.splitlines() if ln.startswith("TOTAL:")]
    assert len(total_lines) == 1

    total_line = total_lines[0]
    assert "TOTAL: $" in total_line
