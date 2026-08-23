n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]


import sys
# Please write your code here.

selected = []

for_cal = []

min_dist = sys.maxsize
max_temp_dist = -1


def cal(start):
    global min_dist
    global max_temp_dist


    if len(for_cal) == 2:

        temp_dist = (for_cal[0][0] - for_cal[1][0]) ** 2 + abs(for_cal[0][1] - for_cal[1][1]) ** 2
        max_temp_dist = max(temp_dist, max_temp_dist)
        return


    for i in range(start, m):
        for_cal.append(selected[i])
        cal(i + 1)
        for_cal.pop()





def selecting(start):
    global max_temp_dist
    max_temp_dist = -1
    global min_dist

    if len(selected) == m:

        cal(0)
        min_dist = min(min_dist, max_temp_dist)
        return

        




    for i in range(start, n):
        selected.append(points[i])
        selecting(i + 1)
        selected.pop()



selecting(0)

print(min_dist)