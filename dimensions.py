from array import array
from numpy import *
a=array([[1,2,3],[4,5,6]])
print(a)
print(a.ndim)#This attribute represents the number of dimensions or axis of the array.The no. of dimensions is also referred as Rank.
print(a.shape)#This attribute represents the shape of an array.'''
print(a.size)#This attribute represents the total no of elements in the array.'''
print(a.itemsize)#This attribute represents the memory size of the array element in bytes.'''
print(a.nbytes)#This attribute represents the total no of bytes occupied by an array.'''
print(a.dtype)#'This attribute represents the datatype of elements in the array.'''
print(".................")
b=array([[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
print(b)
print(b.ndim)
print(b.shape)
print(b.size)
print(b.itemsize)
print(b.nbytes)
print(b.dtype)
print(".................")
c=array([[[[10,20],[30,40]],[[50,60],[70,80]]],[[[100,200],[300,400]],[[500,600],[700,800]]]])
print(c)
print(c.ndim)
print(c.shape)
print(c.size)
print(c.itemsize)
print(c.nbytes)
print(c.dtype)