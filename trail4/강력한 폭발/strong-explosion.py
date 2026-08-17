n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
temp_grid = [[0 for _ in range(n)] for _ in range(n)]


target = []
count = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            count += 1
            target.append((i,j))
    
def is_range(x,y):
    return 0 <= x < n and 0 <= y < n

def one (x,y):
    temp_grid[x][y] += 2
    if is_range(x - 1, y):
        temp_grid[x - 1][y] += 2
    if is_range(x - 2, y):
        temp_grid[x - 2][y] += 2
    if is_range(x + 1, y):
        temp_grid[x + 1][y] += 2
    if is_range(x + 2, y):
        temp_grid[x + 2][y] += 2

def two (x,y):
    temp_grid[x][y] += 2
    if is_range(x - 1, y):
        temp_grid[x - 1][y] += 2
    if is_range(x, y - 1):
        temp_grid[x][y - 1] += 2
    if is_range(x + 1, y):
        temp_grid[x + 1][y] += 2
    if is_range(x, y + 1):
        temp_grid[x][y + 1] += 2


def three (x,y):
    temp_grid[x][y] += 2
    if is_range(x - 1, y - 1):
        temp_grid[x - 1][y - 1] += 2
    if is_range(x - 1, y + 1):
        temp_grid[x - 1][y + 1] += 2
    if is_range(x + 1, y - 1):
        temp_grid[x + 1][y - 1] += 2
    if is_range(x + 1, y + 1):
        temp_grid[x + 1][y + 1] += 2

def cal ():
    temp_cnt = 0
    for i in range(n):
        for j in range(n):
            if temp_grid[i][j] >= 2:
                temp_cnt += 1
    return temp_cnt

max_cnt = 0


def reset_one (x,y):
    temp_grid[x][y] -= 2
    if is_range(x - 1, y):
        temp_grid[x - 1][y] -= 2
    if is_range(x - 2, y):
        temp_grid[x - 2][y] -= 2
    if is_range(x + 1, y):
        temp_grid[x + 1][y] -= 2
    if is_range(x + 2, y):
        temp_grid[x + 2][y] -= 2

def reset_two (x,y):
    temp_grid[x][y] -= 2
    if is_range(x - 1, y):
        temp_grid[x - 1][y] -= 2
    if is_range(x, y - 1):
        temp_grid[x][y - 1] -= 2
    if is_range(x + 1, y):
        temp_grid[x + 1][y] -= 2
    if is_range(x, y + 1):
        temp_grid[x][y + 1] -= 2


def reset_three (x,y):
    temp_grid[x][y] -= 2
    if is_range(x - 1, y - 1):
        temp_grid[x - 1][y - 1] -= 2
    if is_range(x - 1, y + 1):
        temp_grid[x - 1][y + 1] -= 2
    if is_range(x + 1, y - 1):
        temp_grid[x + 1][y - 1] -= 2
    if is_range(x + 1, y + 1):
        temp_grid[x + 1][y + 1] -= 2

def bomb(N):
    global max_cnt
    if N == 0:
        current = cal()
        max_cnt = max(max_cnt, current)
        return

    one(target[N - 1][0], target[N - 1][1])
    bomb(N - 1)
    reset_one(target[N - 1][0], target[N - 1][1])



    two(target[N - 1][0], target[N - 1][1])
    bomb(N - 1)
    current = cal()
    max_cnt = max(max_cnt, current)
    reset_two(target[N - 1][0], target[N - 1][1])

    three(target[N - 1][0], target[N - 1][1])
    bomb(N - 1)
    current = cal()
    max_cnt = max(max_cnt, current)
    reset_three(target[N - 1][0], target[N - 1][1])



bomb(count)

print(max_cnt)