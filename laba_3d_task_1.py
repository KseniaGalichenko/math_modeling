import numpy as np
N = 3
M = 4

A = np.ndarray(shape = (N,M))
for i in range (N):
  for j in range (M):
    A[i][j] = int(input())

B = np.ndarray(shape = (N,M))
for i in range (N):
  for j in range (M):
    B[i][j] = int(input()) 

print(A)
print(B)

C = np.ndarray(shape = (N,M))
for i in range (N):
  for j in range (M):
    if A[i][j] > B[i][j]:
      C[i][j] = A[i][j]
    else:
      C[i][j] = B[i][j]

print(C)
