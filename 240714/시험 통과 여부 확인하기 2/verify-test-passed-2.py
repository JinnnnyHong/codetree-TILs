k = 0
n = int(input())
for i in range(n):
    score = list(map(int, input().split()))
    average = sum(score)/4
    if average >= 60:
        print("pass")
        k += 1
    else:
        print("fail")
        print(k)