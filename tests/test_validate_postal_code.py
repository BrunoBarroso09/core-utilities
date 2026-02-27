from Utilities import Utilities

def test_validate_postal_code_is_bool():
    result = Utilities.validate_postal_code("1231323")
    assert isinstance(result, bool)

def test_validate_postal_code_is_valid():
    result = Utilities.validate_postal_code("1231-323")
    assert result

def test_validate_postal_code_is_invalid():
    result = Utilities.validate_postal_code("12")
    assert not result

def test_validate_postal_code_is_empty():
    result = Utilities.validate_postal_code("")
    assert not result