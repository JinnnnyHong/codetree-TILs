k = 0
l = []  
lst = list(map(int, input().split()))
n = len(lst)
for i in lst:
    if i % 2 == 0:
        k += i
for j in range(1, n, 2):
    l.append(lst[j])
print(k, round(sum(l)/len(l), 1))