from constants import acceleration_of_gravity as g

def my_func(m,H,V):
  X = (m * V **2 /2) + (m * g * H)
  print(X)

my_func(10,5,15)