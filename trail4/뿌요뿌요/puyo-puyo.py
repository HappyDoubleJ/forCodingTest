n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

cnt = 0
result = []

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

check = [[0 for _ in range(n)] for _ in range(n)]


def can_go(x,y):

    return 0 <= x < n and 0 <= y < n and check[x][y] == 0


def go(x,y,N):
    global cnt



    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if can_go(nx,ny) and grid[nx][ny] == N:
            check[nx][ny] = 1
            cnt += 1
            go(nx, ny, N)





for i in range(n):
    for j in range(n):
        k = grid[i][j]
        if check[i][j] == 0:
            cnt = 1
            check[i][j] = 1
            go(i,j,k)
            if cnt != 0:
                result.append(cnt)

bomb_cnt = 0
for a in result:
    if a >= 4:
        bomb_cnt += 1



print(bomb_cnt, max(result))

