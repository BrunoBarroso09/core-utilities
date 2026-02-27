from Utilities import Utilities
import pytest

def test_format_currency_is_string():
    result = Utilities.format_currency(111.00, "USD")
    assert isinstance(result, str)

def test_format_currency_is_valid():
    result = Utilities.format_currency(11091.01, "€")
    assert result == "11.091,01 €"

def test_format_currency_is_invalid():
    result = Utilities.format_currency(11091.01, "€")
    assert not result == "1.091,01 €"

def test_format_currency_empty():
    with pytest.raises(ValueError):
        Utilities.format_currency("abc")