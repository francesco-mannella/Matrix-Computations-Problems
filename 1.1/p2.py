# -*- coding: utf-8 -*-

import numpy as np
from itertools import permutations

# Given the 2D matrix C = A*B
# Compute the order of the 8 multiplications in a 2D matrix
# given ijk, jik, kij, ikj, and kji multiplication algorithms. 


n = 2 # Each dimension of the 2D matrix is of length n

# Compute the default sequence of multiplications
t = np.arange(n)
I, J, K = np.meshgrid(t, t, t)
idcs = [I.ravel(), K.ravel(), J.ravel()]
default_idcs = np.vstack((idcs[0], idcs[1], idcs[2])).T

# Names of the 6 algoritms
algorithm_perms = np.array(list(permutations([0, 1, 2])))
algorithm_indices = ["i","j","k"]

# Names of the 8 multiplications
multiplications_names = []
for curr_idcs in default_idcs:
    i, j, k = curr_idcs + 1
    multiplications_names.append("a[{}{}]*b[{}{}] ".format(i,k,k,j))

#compute the sequences of the 6 algorithms by comparing them with the 
# standard sequence
seqs = []
for (n1, n2, n3) in algorithm_perms:
    
    # Compute the sequence of multiplications given the current algorithm
    curr = np.vstack((idcs[n1], idcs[n2], idcs[n3])).T
    # Get the order of the multiplications in the current sequence by comaring it with
    # the default sequence
    seq = [np.argwhere(np.all(default_idcs == r, axis=1)).ravel()[0] 
            for r in curr]
    seqs.append(seq)

# print hte table
nidcs = len(default_idcs)
print
print "          " + "  ".join(multiplications_names)
print
for i,p in enumerate(algorithm_perms):
    print "{}{}{}     ".format(
            algorithm_indices[p[0]], 
            algorithm_indices[p[1]], 
            algorithm_indices[p[2]]) + \
            ("  {}           "*nidcs).format(*seqs[i])
