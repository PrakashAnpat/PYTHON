'''These arguments are passed to the function with name-value pair so keyword arguments can identify
the formal argument by their names.The keyword argument's name & formal argument's name must match.'''
def show(name,age):
    print(name,age)
show(name="Prakash",age=26)
print()
def disp(name,age):
    print(name,age)
disp(age=26,name="Prakash")#Do not need to maintain order like string,int,etc.
