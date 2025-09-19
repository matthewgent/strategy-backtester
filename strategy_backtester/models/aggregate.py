from datetime import datetime
from decimal import Decimal
from sqlalchemy import Numeric, BigInteger, CheckConstraint, TIMESTAMP, \
    String
from sqlalchemy.orm import Mapped, mapped_column
from strategy_backtester.models.model import Model


class Aggregate(Model):
    __tablename__ = 'aggregates'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    ticker: Mapped[str] = mapped_column(String(5))
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

    def __repr__(self) -> str:
        return (f"Aggregate(id={self.id!r}, ticker={self.ticker!r}, "
                f"close={self.close!r}, recorded_at={self.recorded_at!r})")
