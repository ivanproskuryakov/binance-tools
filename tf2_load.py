import matplotlib.pyplot as plt

import tensorflow as tf
from keras.layers import Dense, GRU, LSTM

from binance import Client
from service.window_generator import WindowGenerator
from service.dataset import build_dataset

# Data load
# ------------------------------------------------------------------------

asset = 'SOL'
interval = Client.KLINE_INTERVAL_1HOUR
filepath_model = f'data/ta_{asset}_{interval}.keras'

[train_df, val_df, test_df, df_num_signals] = build_dataset(
    asset=asset,
    interval=interval
)

# Generator function
# --------------------------------------------------------

window = WindowGenerator(
    input_width=30,
    label_width=30,
    shift=8,
    batch_size=10,
    label_columns=['open'],
    train_df=train_df,
    val_df=val_df,
    test_df=test_df,
)

model = tf.keras.models.Sequential([
    GRU(
        units=20,
        return_sequences=True,
        input_shape=(None, df_num_signals,)
    ),
    LSTM(20, return_sequences=True),
    Dense(units=1),
])

model.load_weights(filepath_model)

print(model.summary())

window.plot(model, 'open', 10)

plt.show()
