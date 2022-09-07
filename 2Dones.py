from numpy import*
c=ones((3,4),dtype=int,order='C')
print(c)
# print(c[0])
# print(c[1])
# print(c[2])
# print(c[0][0])
# print(c[0][1])
# print(c[0][2])
# print(c[0][3])
# print(c[0][0])
# print(c[0][1])
# print(c[0][2])
# print(c[0][3])
# print(c[1][0])
# print(c[1][1])
# print(c[1][2])
# print(c[1][3])
# print(c[2][0])
# print(c[2][1])
# print(c[2][2])
# print(c[2][3])
print("Using for loop1")
for i in c:
    print(i)
print("Using for loop2")
for i in range(len(c)):
    for j in range(len(c[i])):
        print(c[i][j])
print("Using for loop with index")
for i in range(len(c)):
    for j in range(len(c[i])):
        print("Index:",i,j,"=",c[i][j])
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
    while j<len(c[i]):
        print("Index:",i,j,"=",c[i][j])
        j+=1
    i+=1
