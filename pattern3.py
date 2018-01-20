n=int(input("enter the value of n for pattern needed:"))
s=n
for i in range(1,n+1):
    p=s
    for j in range(1,n-i+2):
        print(p-j+1,end="");
    print("")
    s-=1