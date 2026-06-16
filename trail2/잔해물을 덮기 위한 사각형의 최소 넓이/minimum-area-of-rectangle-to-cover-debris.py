x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

#기본값
default = 1000
min_x = 2000
max_x = -1
min_y = 2000
max_y = -1

#x 중에 젤 작은 것과 젤 큰 것. y 중에 젤 작은 것과 젤 큰 것.

#좌표평면
paper = [[0 for i in range(2000)] for i in range(2000)]

#칠하기
def painting(x1,y1, x2,y2):
    for i in range(x1 + default, x2 + default):
        for j in range(y1 + default, y2 + default):
            paper[i][j] = 1

def painting_2(x1,y1, x2,y2):
    for i in range(x1 + default, x2 + default):
        for j in range(y1 + default, y2 + default):
            paper[i][j] = 0


#면적 구하기
def area (s_x, b_x, s_y, b_y):
    return (b_x - s_x + 1) * (b_y - s_y + 1)

#최대 최소 구하기


painting(x1[0],y1[0], x2[0],y2[0])
painting_2(x1[1],y1[1], x2[1],y2[1])

for i in range(2000):
    for j in range(2000):
        if paper[i][j] == 1:
            if i <= min_x:
                min_x = i
            if i >= max_x:
                max_x = i
            if j <= min_y:
                min_y = j
            if j >= max_y:
                max_y = j

if max_x == -1:
    print(0)
else:
    print(area(min_x, max_x, min_y, max_y))


