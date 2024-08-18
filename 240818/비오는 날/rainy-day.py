class weather:
    def __init__(self, date, day, weath):
        self.date = date
        self.day = day
        self.weath = weath
    
    def display(self):
        print(f"{self.date} {self.day} {self.weath}")

l = []
for i in range(int(input())):
    date, day, weath = input().split()
    Weather = weather(date, day, weath)
    l.append(Weather)

nearest_rainy_day = None

for Weather in l:
    if Weather.weath == "Rain":
        if nearest_rainy_day is None or Weather.date < nearest_rainy_day.date:
            nearest_rainy_day = Weather

if nearest_rainy_day:
    nearest_rainy_day.display()