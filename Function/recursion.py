'''A function calling itself again & again to compute a value is referred to recursive function or recursion.'''
def show():
    a=0
    while a<=2000:
        print(a,"Show function")
        a+=1
    show()
show()