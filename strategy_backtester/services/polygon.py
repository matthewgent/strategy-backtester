from datetime import date
from polygon import RESTClient
from polygon.rest.models import Agg
from strategy_backtester.models.ticker import Ticker


class Polygon:
    client: RESTClient

    def __init__(self) -> None:
        self.client = RESTClient()

    def update(self, ticker: Ticker, years: int) -> None:
        # calculate min and max dates
        # check what database values there are (min and max)
        # update for last x years
        pass

    def _fetch_aggregates(
        self,
        ticker: Ticker,
        start: date,
        end: date
    ) -> list[Agg]:
        aggregates = self.client.get_aggs(
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
