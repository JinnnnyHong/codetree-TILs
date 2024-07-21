n, q = map(int, input().split())
lst = list(map(int, input().split()))
for _ in range(q):
    a = input().split()
    b = int(a[0])

    if b == 1:
        t = int(a[1])-1
        print(lst[t])
    elif b == 2:
        k = int(a[1])
        if k in lst:
            print(lst.index(k) + 1)
        else:
            print(0)
    elif b == 3:
        s = int(a[1]) - 1
        e = int(a[2])
        print(' '.join(map(str, lst[s:e])))