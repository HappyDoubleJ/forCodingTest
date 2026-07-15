n, m = map(int, input().split())

# 상 우 하 좌
dxs , dys = [-1, 0, 1, 0] , [0, 1, 0, -1]
x, y = 0 , 0

# 매트릭스
matrix = [[0 for _ in range(m)] for _ in range(n)]

#시작
vector = 1

start = 'A'

def is_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

for i in range (n * m):
    matrix[x][y] = chr(ord(start) + (i % 26))
    if not is_range(x + dxs[vector], y + dys[vector]) or matrix[x + dxs[vector]][y + dys[vector]] != 0:
        vector = (vector + 1) % 4
    x = x + dxs[vector]
    y =  y + dys[vector]

for row in matrix:
    print(*row)
    

