from numpy import*
a=zeros((2,4),dtype=int)
print(a)
# print(".........")
# print(a[0])
# print(a[1])
# print(".........")
# print(a[0][0])
# print(a[0][1])
# print(a[0][2])
# print(a[0][3])
# print(a[1][0])
# print(a[1][1])
# print(a[1][2])
# print(a[1][3])
print("Using for loop1")
for i in a:
    print(i)
print("Using for loop2")
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])
print("Using for loop with index")
for i in range(len(a)):
    for j in range(len(a[i])):
        print("Index:",i,j,"=",a[i][j])
print("Using while loop")
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j])
        j+=1
    i+=1
print("Using while loop with index")
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print("Index:",i,j,"=",a[i][j])
        j+=1
    i+=1

