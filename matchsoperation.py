# mathematical operations on arrays using numpy
import numpy
a=numpy.array([1,2,3,4,5])
print(a)
#a=a+2
a+=3
print(a)
b=numpy.array([6,7,8,9,10])
print(b)
c=a+b
print(c)
d=numpy.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print("d=",d)
e=numpy.array([[12,11,10,9,8,7],[6,5,4,3,2,1]])
print("e=",e)
f=d+e
print(f)

