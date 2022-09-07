# def decor(fun):
#     def inner():
#         a=fun()
#         mul=a*5
#         return mul
#     return inner
# def decor1(fun):
#     def inner():
#         b=fun()
#         add=b+5
#         return add
#     return inner
# def num():
#     return 10
# result=decor1(decor(num))
# print(result())
# print()
def decor(fun):
    def inner():
        a=fun()
        mul=a*5
#        print(mul)
        return mul
    return inner
def decor1(fun):
    def inner():
        b=fun()
#        print(b)
        add=b+5
#        print(add)
        return add
    return inner    
@ decor1
@ decor 
def num():
    return 10
print(num())