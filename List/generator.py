def disp(a,b):
    yield a # Returns the elements from generator function into generator object.
    yield b
result=disp(10,20)
print(result)
print(type(result))
print(next(result))#next()function is used to retrieve element by element from a generator object.
print(next(result))
# lst=list(result)
# print(lst)
def loop(a,b):
    while a<=b:
        yield a
        a+=1
result=loop(1,5)
print(result)
print(type(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print()
def swap(a,b):
    while a>=b:
        yield a
        a-=1
result=swap(5,0)
print(result)
print(type(result))
print(next(result))
for i in result:
    print(i)