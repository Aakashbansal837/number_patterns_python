n=int(input("enter the value of n for pattern needed:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end="");
    print("")
    n-=1