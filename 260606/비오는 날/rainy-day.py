n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

class weather_forecast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

weather_forecasts = []
for i in range(n):
    if weather[i] == 'Rain':
        t = weather_forecast(date[i], day[i], weather[i])
        weather_forecasts.append(t)

weather_forecasts.sort(key = lambda x:x.date)

print(f'{weather_forecasts[0].date} {weather_forecasts[0].day} {weather_forecasts[0].weather}')