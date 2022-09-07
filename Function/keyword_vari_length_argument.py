'''Keyword Variable length Argument is an argument that can accept any no of values provided in the
form of key-value pair.The keyword variable length argument is written with ** symbol.It stores all
the value in a dictionary in the form of key-value pair.'''
def add(**no):
    s=no["a"]+no["b"]+no["c"]
    print(s)
add(a=5,b=4,c=1)
print()
def show(**no):
    print(no["a"])
    print(no["b"])
    print(no["c"])
    print(no["d"])
show(a="prakash",b=10,c="ganesh",d=20)