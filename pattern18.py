n=int(input("enter the value of n for pattern needed:"))
s=n
p=n
for i in range(1,s+1):
    for j in range(1,s+1):
        print(n, end="");
        if n is s:
            n=s
        else:
            n+=1
    print("")
    n=p-1
    p-=1