def print_num(n):
    count = 1
    for i in range(n):
        row = []
        for j in range(n):
            row.append(count)
            count += 1
            if count == 10:
                count = 1
        print(' '.join(map(str, row)))

k = int(input())
print_num(k)