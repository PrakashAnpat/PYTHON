i=0
def sun():
    global i
    s=i+1
    print(s,end=" ")
    # if s==900:
    #     print(end="\n")
    i+=1
    sun()
sun()