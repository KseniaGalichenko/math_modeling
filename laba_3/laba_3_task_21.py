from numpy import pi
from numpy import tan
from numpy import cos
from my_module_constants import acceleration_of_gravity as g 
h = 100
alpha = pi / 3
beta = 30 * (pi / 180)
V = ((g * h * tan(beta) ** 2) / ((2 * cos(alpha) ** 2) * (1 - tan(beta) * tan(alpha)))) ** 0.5
print(V)