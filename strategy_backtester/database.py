from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv as env

connection = env('DATABASE_CONNECTION', 'postgresql+psycopg2')
user = env('DATABASE_USER', 'user')
password = env('DATABASE_PASSWORD', 'password')
host = env('DATABASE_HOST', 'localhost')
port = env('DATABASE_PORT', '5432')
database = env('DATABASE_NAME', 'strategy_backtester')

config_string = f"{connection}://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(config_string)
Session = sessionmaker(bind=engine)
