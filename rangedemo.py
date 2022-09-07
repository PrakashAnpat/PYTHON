a=range(5)# default start value is 0.
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
b=range(1,5)
print(b)
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print()
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print("range accessing using for loop")
for i in b :
    print(i)
print("for loop with index")
for j in range(len(b)) :
    print("Index",j,"=",b[j])

# their is no such use of range() function in while loop statement.


