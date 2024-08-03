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

def is_valid_date(Y, M, D):
    if M < 1 or M > 12:
        return False
    if D < 1 or D > 31:
        return False
    if M in [4, 6, 9, 11] and D > 30:
        return False
    if M == 2:
        if is_leap_year(Y) and D > 29:
            return False
        elif not is_leap_year(Y) and D > 28:
            return False
    return True

def get_season(month):
    if 3 <= month <= 5:
        return "Spring"
    elif 6 <= month <= 8:
        return "Summer"
    elif 9 <= month <= 11:
        return "Fall"
    else:
        return "Winter"


def def1(Y, M, D):
    if not is_valid_date(Y, M, D):
        return -1
    return get_season(M)


a, b, c = map(int, input().split())
print(def1(a, b, c))