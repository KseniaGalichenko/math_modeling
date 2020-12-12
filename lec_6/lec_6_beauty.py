import matplotlib.pyplot as plt
import numpy as np 

x = [3,4,5]
y = [40,10,30]
plt.plot(x,y,color='g', label='luchte' , marker='>', ms=5)
#украшательства

plt.xlabel('Coord:x')#подпись оси Ох
plt.ylabel('Coord:y')#подпись оси Оу
plt.legend()
plt.title('Base')
plt.grid()
plt.show()