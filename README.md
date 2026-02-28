# Core Utilities 🚀

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
│   ├── __init__.py
│   └── utilities.py
```

### 2. Usage examples
```python
from Utilities import Utilities

# Validate Portuguese fiscal number
print(Utilities.validate_fiscal_number("287148300"))    # return True

# Validate Portuguese postal code
print(Utilities.validate_postal_code("1231-323"))   # return True

# Get city by telephone prefix
print(Utilities.get_city_by_telephone("217676778")) # return Lisboa
```

## 🧪 Running Tests

Install dependencies:
```bash
pip install -r requirements.txt
```

Run all tests:
```bash
pytest tests/
```

Expected output:
```
tests/test_env.py .....                                                                                                                                                                                                          [ 13%]
tests/test_format_currency.py ....                                                                                                                                                                                               [ 25%]
tests/test_get_city_by_telephone.py ......                                                                                                                                                                                       [ 41%]
tests/test_mask_email.py .....                                                                                                                                                                                                   [ 55%]
tests/test_validate_email.py ....                                                                                                                                                                                                [ 66%]
tests/test_validate_fiscal_number.py ....                                                                                                                                                                                        [ 77%]
tests/test_validate_iban.py ....                                                                                                                                                                                                 [ 88%]
tests/test_validate_postal_code.py ....                                                                                                                                                                                          [100%]

========================================================================================================== 36 passed in 0.06s ==========================================================================================================
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
│   ├── __init__.py
│   └── utilities.py
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