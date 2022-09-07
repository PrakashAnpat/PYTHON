a="prakash anpat"
b=26
c="My name is {} & my age is {}".format(a,b)
print(c)
e=50
f=3
print("{:.2}".format(e/f))
print("{:.2%}".format(e/f))
value=(10,20)
print("{0[0]} {0[1]}".format(value))
data={"Abhi":1000,"Shubham":2000}
print(type(data))
print("{0[Abhi]} {0[Shubham]}".format(data))
print("{d[Abhi]} {d[Shubham]}".format(d=data))
print("{Abhi} {Shubham}".format(**data))
print("{Shubham} {Abhi}".format(**data))