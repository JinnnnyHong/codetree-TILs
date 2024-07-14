n = int(input()) 
k = list(map(int, input().split())) 

l = []  

for j in k:
    if j % 2 == 0:
        l.append(j)


print(" ".join(map(str, reversed(l))))