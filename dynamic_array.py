import numpy
n=int(input("Enter number of elements:"))
a=numpy.zeros(n,dtype=int)
print(a)
for i in range(len(a)):
    x=int(input("Enter element:"))
    a[i]=x
for j in range(len(a)):
    print(a[j])