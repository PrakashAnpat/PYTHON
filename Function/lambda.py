''' A function without a name is called as Anonymous function.It is also known as lambda function
Syntax:- 
        lambda argument_list : expression '''
a=lambda x:x+5
print(a(5))
b=lambda x,y:x+y
print(b(5,2))
add=lambda x,y : (x+y,x-y)
a,s=add(5,3)
print("Addition",a)
print("Substraction",s)
no=lambda m,n=4 :(m*n,m/n)
mul,div=no(20)
print(mul)
print(div)