piles = [3, 6, 7, 11]
hours = 8

left, right = 1, max(piles)

while left < right:
    mid = (left + right) // 2
    count = 0
    for i in piles:
        count += (i + mid - 1) // mid   # ceil(i/mid)

    if count <= hours:
        right = mid
    else:
        left = mid + 1

print(left)