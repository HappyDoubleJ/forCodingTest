m1, d1, m2, d2 = map(int, input().split())

month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = 0
for i in range(m1, m2):
    day += month[i]

day -= (d1 - 1)
day += d2

print(day)