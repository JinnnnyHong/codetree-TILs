def gcd(a, b):
    k = max(a, b)
    l = []
    cnt = 1
    for i in range(k):
        if a % cnt == 0 and b % cnt == 0:
            l.append(cnt)
            cnt +=1
        else:
            cnt += 1
    print(max(l))

n,m = map(int, input().split())
gcd(n,m)