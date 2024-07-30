def sum_num(a):
    l = []
    cnt = 1
    for i in range(a):
        l.append(cnt)
        cnt += 1
    t = sum(l)/10
    return int(t)

n = int(input())
print(sum_num(n))