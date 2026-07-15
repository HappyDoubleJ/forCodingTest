n, m = map(int, input().split())

x , y = 0 , 0
vector = 2

# 상 좌 하 우 
dxs , dys = [-1, 0, 1, 0] , [0, -1, 0, 1]

#매트릭스 안인지
def is_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m


# out of index 또는 1이면 vector +1


# 0으로 이루어진 N * M 배열
matrix = [[0 for _ in range(m)] for _ in range (n)]


for i in range (1, n * m + 1):
    matrix[x][y] = i
    if not is_range(x + dxs[vector], y + dys[vector]) or matrix[x + dxs[vector]][ y + dys[vector]] != 0:
        vector = (vector + 1) % 4
    x += dxs[vector]
    y += dys[vector]

for row in matrix:
    print(*row)



