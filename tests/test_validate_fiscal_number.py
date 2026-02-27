from Utilities import Utilities

def test_validate_fiscal_number_is_bool():
    result = Utilities.validate_fiscal_number("101000000")
    assert isinstance(result, bool)

def test_validate_fiscal_number_is_valid():
    result = Utilities.validate_fiscal_number("229007813")
    assert result

def test_validate_fiscal_number_is_invalid():
    result = Utilities.validate_fiscal_number("192837587")
    assert not result

def test_validate_fiscal_number_empty():
    result = Utilities.validate_fiscal_number("")
    assert not result