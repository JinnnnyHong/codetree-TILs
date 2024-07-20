lst = list(map(int, input().split()))

counts = [0]*10

for i in lst:
    if i == 0:
        break
    k = (i // 10) % 10
    if k > 0:  
        counts[k] += 1

for j in range(1,10):
    print(f"{j} - {counts[j]}")