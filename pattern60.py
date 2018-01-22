n=input("enter the value of n for pattern needed:")
s=len(n)
for i in range (s):
    for j in range(i,s):
        print(n[j], end=" ")
    print("")