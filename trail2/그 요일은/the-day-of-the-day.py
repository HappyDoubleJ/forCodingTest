m1, d1, m2, d2 = map(int, input().split())
A = input()

month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dayday = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

def days(x1,x2):
    day = 0
    for i in range(1, x1):
        day += month[i]
    day += x2
    return day

t = 0
for i in range (7):
    if dayday[i] == A:
        t = i


day_1 = days(m1,d1)
day_2 = days(m2,d2)

week = (day_2 - day_1) // 7
other = (day_2 - day_1) % 7

print(week + (other >= t))