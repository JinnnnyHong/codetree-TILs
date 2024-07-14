l = []
nums = list(map(int, input().split()))
for i in nums:
    if i != 0:
        l.append(i)
    else:
        break
print(" ".join(map(str, reversed(l))))