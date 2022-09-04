"""copy() method is used to create a copy of an existing array.If the new array get modified,the existing array will not be 
affected or vice versa.Both the arrays are independent."""
from numpy import*
a=array([11,22,33,44,55])
print("a=",a)
print("Copy of a",copy(a))
b=(copy(a))
print("b=",b)
print("a",id(a))
print("b",id(b))
print("Change variable in b,b[2]=300")
b[2]=300
print("b=",b)
print("a=",a)
print("Change variable in a,a[4]=500")
a[4]=500
print("a=",a)
print("b=",b)
print(type(a))
print(a.dtype)