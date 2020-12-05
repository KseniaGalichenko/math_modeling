import numpy as np
def my_func(a=-1,b=1):
  x = np.arange(a,b,0.1)
  y = x ** 2
  print(y)
my_func(-1, 1)


