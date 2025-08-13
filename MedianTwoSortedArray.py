import heapq
def findMedianSortedArrays(nums1, nums2):
    min_heap = nums1 + nums2
    heapq.heapify(min_heap)

    total_len = len(min_heap)
    mid = total_len // 2

    if total_len % 2 == 1:
        for _ in range(mid):
            heapq.heappop(min_heap)
        return heapq.heappop(min_heap)
    else:
        for _ in range(mid - 1):
            heapq.heappop(min_heap)
        first = heapq.heappop(min_heap)
        second = heapq.heappop(min_heap)
        return (first + second) / 2

a=[1,2,3]
b=[4,5]
print(findMedianSortedArrays(a,b))