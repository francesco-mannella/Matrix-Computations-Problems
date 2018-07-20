# -*- coding: utf-8 -*-

import numpy as np


# Suppose A ∈ ℝ^(n × n) and x ∈ ℝ^(r) are given. Give an algorithm for computing
# the first column of M = (A − x₁I)...(A − xrI)  

# Solution: A single column cannot be computed indipendently from the rest of
# the matrix. This operation cannot be decompose into indipendent operations
# over columns




n = 4
r = 3

# A and x
A = np.arange(n*n).reshape(n, n)
x = np.arange(r)
I = np.eye(n, n)


# Compute by columns
# We must comute all columns at each iteration because they are all neded in the
# multiplication

# store te curren state of the multiplication over iterations 
D = np.zeros((n, n))   
# store last multiplication
B = I.copy()  

C = 0*I
B = I.copy()
# iterate over x elements
for k in range(r):   
    # the matrix to be multiplied with the current result of 
    # previous iterations
    E = A - x[k] * I 
    # storage for the current multiplication
    for j in range(n):
        C[:, j]  += np.dot(B, E[:, j])
    B = C.copy()
    print C[:,0].reshape(-1,1)

print

# Compute by rows

# initial value of the desired row 
b = I[0]
# store desired row over iterations
c = 0*I[0]

# iterate over x elements
for k in range(r):   
    # the matrix to be multiplied with the current result of 
    # previous iterations
    E = A - x[k] * I 
    # storage for the current multiplication
    c  += np.dot(b, E)
    b = c.copy()

    print c

print 

