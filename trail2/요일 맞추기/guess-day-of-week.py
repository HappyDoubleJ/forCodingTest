m1, d1, m2, d2 = map(int, input().split())

month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']


def days(a, b, c, d):
    day_1 = 0
    day_2 = 0
    for i in range(1, a):
        day_1 += month[i]
    for i in range(1, c):
        day_2 += month[i]
    day_1 += b
    day_2 += d
    
    return day_2 - day_1
   


print( day[days(m1,d1,m2,d2) % 7]) 

