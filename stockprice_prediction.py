# -*- coding: utf-8 -*-
"""StockPrice_Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1H4op6dr-ZN8fW7EQhOMccAEi2UMH010u
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sp

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.metrics import mean_squared_error
import math
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

df=pd.read_csv('IOC-BSE.csv')
df.head()

df.describe()

df.isnull().sum()

df.shape

df.info()

plt.figure(figsize=(10,5))
plt.plot(df['close'])
plt.title('IOC Close price.', fontsize=15)
plt.ylabel('Price in Rupees.')
plt.show()

# Preprocess Data
# Assuming 'Close' column exists
data = df['close'].values.reshape(-1, 1)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

# Split into train and test
train_size = int(len(scaled_data) * 0.8)
train_data = scaled_data[:train_size]
test_data = scaled_data[train_size - 60:]

#Create sequences
def create_dataset(data, time_step=60):
    x, y = [], []
    for i in range(time_step, len(data)):
        x.append(data[i - time_step:i, 0])
        y.append(data[i, 0])
    return np.array(x), np.array(y)

x_train, y_train = create_dataset(train_data)
x_test, y_test = create_dataset(test_data)

# Reshape input to be [samples, time steps, features]
x_train = x_train.reshape((x_train.shape[0], x_train.shape[1], 1))
x_test = x_test.reshape((x_test.shape[0], x_test.shape[1], 1))

#Build LSTM Model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)),
    LSTM(50),
    Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')
model.summary()

# Train Model
model.fit(x_train, y_train, epochs=20, batch_size=32)

# Predict and Inverse Transform
predicted = model.predict(x_test)
predicted_prices = scaler.inverse_transform(predicted)
real_prices = scaler.inverse_transform(y_test.reshape(-1, 1))

# Visualize
plt.figure(figsize=(14, 6))
plt.plot(real_prices, color='blue', label='Actual IOC Stock Price')
plt.plot(predicted_prices, color='red', label='Predicted IOC Stock Price')
plt.title('IOC Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()

# RMSE
rmse = math.sqrt(mean_squared_error(real_prices, predicted_prices))
print(f"Root Mean Square Error: {rmse:.4f}")

# Display Predicted vs Actual Prices
predicted_df = pd.DataFrame({
    'Actual Price': real_prices.flatten(),
    'Predicted Price': predicted_prices.flatten()
})

# Show the first few rows
print(predicted_df.head(10))

# Get corresponding dates for the test set
dates = df['date'].values  # assuming 'Date' column exists
dates = dates[-len(real_prices):]  # align with actual/predicted data

# Create DataFrame with Date, Actual, Predicted
predicted_df = pd.DataFrame({
    'Date': dates,
    'Actual Price': real_prices.flatten(),
    'Predicted Price': predicted_prices.flatten()
})

# Display first few rows
print(predicted_df.head(10))

# Save to CSV
predicted_df.to_csv('IOC_Predicted_vs_Actual.csv', index=False)
print("File 'IOC_Predicted_vs_Actual.csv' has been saved with Date column.")