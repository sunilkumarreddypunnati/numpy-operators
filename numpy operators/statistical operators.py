'''📝 Problem

Given an array of numbers, calculate:
Sum, Mean, Median, Standard Deviation, Variance, Minimum, Maximum.

Input
5
10 20 30 40 50

Output
150
30.0
30.0
14.142135623730951
200.0
10
50'''

import numpy as np
n=int(input("size of array:"))
arr=np.array(list(map(int,input("enter array elements:").split())))
print(arr)
print(np.sum(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.var(arr))
print(np.min(arr))
print(np.max(arr))
