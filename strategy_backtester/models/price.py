from decimal import Decimal

from sqlalchemy import Integer, Numeric, BigInteger, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column

from strategy_backtester.models.model import Model


class Price(Model):
    __tablename__ = 'prices'
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    open: Mapped[Decimal] = mapped_column(Numeric(11, 4), CheckConstraint('open >= 0'))
    close: Mapped[Decimal] = mapped_column(Numeric(11, 4))
    high: Mapped[Decimal] = mapped_column(Numeric(11, 4))
    low: Mapped[Decimal] = mapped_column(Numeric(11, 4))
    volume: Mapped[int] = mapped_column(BigInteger, unsigned=True)
