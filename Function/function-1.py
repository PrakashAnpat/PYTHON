print("Divide large task into many small task")
print("Separate function for addition")
def add():
    a=10
    b=20
    print(a+b)
add()
print("Separate function for substraction")
def sub(a,b):
    c=a-b
    print(c)
sub(10,20)
print("Separate function for multiplication")
def mul(y):
    a=10
    b=2
    c=a*b*y
    print(c)
    print(f"Formatted output {c:*^+15.2f}")
    print("Formatted output {:>+015.3f}".format(c))
    print("formatted output %+15.5f"%(c))
mul(2)    
