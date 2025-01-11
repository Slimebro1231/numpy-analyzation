import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Read the file and skip the first line
file_path = 'data1.txt'  # Replace 'your_file.txt' with the actual file name
data = np.genfromtxt(file_path, delimiter='\t', skip_header=2, dtype=float)

# Convert degrees to radians
data[:, 1] = np.deg2rad(data[:, 1])

# Separate columns
t = data[:, 0]
theta = data[:, 1]

# Plotting the original data with smaller markers
plt.figure(figsize=(8, 6))
plt.plot(t, theta, marker='o', markersize=4, linestyle='-', color='b', label='Original Data')

# Splitting the data into two ranges based on t values
t_1 = t[t <= 2.49]
theta_1 = theta[t <= 2.49]

# Define the function to fit the curve: theta' = 1/2 * (angular_acceleration) * t^2 + initial_angle
def func(t, angular_accel, initial_angle):
    return 0.5 * angular_accel * t**2 + initial_angle

# Perform curve fitting for the function θ' = 1/2 * (angular_acceleration) * t^2 + initial_angle
popt, pcov = curve_fit(func, t_1, theta_1)

# Generate fitted curve
fit_curve = func(t_1, *popt)

# Plot the fitted curve for t <= 2.49
plt.plot(t_1, fit_curve, linestyle='--', color='orange', label='Fitted Curve (t <= 2.49)')

# Display correlation coefficients and fit equations for t <= 2.49
corrcoef = np.corrcoef(theta_1, fit_curve)[0, 1]
eq = f"θ' = 0.5 * {popt[0]:.2f} rad/s^2 * t^2 + {popt[1]:.2f} rad\nCorrelation: {corrcoef:.8f}"
plt.text(3.4, -4, eq, fontsize=10, color='orange')

plt.title('Data from File with Extended Fitted Curve')
plt.xlabel('t')
plt.ylabel('θ (radians)')
plt.legend()
plt.grid(True)
plt.show()
