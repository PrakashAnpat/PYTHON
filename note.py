'''List-In list use the clear() method for delete all the elements from the list.
   Tuple-In tuple use del command for delete all the elements from the tuple.'''
a="prakash"
b=[1,2,2.22,2,"anpat"]
c=(2,4,6,"prakash")
del a,b,c # del command delete entire elements in the string,list,tuple.
m="prakash"
n=[1,2,2.22,2,"anpat"]
p=(2,4,6,"prakash")
print(m,n,p)
n.clear()# clear() method is used to delete all the elements from the list.
print(n)
del p
p.clear()
print(p)

