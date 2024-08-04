def oper(a, b):
    m = min(a, b)
    M = max(a, b)
    if a == m:
        print(m*2, M+25)
    else:
        print(M+25, m*2)

k, t = map(int, input().split())
oper(k,t)