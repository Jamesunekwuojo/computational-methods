import numpy as np
import matplotlib.pyplot as plt

def modified_euler_method(P0, h, t_end):
    t_values = np.arange(0, t_end + h, h)
    P_values = [P0]

    for t in t_values[:-1]:
        P_pred = P_values[-1] + h * (-0.05 * P_values[-1])  # Prediction step
        P_corr = P_values[-1] + (h/2) * (-0.05 * P_values[-1] + (-0.05 * P_pred))  # Correction step
        P_values.append(P_corr)

    return t_values, P_values


# Initial condition
P0 = 50  # Starting poverty rate in %
h = 1     # Step size (1 year)
t_end = 10  # 10 years simulation


t_values, P_values = modified_euler_method(P0, h, t_end)

# Plot
plt.plot(t_values, P_values, marker="o", linestyle="-", color="g", label="Modified Euler's Method")
plt.xlabel("Years")
plt.ylabel("Poverty Rate (%)")
plt.title("Poverty Rate Decline using Modified Euler's Method")
plt.grid(True)
plt.legend()
plt.show()
