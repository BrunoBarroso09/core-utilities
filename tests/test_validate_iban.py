from Utilities import Utilities

def test_validate_iban_is_bool():
    result = Utilities.validate_iban("PT28003506514517918237350")
    assert isinstance(result, bool)

def test_validate_iban_is_valid():
    result = Utilities.validate_iban("PT28003506514517918237350")
    assert result

def test_validate_iban_is_invalid():
    result = Utilities.validate_iban("PT28000000514517918237350")
    assert not result

def test_validate_iban_is_empty():
    result = Utilities.validate_iban("")
    assert not result