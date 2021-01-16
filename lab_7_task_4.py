import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
 
fig, ax = plt.subplots()
 
anim_object, = plt.plot([], [], 'o', color='r', lw=4)
xdata, ydata = [], []


ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

x0 = 0.1
y0 = 0.1
C = 0.3
D = 0.33
x = [x0]
y = [y0]

def update(i):
  x.append(x[i] **2 - y[i] ** 2 + C)
  y.append(2 * x[i] * y[i] + D)

  anim_object.set_data(xdata, ydata)

  anim_object.set_data(x,y)

ani = FuncAnimation(fig, 
                    update,
                    frames = 100, 
                    interval = 100
                    )            

ani.save('lab_7_points.gif')