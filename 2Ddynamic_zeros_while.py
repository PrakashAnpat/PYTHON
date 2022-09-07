import numpy
m=int(input("Enter no of rows: "))
n=int(input("Enter no of columns: "))
a=numpy.zeros((m,n),dtype=int)
print(a)
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        x=int(input("Enter element: "))
        a[i][j]=x
        j+=1
    i+=1
print(a)
i=0
while i <len(a):
    j=0
    while j<len(a[i]):
        print("Index: ",i,j,"=",a[i][j])
        j+=1
    i+=1