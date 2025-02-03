import numpy as np
import matplotlib.pyplot as plt

def runge_kutta_4(P0, h, t_end):
    t_values = np.arange(0, t_end + h, h)
    P_values = [P0]

    for t in t_values[:-1]:
        k1 = -0.05 * P_values[-1] + 10
        k2 = -0.05 * (P_values[-1] + h/2 * k1) + 10
        k3 = -0.05 * (P_values[-1] + h/2 * k2) + 10
        k4 = -0.05 * (P_values[-1] + h * k3) + 10

        P_next = P_values[-1] + (h/6) * (k1 + 2*k2 + 2*k3 + k4)
        P_values.append(P_next)

    return t_values, P_values

P0 = 50  # Starting poverty rate in %
h = 1     # Step size (1 year)
t_end = 10  # 10 years simulation

t_values, P_values = runge_kutta_4(P0, h, t_end)

# Plot
plt.plot(t_values, P_values, marker="o", linestyle="-", color="r", label="Runge-Kutta Method")
plt.xlabel("Years")
plt.ylabel("Poverty Rate (%)")
plt.title("Poverty Rate Decline using Runge-Kutta Method")
plt.grid(True)
plt.legend()
plt.show()
