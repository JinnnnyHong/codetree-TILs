n, m = map(int, input().split())
a = [[0 for _ in range(m)] for _ in range(n)]
count = 1

for diag in range(n + m - 1):
    if diag % 2 == 0:
        # 짝수 대각선: 왼쪽에서 오른쪽, 위에서 아래
        for row in range(n):
            col = diag - row
            if 0 <= col < m:
                a[row][col] = count
                count += 1
    else:
        # 홀수 대각선: 위에서 아래, 왼쪽에서 오른쪽
        for col in range(m):
            row = diag - col
            if 0 <= row < n:
                a[col][row] = count
                count += 1

for row in range(n):
    for col in range(m):
        print(a[row][col], end=' ')
    print()