import matplotlib.pyplot as plt

# Data
poverty_line = 30000
incomes = [25000, 18000, 40000, 15000, 32000]

# Compute PGI
poverty_gap = [max(0, poverty_line - income) for income in incomes]
pgi = sum(poverty_gap) / (poverty_line * len(incomes))
print("Poverty Gap Index (PGI):", pgi)

# Visualization
plt.figure(figsize=(8, 5))
bars = plt.bar(range(len(incomes)), incomes, color='skyblue', label="Income Levels")

# Add poverty gap markers
for i, (income, gap) in enumerate(zip(incomes, poverty_gap)):
    if gap > 0:  # Highlight only those below the poverty line
        plt.bar(i, income, color='lightcoral', label="Below Poverty Line" if i == 0 else "")
        plt.text(i, income + 1000, f'Gap: {gap}', ha='center', fontsize=10, color='black')

# Poverty line
plt.axhline(y=poverty_line, color='red', linestyle='dashed', linewidth=2, label="Poverty Line")

# Labels and title
plt.xticks(range(len(incomes)), [f"Person {i+1}" for i in range(len(incomes))])
plt.ylabel("Income ($)")
plt.title("Income Levels and Poverty Gap")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot
plt.show()
