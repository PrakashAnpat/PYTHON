# Aliasing array-aliasing means giving another name to the existing object.It doesn't mean copying.
from numpy import*
a=array([11,22,33,44,55])
b=a #aliasing array
print(a,id(a))
print(b,id(b))