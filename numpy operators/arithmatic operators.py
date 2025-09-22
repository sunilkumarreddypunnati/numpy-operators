'''📝 Problem

Given two arrays A and B, perform element-wise:
Addition, Subtraction, Multiplication, Division, Modulus, Power, and Floor Division.

Input
5
10 20 30 40 50
2 5 10 4 25

Output
[12 25 40 44 75]
[ 8 15 20 36 25]
[ 20 100 300 160 1250]
[ 5.  4.  3. 10.  2.]
[0 0 0 0 0]
[100 3200000 59049 256 9765625]
[5 4 3 10 2]'''

import numpy as np
n=int(input("enter size of array:"))
a=np.array(list(map(int,input("enter array elements of a:").split())))
b=np.array(list(map(int,input("enter array elements of b:").split())))

print("addition:",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)
print("modulus:",a%b)
print("power:","",a**b)
print("floor division :",a//b)