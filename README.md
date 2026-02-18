# Core Utilities 🚀

This componente give a lot of essencial static methods to simplify repetitive tasks like hide email, validate data, clear terminal and other.

## ✨ Functionalities

- **mask_email**: Sensitive data protection (GDPR friendly)
- **clear_terminal**: Cross-platform utility for console cleaning.
- **validate_email**: Strict formatting verification using Regex.
- **format_currency**: Conversion of numerical values ​​to the European monetary format.
- **get_env**: Securely read configurations via .env files.
- **validate_fiscal_number**: Validates the Portuguese taxpayer identification number according to Portuguese standards.
- **validate_postal_code**: Validates the format of the Portuguese postal code using regular expressions (Regex).


## ⚙️ Dependencies

This component need python-dotenv library, you need to install using this command

```bash
pip install python-dotenv
```

## 🛠️ How to use

### 1. Project structure
To use this component, simply copy the `CORE-UTILITIES` folder to the root of your project:

```text
your_project/
├── UTilities/
│   ├── __init__.py
│   └── utilities.py
