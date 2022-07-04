from binance import enums

from src.repository.ohlc_repository import OhlcRepository
from src.service.klines import KLines

from src.parameters import assets_down, assets
from src.parameters_btc import assets_btc, market_btc
from src.parameters_futures import assets_futures, market_futures

repository = OhlcRepository()
klines = KLines()

start_at = '1610000000'
end_at = '1656110684'

exchange = 'binance'
interval = '5m'
groups = [
    {
        "market": 'USDT',
        "assets": assets,
        "type": enums.HistoricalKlinesType.SPOT
    },
    {
        "market": 'USDT',
        "assets": assets_down,
        "type": enums.HistoricalKlinesType.SPOT
    },
    {
        "market": market_btc,
        "assets": assets_btc,
        "type": enums.HistoricalKlinesType.SPOT
    },
    {
        "market": market_futures,
        "assets": assets_futures,
        "type": enums.HistoricalKlinesType.FUTURES
    },
]

for group in groups:
    for asset in group["assets"]:
        print(f'processing: {asset} {group["market"]} {interval}')

        collection = klines.build_klines(
            group["market"],
            asset,
            group["type"],
            interval,
            start_at,
            end_at,
        )

        print(len(collection))

        repository.create_many(
            exchange,
            group["market"],
            asset,
            interval,
            collection
        )
