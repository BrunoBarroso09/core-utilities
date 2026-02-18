import os
import re
from os import utime

from dotenv import load_dotenv

#load_env outside the class because here load one time only
load_dotenv()

class Utilities:

    @staticmethod #Privacy: Transform email 'example@email.com' to 'e******@email.com'
    def mask_email(email: str) -> str:
        if not email or '@' not in email:
            return 'Invalid email'
        email_split = email.split('@')
        user_email= email_split[0][0]
        domain = email_split[1]
        return f"{user_email}*****@{domain}"

    @staticmethod #Clear terminal (works in Windows, Mac and Linux)
    def clear_terminal() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod #Validate if the current email is valid
    def validate_email(email: str) -> bool:
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.search(regex, email))

    @staticmethod #Transform a number into a readable currency format.
    def format_currency(value: float, symbol: str = '€') -> str:
        return f"{value:,.2f} {symbol}".replace(",", "X").replace(".", ",").replace("X", ".")

    @staticmethod #Read systems variables or .env file
    def get_env(key: str, default: str = None) -> str:
        return os.getenv(key, default)

    @staticmethod # Private method to validate control digit
    def _validate_digit(digit: str) -> str:
        try:
            if not digit.isdigit():
                raise ValueError("All characters need to to be digit")
            if not len(digit) == 8:
                raise ValueError("Number of digits different from 8 digits")

            sum_digit = (
                    int(digit[0]) * 9
                    + int(digit[1]) * 8
                    + int(digit[2]) * 7
                    + int(digit[3]) * 6
                    + int(digit[4]) * 5
                    + int(digit[5]) * 4
                    + int(digit[6]) * 3
                    + int(digit[7]) * 2
            )
            rest = sum_digit % 11
            if rest < 2:
                return "0"
            return str(11 - rest)
        except ValueError:
            raise ValueError("All characters need to to be digit")

    @staticmethod #Validate if the current fiscal number is valid
    def validate_fiscal_number(fiscal_number: str) -> bool:
        try:
            if not int(fiscal_number.isdigit()) or len(fiscal_number) != 9:
                return False
            else:
                return fiscal_number[-1] == Utilities._validate_digit(fiscal_number[:8])
        except ValueError:
            raise ValueError("Invalid fiscal number")