nums = list(map(int, input().split()))
l = []
k = len(nums)

for j in range(k):
    if nums[j] < 250:
        l.append(nums[j])
    else:
        break

total = sum(l)
average = round(total / len(l), 1)
print(total, average)