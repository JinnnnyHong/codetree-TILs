l = []
nums = list(map(int, input().split()))
for i in nums:
    if i != 0:
        if i % 2 == 0:
            l.append(i)
    else:
        break
print(len(l), sum(l))