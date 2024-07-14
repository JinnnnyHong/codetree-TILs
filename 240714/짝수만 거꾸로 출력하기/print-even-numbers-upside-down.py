n = int(input())
l = []
for i in range(n):
    k = int(input())
    if k % 2 == 0:
        l.insert(0, k)
print(" ".join(map(str, reversed(l))))