"""F-string/Formatted string litral- A formatted string litral or f-string is a string litral that is prefixed with f or F.
These strings may contain replacement fields which are expressions delimited by curly braces {}.While other string litrals
always have a constant value,formatted strings are really expressions evaluated at run time.
Syntax:-f"{index/key/name:[fill][align][sign][#][0][width][,][.precision]type}" """
a=10
b=20
print(f"{a}")
print(f"{a} {b}")
c=f"{a} {b}"
print(c)
d=10.56
e=20.42
print(f"{d}")
print(f"{e}")
print(F"{d} {e}")
print(f"{e} {d}")
s1="prakash"
s2="anpat"
print(f"{s1}")
print(f"{s2}")
print(f"{s1} {s2}")
print(f"{s2} {s1}")
name="prakash"
age="26"
v=f"My name is {name} & my age is {age}"
print(v)
price=1234567890
print(price)
print(f"{price:,}")
print(f"{price:_}")
print(f"{price:,.2f}")
print(f"{price:_.3f}")
print(f"{10*10}")
m=100
n=5
print(f"{m/n:.2}")
print(f"{m/n:.2%}")
value=(20,40)
print(f"{value[0]} {value[1]}")
data={"rahul":2000,"sonam":1000}
print(data)
