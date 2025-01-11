import scipy
from sympy import *
from numpy import *
import scipy.integrate as integrate
import matplotlib.pyplot as plt


# constants
t = 0.01
velocity = symbols('v')
acceleration = symbols('a')
coefficient = 1.3
mass = 1.0
radius = 1.0
area = pi * radius**2
air_density = 1.293

eq = velocity**2

label = [
    "time", "velocity", "acceleration", "displacement"
]
result = [
    [0, 0, 0, 0]
]
for i in range(0, 500):
    last_entry = result[i-1]
    last_time, last_v, last_a, last_d = last_entry
    
    time = last_time + t
    velocity = last_v + last_a * t
    f_net = mass * -9.8 + (1/2)*coefficient * (velocity**2) * air_density * area
    acceleration = f_net / mass
    displacement = last_d + (last_v + 0.5 * acceleration * t) * t
    
    result.append([time, velocity, acceleration, displacement])

for a in label:
    print(a, end=', ')
print("\n")
for title in result:
    for num in title:
        print(num, end=', ')
    print("\t\n")
    
newt = [row[0] for row in result]
newd = [row[3] for row in result]
newv = [row[1] for row in result]

plt.plot(newt, newd, label='Displacement', color='blue')
plt.plot(newt, newv, label='Velocity', color='red')

plt.xlabel('Time')
plt.ylabel('Displacement / Velocity')
plt.title('Displacement and Velocity over Time')
plt.legend()
plt.grid(True)
plt.show()