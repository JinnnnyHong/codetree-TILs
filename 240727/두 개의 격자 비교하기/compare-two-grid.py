def compare_grids(grid1, grid2):
    n = len(grid1)
    m = len(grid1[0])
    result = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if grid1[i][j] == grid2[i][j]:
                result[i][j] = 0
            else:
                result[i][j] = 1
                
    return result

n, m = map(int, input().split())

grid1 = [list(map(int, input().split())) for _ in range(n)]
grid2 = [list(map(int, input().split())) for _ in range(n)]

result = compare_grids(grid1, grid2)

for row in result:
    print(" ".join(map(str, row)))