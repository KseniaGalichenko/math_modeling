from numpy import pi
from my_module_constants import Boltzmann_constant as k
from my_module_constants import Euler_number as e
from my_module_constants import Planck_constant as h
T = 200
E = 300
N = (2 / pi ** 0.5) * (h / ((k * T) ** (1.5))) * e ** ((-E) / k * T) * E ** (T / 2)
print(N)