n=int(input("enter the value of n for pattern needed:"))
m=1
mm=1
for i in range(1,n+2):
    for j in range(1,n+2):
        print(m,end="");
        m+=2
    print("")
    n-=1
    mm+=2
    m=mm