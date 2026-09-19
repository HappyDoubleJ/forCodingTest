n = int(input())
r1, c1, r2, c2 = map(int, input().split())

# Please write your code here.

from collections import deque



dxs = [-2, -2, -1, -1,  1, 1,  2, 2] 
dys = [-1,  1, -2,  2, -2, 2, -1, 1] 

visited = [[False for _ in range(n)] for _ in range(n)]
cnt_grid = [[-1 for _ in range(n)] for _ in range(n)]

def is_range(x,y):
    return 0 <= x < n and 0 <= y < n


def bfs():
    q = deque()

    q.append((r1 - 1,c1 - 1))
    visited[r1 - 1][c1 - 1] = True
    cnt_grid[r1 - 1][c1 - 1] = 0

    while(q):

        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if is_range(nx, ny) and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
                cnt_grid[nx][ny] = cnt_grid[x][y] + 1
    



bfs()

print(cnt_grid[r2 - 1][c2 - 1])





