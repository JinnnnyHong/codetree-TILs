def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

a, b, c = map(int, input().split())
result = a * b * c

print(sum_of_digits(result))