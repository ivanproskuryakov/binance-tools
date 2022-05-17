import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from service.dataset_builder import build_dataset, build_dataset_prepared
from parameters import market, ASSET, INTERVAL

# Data
# ------------------------------------------------------------------------


asset = ASSET
interval = INTERVAL
filepath_model = f'trained/ta_USDT_BTC_1m.keras'

# [
#     df,
#     train_df,
#     val_df,
#     test_df,
#     df_num_signals,
# ] = build_dataset_prepared(
#     market=market,
#     asset=asset,
#     interval=interval,
#     # test=True,
# )

test_df = build_dataset(
    market=market,
    asset=asset,
    interval=interval,
    test=True,
)

df = test_df[:31]

x = np.expand_dims(df, axis=0)

# Model
# ----------------------------------------------------------------------------------


model = tf.keras.models.load_model(filepath_model)
y = model.predict(x)

price_open = y[0][:, 0]

# Plot
# ----------------------------------------------------------------------------------

plt.figure(figsize=(15, 5))

plt.plot(df['open'].values, label='true')
plt.plot(price_open, label='pred')

plt.legend()
plt.show()
