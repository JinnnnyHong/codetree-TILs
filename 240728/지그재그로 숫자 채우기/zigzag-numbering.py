n, m = map(int, input().split())
a = [[0 for j in range(m)] for i in range(n)]
count = 0

for col in range(m):
    if col % 2 == 0:
        for row in range(n):
            a[row][col] = count
            count += 1
    else:
        for row in range(n-1, -1, -1):
            a[row][col] = count
            count += 1

for row in range(n):
    for col in range(m):
        print(a[row][col], end = " ")
    print()