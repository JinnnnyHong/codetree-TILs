a, b = map(int, input().split())
counts = [0] * b
while True:
    c = a % b
    counts[c] += 1
    a = a // b
    if a < 1:
        break
squares_sum = sum(x**2 for x in counts)
print(squares_sum)