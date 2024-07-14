k = []
l = []
lst = list(map(int, input().split()))
n = len(lst)
for i in range(1,n,2):
    k.append(lst[i])
for j in range(2, n, 3):
    l.append(lst[j])
print(sum(k), round(sum(l)/len(l), 1))