n = int(input())
grid = [list(input()) for _ in range(n)]

numbers = [(-1,-1) for i in range(10)]

import sys

start = (0,0)
end = (0,0)

min_dist = sys.maxsize
temp_dist = 0
result = []


def cal():
    global temp_dist
    x,y = start
    distance = abs(x - result[0][0]) + abs(y - result[0][1])
    temp_distance = 0
    for i in range(2):
        temp_distance = temp_distance + abs(result[i][0] - result[i + 1][0]) + abs(result[i][1] - result[i + 1][1])
    temp_2 = abs(result[2][0] - end[0]) + abs(result[2][1] - end[1])
    temp_dist = distance + temp_distance + temp_2





def insert(a, b):
    global start
    global end
    if grid[a][b] == 'S':
        start = (a, b)
        return
    if grid[a][b] == 'E':
        end = (a, b)
        return

    for i in range(1, 10):
        if grid[a][b] == str(i):
            numbers[i] = (a,b)
            return
    
    return



for i in range(n):
    for j in range(n):
        insert(i,j)


def select(c):
    global min_dist


    if len(result) == 3:
        cal()
        min_dist = min(min_dist, temp_dist)
        return

    for i in range(c, 10):
        if numbers[i] != (-1,-1):
            result.append(numbers[i])
            select(i + 1)
            result.pop()

select(0)



if min_dist == sys.maxsize:
    print(-1)
else:
    print(min_dist)
        
