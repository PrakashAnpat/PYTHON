a=[1,2,3,4,5,6,7,8,9,10]
print(a)
def opr(lst):
    add=lst+2
    #print(add)
    return add 
result=map(opr,a)
print(result)
print(list(result))
print()
b=[2,4,6,8,10]
print(b)
def opr1(lst):
    return lst*2
result=list(map(opr1,b))
print(result)
for i in result:
    print(i)
print("Using lambda function")
c=[2,3,4,5,6]
result=list(map((lambda n: n**2),c))
print(result)
for i in result:
    print(i)
print()
m=[10,20,30,40,50]
n=[5,10,15,20,25]
print(m)
print(n)
result=list(map((lambda a,b:a+b), m,n))
print(result)