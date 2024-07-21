a, b = map(int, input().split())
counts = [0] * 100
while True:
    a = a // b
    c = a % b
    counts[c] += 1
    if a < 1:
        break
squares_sum = sum(x**2 for x in counts)
print(squares_sum)