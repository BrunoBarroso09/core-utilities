# Core Utilities 🚀

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Tests](https://img.shields.io/badge/tests-69%2F69%20passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

This component provides essential static methods to simplify repetitive tasks like hide email, validate Portuguese fiscal number, validate Portuguese postal code and other.

## ✨ Functionalities

- **mask_email**: Sensitive data protection (GDPR friendly)
- **validate_email**: Strict formatting verification using Regex.
- **format_currency**: Conversion of numerical values ​​to the European monetary format.
- **get_env**: Securely read configurations via .env files.
- **validate_fiscal_number**: Validates the Portuguese taxpayer identification number according to Portuguese standards.
- **validate_postal_code**: Validates the format of the Portuguese postal code using regular expressions (Regex).
- **validate_iban**: Validates a Portuguese IBAN (format and MOD 97 check)
- **get_city_by_telephone**: Returns the city associated with the telephone prefix

## 🛠️ How to use

### 1. Project structure
Copy the `Utilities` folder to the root of your project:
```text
your_project/
├── Utilities/
│   ├── currency/
│   ├── env/
│   └── validators/
```

### 2. Usage examples
```python
from Utilities.validators import fiscal_number
from Utilities.validators import postal_code
from Utilities.validators import telephone

# Validate Portuguese fiscal number
print(fiscal_number.FiscalNumberUtilities.validate_fiscal_number("287148300"))    # return True

# Validate Portuguese postal code
print(postal_code.PostalCodeUtilities.validate_postal_code("1231-323"))   # return True

# Get city by telephone prefix
print(telephone.TelephonePrefixUtilities.get_city_by_telephone("217676778")) # return Lisboa
```

## 🧪 Running Tests

Install pytest:
```bash
pip install pytest
```

Run all tests:
```bash
pytest tests/
```

Expected output:
```
tests/test_env.py ........                                                                                                                                                                                                       [ 11%]
tests/test_format_currency.py ......                                                                                                                                                                                             [ 20%]
tests/test_get_city_by_telephone.py ...........                                                                                                                                                                                  [ 36%]
tests/test_mask_email.py .......                                                                                                                                                                                                 [ 46%]
tests/test_validate_email.py .......                                                                                                                                                                                             [ 56%]
tests/test_validate_fiscal_number.py ..........                                                                                                                                                                                  [ 71%]
tests/test_validate_iban.py ..........                                                                                                                                                                                           [ 85%]
tests/test_validate_postal_code.py ..........                                                                                                                                                                                    [100%]
========================================================================================================== 69 passed in 0.04s ==========================================================================================================
```

### Test coverage

| Test | Description |
|------|-------------|
| `test_env` | Read environment variable from .env file |
| `test_format_currency` | Transform a number into a readable currency format |
| `test_mask_email` | Transform email 'example@email.com' to 'e******@email.com' |
| `test_validate_email` | Validate if the email format is valid |
| `test_validate_fiscal_number` | Validate if the Portuguese fiscal number is valid |
| `test_validate_iban` | Validate if the Portuguese IBAN is valid |
| `test_validate_postal_code` | Validate if the Portuguese postal code is valid |
| `test_get_city_by_telephone` | Returns the city associated with the telephone prefix |

## 📁 Project Structure
```text
core-utilities/
├── Utilities/
│   ├── currency/
│   ├── env/
│   └── validators/
├── tests/
│   ├── __init__.py
│   ├── test_env.py
│   ├── test_format_currency.py
│   ├── test_mask_email.py
│   ├── test_validate_email.py
│   ├── test_validate_fiscal_number.py
│   ├── test_validate_iban.py
│   ├── test_validate_postal_code.py
│   └── test_get_city_by_telephone.py
├── README.md
└── LICENSE
```
