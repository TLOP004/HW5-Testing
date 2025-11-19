import pytest
from src.pricing import (
    parse_price,
    format_currency,
    apply_discount,
    add_tax,
    bulk_total,
)

#parse_price tests

@pytest.mark.parametrize(
    "text, expected",
    [
        ("$1,234.50", 1234.50),
        ("12.5", 12.5),
        ("   $0.99   ", 0.99),
    ],
)
def test_parse_price_valid(text, expected):
    assert parse_price(text) == pytest.approx(expected)


@pytest.mark.parametrize("text", ["", "abc"])
def test_parse_price_invalid(text):
    with pytest.raises(ValueError):
        parse_price(text)


#format_currency tests

@pytest.mark.parametrize(
    "value, expected",
    [
        (0, "$0.00"),
        (1, "$1.00"),
        (1.2, "$1.20"),
        (1.234, "$1.23"),   
        (1.235, "$1.24"),   
    ],
)
def test_format_currency_rounding(value, expected):
    assert format_currency(value) == expected


#apply_discount tests

def test_apply_discount_zero_percent():
    assert apply_discount(100.0, 0) == pytest.approx(100.0)


def test_apply_discount_large_percent():
    assert apply_discount(200.0, 50) == pytest.approx(100.0)


def test_apply_discount_negative_percent_raises():
    with pytest.raises(ValueError):
        apply_discount(100.0, -1)


#add_tax tests

def test_add_tax_default_rate():
    # default rate is 7%
    result = add_tax(100.0)
    assert result == pytest.approx(107.0)


def test_add_tax_custom_rate():
    result = add_tax(100.0, rate=0.10)  # 10%
    assert result == pytest.approx(110.0)


def test_add_tax_negative_rate_raises():
    with pytest.raises(ValueError):
        add_tax(100.0, rate=-0.05)


#bulk_total tests

def test_bulk_total_simple_list_no_discount_default_tax():
    prices = [10.0, 20.0]  # subtotal = 30
    # no discount, 7% tax -> 30 * 1.07 = 32.1
    total = bulk_total(prices)
    assert total == pytest.approx(32.1)


def test_bulk_total_with_discount_and_tax():
    prices = [50.0, 50.0]  # subtotal = 100
    # 10% discount -> 90
    # 10% tax -> 99
    total = bulk_total(prices, discount_percent=10, tax_rate=0.10)
    assert total == pytest.approx(99.0)
