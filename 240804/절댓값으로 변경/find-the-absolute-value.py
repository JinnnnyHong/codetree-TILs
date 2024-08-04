def absol(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])
    for num in arr:
        print(num, end=" ")

n = int(input())
lst = list(map(int, input().split()))
absol(lst)