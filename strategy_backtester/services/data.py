from datetime import date
from polygon import RESTClient
from polygon.rest.models import Agg


def retrieve(ticker: str, start: date, end: date) -> list[Agg]:
    client = RESTClient()
    aggregates = client.get_aggs(
        ticker,
        1,
        "day",
        start.isoformat(),
        end.isoformat(),
    )

    return aggregates


def store(aggregates: list[Agg]) -> Agg:
    pass


def retrieve_and_store(ticker: str, start: date, end: date) -> None:
    aggregates = retrieve(ticker, start, end)
    store(aggregates)

