n = int(input())
lst = list(map(int, input().split()))
    
arr = [0] * 9
for i in lst:
    if 1 <= i <= 9:
        arr[i - 1] += 1

for k in arr:
    print(k)