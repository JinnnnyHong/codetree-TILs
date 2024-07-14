k = 0
l = []
lst = list(map(int, input().split()))
for i in lst:
    if i % 2 == 0:
        k += i
    elif i % 3 == 0:
        l.append(i)
print(k, round(sum(l)/len(l), 1))