n = int(input())
l = []
for i in range(n):
    k = int(input())
    if k % 2 == 0:
        l.append(k)

if l:
    print("".join(map(str, reversed(l))))
else:
    print(0)