str="Prakash" "Anpat"
print("     1:-In double quotes")
print(str)
str1='Prakash''Anpat'
print("     2:In single quotes")
print(str1)
str2="Hello, I'm Prakash Anpat.I'm basically from 'Satara'."
print("     3:Single quotes inside double quotes")
print(str2)
str3='Hello, I"m Prakash Anpat.I"m basically from "Satara".'
print("     4:Double quotes inside single quotes")
print(str3)
str4="""Hello guys
      please subscribe
      my channel"""
print("     5:Triple double quotes")#This is useful to create strings which span into several lines.
print(str4)
str5='''Hello guys
        please subscribe
        my channel'''
print("     6:Triple single quotes")#This is useful to create strings which span into several lines.
print(str5)
str6="Hello,\n How are you?"
print("     7:Using escape charactor")
print(str6)
str7=r"Hello,\n How are you?"#Raw string is used to nullify the effect of escape characters.
print("     8:Raw string")
print(str7)
print("................................................")
a="prakash" ,"anpat", "abhi", "phadtare"
print(a)
print(a[0],a[3])
print(a[-2],a[-4])
print(a[1],a[3])
print(a[-3],a[-2])
