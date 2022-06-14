import pandas as pd
from sklearn.preprocessing import MinMaxScaler

from src.service.estimator import estimate_ta_fill_na
from src.repository.ohlc_repository import OhlcRepository


def build_dataset_window(market: str, asset: str, interval: str):
    repository = OhlcRepository()

    df_ohlc = repository.find_all_with_df(
        exchange='binance',
        market=market,
        asset=asset,
        interval=interval
    )

    df_ta_na = estimate_ta_fill_na(df_ohlc)

    # Data Scaling
    # ------------------------------------------------------------------------

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df_ta_na)

    df = pd.DataFrame(scaled, None, df_ta_na.keys())

    # Data split
    # --------------------------------------------------------
    n = len(df)
    df_train = df[0:int(n * 0.9)]
    dv_validate = df[int(n * 0.9):]

    return df_train, dv_validate


def build_dataset_window_many(market: str, assets: list[str], interval: str):
    train = pd.DataFrame()
    validate = pd.DataFrame()

    for asset in assets:
        df_train, df_validate = build_dataset_window(
            asset=asset,
            market=market,
            interval=interval
        )

        if train.empty:
            train = df_train
            validate = df_validate
        else:
            train.append(df_train)
            validate.append(df_validate)

    return train, validate


def build_dataset_random(market: str, asset: str, interval: str):
    repository = OhlcRepository()

    df_ohlc = repository.find_all_with_df(
        exchange='binance',
        market=market,
        asset=asset,
        interval=interval
    )

    df = df_ohlc.fillna(0)

    # df_ta_na = estimate_ta_fill_na(df_na)

    # Data Scaling
    # ------------------------------------------------------------------------

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df)

    return pd.DataFrame(scaled, None, df.keys())
