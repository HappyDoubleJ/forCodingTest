n = int(input())
grid = [[0] * n for _ in range(n)]

# 우 상 좌 하 
dxs , dys = [0, -1, 0, 1] , [1, 0, -1, 0]

vector = 3
x, y = (n // 2) , (n // 2)

matrix = [[0 for _ in range(n)] for _ in range (n)]


first_standard = 1
first_point = 1
cnt = 2

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

#순서는 2,3,5,7,10,13

for i in range (1, n * n + 1):

    if i == first_point:
        vector = (vector + 1) % 4
        first_point += first_standard
        cnt -= 1
    if cnt == 0:
        first_standard += 1
        cnt = 2
    
    if in_range(x,y):
        matrix[x][y] = i


    x += dxs[vector]
    y += dys[vector]


for row in matrix:
    print(*row)


