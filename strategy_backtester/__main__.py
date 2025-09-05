from strategy_backtester.services.polygon import retrieve
from datetime import date

results = retrieve(
    "AAPL",
    date(2025, 8, 1),
    date(2025, 8, 7),
)

print('end')
