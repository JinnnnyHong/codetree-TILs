def sum5(n):
    if n % 2 == 0 and (n // 10 + n % 10) % 5 == 0:
        return ("Yes")
    else:
        return ("No")


a = int(input())
print(sum5(a))