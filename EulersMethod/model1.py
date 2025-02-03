import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
X = np.array([[10, 8], [12, 9], [14, 10], [16, 11]])  # Independent variables: Unemployment & Inflation
y = np.array([40, 45, 50, 55])  # Dependent variable: Poverty Rate

# Model
model = LinearRegression()
model.fit(X, y)

# Predictions
new_data = np.array([[13, 9.5]])  # New input
predicted_poverty_rate = model.predict(new_data)

# Extract coefficients
intercept = model.intercept_
coefficients = model.coef_

# Plot 1: Unemployment vs. Poverty Rate
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], y, color='blue', label='Actual Data')
plt.scatter(new_data[:, 0], predicted_poverty_rate, color='red', marker='x', s=100, label='Prediction')
plt.plot(X[:, 0], model.predict(X), color='green', linestyle='dashed', label='Regression Line')
plt.xlabel('Unemployment Rate')
plt.ylabel('Poverty Rate')
plt.title('Unemployment vs. Poverty Rate')
plt.legend()

# Plot 2: Inflation vs. Poverty Rate
plt.subplot(1, 2, 2)
plt.scatter(X[:, 1], y, color='blue', label='Actual Data')
plt.scatter(new_data[:, 1], predicted_poverty_rate, color='red', marker='x', s=100, label='Prediction')
plt.plot(X[:, 1], model.predict(X), color='green', linestyle='dashed', label='Regression Line')
plt.xlabel('Inflation Rate')
plt.ylabel('Poverty Rate')
plt.title('Inflation vs. Poverty Rate')
plt.legend()

plt.tight_layout()
plt.show()
