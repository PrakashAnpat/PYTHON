'''reshape() function is used to change the shape of array.We can convert 1D to 2D or 3D array & vice versa.The new array 
should have the same number of elements as in the original array.
Syntax:- reshape(array_name,(n,r,c))'''
from numpy import*
c=array([1,2,3,4,5,6,7,8,9,10])
print(type(c))
print(c)
print("Convert 1D t0 2D")
print(reshape(c,(2,5)))
print(reshape(c,(5,2)))
d=array([2,4,6,8,10,12,14,16,18,20,22,24])
print(d)
print("1D to 3D")
print(reshape(d,(2,2,3)))
e=array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(e)
print("3D to 2D")
print(reshape(e,(2,6)))
print("3D to 1D")
print(reshape(e,(12)))
f=array([3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48])
print(f)
print("1D to 4D")
print(reshape(f,(4,2,2)))


