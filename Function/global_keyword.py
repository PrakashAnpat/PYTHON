s=20        #global variable
def world():
    global s# Access global variable using global keyword followed by variable name 
    s=s+20
    print("Local+Global variable:",s)
world()
print("Global variable:",s)