import numpy
n=int(input("Enter no of elements:"))
a=numpy.ones([n],dtype=int)
print(a)
for i in range(len(a)):
    a[i]=int(input("Enter element:"))
for j in range(len(a)):
    print(a[j])