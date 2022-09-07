'''% operator/Modulo operator/Interpolation operator-This operator is used for formatting strings.It interpreates the left
   argument much like a sprintf() style format string to be applied to the right argument, & returns the string resuliting
   from this formatting operation.
   Syntax:- ("format placeholder" % (data))
          Format placeholder= %[flags][width][.precision]type
   Syntax:- ("format placeholder" % {'key':value})
          Format placeholder= %(mapping_key)[flags][width][.precision]type'''

a=("My name is %s & my age is %d"%("Prakash",26))# Maintain order in this statement first string then integer.
print(a)
b=("My name is %(nm)s & my age is %(ag)d" %{"nm":"Prakash","ag":26})# This statement do not essiential to maintain order.
print(b)
c=("My name is %(nm)s & my age is %(ag)d" %{"ag":27,"nm":"Prakash"})
print(c)
d=("My workshop name is %s & schaduled on monday %d" %("Html",26))
print(d)
print("This is my frind %s & his coming today at %d am" %("abhi",11))
print("%d" % 432)
print("%d %d"%(432,345))
print("%f"%432.123)# Python automatically takes 6 digit after dot(.).
print("%f"%432.123456)
print("%f"%432.12345651)# If 4>no after the .(dot) then it will round the number.
print("%f"%432.12345641)
print("%s"%"Prakash")
print("%s %s"%("Prakash","Anpat"))
print("%d %s"%(432,"Prakash"))
print("%(nm)s %(no)d"%{"nm":"Prakash","no":123})
print("%(nm)s %(no)d"%{"no":123,"nm":"Prakash"})
print("Using flag")
print("% d"%432)
print("%+d"%432)
print("%  d  "%432)
print("% d   hello"%432)
print("%05d"%432)
print("using width")
print("%9s"%"Prakash")
print("%010s"%"Prakash")
print("%10d"%432)
print("Using precision")
print("%.2f"%432)
print("%.2f"%432.123)
print("%+10.3f"%432.12345)
print("%010.3f"%432.12345)
z=("My name is %(name)10s & my no is %(number)+10.1f"%{"name":"Prakash","number":8010.1918})
print(z)
