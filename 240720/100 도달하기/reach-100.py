l = [1]
n = int(input())
l.append(n)
i = 2
while True:
    k = l[i-1] + l[i-2]
    l.append(k)
    if k > 100:
        break
    i += 1      
print(' '.join(map(str, l)))