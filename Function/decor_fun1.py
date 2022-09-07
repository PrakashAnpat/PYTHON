def decor(fun):
    def inner():
        a=fun()
        add=a+5
        return add
    return inner
@ decor
def num():
    return 10
print(num())
print(".............................")
def decor(fun):
    def inner():
        a=fun()
        add=a+5
        return add
    return inner
def num():
    return 10
st=decor(num)
print(st())