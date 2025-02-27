import numpy as np

# Function defining the given differential equation y' = 3x^2y
def f(x, y):
    return 3 * x**2 * y

def exact_solution(x):
    return np.exp(x**3)  # Corrected solution

# Euler's Method Implementation
def euler_method(x0, y0, h, x_end):
    # Generate x values from x0 to x_end with step size h
    x_values = np.arange(x0, x_end + h, h)
    y_values = [y0]  # List to store computed y values
    
    # Print header
    print(f"{'x':<10}{'y_approx':<15}{'y_exact'}")
    print("-" * 35)

    # Iterate through x values using Euler's formula
    for xk in x_values[:-1]:
        yk = y_values[-1]  # Get the last computed y value
        yk1 = yk + h * f(xk, yk)  # Compute next y value using Euler's method
        y_values.append(yk1)  # Store the new y value

        # Print formatted row
        print(f"{xk:<10.4f}{yk1:<15.6f}{exact_solution(xk):.6f}")

x0, y0, h, x_end = 0, 1, 0.1, 1  # Initial condition, step size, and endpoint
euler_method(x0, y0, h, x_end)
