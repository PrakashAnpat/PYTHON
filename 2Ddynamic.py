from numpy import*
m=int(input("Enter number of rows: "))
n=int(input("Enter number of columns: "))
a=zeros((m,n),dtype=int)
print(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j]=input("Enter elements: ")
print(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        print("Index:",i,j,"=",a[i][j])
print("Another type of print")
for i in a:
    for j in i:
        print(j)