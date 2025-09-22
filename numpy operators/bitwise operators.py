'''📝 Problem

Given two arrays A and B, 
perform element-wise bitwise operations:
AND (&), OR (|), XOR (^), Left Shift (<<), Right Shift (>>).

Input
5
10 20 30 40 50
2 5 10 4 25

Output
[2 4 10 0 16]    # A & B
[10 21 30 44 59]  # A | B
[8 17 20 44 43]   # A ^ B
[40 640 30720 640 1600000]  # A << B
[2 0 0 2 1]       # A >> B'''

import numpy as np
n=int(input("enter size:"))
a=np.array(list(map(int,input("enter elements of a:").split())))
b=np.array(list(map(int,input("enter elements of b:").split())))
print(a,b)
print(a&b)
print(a|b)
print(a^b)
print(a<<b)
print(a>>b)