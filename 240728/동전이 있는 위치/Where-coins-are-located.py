n, m = map(int, input().split())
a = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(m):
    r, c = tuple(map(int, input().split()))
    a[r-1][c-1] =1

for i in range(n):
    for j in range(n):
        print(a[i][j], end = ' ')
    print()