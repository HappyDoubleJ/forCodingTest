n, m, r, c = map(int, input().split())


grid = [[0 for _ in range(n)] for _ in range(n)]

grid[r - 1][c - 1] = 1

temp_grid = [[*row] for row in grid]

def is_range(x,y):
    return 0 <= x < n and 0 <= y < n




def bomb(second):
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    #아래
                    if is_range(i + 1 *(2 ** (second -1)), j):
                        temp_grid[i + 1 *(2 ** (second -1))][j] = 1
                    
                    #위
                    if is_range(i - 1 *(2 ** (second -1)), j):
                        temp_grid[i - 1 *(2 ** (second -1))][j] = 1
                    
                    #좌
                    if is_range(i, j - 1 *(2 ** (second -1))):
                        temp_grid[i][j - 1 *(2 ** (second -1))] = 1
                    
                    #우
                    if is_range(i, j + 1 *(2 ** (second -1))):
                        temp_grid[i][j + 1 *(2 ** (second -1))] = 1
        for i in range(n):
            for j in range(n):
                grid[i][j] = temp_grid[i][j]



#반복
for i in range(1, m + 1):
    bomb(i)


cnt = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            cnt += 1

print(cnt)