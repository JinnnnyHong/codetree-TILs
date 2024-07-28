n = int(input())
a = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or j == 0:
            a[i][j] = 1
        else:
            a[i][j] = a[i-1][j-1] + a[i-1][j]
        if j == i:
            break
        

for i in range(n):
    for j in range(n):
        if a[i][j] == 0:
            print(" ", end=' ')
        else:
            print(a[i][j], end=' ')
    print()