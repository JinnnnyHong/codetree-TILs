a , b = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
for i in lst:
    if i == b:
        cnt += 1
print(cnt)