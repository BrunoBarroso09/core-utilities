from Utilities import Utilities
import pytest

class TestFormatCurrency:
    """Test suite for format_currency() method"""

    def test_format_currency_is_string(self):
        """Test that format_currency returns a string."""
        result = Utilities.format_currency(111)
        assert isinstance(result, str)

    def test_format_currency_basic(self):
        """Test that format_currency returns basic formatted string."""
        result = Utilities.format_currency(1234.56)
        assert result == "1.234,56 €"

    def test_format_currency_small(self):
        """Test that format_currency returns small formatted string."""
        result = Utilities.format_currency(111)
        assert result == "111,00 €"

    def test_format_currency_large(self):
        """Test that format_currency returns large formatted string."""
        result = Utilities.format_currency(1000000)
        assert result == "1.000.000,00 €"

    def test_format_currency_negative(self):
        """Test that format_currency returns negative formatted string."""
        result = Utilities.format_currency(-1234.56)
        assert result == "-1.234,56 €"

    def test_format_currency_invalid_type(self):
        """Test that format_currency returns invalid type."""
        with pytest.raises(ValueError):
            Utilities.format_currency("not a number")