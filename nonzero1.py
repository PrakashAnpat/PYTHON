''' nonzero() function is used to determine the positions of elements which are non-zero.This function returns an array that 
contains the indexses of element of the array which are not equal to zero.'''
from numpy import *
a=array([1,3,5,7,9])
print(a)
result=nonzero(a)
print(result)
print()
b=array([10,20,0,40,0,60])
print(b)
result1=nonzero(b)
print(result1)# nonzero() function do not returns index number of zero element in the array.