n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


def is_range(x,y):
    return 0 <= x <n and 0 <= y < n

def swap(x, y):
    target_x = 0
    target_y = 0
    max = 0
    if is_range(x + 1, y) and grid[x + 1][y] > max:
        max = grid[x + 1][y]
        target_x = x + 1
        target_y = y

    if is_range(x - 1, y) and grid[x - 1][y] > max:
        max = grid[x - 1][y]
        target_x = x - 1
        target_y = y
    
    if is_range(x + 1, y + 1) and grid[x + 1][y + 1] > max:
        max = grid[x+1][y + 1]
        target_x = x + 1
        target_y = y + 1
    
    if is_range(x + 1, y - 1) and grid[x + 1][y - 1] > max:
        max = grid[x+1][y - 1]
        target_x = x + 1
        target_y = y - 1
    
    if is_range(x - 1, y + 1) and grid[x - 1][y + 1] > max:
        max = grid[x-  1][y + 1]
        target_x = x - 1
        target_y = y + 1

    if is_range(x - 1, y - 1) and grid[x - 1][y - 1] > max:
        max = grid[x - 1][y - 1]
        target_x = x - 1
        target_y = y - 1


    if is_range(x, y + 1) and grid[x][y + 1] > max:
        max = grid[x][y + 1]
        target_x = x
        target_y = y + 1

    if is_range(x, y -1 ) and grid[x][y - 1] > max:
        max = grid[x][y - 1]
        target_x = x
        target_y = y - 1
    
    grid[x][y], grid[target_x][target_y] = grid[target_x][target_y] , grid[x][y]


 
for l in range(m):
    for i in range(1, n * n + 1):
        cnt = 0
        for j in range(n):
            for k in range(n):
                if cnt == 0 and grid[j][k] == i:
                    swap(j, k)
                    cnt += 1
        cnt = 0

for row in grid:
    print(*row)
