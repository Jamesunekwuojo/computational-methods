import numpy as np

# Given parameters
h = 0.1
x0, y0 = 0, 1  # Initial condition
x_values = np.arange(x0, 1 + h, h)  # Generate x values from 0 to 1 with step size h
y_values = [y0]  # List to store y values

# Function f(x, y) = 3x^2y
def f(x, y):
    return 3 * x**2 * y

def exact_solution(x):
    return np.exp(x**3)  # Exact solution for comparison

# Implement Euler's Modified Method
for xk in x_values[:-1]:  # Iterate over all x values except the last
    yk = y_values[-1]
    k1 = f(xk, yk)
    yk_half_step = yk + 0.5 * h * k1  # Intermediate y value
    xk_half_step = xk + 0.5 * h  # Intermediate x value
    k2 = f(xk_half_step, yk_half_step)  # Compute f at the intermediate step
    yk1 = yk + h * k2  # Compute next y value
    y_values.append(yk1)

# Print formatted table
print(f"{'x':<10}{'y_approx':<15}{'y_exact'}")
print("-" * 35)

for x, y_approx in zip(x_values, y_values):
    print(f"{x:<10.4f}{y_approx:<15.6f}{exact_solution(x):.6f}")
