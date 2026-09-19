n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

visited = [[False for _ in range(m)] for _ in range(n)]

dist_grid = [[-1 for _ in range(m)] for _ in range(n)]


dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]


cnt = 0

def is_range(x,y):
    return 0 <= x < n and 0 <= y < m and a[x][y] == 1





def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    dist_grid[0][0] = 0
    

    while(q):
        x , y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if is_range(nx, ny) and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
                dist_grid[nx][ny] = dist_grid[x][y] + 1

            

bfs()



print(dist_grid[n - 1][m - 1])