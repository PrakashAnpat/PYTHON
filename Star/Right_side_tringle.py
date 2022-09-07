# Right side tringle- 1-:Decreasing spaces
#                     2-:Increasing stars
n=int(input("Enter number: "))
for i in range(n):
    for j in range(i,n): # this loop for printing spaces
       print(" ",end=" ")
    for k in range(i+1): # this loop for printing star
        print("*",end=" ")
    print() 
# Right side tringle- 1-:Decreasing stars
#                     2-:Increasing spaces
print("-----------------")
for i in range(n):
    for j in range(i+1): # this loop for printing spaces
        print(" ",end=" ")
    for k in range(i,n):# this loop for printing stars
        print("*",end=" ")
    print()
    
    