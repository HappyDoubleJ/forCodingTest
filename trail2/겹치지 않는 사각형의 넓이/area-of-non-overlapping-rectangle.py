x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

#좌표 평면
paper = [[0 for i in range(2000)] for i in range(2000)]
cnt = 0

# 넓이 구하기 함수
def area (x1,y1, x2,y2):
    return abs(x1 - x2) * abs(y1 - y2)


for i in range (2):
    for j in range(x1[i] + 1000, x2[i] + 1000):
        for k in range(y1[i] + 1000, y2[i] + 1000):
            paper[j][k] = 1

for i in range(x1[2] + 1000, x2[2] + 1000):
    for j in range(y1[2] + 1000, y2[2] + 1000):
        paper[i][j] = 2

for i in range(2000):
    for j in range(2000):
        if paper[i][j] == 1:
            cnt += 1

print(cnt)
    