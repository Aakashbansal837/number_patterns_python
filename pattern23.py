n=int(input("enter the value of n for pattern needed:"))
s=n
for i in range(1,n+1):
    for j in range(1,s+1):
        print(j, end="")
    for j in range(1,i):
        print("*",end="")
    for j in range(1,i):
        print("*",end="")
    for j in range(1,s+1):
        print(s-j+1,end="")
    print("")
    s-=1