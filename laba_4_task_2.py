import numpy as np
N = int(input())
A = np.zeros((N))
for i in range(N):
  A[i] = int(input())
print(A)

def my_func(a):
  x = np.prod(a)
  print(x)

my_func(A)
