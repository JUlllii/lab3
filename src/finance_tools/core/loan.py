from math import pow
from finance_tools.utils.validators import validate_amount, validate_rate


class LoanCalculator:
    def __init__(self, principal: float, rate: float, periods: int):
        validate_amount(principal)
        validate_rate(rate)

        self.principal = principal
        self.rate = rate
        self.periods = periods

    def annuity_payment(self) -> float:
        r = self.rate
        n = self.periods
        return self.principal * (r * pow(1 + r, n)) / (pow(1 + r, n) - 1)

    def total_payment(self) -> float:
        return self.annuity_payment() * self.periods