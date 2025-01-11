from sympy import *

x = symbols('x')
u = Function('u')(x)

u = sqrt(x)

y = (u**3) - 5*(u**3-7*u)**2
init_printing(use_unicode=True)

derivative = Derivative(y, x).doit()

print("Derivative:", derivative)
print("Derivative at x=4:", derivative.subs(x, 4))
