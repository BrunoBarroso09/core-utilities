from Utilities.validators import email
import pytest

class TestValidateEmail:
    """Test suite for validate_email() method"""

    def test_validate_email_is_bool(self):
        """Test that test_validate returns boolean value."""
        result = email.EmailUtilities.validate_email("example@gmail.com")
        assert isinstance(result, bool)

    def test_validate_email_valid(self):
        """Test that test_validate returns if email is valid."""
        result = email.EmailUtilities.validate_email("example@gmail.com")
        assert result is True

    def test_validate_email_invalid(self):
        """Test that test_validate returns if email is invalid."""
        result = email.EmailUtilities.validate_email("example@gm")
        assert result is False

    def test_validate_email_empty(self):
        """Test that test_validate returns if email is empty."""
        with pytest.raises(ValueError):
            email.EmailUtilities.validate_email("")

    def test_validate_email_subdomain(self):
        """Test that test_validate returns if the subdomain is valid."""
        result = email.EmailUtilities.validate_email("example@company.co.uk")
        assert result is True

    def test_invalid_type_int(self):
        """Test that test_validate returns error if integer is passed."""
        with pytest.raises(TypeError):
            email.EmailUtilities.validate_email(123456)

    def test_invalid_type_none(self):
        """Test that test_validate returns error if none is passed."""
        with pytest.raises(TypeError):
            email.EmailUtilities.validate_email(None)