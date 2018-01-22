n=int(input("enter the value of n for pattern needed:"))
for i in range(1,n+1):
    for j in range(1,n-1+2):
        p=n-j+1
        if p is i:
            print("*",end="")
        else:
            print(p, end="")

    print("")