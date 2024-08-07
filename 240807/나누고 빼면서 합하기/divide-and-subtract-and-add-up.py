def kk(a, b, A):
    total_sum = 0
    while b >= 1:
        total_sum += A[m - 1]
        if b % 2 == 0:
            b //= 2
        else:
            b -= 1

    total_sum += A[0]
    return total_sum


n, m = map(int, input().split())
A = list(map(int, input().split()))
result = kk(n, m, A)
print(result)