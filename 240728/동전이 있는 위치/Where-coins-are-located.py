n, m = map(int, input().split())
a = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c = map(int, input().split())
    a[r-1][c-1] =1

for row in a:
    print(" ".join(map(str, row)))