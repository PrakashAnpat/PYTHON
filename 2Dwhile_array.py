from numpy import*
c=array([[1,2,3,4],[5,6,7,8]])
print(c)
print("Using while loop")
i=0
while i<len(c):
    j=0
    while j<len(c[i]):
        print(c[i][j])
        j+=1
    i+=1
print("Using while loop with index")
i=0
while i<len(c):
    j=0
    while j<len(c[0]):
        print("Index:",i,j,"=",c[i][j])
        j+=1
    i+=1


