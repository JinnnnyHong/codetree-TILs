n = int(input())
l = []

for _ in range(n):
    x1, x2 = map(int, input().split())
    l.append((x1, 'start'))
    l.append((x2, 'end'))

l.sort()

a = 0
b = 0

for event in l:
    if event[1] == 'start':
        a += 1
        b = max(b, a)
    else:
        a -= 1

print(b)