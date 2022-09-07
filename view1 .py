'''view() method is used to construct a new view of array with same data of existing array.This existing array & new array will 
share different memory locations.
    If the new array get modified, the existing array will also be modified as the elements in both the array's will be like
mirror image.'''
import numpy
a=numpy.array([10,20,30,40,50])
print("a=",a)
print()
print("view of a",a.view())
print()
b=a.view()
print("b=",b) 
print("a",id(a))
print("b",id(b))
print("Change variable in array a,a[0]")
a[0]=200
print("a=",a)
print("b=",b)
print(  )
print("a",id(a))
print("b",id(b))
print("Change variable in array b,b[1]")
b[1]=100
print("b=",b)
print("a=",a)