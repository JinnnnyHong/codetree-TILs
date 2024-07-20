lst = list(map(int, input().split()))

counts = [0] * 6

for num in lst:
    if 1 <= num <= 6:
        counts[num - 1] += 1

for i in range(6):
    print(f"{i + 1} - {counts[i]}")