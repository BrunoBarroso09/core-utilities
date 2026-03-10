import math

class CurrencyUtilities:

    @staticmethod
    def format_currency(value: float) -> str:
        """
        Transform a number into a readable currency format

        Args:
            value: The value to format.
        Returns:
            The formatted value.
        Raises:
            ValueError: If the value is not valid.
        """
        if not isinstance(value, (int, float)):
            raise ValueError("Invalid value")

        if math.isnan(value) or math.isinf(value):
            raise ValueError(f"Invalid value: {value}")

        formatted = f"{value:.2f}"
        integer_part, decimal_part = formatted.split('.')

        is_negative = integer_part.startswith('-')
        if is_negative:
            integer_part = integer_part[1:]

        integer_formatted = f"{int(integer_part):,}".replace(',', '.')

        result = f"{integer_formatted},{decimal_part} €"

        if is_negative:
            result = f"-{result}"

        return result
