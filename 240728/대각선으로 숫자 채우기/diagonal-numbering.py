n, m = map(int, input().split())
a = [[0 for _ in range(m)] for _ in range(n)]
count = 1

for diag in range(n + m):
    for i in range(n):
        for j in range(m):
            if diag == i+j:
                a[i][j] = count
                count +=1

for i in range(n):
    for j in range(m):
        print(a[i][j], end = ' ')
    print()