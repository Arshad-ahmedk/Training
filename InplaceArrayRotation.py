def rotate(nums, k):
    n = len(nums)
    k = k % n

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

nums = [1, 2, 3, 4, 5, 6, 7]
rotate(nums, 3)
print(nums)
