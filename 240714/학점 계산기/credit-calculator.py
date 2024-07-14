n = int(input())
l = list(map(float, input().split()))

average = round(sum(l)/len(l),1)

if average >= 4.0:
    print(average)
    print("Perfect")
elif 3.0 <= average < 4.0:
    print(average)
    print("Good")
else:
    print(average)
    print("Poor")