# Finance Tools

Python-библиотека для финансовых расчетов.

## Возможности
- расчет НДС
- работа со счетами (Invoice)
- расчет кредита

## Пример использования

from finance_tools import Invoice

invoice = Invoice([100, 200, 300])
print(invoice.total(0.2))
