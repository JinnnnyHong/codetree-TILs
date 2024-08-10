import math

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_of_list(arr, n):
    if n == 1:
        return arr[0]
    return lcm(arr[n-1], lcm_of_list(arr, n-1))

n = int(input())
arr = list(map(int, input().split()))

print(lcm_of_list(arr, n))