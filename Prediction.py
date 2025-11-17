# -------------------------------------------------------
# LINEAR REGRESSION - AI & ML INTERNSHIP (Elevate Labs)
# Full Combined Code (Dataset name updated)
# -------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ---------------------------------------------
# 1. Load Dataset (Updated name)
# ---------------------------------------------
df = pd.read_csv("House Price Prediction Dataset.csv")

print("📌 First 5 rows of dataset:")
print(df.head())

# ---------------------------------------------
# 2. Prepare Features and Target
# ---------------------------------------------
X = df.drop("Price", axis=1)
y = df["Price"]

print("\n📌 Features used:")
print(X.columns)

# ---------------------------------------------
# 3. Train-Test Split
# ---------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\n📌 Dataset split completed.")
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

# ---------------------------------------------
# 4. Train Linear Regression Model
# ---------------------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

print("\n📌 Model training complete.")

# ---------------------------------------------
# 5. Predictions
# ---------------------------------------------
y_pred = model.predict(X_test)

# ---------------------------------------------
# 6. Evaluation Metrics
# ---------------------------------------------
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n📊 MODEL EVALUATION")
print("MAE  :", mae)
print("MSE  :", mse)
print("RMSE :", rmse)
print("R² Score :", r2)

# ---------------------------------------------
# 7. Coefficients & Intercept
# ---------------------------------------------
print("\n📌 Model Intercept:", model.intercept_)
print("\n📌 Model Coefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}  -->  {coef}")

# ---------------------------------------------
# 8. Plot Regression Line (only when single feature)
# ---------------------------------------------
if X.shape[1] == 1:
    plt.scatter(X_test, y_test)
    plt.plot(X_test, y_pred)
    plt.xlabel(X.columns[0])
    plt.ylabel("Price")
    plt.title("Regression Line")
    plt.show()

print("\n🎉 Task Completed Successfully!")
