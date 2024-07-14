l = []
nums = list(map(int, input().split()))
for i in nums:
    if i != 0:
        l.append(i)
    else:
        break
total = sum(l)
average = round(sum(l)/len(l),1)
print(total, average)