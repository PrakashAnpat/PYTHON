'''where() function is used to create a new array which contains, returned element choosen from expression1 or expression2 depending 
on condition.If condition is True expression1 is executed else expression2.'''
from array import array
from numpy import*
a=array([100,200,300,40,5])
b=array([100,20,30,60,50])
print(a)
print(b)
result=(where(a>b,a,b))
print(result)
result2=(where(a<b,a,b))
print(result2)