lst = list(map(int, input().split()))
e = []
o = []
for i in range(len(lst)):
    if i % 2 == 0:
        o.append(lst[i])
    else:
        e.append(lst[i])
if sum(e) >= sum(o):
    print(sum(e)-sum(o))
else:
    print(sum(o)-sum(e))