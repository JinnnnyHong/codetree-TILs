def generate_square_grid(n):
    grid = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            grid[i][j] = i + 1 + j * n
    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

n = int(input())
grid = generate_square_grid(n)
print_grid(grid)