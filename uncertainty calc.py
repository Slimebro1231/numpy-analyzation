import math

# Constants and their uncertainties
m = 0.1004  # kg
uncertainty_m = 0.0005  # kg

a = 0.0074  # kg
uncertainty_a = 0.0005  # kg

b = 0.0186  # kg
uncertainty_b = 0.00005  # kg

ri = 0.0030  # m
uncertainty_ri = 0.00005  # m

ro = 0.1270  # m
uncertainty_ro = 0.00005  # m

g = 9.81  # m/s^2

def calculate_ic(m, a, b, ri, ro, g):
    ic = 0.5 * a * ri**2 + 0.5 * b * ro**2
    return ic
def calculate_wdot(m, a, b, ri, ro, g):
    ic = calculate_ic(m, a, b, ri, ro, g)
    wdot = (-m * g * ri) / (m * ri**2 + ic)
    return wdot

wdot_nominal = calculate_wdot(m, a, b, ri, ro, g)
print("wdot without uncertainty:", wdot_nominal)

constants = {'m': (m, uncertainty_m), 'a': (a, uncertainty_a), 'b': (b, uncertainty_b), 'ri': (ri, uncertainty_ri), 'ro': (ro, uncertainty_ro)}

for constant, (value, uncertainty) in constants.items():
    if constant == 'm':
        m_uncertain = value + uncertainty
        wdot_m_uncertain = calculate_wdot(m_uncertain, a, b, ri, ro, g)
        delta_wdot = abs(wdot_nominal - wdot_m_uncertain)
    elif constant == 'a':
        a_uncertain = value + uncertainty
        wdot_a_uncertain = calculate_wdot(m, a_uncertain, b, ri, ro, g)
        delta_wdot = abs(wdot_nominal - wdot_a_uncertain)
    elif constant == 'b':
        b_uncertain = value + uncertainty
        wdot_b_uncertain = calculate_wdot(m, a, b_uncertain, ri, ro, g)
        delta_wdot = abs(wdot_nominal - wdot_b_uncertain)
    elif constant == 'ri':
        ri_uncertain = value + uncertainty
        wdot_ri_uncertain = calculate_wdot(m, a, b, ri_uncertain, ro, g)
        delta_wdot = abs(wdot_nominal - wdot_ri_uncertain)
    elif constant == 'ro':
        ro_uncertain = value + uncertainty
        wdot_ro_uncertain = calculate_wdot(m, a, b, ri, ro_uncertain, g)
        delta_wdot = abs(wdot_nominal - wdot_ro_uncertain)
    
    print(f"{constant} uncertainty:", delta_wdot)
    