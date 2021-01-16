import matplotlib.pyplot as plt
import numpy as np

def cycloid(R=2):

  t = np.arange(2,16,0.1)

  x = R * (t - np.sin (t))
  y = R * (1 - np.cos (t))

  plt.plot(x, y, ls='-', lw=3)
  plt.axis('equal')
  plt.show()

cycloid()