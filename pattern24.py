n=int(input("enter the value of n for pattern needed:"))
s=1
for i in range(1,n*2,2):
    for r in range(1,n*2-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(s,end=" ")
        s+=1
    print(" ")