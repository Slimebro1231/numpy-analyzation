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

# Splitting the data into three ranges based on t values
t_1 = t[t <= 2.49]
theta_1 = theta[t <= 2.49]

t_2 = t[(t > 2.5) & (t <= 5.0)]  # New range for the second curve
theta_2 = theta[(t > 2.5) & (t <= 5.0)]

t_3 = t[t > 5.0]  # Data after t = 5.0
theta_3 = theta[t > 5.0]

# Define the functions for curve fitting

# Function for the first curve: θ' = 1/2 * (angular_acceleration) * t^2 + initial_angle
def func_1(t, angular_accel, initial_angle):
    return 0.5 * angular_accel * t**2 + initial_angle

# Function for the second curve starting at t = 2.5s: θ' = 1/2 * (angular_accel) * t^2 + initial_velocity * t + initial_angle
def func_2(t, angular_accel, initial_velocity, initial_angle):
    return -0.5 * angular_accel * t**2 + initial_velocity * t + initial_angle  # Changed sign for angular_accel for deceleration

# Perform curve fitting for the first function for t <= 2.49
popt_1, pcov_1 = curve_fit(func_1, t_1, theta_1)

# Generate fitted curve for the first range
fit_curve_1 = func_1(t_1, *popt_1)

# Plot the fitted curve for t <= 2.49
plt.plot(t_1, fit_curve_1, linestyle='--', color='orange', label='Fitted Curve (t <= 2.49)')

# Display correlation coefficients and fit equations for t <= 2.49
corrcoef_1 = np.corrcoef(theta_1, fit_curve_1)[0, 1]
eq_1 = f"θ' = 0.5 * {popt_1[0]:.2f} rad/s^2 * t^2 + {popt_1[1]:.2f} rad\nCorrelation: {corrcoef_1:.8f}"
plt.text(3.4, -4, eq_1, fontsize=10, color='orange')

# Perform curve fitting for the second function for t > 2.5 and t <= 5.0
# Setting an angular deceleration of approximately +- 3.7763 (absolute value)
angular_deceleration = 3.7763
popt_2, pcov_2 = curve_fit(func_2, t_2, theta_2, bounds=([-angular_deceleration, -np.inf, -np.inf], [angular_deceleration, np.inf, np.inf]))

# Generate fitted curve for the second range
fit_curve_2 = func_2(t_2, *popt_2)

# Plot the fitted curve for t > 2.5 and t <= 5.0
plt.plot(t_2, fit_curve_2, linestyle='--', color='green', label='Fitted Curve (2.5 < t <= 5.0)')

# Display correlation coefficients and fit equations for 2.5 < t <= 5.0
corrcoef_2 = np.corrcoef(theta_2, fit_curve_2)[0, 1]
eq_2 = f"θ' = -0.5 * {abs(popt_2[0]):.4f} rad/s^2 * t^2 + {popt_2[1]:.2f} rad/s * t + {popt_2[2]:.2f} rad\nCorrelation: {corrcoef_2:.8f}"
plt.text(3.4, -201, eq_2, fontsize=10, color='green')

plt.title('Data from File with Extended Fitted Curves')
plt.xlabel('t')
plt.ylabel('θ (radians)')
plt.legend()
plt.grid(True)
plt.show()
