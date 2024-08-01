def is_369(number):
    return '3' in str(number) or '6' in str(number) or '9' in str(number)

def count_special_numbers(a, b):
    count = 0
    for num in range(a, b + 1):
        if is_369(num) or num % 3 == 0:
            count += 1
    return count

a, b = map(int, input().split())
result = count_special_numbers(a, b)
print(result)