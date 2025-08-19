import heapq

def min_days_to_produce_heap(machines, target):
    heap = []

    # machines = [(units, maint_days)]
    for idx, (units, maint_days) in enumerate(machines):
        cycle_len = 1 + maint_days
        heapq.heappush(heap, (1, idx, units, cycle_len))
    produced = 0
    last_day = 0

    while produced < target:
        day, idx, units, cycle_len = heapq.heappop(heap)
        produced += units
        last_day = day

        heapq.heappush(heap, (day + cycle_len, idx, units, cycle_len))

    return last_day


# Example usage:
n=int(input("Enter the number of machines: "))
machines=[]
for i in range(n):
    machines.append(tuple(map(int,input().split())))
target = 50
print(min_days_to_produce_heap(machines, target))  # minimal days
