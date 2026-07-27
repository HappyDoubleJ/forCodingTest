n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())







def is_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n


def bomb(size, c_x, c_y):
    #그냥 편하게 자기 자신 포함하자...
    #상
    for i in range(size):
        if is_range(c_x -1 * i, c_y):
            grid[c_x -1 * i][c_y] = 0

    #하
    for i in range(size):
        if is_range(c_x + 1 * i, c_y):
            grid[c_x + 1 * i][c_y] = 0

    #좌
    for i in range(size):
        if is_range(c_x, c_y -1 * i):
            grid[c_x][c_y -1 * i] = 0
    
    #우
    for i in range(size):
        if is_range(c_x, c_y + 1 * i):
            grid[c_x][c_y + 1 * i] = 0 

def shift():
    #각 열들에 대해
    for j in range(n):
        #각 행에 대해
        for k in range(n - 1, -1, -1):
            if temp[k][j] == 0:
                for l in range(k - 1, -1, -1):
                    if temp[l][j] != 0:
                        temp[k][j] = temp[l][j]
                        temp[l][j] = 0
                        break
                    
        
bomb(grid[r - 1][c - 1],r - 1, c - 1)

temp = [row[:] for row in grid]


shift()

for row in temp:
    print(*row)