import matplotlib.pyplot as plt
import numpy as np

def astroid(R=2):
  t = np.arange(2,10,0.1)

  x = R * (np.cos (t)) ** 3
  y = R * (np.sin (t)) ** 3

  plt.plot(x, y, ls='-', lw=3)
  plt.axis('equal')
  plt.show()

astroid()