n=int(input("Enter any number: "))
for i in range(n):
    for j in range(i):
        print(i,end=" ")
    print()
print("....In reverse....")
for i in range(n):
    if i==0:
        continue
    for j in range(i,n):
        c=n-i
        print(c,end=" ")
    print()