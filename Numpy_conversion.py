#conversion(Type casting)
import numpy
a=numpy.array([10,20,30,40,50])
print(a)
print(a.dtype)
#implicit conversion
b=numpy.array([60,70,80,90,100.0])
print(b)
c=numpy.array([60,70,80.5,90,100])
print(c)
#explicit conversion
d=numpy.array([3,4,5,6,8,9],dtype="float")
print(d)