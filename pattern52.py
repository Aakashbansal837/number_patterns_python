n=int(input("enter the value of n for pattern needed:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i-j+1,end=" ")
    for j in range(1,n-i+1):
        print(j+1,end=" ")
    print("")