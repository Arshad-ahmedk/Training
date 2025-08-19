# def longest_equal_boys_girls(s: str) -> int:
#     prefix_sum = 0
#     seen = {0: -1}
#     max_len = 0
#
#     for i, ch in enumerate(s):
#         prefix_sum += 1 if ch == 'B' else -1
#
#         if prefix_sum in seen:
#             max_len = max(max_len, i - seen[prefix_sum])
#         else:
#             seen[prefix_sum] = i
#
#     return max_len
#
# line = "BBGGGB"
# print(longest_equal_boys_girls(line))

def longest_equal_boys_girls(s: str) -> int:
    vowels=['a', 'e', 'i', 'o', 'u']
    prefix_sum = 0
    seen = {0: -1}
    max_len = 0

    for i, ch in enumerate(s):
        prefix_sum += 1 if ch.lower() in vowels else -1

        if prefix_sum in seen:
            max_len = max(max_len, i - seen[prefix_sum])
        else:
            seen[prefix_sum] = i

    return max_len

line = "ABABGGGBEAEAE"
print(longest_equal_boys_girls(line))