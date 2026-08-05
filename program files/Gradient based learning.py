import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
housing = fetch_california_housing()
X= housing.data
Y = housing.target
print(housing.feature_names)
df = pd.DataFrame(X, columns=housing.feature_names)
df["HouseValue"] = Y
df.head()
print(df.shape)
print(df.info())
print(df.describe())
df.isnull().sum()
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = Sequential([
    Dense(64, activation='relu', input_shape=(8,)),
    Dense(32, activation='relu'),
    Dense(16, activation='linear'),
    Dense(1)
    ])
model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
    )
model.summary()
history = model.fit(
    X_train,
    y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    verbose=1
    )
plt.figure(figsize=(8,5))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training vs Validation Loss")
plt.legend()
plt.show()
loss, mae = model.evaluate(X_test, y_test)
print("Test Loss:", loss)
print("Test MAE:", mae)
predictions = model.predict(X_test)
comparison = pd.DataFrame({
    "Actual": y_test[:10],
    "Predicted": predictions[:10].flatten()
    })
print(comparison)
