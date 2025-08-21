def print_pattern(n):
    num = 1
    mid = (n + 1) // 2   # middle height

    for i in range(1, n+1):
        # decide line length
        if n % 2 == 1:  # odd case
            if i <= mid:
                length = i
            else:
                length = n - i + 1
        else:           # even case
            if i <= mid:
                length = i
            else:
                length = n - i

        line = ""
        for j in range(length):
            line = str(num) + line
            num += 1
        print(line)



print_pattern(4)

