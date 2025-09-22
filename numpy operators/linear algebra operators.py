"""📝 Problem

Given two square matrices A and B, perform:
Matrix Multiplication, 
Dot Product (first row of A × first column of B), 
Transpose of A, Determinant of A, 
Inverse of A, Trace of A."""

import numpy as np
A=np.array([[1,2],[4,5]])
B=np.array([[6,8],[9,8]])
print(A)
print(B)
print("Matrix Multiplication:\n",np.matmul(A,B))
print("Dot Product:\n",np.dot(A[0,:], B[:,0]))
print("Transpose of A:\n",np.transpose(A))
print("Determinant of A:",np.linalg.det(A))
print("Inverse of A:\n",np.linalg.inv(A))
print("Trace of A:",np.trace(A))