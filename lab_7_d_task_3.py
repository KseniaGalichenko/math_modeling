import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
	
fig, ax = plt.subplots()
anim_object, = plt.plot([], [], '-', lw=2)
	
xdata, ydata = [], []
	
ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)
t = np.arange(0,4*np.pi,0.1)
x1 = (12 * np.cos(t) + 8 * np.cos(1.5 * t))
y1 = (12 * np.sin(t) - 8 * np.sin(1.5 * t))
	
def update(frame):
	xdata = x1 * np.cos(frame) - y1 * np.sin(frame)
	ydata = y1 * np.cos(frame) + x1 * np.sin(frame)
	anim_object.set_data(xdata, ydata) 
	

ani = FuncAnimation(fig,
                    update,
                    frames=np.arange(0, 4*np.pi,0.1), 
                    interval=100
                    )            

ani.save('star.gif')