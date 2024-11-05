# Define the recurrence relation
def calculate_y(n, y_values):
    return 0.8 * y_values[n-2] + 1.19 * y_values[n-1] - 0.99 * y_values[n-3]

# Initial conditions
y_values = [1, 0.95, 0.905]  # Example initial conditions for y0, y1, y2. You can modify these

# Calculate y3 to y100
for n in range(3, 1001):
    y_next = calculate_y(n, y_values)
    y_values.append(y_next)

# Output the results
for i in range(len(y_values)):
    print(f'y{i} = {y_values[i]}')
