counts = [0] * 4
for i in range(3):
    a, b = input().split()
    b = int(b)
    if a == 'Y' and b >= 37:
        counts[0] += 1
    elif a == "N" and b >= 37:
        counts[1] += 1
    elif a == "Y" and b < 37:
        counts[2] += 1
    else:
        counts[3] += 1
if counts[0] >= 2:
    counts.append('E')
    print(' '.join(map(str, counts)))
else:
    print(counts)