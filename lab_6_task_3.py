import matplotlib.pyplot as plt
import numpy as np 

def charts(g=2,x_a=-15,x_b=15,N=0.1,a=7,b=3,radius=10,title='my_chart'):
  ''' g - фигура, график которой нужно построить(1 - окружность  (на входе нужно указать радиус), 2 - эллипс(на входу нужно указать коэффециенты уравнения эллипса(а>b)))
  '''
  x = np.arange(x_a, x_b, N)
  y = np.arange(x_a, x_b, N)

  X,Y = np.meshgrid(x,y)

  if g==1:
    fxy = X**2 + Y**2
    plt.contour(X,Y,fxy, levels=[radius**2])
  elif g==2:
    fxy= X**2/a**2 + Y**2/b**2
    plt.contour(X,Y,fxy, levels=[1])
    
  plt.axis('equal')
  plt.show()
charts()