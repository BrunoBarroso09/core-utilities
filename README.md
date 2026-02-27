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
tests/test_env.py .....                                                                                                                                                                                                          [ 16%]
tests/test_format_currency.py ....                                                                                                                                                                                              [ 30%]
tests/test_mask_email.py .....                                                                                                                                                                                                   [ 46%]
tests/test_validate_email.py ....                                                                                                                                                                                                [ 60%]
tests/test_validate_fiscal_number.py ....                                                                                                                                                                                        [ 73%]
tests/test_validate_iban.py ....                                                                                                                                                                                                 [ 86%]
tests/test_validate_postal_code.py ....                                                                                                                                                                                          [100%]

========================================================================================================== 30 passed in 0.03s ==========================================================================================================
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
│   └── test_validate_postal_code.py
├── README.md
└── LICENSE
```