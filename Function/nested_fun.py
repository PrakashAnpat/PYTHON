'''When we define one function inside another function,it is known as Nested function or Function nesting.'''
def disp():
    def show():
        print("Show function")
    print("Disp function")
    show()
disp()
print()
def disp():
    def show():
        return "Show function "
    result=show()+"Disp function "
    return result
a=disp()
print(a)
print()
def disp(y):
    def show():
        return "show function "
    result=show()+y+" Disp function"
    return result
a=disp("Prakash")
print(a)