import numpy as np
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler

from service.dataset_builder import build_dataset_unseen
from parameters import market, ASSET, INTERVAL

# Data
# ------------------------------------------------------------------------

tail = 20
asset = ASSET
interval = INTERVAL
filepath_model = f'data/ta_{market}_{asset}_{interval}.keras'

x_df = build_dataset_unseen(
    market=market,
    asset=asset,
    interval=interval,
)

# Scale
# ------------------------------------------------------------------------

scaler = MinMaxScaler()
scaled = scaler.fit_transform(x_df)

x_df_scaled = pd.DataFrame(scaled, None, x_df.keys())
x_df_scaled_expanded = np.expand_dims(x_df_scaled, axis=0)

# Model
# ------------------------------------------------------------------------

model = tf.keras.models.load_model(filepath_model)
y = model.predict(x_df_scaled_expanded)

# Append
# ------------------------------------------------------------------------

x_df_open = pd.DataFrame(np.zeros((len(x_df), len(x_df.columns))), columns=x_df.columns)
x_df_open['open'] = x_df['open'].values

y_df_open = pd.DataFrame(np.zeros((len(x_df), len(x_df.columns))), columns=x_df.columns)
y_df_open['open'] = y[0][:, 0]

y_df_open.loc[-1] = y_df_open.loc[0]
y_df_open = y_df_open.sort_index().reset_index(drop=True)

# Inverse
# ------------------------------------------------------------------------

y_df_open_inversed = scaler.inverse_transform(y_df_open)
y_df_open['open'] = y_df_open_inversed[:, 0]

# Plot
# ------------------------------------------------------------------------

plt.figure(figsize=(16, 8))

plt.plot(x_df_open['open'].tail(tail - 1).values, label='real', marker='.')
plt.plot(y_df_open['open'].tail(tail).values, label='predict', marker='.')

plt.ylabel('open')
plt.xlabel('time')
plt.legend()
plt.show()
