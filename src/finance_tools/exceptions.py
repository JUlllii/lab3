class FinanceError(Exception):
    pass


class InvalidRateError(FinanceError):
    pass


class NegativeAmountError(FinanceError):
    pass