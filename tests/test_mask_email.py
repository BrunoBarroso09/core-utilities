from Utilities import Utilities
import pytest

def test_mask_email_is_string():
    result = Utilities.mask_email("example@gmail.com")
    assert isinstance(result, str)

def test_mask_email_valid():
    result = Utilities.mask_email("example@gmail.com")
    assert result == "e******@g****.com"

def test_mask_email_invalid():
    with pytest.raises(ValueError):
        Utilities.mask_email("example@gm")

def test_mask_email_empty():
    with pytest.raises(ValueError):
        Utilities.mask_email("")

def test_mask_email_subdomain():
    result = Utilities.mask_email("example@company.co.uk")
    assert result == "e******@c******.co.uk"