n = int(input())
l = []
cnt = 0
for i in range(n):
    k = int(input())
    l.append(k)

for j in range(1, len(l)):
    if l[j] == l[j-1]:
        cnt +=1

print(cnt+1)