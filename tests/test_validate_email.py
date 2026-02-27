from Utilities import Utilities

def test_validate_email_is_bool():
    result = Utilities.validate_email("example.com")
    assert isinstance(result, bool)

def test_validate_email_is_valid():
    result = Utilities.validate_email("example@company.co.uk")
    assert result

def test_validate_email_is_invalid():
    result = Utilities.validate_email("example@comp")
    assert not result

def test_validate_email_is_empty():
    result = Utilities.validate_email("")
    assert not result