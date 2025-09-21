from strategy_backtester.database.config import engine
from strategy_backtester.database.models.model import Model

Model.metadata.create_all(engine)
print('Database created.')
