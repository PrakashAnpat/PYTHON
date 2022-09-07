# logspace() function is used to create an array with evenly spaced numbers logarithmically.
# The sequence start at base ** start(base to the power of start) & ends with base ** stop.
import numpy
'''a=numpy.logspace(1,3) # by default num=50 & base=10.0
print(a)
print()'''
b=numpy.logspace(1,3,5)
print(b)
print()
c=numpy.logspace(1,3,num=5,base=12)
print(c)
print("Access using for loop")
for i in c :
    print(i)
print("for loop with index")
for i in range(len(c)) :
    print("Index",i,"=",c[i])
print("Access using while loop")
n=len(c)
i=0
while i<n :
    print(c[i])
    i+=1
print("while loop with index")
i=0
while i<n :
    print("Index",i,"=",c[i])
    i+=1