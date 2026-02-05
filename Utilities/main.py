import os
import re
from dotenv import load_dotenv

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

    @staticmethod
    def validate_email(email: str) -> bool:
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.search(regex, email))

    @staticmethod #Transform a number into a readable currency format.
    def formate_currency(value: float, symbol: str = '€') -> str:
        return f"{value:,.2f} {symbol}".replace(",", "X").replace(".", ",").replace("X", ".")

    @staticmethod #Read systems v=ariables or .env file
    def get_env(key: str, default: str = None) -> str:
        load_dotenv()
        return os.getenv(key, default)