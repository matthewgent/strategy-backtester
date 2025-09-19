from datetime import date
from dateutil.relativedelta import relativedelta
from polygon import RESTClient
from polygon.rest.models import Agg
from sqlalchemy import select
from sqlalchemy.orm import Session

from strategy_backtester.models.aggregate import Aggregate


class Polygon:
    client: RESTClient

    def __init__(self) -> None:
        self.client = RESTClient()

    def update_aggregates(self, ticker: str, years: int) -> None:
        end = date.today()
        start = end - relativedelta(years=years)

        session = Session(engine)

        latest_stmt = (select(Aggregate.recorded_at)
                       .where(Aggregate.ticker == ticker)
                       .order_by(Aggregate.recorded_at.desc())
                       )
        latest = session.scalar(latest_stmt)

        # find min and max dates for ticker, calculate if we have it all
        # retrieve all data if we are missing anything (1 API call anyway)
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
