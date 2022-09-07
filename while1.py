import numpy
b=numpy.array([9,8,7,6,5,4,3,2,1])
# without index number
n=len(b)
print(n)
print()
i=0
while i<n :
    print(b[i])
    i+=1
# with index number
i=0
while i<n :
    print("Index",i,"=",b[i])
    i+=1