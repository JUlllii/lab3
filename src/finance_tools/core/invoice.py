from finance_tools.utils.validators import validate_rate


class Invoice:
    def __init__(self, items: list[float]):
        self.items = items

    def subtotal(self) -> float:
        return sum(self.items)

    def tax(self, rate: float) -> float:
        validate_rate(rate)
        return self.subtotal() * rate

    def total(self, rate: float) -> float:
        return self.subtotal() * (1 + rate)