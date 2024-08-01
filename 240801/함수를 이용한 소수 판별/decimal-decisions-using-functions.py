def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(a, b):
    total = 0
    for num in range(a, b + 1):
        if is_prime(num):
            total += num
    return total

a, b = map(int, input().split())
result = sum_of_primes(a, b)
print(result)