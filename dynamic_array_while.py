from numpy import*
n=int(input("Enter number of elements:"))
a=zeros(n,dtype=int)
print(a)
i=0
while i<len(a):
    a[i]=int(input("Enter elements:"))
#    x=int(input("Enter elements:"))
#    a[i]=x
    i+=1
j=0
while j<len(a):
    print(a[j])
    j+=1