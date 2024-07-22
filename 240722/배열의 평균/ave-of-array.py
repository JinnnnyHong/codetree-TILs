n = 2
m = 4
l = []

for i in range(n):
    lst = list(map(int, input().split())) 
    l.append(lst)

# 가로 평균 계산
for i in range(n):
    avg1 = sum(l[i]) / m
    print(f"{avg1:.1f}", end=" ")
print()

# 세로 평균 계산
for j in range(m):
    col_sum = 0
    for i in range(n):
        col_sum += l[i][j]
    avg2 = col_sum / n
    print(f"{avg2:.1f}", end=" ")
print()

# 전체 평균 계산
total_sum = 0
for i in range(n):
    total_sum += sum(l[i])
avg3 = total_sum / (n * m)
print(f"{avg3:.1f}")