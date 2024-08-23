a, b = map(int, input().split())
n = input().strip()

Binary = int(n, a)

result = ''
while Binary > 0:
    result = str(Binary % b) + result
    Binary //= b

print(result if result else '0')