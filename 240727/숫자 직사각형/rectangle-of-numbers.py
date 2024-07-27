n, m = map(int, input().split())
l = []
num = 1
for i in range(n):
    row = []
    for j in range(m):
        row.append(num)
        num += 1
    l.append(row)
for row in l:
    print(' '.join(map(str, row)))