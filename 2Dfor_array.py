import numpy
a=numpy.array([[10,20,30,40],[50,60,70,80]])
print(a)
print("Modify elements")
a[0][0]=90
a[1][0]=100
print(a)
print("Using for loop")
for b in a:
    for c in b:
        print(c)
print("Using for loop with index")
for i in range(len(a)):
    for j in range(len(a[i])):
        print("index:",i,j,"=",a[i][j])
