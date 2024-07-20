lst = list(map(int, input().split()))
l = []
for i in range(len(lst)-1):
    if lst[i] == 0:
        break  
    if lst[i] % 2 == 0:
        l.append(lst[i]//2)
    else:
        l.append(lst[i]+3)
print(' '.join(map(str,l)))