'''globals() function returns a table of current global variables in the form of dictionary.'''
a=50       # global variable
def show():
    a=10   # local variable
    print("Local variable A:",a)
    x=globals()['a']
    print("X:",x)
    print(type(x))
show()
print("Global variable A:",a)
print()
#a=60
def show():
    a=20
    print("Local variable A:",a)
    x=globals()["a"]
    print("X:",x)
    x=40
    print("X:",x)
show()
print("Global variable:",a)