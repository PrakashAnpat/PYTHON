# zeros() function is used to create an array with all zeros.
import numpy
a=numpy.zeros(5) # by default dtype is float.
print(a)
b=numpy.zeros(5,dtype=int)
print(b)
c=numpy.zeros((3,2),dtype=int)
print(c)
d=numpy.zeros((3,3))
print(d)
print("Accessing array using for loop: ")
for i in d :
    print(i)
print("for loop with index for row : ")
for j in range(len(d)) :
    print("Index",j,"=",d[j])
print("for loop with index for row & column :")
for j in range(len(d)) :
    print(j)
    for k in range(len(d[j])) :
        print("Index",j,k,"=",d[j][k])

print("end of the program")
