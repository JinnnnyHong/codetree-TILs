a = int(input())
l = []
k = 0
i = 1

while True:
    t = i * a
    l.append(t)
    if t % 5 == 0:
        k += 1
        if k == 2:
            print(' '.join(map(str, l)))
            break
    i += 1