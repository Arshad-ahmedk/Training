import heapq

def hahaa(a,b):
    c=a+b
    length = len(c)
    m=length//2
    print(m)
    heapq.heapify(c)

    if (length%2)==1:
        for i in range(m):
            heapq.heappop(c)
        return heapq.heappop(c)
    else:
        for i in range(m-1):
            heapq.heappop(c)
        first = heapq.heappop(c)
        second = heapq.heappop(c)
        print(first, second)
        return ((first + second) / 2)

a=[1,2]
b=[3,4]
print(hahaa(a,b))