a = int(input())
l = []
lst = list(map(int, input().split()))
for i in range(len(lst)):
    if lst[i] % 2 == 0:
        l.append(lst[i])
print(' '.join(map(str, l)))