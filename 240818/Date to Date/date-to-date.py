a, b, c, d = map(int, input().split())
day = 0

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    if a == c and b == d:
        break

    day += 1
    b += 1

    if b > num_of_days[a]:
        a += 1
        b = 1

print(day+1)