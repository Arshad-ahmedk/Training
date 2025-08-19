n=int(input("Enter the number of machines: "))
c=[]
for i in range(n):
    c.append(tuple(map(int,input().split())))
print(c)