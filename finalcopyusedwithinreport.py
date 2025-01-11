import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from matplotlib.patches import FancyArrowPatch
import pandas as pd


# Read the file and skip the first line
file_path = 'data1.txt'  
data = np.genfromtxt(file_path, delimiter='\t', skip_header=2, dtype=float)

# Convert degrees to radians
data[:, 1] = np.deg2rad(data[:, 1])

# Separate columns
t = data[:, 0]
theta = data[:, 1]

# Plotting the original data with smaller markers
plt.figure(figsize=(8, 6))
plt.plot(t, theta, marker='o', markersize=4, linestyle='-', color='#e0147c', label='Original Data')

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
plt.plot(t_1, fit_curve_1, linestyle='dotted', color='blue', label='Fitted Curve (t <= 2.49)', marker='o', markersize=1)

# Display correlation coefficients and fit equations for t <= 2.49
corrcoef_1 = np.corrcoef(theta_1, fit_curve_1)[0, 1]
eq_1 = r"$θ' = \frac{1}{2} \cdot %.2f \cdot t^2 + %.2f$" % (popt_1[0], popt_1[1]) + '\n' + r"Correlation: %.8f" % corrcoef_1
plt.text(4, -50, eq_1, fontsize=10, color='blue')

# Perform curve fitting for the second function for t > 2.5 and t <= 5.0
# Setting an angular deceleration of approximately +- 3.7763 (absolute value)
angular_deceleration = 3.7763
popt_2, pcov_2 = curve_fit(func_2, t_2, theta_2, bounds=([-angular_deceleration, -np.inf, -np.inf], [angular_deceleration, np.inf, np.inf]))

# Generate fitted curve for the second range
fit_curve_2 = func_2(t_2, *popt_2)

# Plot the fitted curve for t > 2.5 and t <= 5.0
plt.plot(t_2, fit_curve_2, linestyle='-', color='black', label='Fitted Curve (2.5 < t <= 5.0)', marker='o', markersize=1)



# Display correlation coefficients and fit equations for 2.5 < t <= 5.0
corrcoef_2 = np.corrcoef(theta_2, fit_curve_2)[0, 1]
eq_2 = r"$θ' = -\frac{1}{2} \cdot %.4f \cdot t^2 + %.2f \cdot t + %.2f$" % (abs(popt_2[0]), popt_2[1], popt_2[2]) + '\n' + r"Correlation: %.8f" % corrcoef_2
plt.text(7.5, -150, eq_2, fontsize=10, color='black')


# Calculate midpoints of the fitted curves
midpoint_1 = ((t_1[0] + t_1[-1]) / 2 + 0.5, (fit_curve_1[0] + fit_curve_1[-1]) / 2 + 0.5)
midpoint_2 = ((t_2[0] + t_2[-1]) / 2 , (fit_curve_2[0] + fit_curve_2[-1]) / 2 )

# Lines connecting midpoint of fitted curves to the displayed equation points
plt.plot([midpoint_1[0], 3.9], [midpoint_1[1], -35], linestyle='--', color='blue')
plt.plot([midpoint_2[0], 7.3], [midpoint_2[1], -135], linestyle='--', color='black')


plt.title('Data from File with Extended Fitted Curves')
plt.xlabel('t')
plt.ylabel('θ (radians)')
plt.legend()
plt.grid(True)
plt.show()

# Read the GDP data file and skip the first line
gdp_file_path = 'gdpdata.txt'  
gdp_data = pd.read_csv(gdp_file_path, delimiter='\t', skiprows=1)

# Extract relevant columns for Real and Nominal GDP
real_gdp = gdp_data['NGDPRSAXDCCAQ']
nominal_gdp = gdp_data['NGDPSAXDCCAQ']
years = gdp_data['Year']

# Plotting Real and Nominal GDP
plt.figure(figsize=(10, 6))
plt.plot(years, real_gdp, marker='o', markersize=4, linestyle='-', color='blue', label='Real GDP (NGDPRSAXDCCAQ)')
plt.plot(years, nominal_gdp, marker='o', markersize=4, linestyle='-', color='orange', label='Nominal GDP (NGDPSAXDCCAQ)')

plt.title('Real and Nominal GDP Over Time')
plt.xlabel('Year')
plt.ylabel('GDP Value')
plt.legend()
plt.grid(True)
plt.show()


