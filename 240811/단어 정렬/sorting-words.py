n = int(input())
strings = []

for i in range(n):
    arr = input()
    strings.append(arr)

strings.sort()

for s in strings:
    print(s)