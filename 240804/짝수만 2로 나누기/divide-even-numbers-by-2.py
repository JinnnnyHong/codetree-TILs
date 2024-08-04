def divide_even_elements(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] //= 2

n = int(input())
arr = list(map(int, input().split()))

divide_even_elements(arr)
print(' '.join(map(str, arr)))