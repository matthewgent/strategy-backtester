from datetime import date
from dateutil.relativedelta import relativedelta
from polygon import RESTClient
from polygon.rest.models import Agg


class Polygon:
    client: RESTClient

    def __init__(self) -> None:
        self.client = RESTClient()

    def update_aggregates(self, ticker: str, years: int) -> None:
        end = date.today()
        start = end - relativedelta(years=years)

        # find min and max dates for ticker, calculate what needs downloading
        # ignore potentially missing days in the center
        # retrieve missing data on either end
        # store
        pass

    def _fetch_aggregates(
        self,
        ticker: str,
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
