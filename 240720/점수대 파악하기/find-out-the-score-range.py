lst = list(map(int, input().split()))
counts = {t: 0 for t in range(100, 9, -10)}

for i in lst:
    if i == 0:
        break
    k = (i //10) * 10
    if k in counts:
        counts[k] += 1

for j in range(100, 9, -10):
    print(f"{j} - {counts[j]}")