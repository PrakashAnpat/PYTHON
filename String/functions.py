name="prakash"
print("1:",name)
print("2:",name.upper())# Convert all character of a string into uppercase.
name1="ANPAT"
print("3:",name1)
print("4:",name1.lower())# Convert all character of string into lowercase.
print("5:",name.swapcase(),name1.swapcase())# Convert all lowercase into uppercase & uppercase into lowercase.
a="hello i'm prakash anpat."
b="Hello Im Prakash Anpat."
print("6:",a.title())
print("7:",name1.isupper(),name.isupper())# Test wheather given string is in uppercase or not.
print("8:",name.islower(),name1.islower())# Test wheather given string is in lowercase or not.
print("9:",a.istitle(),b.istitle())# Test wheather given string is in title format or not.
c="123456789"
print("10:",c.isdigit())#  To check the string contains only numeric digits(0-9).
print("11:",name.isalpha())# It returns true if the string has at least one character &all are alphabates(A-Z & a-z).
print("12:",name1.isalpha())
print("13:",c.isalpha())
d="prakashanpat12345"
print("14:",d.isalnum())#It returns true if the string has at least one character & all characters in the string are alphanumeric(A-Z,a-z or 0-9).
print("15:",c.isalnum())
e="  "
f="   abc"
g="xyz   "
h="     prakash     "
print("16:",e.isspace(),f.isspace())#It returns true if the string contains only space.
print("17:",f.lstrip())# Remove the space which are at left side of the string.
print("18:",g.rstrip())# Remove the space which are at right side of the string.
print("19:",h.strip())# Remove the space from the both side of the string.
print("20:",name.replace("p","Su"),name1.replace("PAT","KNOW"))# Replace a sub string in a string with another sub string.
i="Hello-prakash-anpat"
j="hello","how","are"
print("21:",i,i.split("-"))# To split/break a string into pieces.This pieces returns as a list.
print("22:",j,"-".join(j))# To join string into one string.
print("23:",b,b.startswith("He"),b.startswith("Im"))#To check wheather a string is starting with a sub-string(specified_string) or not.
print("24:",b,b.endswith("pat."),b.endswith("Hello"))