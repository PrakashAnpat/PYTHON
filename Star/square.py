n=int(input("Enter number: "))
for i in range(n) :
    print("* "*n)
print()
for j in range(n) :
    print(" "*j,"* "*n," *"*j)
print()
for i in range(n):
    for j in range(n) :
        print("*",end=" ")
    print()