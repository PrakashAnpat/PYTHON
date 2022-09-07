a=[10,50,60,80,90,5,45,65]
def high_marks(n):
    if n>= 60:
        return True
b=filter(high_marks,a)
print(b)
for i in b:
    print(i)
print()
b=[1,2,3,4,5,6,7,8,9,10]
def marks(n):
    if n>=5:    
        return True
result=filter(marks,b)
print(list(result))
for i in result:
    print(i)
print("Using lambda function")
c=[10,50,60,80,90,5,45,65]
result=list(filter((lambda n: n<=60),c))
print(result)
for i in result:
    print(i)