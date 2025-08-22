# def bsort(nums, target, left, right):
#     mid = (left + right) // 2
#     if target == nums[mid]:
#         return mid+1
#     elif target > nums[mid]:
#         return bsort(nums, target, mid + 1, right)
#     else:
#         return bsort(nums, target, left, mid - 1)
#
# nums = [-1, 0, 3, 5, 9, 12]
# right =len(nums) - 1
# left = 0
# tar = 9
# print(bsort(nums, tar, left, right))

def search(nums,target):
    left=0
    right=len(nums)-1
    while left!=right:
        mid=(left+right)//2
        if nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
