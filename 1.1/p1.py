# -*- coding: utf-8 -*-

import numpy as np


# Suppose A ∈ ℝ^(n × n) and x ∈ ℝ^(r) are given. Give an algorithm for
# computing the first column of M = (A − x[1]I)...(A − x[r]I)  

# Solution: A single column cannot be computed indipendently from the
# rest of the matrix. This operation cannot be decomposed into
# indipendent operations over columns

n = 4
r = 3

# A and x
A = np.arange(n*n).reshape(n, n)
x = np.arange(r)
I = np.eye(n, n)

# Compute by columns
# store te curren state of the multiplication over iterations 
D = np.zeros((n, n))   
# store last multiplication
B = I.copy()  
C = 0*I

# iterate over x elements
for k in range(r):   
    # the matrix to be multiplied with the current result of 
    # previous iterations
    E = A - x[k] * I 
    # We must comute all columns at each iteration because they are
    # all neded in the multiplication
    for j in range(n):
        C[:, j]  += np.dot(B, E[:, j])
    B = C.copy()
    print C[:,0].reshape(-1,1)

print

# Instead it can be decomposed into indpendent operations over rows

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
    # we compute only the multiplication between the desired column
    # and the k-th matrix
    c  += np.dot(b, E)
    b = c.copy()

    print c

print 

