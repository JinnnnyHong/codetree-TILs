lst = list(map(int, input().split()))
k = 0
for i in range(len(lst)):
    if lst[i] == 0:
        k += lst[i-1]+lst[i-2]+lst[i-3]
        break
        
print(k)