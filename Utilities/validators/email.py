import re

class EmailUtilities:

    @staticmethod
    def mask_email(email: str) -> str:
        """
        Masks an email address for gdpr compliance.

        Args:
            email: The email address to mask.
        Returns:
            The masked email address.
        Raises:
            ValueError: If the email format is invalid.
        """
        if not email or '@' not in email or '.' not in email:
            raise ValueError(f"Invalid email: {email}")

        local, domain = email.rsplit('@', 1)

        if len(local) == 1:
            masked_local = '*'
        else:
            masked_local = local[0] + '*' * (len(local) - 1)

        domain_name, tld = domain.rsplit('.', 1)

        if len(domain_name) == 1:
            masked_domain = '*'
        else:
            masked_domain = domain_name[0] + '*' * (len(domain_name) - 1)

        return f"{masked_local}@{masked_domain}.{tld}"

    _EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validate if the email format is valid

        Args:
            email: The email address to validate.
        Returns:
            True if the email format is valid, False otherwise.
        """
        if not isinstance(email, str):
            raise TypeError(f"Invalid email: {email}")

        if not email or '@' not in email:
            raise ValueError(f"Invalid email: {email}")

        email = email.strip()

        return bool(EmailUtilities._EMAIL_REGEX.search(email))