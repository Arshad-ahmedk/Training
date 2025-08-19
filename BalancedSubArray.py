def longest_equal_boys_girls(s: str) -> int:
    prefix_sum = 0
    seen = {0: -1}
    max_len = 0

    for i, ch in enumerate(s):
        if ch == 'B':
            prefix_sum += 1
        elif ch == 'G':
            prefix_sum -= 1

        if prefix_sum in seen:
            max_len = max(max_len, i - seen[prefix_sum])
        else:
            seen[prefix_sum] = i

    return max_len

line = "BBGGGB"
print(longest_equal_boys_girls(line))
