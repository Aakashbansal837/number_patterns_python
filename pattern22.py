n=int(input("enter the value of n for pattern needed:"))
for i in range(1,n*2+1,2):
    for j in range(1,i+1):
        print(j, end="")
    print("")