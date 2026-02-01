import os

class Utilities:

    @staticmethod
    def mask_email(email: str) ->str:
        #Privacy: Transform email 'example@email.com' to 'e******@email.com'
        email_split = email.split('@')
        print(f"{email_split[0][0]}*****@{email_split[1]}")

    def clear_terminal():
        #Clear terminal (works in Windows, Mac and Linux)
        os.system('cls' if os.name == 'nt' else 'clear')

em = Utilities.mask_email('brunomcbarroso@gmail.com')