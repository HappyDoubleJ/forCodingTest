R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]


cnt = 0
if grid[0][0] == grid[R - 1][C - 1]:
    cnt = 0

elif grid[0][0] == 'W':
    for i in range(1, R - 2):
        for j in range(1, C - 2):
            if grid[i][j] == 'B':
                for k in range(i + 1, R - 1):
                    for l in range(j + 1, C - 1):
                        if grid[k][l] == 'W':
                            cnt += 1

elif grid[0][0] == 'B':
    for i in range(1, R - 2):
        for j in range(1, C - 2):
            if grid[i][j] == 'W':
                for k in range(i + 1, R - 1):
                    for l in range(j + 1, C - 1):
                        if grid[k][l] == 'B':
                            cnt += 1                            

print(cnt)                           