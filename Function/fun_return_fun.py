'''A function can return another function.'''
def disp():
    def show():
        return "Show function"
    print("Disp function")
    return show
a=disp()
print(a())
print()
def disp(sh):
    print("Disp function")
    return sh
def show():
    return "Show function"
a=disp(show)
print(a())