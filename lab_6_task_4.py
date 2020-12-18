import matplotlib.pyplot as plt
import numpy as np 
from math import pi, sin, cos

def charts(k=3,title='Archimed'):
  fi = np.arange(0.01,8*pi,1)
  r = k * fi ** 0.5
  x = r * cos(fi)
  y = r * sin(fi)
  plt.plot(x,y,label = 'Archimed')
  plt.title(title)
  plt.legend()
  plt.show()
charts()
