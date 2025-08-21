num=5
boxes = [set() for _ in range(9)]
boxes[(4 // 3) * 3 + 7 // 3].add(num)
print(boxes)