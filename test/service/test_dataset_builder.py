from fixture.ohlc import crate_ohlc_many

from src.entity.ohlc import Ohlc
from src.service.dataset_builder_db import DatasetBuilderDB
from src.connector.db_connector import db_connect


def test_build_dataset_all():
    engine = db_connect()
    Ohlc.metadata.drop_all(bind=engine)
    Ohlc.metadata.create_all(bind=engine)

    builder = DatasetBuilderDB()

    assets = [
        'BTC',
        'ETH',
    ]
    assets_down = [
        'BTCUP',
        'BTCDOWN',
        'ETHUP',
        'ETHDOWN',
    ]
    assets_btc = [
        'ETH',
        'LTC',
    ]
    for asset in assets:
        crate_ohlc_many(asset=asset, market='USDT', interval='5m', quantity=10)

    # USDT market
    crate_ohlc_many(asset='BTCUP', market='USDT', interval='5m', quantity=9)
    crate_ohlc_many(asset='BTCDOWN', market='USDT', interval='5m', quantity=8)
    crate_ohlc_many(asset='ETHUP', market='USDT', interval='5m', quantity=7)
    crate_ohlc_many(asset='ETHDOWN', market='USDT', interval='5m', quantity=6)

    # BTC market
    crate_ohlc_many(asset='ETH', market='BTC', interval='5m', quantity=5)
    crate_ohlc_many(asset='LTC', market='BTC', interval='5m', quantity=4)

    train, validate = builder.build_dataset_all(
        market='USDT',
        assets=assets,
        assets_down=assets_down,
        assets_btc=assets_btc,
        interval='5m',
    )

    assert len(train) == 6
    assert len(train.keys()) == 86

    assert len(validate) == 2
    assert len(train.keys()) == 86
