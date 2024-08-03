def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sum_even(a, b):
    cnt = 0
    for j in range(a, b+1):
        if is_prime(j):
            if (j // 10 + j % 10) % 2 == 0:
                cnt +=1

    print(cnt)

k, t = map(int, input().split())
sum_even(k,t)