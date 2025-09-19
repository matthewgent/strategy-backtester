from datetime import datetime
from decimal import Decimal
from sqlalchemy import Numeric, BigInteger, CheckConstraint, TIMESTAMP, \
    ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from strategy_backtester.models.model import Model
from strategy_backtester.models.ticker import Ticker


class Price(Model):
    __tablename__ = 'prices'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    ticker_id: Mapped[int] = mapped_column(ForeignKey('tickers.id'))

    open: Mapped[Decimal] = mapped_column(
        Numeric(11, 4),
        CheckConstraint('open >= 0'),
        nullable=False,
    )
    close: Mapped[Decimal] = mapped_column(
        Numeric(11, 4),
        CheckConstraint('close >= 0'),
        nullable=False,
    )
    high: Mapped[Decimal] = mapped_column(
        Numeric(11, 4),
        CheckConstraint('high >= 0'),
        nullable=False,
    )
    low: Mapped[Decimal] = mapped_column(
        Numeric(11, 4),
        CheckConstraint('low >= 0'),
        nullable=False,
    )
    volume: Mapped[int] = mapped_column(
        BigInteger,
        CheckConstraint('volume >= 0'),
        nullable=False,
    )
    transactions: Mapped[int] = mapped_column(
        BigInteger,
        CheckConstraint('transactions >= 0'),
        nullable=False,
    )
    vwap: Mapped[Decimal] = mapped_column(
        Numeric(11, 4),
        CheckConstraint('vwap >= 0'),
        nullable=False,
    )
    recorded_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=False,
    )

    ticker: Mapped["Ticker"] = relationship(back_populates="prices")

    def __repr__(self) -> str:
        return (f"Price(id={self.id!r}, ticker_id={self.ticker_id!r}, "
                f"open={self.open!r}, recorded_at={self.recorded_at!r})")
