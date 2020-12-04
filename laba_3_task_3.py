import numpy as np
from numpy import pi, cos, sin
from my_module_constants import acceleration_of_gravity as g
x_0 = 0
y_0 = 0
V_0 = 15
alpha = 30 * (pi / 180)
t = np.linspace(0,5,100)
x = x_0 + V_0 * cos(alpha) * t
y = y_0 + V_0 * sin(alpha) * t - ((g * t **2) / 2)
A = np.ndarray(shape=(100, 3))
for i in range(100):
  A[i,0] = t[i]
  A[i,1] = x[i]
  A[i,2] = y[i]
print(A)