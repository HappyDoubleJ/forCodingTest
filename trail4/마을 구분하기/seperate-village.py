n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

check_grid = [[0 for _ in range(n)] for _ in range(n)]




# 좌, 하, 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


result = []

def is_range(x,y):
    return 0 <= x < n and 0 <= y < n



cnt = 0



def check(x,y):
    global cnt

    

    for i, j in zip(dxs, dys):
        nx = x + i
        ny = y + j

        if is_range(nx, ny) and grid[nx][ny] == 1:
            if check_grid[nx][ny] == 0:
                cnt += 1
                check_grid[nx][ny] = 1
                check(nx, ny)
    

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and check_grid[i][j] == 0:

            cnt = 1
            check_grid[i][j] = 1

            check(i, j)

            result.append(cnt)    


result.sort()



print(len(result))
for a in result:
    print(a)






    