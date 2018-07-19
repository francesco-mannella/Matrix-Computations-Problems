import numpy as np


n = 4
r = 3

A = np.arange(n*n).reshape(n, n)
x = np.arange(r)
I = np.eye(n, n)

def get_mat(M, s): return M -s*I

D = np.zeros((n, n))

B = I.copy()
for h in range(r):   
    E = A - x[h] * I
    C = np.zeros((n, n))
    for j in range(n):
        C[:, j]  += np.dot(B, E[:, j])
    B = C.copy()
    D += B 
    print C[:, 0]

