l = []
a, b = map(int, input().split())
l.append(a)
l.append(b)
for i in range(2,10):
    k = 0
    k += l[i-2] + l[i-1]
    t = k % 10
    l.append(t)
result = ' '.join(map(str, l))
print(result)