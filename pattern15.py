n=int(input("enter the value of n for pattern needed:"))
m=1
for i in range(1,n):
    for j in range(1,i+1):
        print(m,end="");
        if m is 1:
            m=0
        else:
            m=1
    print("")
    n-=1
    if j % 2 == 0:
        m = 1