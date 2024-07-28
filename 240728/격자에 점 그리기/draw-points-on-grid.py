n, m = map(int, input().split())
a = [[0 for _ in range(n)] for _ in range(n)]
count = 0

for i in range(m):
    r,c = map(int, input().split())
    a[r-1][c-1] += 1
    if a[r-1][c-1] == 1:
        a[r-1][c-1] += count
        count+=1


for row in a:
    print(" ".join(map(str, row)))