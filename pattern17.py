n=int(input("enter the value of n for pattern needed:"))
m=1
mm=2
s=m
for i in range(1,n+1):
    for j in range(1,i+1):
        print(s,end=" ");
        s+=2
    print(" ")
    n-=1
    if (i %2== 0):
        s=m
    else:
        s=mm