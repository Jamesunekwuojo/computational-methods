import numpy as np
import matplotlib.pyplot as plt

# Given differential equation: dP/dt = -0.05P
def euler_method(P0, h, t_end):
    t_values = np.arange(0, t_end + h, h)
    P_values = [P0]

    for t in t_values[:-1]:
        P_next = P_values[-1] + h * (-0.05 * P_values[-1])
        P_values.append(P_next)

    return t_values, P_values

# Initial condition
P0 = 50  # Starting poverty rate in %
h = 1     # Step size (1 year)
t_end = 10  # 10 years simulation

t_values, P_values = euler_method(P0, h, t_end)

# Plot
plt.plot(t_values, P_values, marker="o", linestyle="-", color="b", label="Euler's Method")
plt.xlabel("Years")
plt.ylabel("Poverty Rate (%)")
plt.title("Poverty Rate Decline using Euler's Method")
plt.grid(True)
plt.legend()
plt.show()
