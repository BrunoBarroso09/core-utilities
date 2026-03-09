from Utilities.validators import fiscal_number

class TestValidateFiscalNumber:
    """Test suite for validate_fiscal_number() method"""

    def test_validate_fiscal_number_is_bool(self):
        """Test validate fiscal number returns boolean type."""
        result = fiscal_number.FiscalNumberUtilities.validate_fiscal_number("101000000")
        assert isinstance(result, bool)

    def test_validate_fiscal_number_is_valid(self):
        """Test validate fiscal number returns is valid."""
        result = fiscal_number.FiscalNumberUtilities.validate_fiscal_number("229007813")
        assert result is True

    def test_validate_fiscal_number_is_invalid(self):
        """Test validate fiscal number returns invalid type."""
        result = fiscal_number.FiscalNumberUtilities.validate_fiscal_number("192837587")
        assert result is False

    def test_validate_fiscal_number_empty(self):
        """Test validate fiscal number returns empty."""
        result = fiscal_number.FiscalNumberUtilities.validate_fiscal_number("")
        assert result is False

    def test_validate_fiscal_number_too_short(self):
        """Test validate fiscal number returns too short."""
        result = fiscal_number.FiscalNumberUtilities.validate_fiscal_number("12345")
        assert result is False

    def test_validate_fiscal_number_too_long(self):
        """Test validate fiscal number returns too long."""
        result = fiscal_number.FiscalNumberUtilities.validate_fiscal_number("1234567890")
        assert result is False

    def test_validate_fiscal_number_with_letters(self):
        """Test validate fiscal number with letters."""
        result = fiscal_number.FiscalNumberUtilities.validate_fiscal_number("ABC123456")
        assert result is False

    def test_validate_fiscal_number_with_spaces(self):
        """Test validate fiscal number with spaces."""
        result = fiscal_number.FiscalNumberUtilities.validate_fiscal_number("229 007 813")
        assert result is False

    def test_validate_fiscal_number_invalid_type_int(self):
        """Test validate fiscal number with invalid type."""
        result = fiscal_number.FiscalNumberUtilities.validate_fiscal_number(123456789)
        assert result is False

    def test_validate_fiscal_number_invalid_type_none(self):
        """Test validate fiscal number with none type."""
        result = fiscal_number.FiscalNumberUtilities.validate_fiscal_number(None)
        assert result is False