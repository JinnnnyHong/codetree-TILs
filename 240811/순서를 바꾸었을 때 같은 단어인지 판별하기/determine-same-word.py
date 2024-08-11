arr1 = input()
arr2 = input()
l1 = list(arr1)
l2 = list(arr2)

l1.sort()
l2.sort()
if l1 == l2:
    print("Yes")
else:
    print("No")