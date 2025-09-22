'''📝 Task: Unique & Set Ops
Problem
Given:

A = [1,2,3,4,5,6,2,4]  
B = [4,5,6,7,8,9,4,7]

Do the following:
Unique elements of A,Unique elements of B

Intersection of A & B,Union of A & B

Elements in A not in B,Elements in B not in A

Symmetric difference (A ^ B)

Check membership of [2,7,10] in A'''

import numpy as np
A=np.array([1,2,3,4,5,6,2,4])
B=np.array([4,5,6,7,8,9,4,7])
print("Unique elements of A:\n",np.unique(A))
print("Unique elements of b:\n",np.unique(B))
print("Intersection of A & B:\n",np.intersect1d(A,B))
print("Union of A & B:\n",np.union1d(A,B))
print("Elements in A not in B:\n",np.setdiff1d(A,B))
print("Elements in B not in A:\n",np.setdiff1d(B,A))
print("Symmetric difference (A ^ B):\n",np.setxor1d(B,A))
print("Check membership of [2,7,10] in A:\n",np.isin([2,7,10],A))