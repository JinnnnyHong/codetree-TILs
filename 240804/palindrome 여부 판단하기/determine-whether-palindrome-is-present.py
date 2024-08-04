def is_palindrome(arr):
    for i in range(len(arr)//2):
        if arr[i] == arr[-i-1]:
            return 'Yes'
        return 'No'

lst = list(input())
print(is_palindrome(lst))