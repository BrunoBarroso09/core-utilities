from Utilities.validators import email
import pytest

class TestMaskEmail:
    """Test suite for mask_email() method"""

    def test_mask_email_returns_string(self):
        """Test that mask_email returns a string."""
        result = email.EmailUtilities.mask_email("example@gmail.com")
        assert isinstance(result, str)

    def test_mask_email_valid(self):
        """Test valid email masking."""
        result = email.EmailUtilities.mask_email("example@gmail.com")
        assert result == "e******@g****.com"

    def test_mask_email_invalid_short_domain(self):
        """Test invalid email with short domain raises ValueError."""
        with pytest.raises(ValueError):
            email.EmailUtilities.mask_email("example@gm")

    def test_mask_email_empty_string(self):
        """Test empty string raises ValueError."""
        with pytest.raises(ValueError):
            email.EmailUtilities.mask_email("")

    def test_mask_email_with_subdomain(self):
        """Test email with subdomain masking."""
        result = email.EmailUtilities.mask_email("example@company.co.uk")
        assert result == "e******@c*********.uk"

    def test_mask_email_invalid_type_int(self):
        """Test integer input raises TypeError."""
        with pytest.raises(TypeError):
            email.EmailUtilities.mask_email(123456)

    def test_mask_email_invalid_type_none(self):
        """Test None input raises TypeError."""
        with pytest.raises(TypeError):
            email.EmailUtilities.mask_email()