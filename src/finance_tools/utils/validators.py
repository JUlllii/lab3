from finance_tools.exceptions import NegativeAmountError, InvalidRateError


def validate_amount(value: float) -> None:
    if value < 0:
        raise NegativeAmountError("Amount cannot be negative")


def validate_rate(rate: float) -> None:
    if rate < 0 or rate > 1:
        raise InvalidRateError("Rate must be between 0 and 1")