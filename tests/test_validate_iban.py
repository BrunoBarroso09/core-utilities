from Utilities import Utilities

class TestValidateIBAN:
    """Test suite for validate_iban() method"""

    def test_validate_iban_is_bool(self):
        """Test validate iban return boolean type."""
        result = Utilities.validate_iban("PT28003506514517918237350")
        assert isinstance(result, bool)

    def test_validate_iban_is_valid(self):
        """Test validate_iban returns True for valid IBAN."""
        result = Utilities.validate_iban("PT28003506514517918237350")
        assert result is True

    def test_validate_iban_is_invalid(self):
        """Test validate iban return is invalid."""
        result = Utilities.validate_iban("PT28000000514517918237350")
        assert result is False

    def test_validate_iban_is_empty(self):
        """Test validate iban return is empty."""
        result = Utilities.validate_iban("")
        assert result is False

    def test_validate_iban_too_short(self):
        """Test validate iban return is too short."""
        result = Utilities.validate_iban("PT28003506")
        assert result is False

    def test_validate_iban_too_long(self):
        """Test validate iban return is too long."""
        result = Utilities.validate_iban("PT28000000514517918237350324124234")
        assert result is False

    def test_validate_iban_with_space(self):
        """Test validate iban return is with space."""
        result = Utilities.validate_iban("PT280000005 14517918237350")
        assert result is False

    def test_validate_iban_with_spaces_formatted(self):
        """Test validate_iban handles spaces in standard format."""
        result = Utilities.validate_iban("PT28 0035 0651 4517 9182 3735 0")
        assert result is True

    def test_validate_iban_invalid_type_int(self):
        """Test validate_iban returns False for integer type."""
        result = Utilities.validate_iban(28003506514517918237350)
        assert result is False

    def test_validate_iban_invalid_type_none(self):
        """Test validate iban return is invalid type."""
        result = Utilities.validate_iban(None)
        assert result is False