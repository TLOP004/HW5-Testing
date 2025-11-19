from src.pricing import apply_discount

def test_apply_discount_regression():
    """
    Regression test for the bug in apply_discount.

    Expected behavior:
    - apply_discount(100.0, 10) should return 90.0 (10% off).
    """
    result = apply_discount(100.0, 10)
    # Correct discounted price is 90.0
    assert result == 90.0
