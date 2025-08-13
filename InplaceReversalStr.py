a=list("Hello")
start,end=0,len(a)-1
while start<end:
    a[start],a[end]=a[end],a[start]
    start+=1
    end-=1
print("".join(a))