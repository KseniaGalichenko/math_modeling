import matplotlib.pyplot as plt
import numpy as np 
from numpy import sqrt, sin, cos

def charts(g=4,b=1,k=1):
  '''g=1 (логарифмическая спираль),
     g=2 (архимедова спираль),
     g=3 (спираль "жезл"),
     g=4 (роза)
  '''
  if g==1:
    phi = np.arange(0, 8*np.pi, 0.01)
    r = np.exp(b * phi)
    
  elif g==2:
    phi = np.arange(0, 8*np.pi, 0.01)
    r = k * phi

  elif g==3:
    phi = np.arange(0.01, 8*np.pi, 0.01)
    r = k / np.sqrt(phi)

  elif g==4:
    phi = np.arange(0, 8*np.pi, 0.01)
    r = np.sin(k * phi)

  x = r * np.cos(phi)
  y = r * np.sin(phi) 

  plt.plot(x,y,label = 'my_chart')
  plt.show()
charts()
