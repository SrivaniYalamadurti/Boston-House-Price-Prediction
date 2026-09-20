import pandas as pd

data = pd.read_csv("data/BostonHousing.csv")

print(data.head())

print("\nDataset Shape:")
print(data.shape)

print("\nColumn Names:")
print(data.columns)

print("\nData Information:")
print(data.info())

print("\nMissing Values:")
print(data.isnull().sum())

print("\nMedian values:")
print(data.median(numeric_only=True))

data = data.fillna(data.median(numeric_only=True))

print("\nMissing Values After Preprocessing:")
print(data.isnull().sum())

X = data.drop("MEDV", axis=1)
y = data["MEDV"]

print("\nFeatures (X):")
print(X.shape)

print("\nTarget (y):")
print(y.shape)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining Features:", X_train.shape)
print("Testing Features:", X_test.shape)
print("Training Target:", y_train.shape)
print("Testing Target:", y_test.shape)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

print("\nLinear Regression model trained successfully!")

y_pred = model.predict(X_test)

print("\nFirst 5 Predictions:")
print(y_pred[:5])

print("\nFirst 5 Actual Prices:")
print(y_test.iloc[:5].values)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)

from sklearn.ensemble import RandomForestRegressor

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

rf_mae = mean_absolute_error(y_test, rf_pred)
rf_mse = mean_squared_error(y_test, rf_pred)
rf_rmse = rf_mse ** 0.5
rf_r2 = r2_score(y_test, rf_pred)

print("\nRandom Forest Evaluation:")
print("MAE:", rf_mae)
print("MSE:", rf_mse)
print("RMSE:", rf_rmse)
print("R2 Score:", rf_r2)

import joblib

joblib.dump(rf_model, "house_price_model.pkl")

print("\nRandom Forest model saved successfully!")

import matplotlib.pyplot as plt

plt.scatter(y_test, rf_pred)

plt.xlabel("Actual House Prices")
plt.ylabel("Predicted House Prices")
plt.title("Actual vs Predicted House Prices")

plt.show()