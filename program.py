import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Read the file and skip the first line
file_path = 'data1.txt'  # Replace 'your_file.txt' with the actual file name
data = np.genfromtxt(file_path, delimiter='\t', skip_header=2, dtype=float)

# Separate columns
t = data[:, 0]
theta = data[:, 1]

# Plotting the original data with smaller markers
plt.figure(figsize=(8, 6))
plt.plot(t, theta, marker='o', markersize=4, linestyle='-', color='b', label='Original Data')

# Splitting the data into two ranges based on t values
t_1 = t[t <= 2.97]
theta_1 = theta[t <= 2.97]

t_2 = t[t > 2.97]
theta_2 = theta[t > 2.97]

# Define the function to fit the curve: theta = 1/2 * theta * t^2 + v_0 * t + d_0
def func(t, half_theta, v_0, d_0):
    return 0.5 * half_theta * t**2 + v_0 * t + d_0

# Perform curve fitting for the two ranges
popt_1, pcov_1 = curve_fit(func, t_1, theta_1)


# Generate fitted curves
fit_1 = func(t_1, *popt_1)


# Plot the fitted curves
plt.plot(t_1, fit_1, linestyle='--', color='orange', label='Fitted Curve (t <= 2.97)')


# Display correlation coefficients and fit equations
corrcoef_1 = np.corrcoef(theta_1, fit_1)[0, 1]


eq_1 = f"θ = 0.5 * {popt_1[0]:.2f} * t^2 + {popt_1[1]:.2f} * t + {popt_1[2]:.2f}\nCorrelation: {corrcoef_1:.2f}"


plt.text(3.4, -4000, eq_1, fontsize=10, color='orange')


plt.title('Data from File with Extended Fitted Curves')
plt.xlabel('t')
plt.ylabel('θ')
plt.legend()
plt.grid(True)
plt.show()
