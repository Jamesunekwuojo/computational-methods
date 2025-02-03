import numpy as np
import matplotlib.pyplot as plt

def adams_bashforth_2step(P0, P1, h, t_end):
    t_values = np.arange(1, t_end + h, h)
    P_values = [P0, P1]  # First two values

    for t in t_values[1:]:
        P_next = P_values[-1] + h * ( (3/2) * (-0.05 * P_values[-1]) - (1/2) * (-0.05 * P_values[-2]) )
        P_values.append(P_next)

    return np.insert(t_values, 0, 0), P_values


P0 = 50  # Starting poverty rate in %
h = 1     # Step size (1 year)
t_end = 10  # 10 years simulation
P1 = 47.5  # Precomputed next step using Euler’s method
t_values, P_values = adams_bashforth_2step(P0, P1, h, t_end)

# Plot
plt.plot(t_values, P_values, marker="o", linestyle="-", color="purple", label="Adams-Bashforth Method")
plt.xlabel("Years")
plt.ylabel("Poverty Rate (%)")
plt.title("Poverty Rate Decline using Adams-Bashforth Method")
plt.grid(True)
plt.legend()
plt.show()
