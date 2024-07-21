a, b = map(int, input().split())
counts = [0] * b
while a > 1:
    c = a % b
    counts[c] += 1
    a = a // b
squares_sum = sum(x**2 for x in counts)
print(squares_sum)