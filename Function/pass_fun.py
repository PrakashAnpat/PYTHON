'''We can pass a function as parameter to another function.'''
def disp(sh):
    print("Disp function "+sh())
def show():
    return "Show function"
disp(show)
print()
def disp(sh):
    return "Disp function "+sh()
def show():
    return "Show function"
a=disp(show)
print(a)