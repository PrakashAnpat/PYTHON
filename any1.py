#any() function returns True if any one element of iterable is True.If iterable is empty then returns False.
import numpy
a=numpy.array([10,20,30,40,50])
b=numpy.array([1,2,3,4,50])
c=a==b
print(c)
print()
d=any(c)
print(d)
print()
e=numpy.array([100,200,300,400,500])
f=numpy.array([10,20,30,40,50])
g=e==f
print(g)
print()
print(any(g))
