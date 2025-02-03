import numpy as np
import matplotlib.pyplot as plt

# Parameters
np.random.seed(42)  # Ensuring reproducibility
income_levels = np.random.normal(50000, 15000, 1000)  # Mean: 50000, Std: 15000, 1000 samples
poverty_threshold = 30000  # Income level below which people are considered in poverty

# Simulation
poverty_counts = np.sum(income_levels < poverty_threshold)
poverty_rate = (poverty_counts / len(income_levels)) * 100
print("Simulated Poverty Rate:", poverty_rate, "%")

# Plot the histogram
plt.figure(figsize=(10, 5))
plt.hist(income_levels, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

# Add poverty threshold line
plt.axvline(poverty_threshold, color='red', linestyle='dashed', linewidth=2, label="Poverty Threshold")

# Labels and title
plt.xlabel("Income Levels")
plt.ylabel("Frequency")
plt.title("Income Distribution and Poverty Threshold")
plt.legend()
plt.grid(True)

# Show plot
plt.show()
