import numpy as np
from math import sin
N = int(input())
M = int(input())
A = np.zeros((N,M))
for i in range(N):
  for j in range(M):
    A[i][j] = sin(N*(i + 1) + M*(j + 1))
    if A[i][j] < 0:
      A[i][j] = 0
B = np.zeros(N)
a = int(input())
b = int(input())
for i in range(N):
  B[i] = A[i][b-1]
  A[i][a-1] = A[i][b-1]
  A[i][b-1] = B[i]
print(A)
