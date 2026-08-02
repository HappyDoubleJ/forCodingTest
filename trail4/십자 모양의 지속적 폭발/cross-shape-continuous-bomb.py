n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input()) for _ in range(m)]


temp_grid = [row[:] for row in grid]



def is_range(x,y):
    return 0 <= x and x < n and 0 <=  y and y < n

# 청소
def clean():
    #열
    for i in range(n):
        target_row = n - 1
        for j in range(n - 1, -1, -1):
            if temp_grid[j][i] == 0:
                continue
            else:
                temp_grid[target_row][i] = temp_grid[j][i]
                if target_row != j:
                    temp_grid[j][i] = 0
                target_row -= 1
    for i in range(n):
        for j in range(n):
            grid[i][j] = temp_grid[i][j]
    
        

#폭탄 터뜨리기
def bomb(row, col):
    for i in range(grid[row][col]):
        if is_range(row - i, col):
            temp_grid[row - i][col] = 0
        if is_range(row + i, col):
            temp_grid[row + i][col] = 0
        if is_range(row, col - i):
            temp_grid[row][col - i] = 0
        if is_range(row, col + i):
            temp_grid[row][col + i] = 0
    

#특정 열을 행 0부터 탐색하자
def search(col):
    for i in range(n):
        if grid[i][col] != 0:
            # 펑
            bomb(i, col)
            clean()
            return

for i in range(m):
    search(commands[i] -1)
    

for row in grid:
    print(*row)