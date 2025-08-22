# heights = [10,6,8,5,11,9]
# n=len(heights)
# counts=[]
# for h in range(n):
#     a=heights.pop(0)
#     max = 0
#     count = 0
#     for h2 in heights:
#         if a>h2 and max<h2:
#             count+=1
#             max=h2
#         elif a<h2:
#             count+=1
#             break
#     counts.append(count)
# print(counts)
# #TIME LIMIT EXCEEDED

class Solution:
    def canSeePersonsCount(self, heights):
        n = len(heights)
        res = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            count = 0
            while stack and stack[-1] <= heights[i]:
                stack.pop()
                count += 1
            if stack:
                count += 1

            res[i] = count
            stack.append(heights[i])

        return res
print(Solution().canSeePersonsCount([10,6,8,5,11,9]))