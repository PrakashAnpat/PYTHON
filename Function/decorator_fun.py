''' A decorator function is a function that accepts a function as parameter & returns a function. A decorator takes the 
result of a function,modifies the result & returns it. In decorator's functions are taken as the argument into anoter function
& then called inside the wrapper function.
   We use @ function_name to specify a decorator to be applied on the another function. '''
def decor(fun):
    def inner():
        print("Before modifying function")
        fun()
        print("After modifying function")
    return inner
def num():
    print("We will use this function")
    print("And will enhance this in decorator")
result_fun=decor(num)
result_fun()
print(".............................")
def decor (fun):
    def inner():
        print("Before modifying")
        fun()
        print("After modifying")
    return inner
@ decor
def num():
    print("We will use this function")
    print("And will enhance this in decorator")
num()
