def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# 예제 실행
y = int(input())
if is_leap_year(y):
    print("true")
else:
    print("false")