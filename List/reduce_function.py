from functools import reduce
a=[1,2,3,4,5,6,7,8,9,10]
print(a)
def add(lst,lst1):
    return lst+lst1
result=reduce(add,a)
print(result)
print("Using lambda function")
lst=[11,12,13,14,15,16,17,18,19,20]
print(lst)
result=reduce(lambda m,n:m+n,lst)
print(result)