nums = list(map(int, input().split()))
l = []
k = len(nums)

for j in range(k):
    if nums[j] < 250:
        l.append(nums[j])
    else:
        break

print(sum(l), sum(l)/len(l))