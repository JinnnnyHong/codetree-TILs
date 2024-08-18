a, b, c = map(int, input().split())

start_day = 11
start_hour = 11
start_minute = 11

if (a < start_day) or (a == start_day and b < start_hour) or (a == start_day and b == start_hour and c < start_minute):
    print(-1)
else:
    day_diff = a - start_day
    hour_diff = b - start_hour
    minute_diff = c - start_minute

    total_minutes = day_diff * 24 * 60 + hour_diff * 60 + minute_diff

    print(total_minutes)