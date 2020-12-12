import matplotlib.pyplot as plt
import numpy as np 

def parabola_plotter(a=1,b=1,c=0,title='parabola_plotter'):
  '''
    рисователь парабол общего вида
    на входе нужно указать коэффециенты уравнения параболы
  '''
  x = np.arange(-10,10,0.01)
  y = a*x**2 + b*x + c

  plt.plot(x,y,label='my_parabola')
  
  plt.title(title)
  
  plt.show()
parabola_plotter()