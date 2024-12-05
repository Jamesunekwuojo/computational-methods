import numpy as np
import matplotlib.pyplot as plt

# Define the function for the differential equation
def f(x, y):
    return 3 * x**2 * y

# Euler's method to solve the ODE
def euler_method(f, x0, y0, x_end, h):
    x_values = np.arange(x0, x_end, h)
    y_values = np.zeros(len(x_values))
    y_values[0] = y0

    for i in range(1, len(x_values)):
        y_values[i] = y_values[i-1] + h * f(x_values[i-1], y_values[i-1])

    return x_values, y_values

# Initial condition
x0 = 0        # Start of the interval
y0 = 1        # Initial value of y at x0
x_end = 1     # End of the interval
h = 0.1       # Step size

# Solve the equation using Euler's method
x_values, y_values = euler_method(f, x0, y0, x_end, h)
print("x_values: ", x_values, "\ny_values: ", y_values)

# Plot the results
plt.plot(x_values, y_values, label="Euler's method", color='b')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Euler's Method for y' = 3x²y")
plt.legend()
plt.grid(True)
plt.show()
