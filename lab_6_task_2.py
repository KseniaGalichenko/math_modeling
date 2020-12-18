import matplotlib.pyplot as plt
import numpy as np 

def charts(x_a_1=-10,x_b_1=10,N_1=0.01,a=1,b=1,c=0,x_a_2=0,x_b_2=10,N_2=0.01,x_a_3=-10,x_b_3=0,N_3=0.01,title='my_chart'):
  
  x_1 = np.arange(x_a_1,x_b_1,N_1)
  x_2 = np.arange(x_a_2,x_b_2,N_2)
  x_3 = np.arange(x_a_3,x_b_3,N_3)
  y_1 = a*x_1**2 + b*x_1 + c
  y_2 = 1 / x_2
  y_3 = 1 / x_3
    

  plt.plot(x_1,y_1,label = 'Parabola')
  plt.plot(x_2,y_2,label = 'Giperbola')
  plt.plot(x_3,y_3,label = 'Giperbola')
  plt.title(title)
  plt.legend()
  plt.show()

charts()



  
