def lcm(a, b):
    num = 1
    k = max(a, b)
    l = []
    for i in range(k):
        if a % num == 0 and b % num == 0:
            l.append(num)
            num += 1
        else:
            num += 1
    for j in range(1,len(l)):
        l[j] = l[j]*l[j-1]
    print(l[-1])

n, m = map(int, input().split())
lcm(n,m)