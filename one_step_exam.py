import numpy as np

# Function defining the given differential equation y' = 3x^2y
def f(x, y):
    return 3 * x**2 * y

# Euler's Method Implementation
def euler_method(x0, y0, h, x_end):
    # Generate x values from x0 to x_end with step size h
    x_values = np.arange(x0, x_end + h, h)
    y_values = [y0]  # List to store computed y values
    
    # Iterate through x values using Euler's formula
    for xk in x_values[:-1]:
        yk = y_values[-1]  # Get the last computed y value
        yk1 = yk + h * f(xk, yk)  # Compute next y value using Euler's method
        y_values.append(yk1)  # Store the new y value
    
    return x_values, y_values

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

# Heun's Method Implementation
def heun_method(x0, y0, h, x_end):
    # Generate x values from x0 to x_end with step size h
    x_values = np.arange(x0, x_end + h, h)
    y_values = [y0]  # List to store computed y values
    
    # Iterate through x values using Heun's formula
    for xk in x_values[:-1]:
        yk = y_values[-1]  # Get the last computed y value
        k1 = f(xk, yk)  # Compute k1
        k2 = f(xk + (2/3) * h, yk + (2/3) * h * k1)  # Compute k2
        
        # Compute next y value using Heun's method
        yk1 = yk + (h/4) * (k1 + 3 * k2)
        y_values.append(yk1)  # Store the new y value
    
    return x_values, y_values

# Define problem parameters
x0, y0, h, x_end = 0, 1, 0.1, 1  # Initial condition, step size, and endpoint

# Solve IVP using all three numerical methods
euler_result = euler_method(x0, y0, h, x_end)
runge_kutta_result = runge_kutta_4(x0, y0, h, x_end)
heun_result = heun_method(x0, y0, h, x_end)

# Print computed results for each method
methods = ['Euler', 'Runge-Kutta 4', 'Heun']
results = [euler_result, runge_kutta_result, heun_result]
for method, (x_vals, y_vals) in zip(methods, results):
    print(f"{method} Method:")
    for x, y in zip(x_vals, y_vals):
        print(f"x = {x:.1f}, y = {y:.6f}")
    print()
