import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib.patches import FancyArrowPatch

# pyVIS

# Read the file and skip the first line
file_path = 'data1.txt'  
data = np.genfromtxt(file_path, delimiter='\t', skip_header=2, dtype=float)
# np.read_fromtxt(file_path, delimiter='\t', skip_header=2, dtype=float)

# Convert degrees to radians
data[:, 1] = np.deg2rad(data[:, 1])

# Separate columns
t = data[:, 0]
theta = data[:, 1]

# Plotting the original data
plt.figure(figsize=(8, 6))
plt.plot(t, theta, marker='o', markersize=4, linestyle='-', color='#e0147c', label='Original Data')


# Splitting the data
t_1 = t[t <= 2.49]
theta_1 = theta[t <= 2.49]

t_2 = t[(t > 2.5) & (t <= 4.0)]  # New range for the second curve
theta_2 = theta[(t > 2.5) & (t <= 4.0)]

# Define the functions
def func_1(t, angular_accel, initial_angle):
    return 0.5 * angular_accel * t**2 + initial_angle

def func_2(t, angular_accel, initial_velocity, initial_angle):
    return 0.5 * angular_accel * t**2 + initial_velocity * t + initial_angle  

# curve fit w bounds
angular_acceleration = -16.7813 
angular_deceleration_min = -2.8273
angular_deceleration = -3.5743
initial_angle = -48.723
popt_1, pcov_1 = curve_fit(func_1, t_1, theta_1)
popt_2, pcov_2 = curve_fit(func_2, t_2, theta_2, bounds=([angular_deceleration, -np.inf, initial_angle], [angular_deceleration_min, np.inf, -initial_angle]))

# Generate fit
fit_curve_1 = func_1(t_1, *popt_1)
fit_curve_2 = func_2(t_2, *popt_2)


# Plot
plt.plot(t_1, fit_curve_1, linestyle='dotted', color='blue', label='Fitted Curve (t <= 2.49)', marker='o', markersize=1)
plt.plot(t_2, fit_curve_2, linestyle='-', color='black', label='Fitted Curve (2.5 < t <= 4.0)', marker='o', markersize=1)


# coefficients
corrcoef_1 = np.corrcoef(theta_1, fit_curve_1)[0, 1]
corrcoef_2 = np.corrcoef(theta_2, fit_curve_2)[0, 1]

eq_1 = r"$θ' = \frac{1}{2} \cdot %.2f \cdot t^2 + %.2f$" % (popt_1[0], popt_1[1]) + '\n' + r"Correlation: %.8f" % corrcoef_1
eq_2 = r"$θ' = \frac{1}{2} \cdot %.4f \cdot t^2 + %.2f \cdot t + -%.2f$" % (abs(popt_2[0]), popt_2[1], popt_2[2]) + '\n' + r"Correlation: %.8f" % corrcoef_2


plt.text(4.2, -50, eq_1, fontsize=10, color='blue')
plt.text(7.5, -100, eq_2, fontsize=10, color='black')

midpoint_1 = ((t_1[0] + t_1[-1]) / 2 + 0.5, (fit_curve_1[0] + fit_curve_1[-1]) / 2 + 0.5)
midpoint_2 = ((t_2[0] + t_2[-1]) / 2 , (fit_curve_2[0] + fit_curve_2[-1]) / 2 )
plt.plot([midpoint_1[0], 4.1], [midpoint_1[1], -35], linestyle='--', color='blue')
plt.plot([midpoint_2[0], 7.3], [midpoint_2[1], -85], linestyle='--', color='black')
plt.grid(True, linestyle=':', color='gray')
plt.title('θt graph for disc motion')
plt.xlabel('t (seconds)')
plt.ylabel('θ (radians)')
plt.legend()
plt.grid(True)

plt.axvline(x=0, color='grey', linestyle='--', label='x=0')
plt.axvline(x=2.5, color='grey', linestyle='--', label='x=2.5')
plt.axvline(x=4, color='grey', linestyle='--', label='x=4')




plt.show()


