from finance_tools.core.invoice import Invoice


def calculate_invoice_total(items, rate):
    invoice = Invoice(items)
    return invoice.total(rate)