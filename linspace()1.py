# linspace() is used to create an array with evenly spaced numbers between a start & stop point.
from numpy import *
#a=linspace(1,8) # bydefault num=50, num represents no. of parts elements should be divided
#print(a)
print()
b=linspace(1,8,num=5)
print(b)
print()
c=linspace(1,8,5)
print(c)
print("using for loop")
for i in c :
    print(i)
print("for loop with index")
for i in range(len(c)) :
    print("Index",i,"=",c[i])
print("using while loop")
m=len(c)
i=0
while i<m :
    print(c[i])
    i+=1
print("using while loop with index")
i=0
while i<m :
    print("Index",i,"=",c[i])
    i+=1