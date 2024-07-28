n = int(input())
a = [[0 for j in range(n)] for i in range(n)]
count = n**2

for col in range(n):
    if n % 2 == 0:
        if col % 2 == 0:
            for row in range(n-1, -1, -1):
                a[row][col] = count
                count -= 1
        else:
            for row in range(n):
                a[row][col] = count
                count -= 1
    else:
        if col % 2 == 0:
            for row in range(n):
                a[row][col] = count
                count -= 1
        else:
            for row in range(n-1, -1, -1):
                a[row][col] = count
                count -= 1

for row in range(n):
    for col in range(n):
        print(a[row][col], end = " ")
    print()