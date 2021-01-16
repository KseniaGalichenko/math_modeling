import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
 
fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='cyan', label='Ball')
 
def circle_move(R,ang_vel,phi,time):
  alpha = ang_vel * (np.pi/180) * time
  R = alpha * time
  x = R*np.cos(phi)
  y = R*np.sin(phi)
  return x,y

edge = 50
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
  ball.set_data(circle_move(R=5, phi = np.arange(0,2*np.pi,0.01),ang_vel=3, time=i))
    
ani = animation.FuncAnimation(fig,
                              animate,
                              frames=100,
                              interval=50
                              )

ani.save('lec_7_circle.gif')

  