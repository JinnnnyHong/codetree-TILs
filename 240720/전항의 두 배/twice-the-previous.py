a, b = map(int, input().split())
l = []
l.append(a)
l.append(b)
for i in range(2,10):
    k = l[i-1] + 2*l[i-2]
    l.append(k)
print(' '.join(map(str, l)))