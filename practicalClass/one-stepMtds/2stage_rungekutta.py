import numpy as np

def f(x, y):
    """Defines the differential equation y' = 3x^2y"""
    return 3 * x**2 * y

def exact_solution(x):
    """Exact solution for comparison"""
    return np.exp(x**3)

def runge_kutta_2_stage(x0, y0, h, x_end, a=0.5):
    """
    Implements the 2-Stage Runge-Kutta Method for solving y' = 3x^2y.
    
    Parameters:
    x0: Initial x value
    y0: Initial y value (y(x0))
    h: Step size
    x_end: Final x value
    a: Parameter for the method (default is 0.5)
    
    Returns:
    x_values, y_values: Arrays of computed x and y values
    """
    # Compute constants c1 and c2
    c1 = h * (1 - (1 / (2 * a)))
    c2 = h / (2 * a)
    
    # Create arrays for x and y values
    x_values = np.arange(x0, x_end + h, h)
    y_values = [y0]
    
    # Iterate over each step
    for xk in x_values[:-1]:
        yk = y_values[-1]
        
        # Compute k1 and k2
        k1 = f(xk, yk)
        k2 = f(xk + a * h, yk + a * h * k1)
        
        # Compute y_{k+1} using the formula
        yk1 = yk + c1 * k1 + c2 * k2
        y_values.append(yk1)
    
    return x_values, y_values

# Define problem parameters
x0, y0, h, x_end = 0, 1, 0.1, 1

# Solve IVP using 2-Stage Runge-Kutta Method
rk2_x, rk2_y = runge_kutta_2_stage(x0, y0, h, x_end)

# Print formatted table
print(f"{'x':<10}{'y_approx':<15}{'y_exact'}")
print("-" * 35)

for x, y_approx in zip(rk2_x, rk2_y):
    print(f"{x:<10.4f}{y_approx:<15.6f}{exact_solution(x):.6f}")
