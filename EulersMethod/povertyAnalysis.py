import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Sample Data (Simulated)
data = {
    'Years_of_Education': [0, 2, 4, 6, 8, 10, 12, 14, 16],
    'Household_Income': [2000, 4000, 6000, 8000, 12000, 16000, 20000, 24000, 30000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Define features and target
X = df[['Years_of_Education']]
y = df['Household_Income']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Visualization
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel('Years of Education')
plt.ylabel('Household Income')
plt.title('Impact of Education on Household Income')
plt.legend()
plt.show()