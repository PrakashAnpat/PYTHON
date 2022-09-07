# ones() function is used to create an array with all ones.
from numpy import *
a=ones(5) # bydefault dtype is float.
print(a)
b=ones(5,dtype=int) # explicit conversion
print(b)
print("accessing array using for loop: ")
for i in b :
    print(i)
print("array for loop with index: ")
for i in range(len(b)) :
    print("Index",i,"=",b[i])
c=ones((2,3),dtype=int)
print(c)
print("accessing array using for loop: ")
for i in c :
    for j in i :
        print(j)
print("array for loop with index:")
for i in range(len(c)) :
    for j in range(len(c[i])) :
        print("Index",i,j,"=",c[i][j])