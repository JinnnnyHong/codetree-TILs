def swap(a, b):
    a, b = b, a
    print(a, b)

k, t = map(int, input().split())
swap(k,t)