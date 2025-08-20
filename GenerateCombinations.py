def generate_combinations(s):
    n = len(s)
    result = []

    # Loop through all possible combinations
    for i in range(1, 1 << n):  # from 1 to (2^n - 1)
        subset = ""
        for j in range(n):
            # If j-th bit in i is set, include s[j]
            if i & (1 << j):
                subset += s[j]
        result.append(subset)
    return result

# Example
s = "abc"
print(generate_combinations(s))
