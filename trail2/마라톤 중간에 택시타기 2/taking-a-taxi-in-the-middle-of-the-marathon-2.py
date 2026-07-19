n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

max_dist = 0
sum_dist = 0
#거리 계산
def distance(x1,y1,x2,y2):

    return abs(x1 - x2) + abs(y1 - y2)



for i in range(n - 2):
    current_dist_1 = distance(x[i],y[i],x[i + 1],y[i + 1])
    current_dist_2 = distance(x[i + 1],y[i + 1],x[i + 2],y[i + 2])
    after_dist = distance(x[i],y[i],x[i + 2],y[i + 2])
    max_dist = max(max_dist, current_dist_1 + current_dist_2 - after_dist)
    sum_dist += current_dist_1
    if i == n -3:
        sum_dist += current_dist_2


print(sum_dist - max_dist)