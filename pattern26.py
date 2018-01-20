n=int(input("enter the value of n for pattern needed:"))
s=1
m=n
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(s,end="")
    print("")
    if (i < (n/2)):
        s+=1
    else:
        s-=1