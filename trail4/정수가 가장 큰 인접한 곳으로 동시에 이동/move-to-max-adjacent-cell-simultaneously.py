n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0] for pos in marbles]
c = [pos[1] for pos in marbles]


marble_grid = [[0 for _ in range(n)] for _ in range(n)]
temp_marble_grid = [[0 for _ in range(n)] for _ in range(n)]

cnt = 0

for i in range(m):
    marble_grid[r[i] - 1][c[i] - 1] = 1


def is_range(x,y):
    return 0 <= x < n and 0 <= y < n

def move(x,y):
    target_x = 0
    target_y = 0
    max = 0
    if is_range(x - 1, y) and a[x - 1][y] > max:
        max = a[x-1][y]
        target_x = x - 1
        target_y = y
    if is_range(x + 1, y) and a[x + 1][y] > max:
        max = a[x + 1][y]
        target_x = x + 1
        target_y = y
    if is_range(x, y - 1) and a[x][y - 1] > max:
        max = a[x][y - 1]
        target_x = x
        target_y = y - 1
    if is_range(x, y + 1) and a[x][y + 1] > max:
        max = a[x][y + 1]
        target_x = x
        target_y = y + 1
    temp_marble_grid[target_x][target_y] += 1


for l in range(t):
    for i in range(n):
        for j in range(n):
            if marble_grid[i][j] == 1:
                move(i,j)
    
    for i in range(n):
        for j in range(n):
            if temp_marble_grid[i][j] >= 2:
                temp_marble_grid[i][j] = 0
    for i in range(n):
        for j in range(n):
            marble_grid[i][j] = temp_marble_grid[i][j]
    for i in range(n):
        for j in range(n):
            temp_marble_grid[i][j] = 0

for i in range(n):
    for j in range(n):
        if marble_grid[i][j] == 1:
            cnt += 1


print(cnt)
