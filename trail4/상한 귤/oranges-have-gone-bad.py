n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]



from collections import deque

bad = []


visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            bad.append((i,j))


time_grid = [[-2 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            time_grid[i][j] = 0


dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def is_range(x,y):
    return 0 <= x <n and 0 <= y < n


def bfs():
    q = deque()

    for a,b in bad:
        q.append((a,b))
        visited[a][b] = True

    while(q):

        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = dx + x
            ny = dy + y
            if is_range(nx,ny) and not visited[nx][ny] and grid[nx][ny] != 0:
                q.append((nx,ny))
                visited[nx][ny] = True
                time_grid[nx][ny] = time_grid[x][y] + 1
            


bfs()

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            time_grid[i][j] = -1


for row in time_grid:
    print(*row)
