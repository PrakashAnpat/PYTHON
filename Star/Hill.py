n=int(input("Enter Number: "))
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    for l in range(i):
        print("*",end=" ")
    print()
print("  ....In Reverse....")
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    for k in range(i,n-1):
        print("*",end=" ")
    print()