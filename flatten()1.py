'''flatten() method is used to convert 2D or 3D array to 1D array.
Syntax:-array_name.flatten()'''
import numpy
a=numpy.array([[[[10,20],[30,40]],[[50,60],[70,80]]],[[[90,100],[110,120]],[[130,140],[150,160]]]])
print("4D array")
print(a)
b=a.flatten() 
print(b)
c=numpy.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("3D array")
print(c)
print(c.flatten())
d=numpy.array([[2,4,6],[3,6,9]])
print("2D array")
print(d.flatten())