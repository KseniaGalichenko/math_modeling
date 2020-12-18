import matplotlib.pyplot as plt
import numpy as np 

def charts(x_a=-15,x_b=15,N=0.1,a=7,b=3,radius=10,title='my_chart'):

  x = np.arange(x_a, x_b, N)
  y = np.arange(x_a, x_b, N)

  X,Y = np.meshgrid(x,y)
  fxy_1 = X**2 + Y**2
  plt.contour(X,Y,fxy_1, levels=[radius**2])
  
  fxy_2= X**2/a**2 + Y**2/b**2
  plt.contour(X,Y,fxy_2, levels=[1])
    
  plt.axis('equal')
  plt.show()
charts()