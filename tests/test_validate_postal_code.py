from Utilities import Utilities

class TestValidatePostalCode:
    """Test suite for validate_postal_code() method"""

    def test_validate_postal_code_is_bool(self):
        """Test validate postal code returns boolean type."""
        result = Utilities.validate_postal_code("1211-100")
        assert isinstance(result, bool)

    def test_validate_postal_code_is_valid(self):
        """Test validate postal code returns valid."""
        result = Utilities.validate_postal_code("1231-323")
        assert result is True

    def test_validate_postal_code_is_invalid(self):
        """Test validate postal code returns invalid."""
        result = Utilities.validate_postal_code("1230323")
        assert result is False

    def test_validate_postal_code_empty(self):
        """Test validate postal code returns empty."""
        result = Utilities.validate_postal_code("")
        assert result is False

    def test_validate_postal_code_too_short(self):
        """Test validate postal code returns too short."""
        result = Utilities.validate_postal_code("1234")
        assert result is False

    def test_validate_postal_code_too_long(self):
        """Test validate postal code returns too long."""
        result = Utilities.validate_postal_code("12341-090")
        assert result is False

    def test_validate_postal_code_with_letters(self):
        """Test validate postal code with letters."""
        result = Utilities.validate_postal_code("2313-bah")
        assert result is False
        
        
    def test_validate_postal_code_with_spaces(self):
        """Test validate postal code with spaces."""
        result = Utilities.validate_postal_code("1314 -211")
        assert result is False

    def test_validate_postal_code_invalid_type_int(self):
        """Test validate postal code with invalid type."""
        result = Utilities.validate_postal_code(1222462)
        assert result is False

    def test_validate_postal_code_invalid_type_none(self):
        """Test validate postal code with none type."""
        result = Utilities.validate_postal_code(None)
        assert result is False