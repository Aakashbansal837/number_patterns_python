n=int(input("enter the value of n for pattern needed:"))
s=n
for i in range(1,n+1):
    m=i
    s=n-1
    for j in range(1,i+1):
        print(m, end=" ")
        m+=s
        s-=1
    print("")