n = 4
m = 4
total = 0
l = []

for i in range(n):
    lst = list(map(int, input().split()))
    l.append(lst)

for i in range(n):    
    for j in range(m):
        if j <= i:
            total += l[i][j]
            
print(total)