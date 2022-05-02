from binance import Client

assets = [
    "BNB",
    "ETH",
    "ADA",
    "ROSE",
    "SOL", "XRP",
    "DOT", "ATOM", "HBAR", "IOTA", "AVAX",
    "COTI", "NEAR", "BAT", "WAVES", "MINA",
    "EGLD", "XTZ", "ALGO", "LUNA", "KSM",
    "MATIC", "ONE", "1INCH", "KAVA", "OCEAN",
    "GRT", "ROSE", "CTSI", "ZRX", "TRX",
    "ETC", "BCH", "LINK", "FIL", "UNI",
    "GTC", "NU", "POND", "CELO"
]

market = 'BTC'

intervals = [
    Client.KLINE_INTERVAL_1MINUTE,
    Client.KLINE_INTERVAL_3MINUTE,
    Client.KLINE_INTERVAL_5MINUTE,
    Client.KLINE_INTERVAL_15MINUTE,
    Client.KLINE_INTERVAL_30MINUTE,
    Client.KLINE_INTERVAL_1HOUR,
    Client.KLINE_INTERVAL_4HOUR,
    Client.KLINE_INTERVAL_12HOUR,
    Client.KLINE_INTERVAL_1DAY,
]

start_at = '6 month ago UTC'

SIZE_SHIFT = 2
SIZE_BATCH = 100
