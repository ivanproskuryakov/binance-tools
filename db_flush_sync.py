from src.entity.ohlc import Ohlc
from src.entity.trade import Trade
from src.entity.exchange import Exchange
from src.connector.db_connector import db_connect

engine = db_connect()

Ohlc.metadata.drop_all(bind=engine)
Trade.metadata.drop_all(bind=engine)
Exchange.metadata.drop_all(bind=engine)

Ohlc.metadata.create_all(bind=engine)
Trade.metadata.create_all(bind=engine)
Exchange.metadata.create_all(bind=engine)
