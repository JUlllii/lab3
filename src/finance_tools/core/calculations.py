from finance_tools.utils.validators import validate_amount, validate_rate


def add_tax(amount: float, rate: float) -> float:
    validate_amount(amount)
    validate_rate(rate)
    return amount * (1 + rate)


def extract_tax(amount: float, rate: float) -> float:
    validate_amount(amount)
    validate_rate(rate)
    return amount * rate / (1 + rate)