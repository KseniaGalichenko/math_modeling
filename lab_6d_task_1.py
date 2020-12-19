import matplotlib.pyplot as plt
import numpy as np 
from numpy import sin, pi

def chart(a=5,b=4,A=1,B=1,title = 'Lissajous Curves'):
  t = np.arange(1,10,0.01)
  delta = pi / 2
  x = A * np.sin(a * t + delta)
  y = B * np.sin(b * t)
  plt.plot(x,y,label = 'Lissajous')
  plt.title(title)
  plt.legend()
  plt.show()
chart()
