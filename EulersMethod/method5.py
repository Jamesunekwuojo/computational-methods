import numpy as np
import matplotlib.pyplot as plt

def adams_moulton_2step(P0, h, t_end, tol=1e-6, max_iter=10):
    t_values = np.arange(1, t_end + h, h)
    P_values = [P0]  # First value

    for t in t_values:
        P_pred = P_values[-1] + h * (-0.05 * P_values[-1] + 10)  # Predict
        P_corr = P_pred
        for _ in range(max_iter):  # Iterative correction
            P_corr_new = P_values[-1] + (h / 2) * ((-0.05 * P_values[-1] + 10) + (-0.05 * P_corr + 10))
            if abs(P_corr_new - P_corr) < tol:
                break
            P_corr = P_corr_new
        P_values.append(P_corr)

    return np.insert(t_values, 0, 0), P_values

P0 = 50  # Starting poverty rate in %
h = 1     # Step size (1 year)
t_end = 10  # 10 years simulation
P1 = 47.5  # Precomputed next step using Euler’s method

t_values, P_values = adams_moulton_2step(P0, h, t_end)

# Plot
plt.plot(t_values, P_values, marker="o", linestyle="-", color="orange", label="Adams-Moulton Method")
plt.xlabel("Years")
plt.ylabel("Poverty Rate (%)")
plt.title("Poverty Rate Decline using Adams-Moulton Method")
plt.grid(True)
plt.legend()
plt.show()
