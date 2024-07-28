n, m = map(int, input().split())
a = [[0 for i in range(m)] for j in range(n)]
count = 0
for col in range(m):
    for row in range(n):
        if col <= row:
            a[row][col] = count
        count += 1

for row in range(n):
    for col in range(m):
        print(A[row][col], end = ' ')
    print()