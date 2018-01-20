s=int(input("enter the value of n for pattern needed:"))
n=1
for i in range(1,s+1):
    for j in range(1,i+1):
        print(n, end="");
        if n is 1:
            n =0
        else:
            n = 1
    print("")
    n=1