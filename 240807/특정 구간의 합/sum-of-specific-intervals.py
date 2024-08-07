def sumof(n, m):
    s = 0
    for k in range(n-1, m):
        s += A[k]
    print(s)

global A

n, m = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(m):
    a, b = map(int, input().split())
    sumof(a, b)