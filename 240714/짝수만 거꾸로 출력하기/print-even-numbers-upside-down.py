n = int(input())
l = []
for i in range(n):
    k = map(int, input().split())
    for j in k:
        if j % 2 == 0:
            l.append(j)
print("".join(map(str, reversed(l))))