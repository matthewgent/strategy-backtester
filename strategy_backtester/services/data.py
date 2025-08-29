from datetime import date
from polygon import RESTClient
from polygon.rest.models import Agg


def retrieve(ticker: str, start: date, end: date) -> list[Agg]:
    client = RESTClient()
    aggs = client.get_aggs(
        ticker,
        1,
        "day",
        start.isoformat(),
        end.isoformat(),
    )

    return aggs


def store(aggs: list[Agg]) -> Agg:
    pass


results = retrieve("AAPL", date(2025, 8, 1), date(2025, 8, 7))
print(results)
