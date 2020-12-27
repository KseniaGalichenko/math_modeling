import matplotlib.pyplot as plt
import numpy as np 
from numpy import pi, cos

def chart(a=10,b=5,p=2,eccentricity=0.9):
  phi = np.arange(0, 8*np.pi, 0.01 )
  
  
  r = p / (1 + eccentricity * np.cos(phi))

  x = r * np.cos(phi)
  y = r * np.sin(phi)
  
  plt.plot(x,y,label = 'my_chart')
  plt.show()
  

chart()
