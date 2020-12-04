import numpy as np
from math import sin
N = int(input())
M = int(input())
A = np.zeros((N,M))
for i in range(N):
  for j in range(M):
    if i == 0 and j == 0:
      A[i][j] = sin(N*(i + 1) + M*(j + 1))
    else:
      A[i][j] = sin(N * i + M * j)
    
    if A[i][j] < 0:
       A[i][j] = 0
print(A)

B = np.zeros(N)
a = int(input())
b = int(input())
for i in range(N):
  B[i] = A[i][a-1]
  A[i][a-1] = A[i][b-1]
  A[i][b-1] = B[i]
print(A)


