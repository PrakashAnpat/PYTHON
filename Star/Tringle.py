n=(int(input("Enter number you want to it: ")))
for i in range(n):
#    if i==0:
#        continue
    for c in range(i):
       print("*",end=" ")
    print()
print("In reverse: ")
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()

