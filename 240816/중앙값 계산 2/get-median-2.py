def find_median(n, numbers):
    current_numbers = []
    
    for i in range(n):
        current_numbers.append(numbers[i])
        
        if (i + 1) % 2 != 0:
            current_numbers.sort()
            median = current_numbers[len(current_numbers) // 2]
            print(median, end=" ")

n = int(input())
numbers = list(map(int, input().split()))

find_median(n, numbers)