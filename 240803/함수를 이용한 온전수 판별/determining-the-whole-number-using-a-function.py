def num1(n):
    if n % 2 == 0:
        return False
    if n % 10 == 5:
        return False
    if n % 3 == 0 and n % 9 != 0:
        return False     
    return True

def num2(a, b):
    cnt = 0
    for i in range(a, b+1):
        if num1(i):
            cnt += 1
    print(cnt)

s,v = map(int, input().split())
num2(s,v)