N = int(input())

l = []

for i in range(N):
    h, w = map(int, input().split())
    l.append((h, w, i + 1))

l.sort(key=lambda x: (x[0], -x[1]))

for student in l:
    print(student[0], student[1], student[2])