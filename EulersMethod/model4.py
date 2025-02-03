import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Data
data = [40, 42, 44, 45, 48, 50, 52, 54]  # Hypothetical poverty rates
index = pd.date_range("2015", periods=len(data), freq="Y")
series = pd.Series(data, index=index)

# ARIMA Model
model = ARIMA(series, order=(1, 1, 1))
model_fit = model.fit()
forecast = model_fit.forecast(steps=1)
predicted_year = pd.date_range("2024", periods=1, freq="Y")
predicted_value = forecast[0]

print("Predicted Poverty Rate for 2024:", predicted_value)

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(series.index, series, marker="o", linestyle="-", color="blue", label="Historical Poverty Rates")
plt.scatter(predicted_year, predicted_value, color="red", marker="x", s=100, label="Forecasted 2024 Poverty Rate")

# Labels & Title
plt.xlabel("Year")
plt.ylabel("Poverty Rate (%)")
plt.title("Poverty Rate Trend with ARIMA Forecast")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

# Show plot
plt.show()
