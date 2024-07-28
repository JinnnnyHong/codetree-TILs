n, m = map(int, input().split())
a = [[0 for _ in range(m)] for _ in range(n)]
count = 1

for s in range(n + m - 1):
    if s % 2 == 0:
        for row in range(n):
            col = s - row
            if 0 <= col < m:
                a[row][col] = count
                count += 1
    else:
        for col in range(m):
            row = s - col
            if 0 <= row < n:
                a[col][row] = count
                count += 1

for row in range(n):
    for col in range(m):
        print(a[row][col], end=' ')
    print()