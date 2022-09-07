from array import*
def sun(b):
    print("Passing array to a function")
    print(b)
    print(type(a))
    for i in b:
        print(i)
def sun1(d):
    print("Return array to a function")
    print(d)
    print(type(d))
    for i in d:
        print(i)
    return d
a=array("i",[1,2,3,4,5])
sun(a)
m=sun1(a)
print("Return array:",m)
print("........Numpy array.........")
def fun(arr):
    print("Passing array to a function")
    print(arr)
    print(type(arr))
def fun1(arr):
    print("Return array to a function")
    return arr
from numpy import*
c=array([2,4,6,8,10])
fun(c)
result=fun1(c)
print("Returning array:",result)