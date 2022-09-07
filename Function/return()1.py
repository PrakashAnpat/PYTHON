'''Return statement can be used to return something from the function.In Python, it is possible to return one or more 
variables/values.
Syntax:- return(variable or expression) '''
def add(y):
    x=10
    c=x+y
    return c
s=add(2)
print(s)
def add(y):
    x=20
    return x+y
a=add(10)
print(a)
def add(a):
    b=20
    m=a+b
    n=a-b
    return m,n
A,S=add(10)
print("Addition:",A)
print("Substraction:",S)
def opr(x,y):
    d=x-y
    e=x+y
    return d,e,50
S,A,k=opr(20,10)
print(S)
print(A)
print(k)