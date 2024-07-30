def Rectangle(n, m):
    for i in range(n):
        print('1'*m)

k, t = map(int, input().split())
Rectangle(k,t)