n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

from collections import deque


exist = 0

q = deque()

# Please write your code here.
def can_go(x, y):
    return 0 <= x < n and 0 <= y < m and a[x][y] == 1 and visited[x][y] != 1

dxs, dys = [-1, 1, 0, 0], [0, 0, 1, -1]

def bfs(sx, sy):
    q.append((sx, sy))
    visited[sx][sy] = 1
    while q:
        x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            return 1
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = 1
                q.append((nx, ny))
    return 0

if can_go(0, 0):
    exist = bfs(0, 0)



print(exist)