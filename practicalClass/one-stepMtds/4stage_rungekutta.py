import numpy as np

# Function defining the given differential equation y' = 3x^2y
def f(x, y):
    return 3 * x**2 * y

def exact_solution(x):
    return np.exp(x**3)

# 4-Stage Runge-Kutta Method Implementation
def runge_kutta_4(x0, y0, h, x_end):
    # Generate x values from x0 to x_end with step size h
    x_values = np.arange(x0, x_end + h, h)
    y_values = [y0]  # List to store computed y values
    
    # Iterate through x values using Runge-Kutta formula
    for xk in x_values[:-1]:
        yk = y_values[-1]  # Get the last computed y value
        k1 = f(xk, yk)  # Compute k1
        k2 = f(xk + h/2, yk + (h/2) * k1)  # Compute k2
        k3 = f(xk + h/2, yk + (h/2) * k2)  # Compute k3
        k4 = f(xk + h, yk + h * k3)  # Compute k4
        
        # Compute next y value using weighted average of k values
        yk1 = yk + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
        y_values.append(yk1)  # Store the new y value
    
    return x_values, y_values

# Call function
x0, y0, h, x_end = 0, 1, 0.1, 1  # Initial condition, step size, and endpoint
x_values, y_approx_values = runge_kutta_4(x0, y0, h, x_end)

# Print formatted table
print(f"{'x':<10}{'y_approx':<15}{'y_exact'}")
print("-" * 35)

for x, y_approx in zip(x_values, y_approx_values):
    print(f"{x:<10.4f}{y_approx:<15.6f}{exact_solution(x):.6f}")
