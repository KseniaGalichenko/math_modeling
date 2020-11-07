a = [5,6,7,10,8,4,3]
print(a[:]) 
print(a[3::2])
print(a[::3])
print(a[::])

import numpy as np
A = np.array([[1,2,3],[4,5,6]])
print(A[1,:])

print(A[:,1])

B = A[:,::-1]
print('A',A)