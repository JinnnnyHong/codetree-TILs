n = int(input())
l = list(map(int, input().split()))

l.sort()
print(' '.join(map(str, l)))

l.sort(reverse = True)
print(' '.join(map(str, l)))