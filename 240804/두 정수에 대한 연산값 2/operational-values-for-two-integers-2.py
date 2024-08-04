def oper(a, b):
    m = min(a,b)
    M = max(a,b)
    if a == m:
        print(a+10, b*2)
    else:
        print(a*2, b+10)

k, t = map(int, input().split())
oper(k,t)