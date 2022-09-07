'''Variable length argument is an argument that can accept any no of values.The variable length 
argument is written with * symbol.It stores all the value in a tuple.'''
def show(*no):
    a=no[0]+no[1]+no[2]+no[3]+no[4]
    print(a)
show(20,40,60,80,100)
print()
def disp(*chr):
    print(chr[0])
    print(chr[1])
    print(chr[2])
    print(chr[3])
disp("prakash","Ganesh","akash","sushank")