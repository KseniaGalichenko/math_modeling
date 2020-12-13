import matplotlib.pyplot as plt
import numpy as np 

def charts(g=1,x_a=0,x_b=10,N=0.1,a=1,b=1,c=0,title='my_chart'):
  ''' g - график(1 - парабола (на входе нужно указать коэффициенты уравнения параболы), 2 - гипербола)
  '''
  x = np.arange(x_a,x_b,N)
  if g == 1:
    y = a*x**2 + b*x + c
  elif g == 2:
    y = 1 / x
    

  plt.plot(x,y,label = 'My_chart')
  plt.title(title)
  plt.legend()
  plt.show()

charts(g=1)




  
