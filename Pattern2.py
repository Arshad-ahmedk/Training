def zigzag_triangle(n):
    arr = [[0]*n for _ in range(n)]
    num = 1

    for j in range(n):
        if j % 2 == 0:

            for i in range(j, n):
                arr[i][j] = num
                num += 1
        else:
            for i in range(n-1, j-1, -1):
                arr[i][j] = num
                num += 1

    for i in range(n):
        for j in range(i+1):
            print(arr[i][j], end=" ")
        print()

zigzag_triangle(5)