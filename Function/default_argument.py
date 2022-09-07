'''Sometime we mention default value to the formal argument in function defination & we may not 
required to provide actual argument,In this case default argument will be used by formal argument.'''
def show(name,age=26):   # Default argument
     print(name,age)
show("Prakash")
def disp(name,age=26):
    print(name,age)
disp(name="Prakash",age=62)#we provide actual argument then it will use provided value