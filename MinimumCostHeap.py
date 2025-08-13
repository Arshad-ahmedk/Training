import heapq
def min_cost_to_add(nums):

    heapq.heapify(nums)

    total_cost = 0

    while len(nums) > 1:
        # Pop two smallest elements
        first = heapq.heappop(nums)
        second = heapq.heappop(nums)

        current_sum = first + second
        total_cost += current_sum

        heapq.heappush(nums, current_sum)

    return total_cost

nums = [4, 3, 2, 6]
print(min_cost_to_add(nums))
