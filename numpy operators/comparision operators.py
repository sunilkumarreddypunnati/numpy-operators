'''📝 Problem

Given two arrays A and B, perform element-wise comparison using NumPy:
Greater than (>), Less than (<), 
Greater than or equal (>=), 
Less than or equal (<=), 
Equal (==), Not equal (!=).'''

import numpy as np
A=np.array(list(map(int,input("enter elements of A:").split())))
B=np.array(list(map(int,input("enter elements of B:").split())))
print(A<B)
print(A>B)
print(A<=B)
print(A>=B)
print(A==B)
print(A!=B)