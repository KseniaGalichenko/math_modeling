import matplotlib.pyplot as plt
import numpy as np 
from math import sin, pi

def chart(a=5,b=4,A=1,B=1,title = 'Lissajous Curves'):
  delta = pi / 2
  x = A * sin(a  + delta)
  y = B * sin(b)
  plt.plot(x,y,label = 'Lissajous')
  plt.title(title)
  plt.legend()
  plt.show()
chart()