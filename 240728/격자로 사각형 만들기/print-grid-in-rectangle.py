n = int(input())
a = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:
            a[i][j] = 1
        else:
            a[i][j] = a[i-1][j] + a[i-1][j-1] + a[i][j-1]

for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()