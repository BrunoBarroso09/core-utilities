import os
import re

class Utilities:

    @staticmethod
    def mask_email(email: str) -> str:
        #Privacy: Transform email 'example@email.com' to 'e******@email.com'
        if not email or '@' not in email:
            return 'Invalid email'

        email_split = email.split('@')
        user_email= email_split[0][0]
        domain = email_split[1]

        return f"{user_email}*****@{domain}"

    @staticmethod
    def clear_terminal():
        #Clear terminal (works in Windows, Mac and Linux)
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def valid_email(email: str) -> bool:
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.search(regex, email))