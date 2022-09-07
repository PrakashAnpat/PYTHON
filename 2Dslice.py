'''Slicing on arrays can be used to retrive a piece of the array that contains a group of elements.Slicing is useful to 
retrive a range of elements.
                                        Row                 Column
Synatx:- new_array_name = array_name[start:stop:step_size,start:stop:step_size]'''
import numpy
a=numpy.array([[2,4,6,8,10],[12,14,16,18,20]])
print(a)
b=a[0:2,1:4:2]
print(b)
c=a[0:2,1:3]
print(c)
d=a[0:2,0:5:2]
print(d)
print("......................")
m=numpy.array([[[2,4,6,8,10],[12,14,16,18,20]],[[3,6,9,12,15],[18,21,24,27,30]]])
print(m)
print("......................")
n=m[0:2,0:2,0:5:2]
print(n)
print("......................")
p=m[0:2,0:1,0:3]
print(p)
print("......................")
q=m[:,:,0:5:2]
print(q)