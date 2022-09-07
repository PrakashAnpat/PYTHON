# all() function returns True ,if all elements of the iterable are True or iterable is empty.
from array import array
from numpy import *
a=array([11,22,33,44,55])
print(a)
b=array([11,22,33,44,55])
print(b)
print()
c=a==b
print(c)
print()
print(all(c))
e=array([1,2,3,4,5])
f=array([])
print(e)
print(f)
print()
g=e==f
print(g)
print()
print(all(g))
h=array([10,20,30,40,50])
i=array([10,23,30,45,78])
print()
print(h)
print(i)
print()
j=h==i
print(j)
print(all(j))