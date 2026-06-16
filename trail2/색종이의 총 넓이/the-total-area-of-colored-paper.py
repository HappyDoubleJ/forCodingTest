n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

length = 8
area = 0
paper = [[0 for i in range(200)] for i in range (200)]

def painting(x, y):
    global paper
    for i in range(x, x + length):
        for j in range(y, y + length):
            paper[i][j] = 1


for i in range(n):
    painting(x[i],y[i])



for i in range(200):
    for j in range(200):
        if paper[i][j] == 1:
            area += 1


print(area)