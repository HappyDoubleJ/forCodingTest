n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())


from collections import deque
import sys

temp_grid = [[0 for _ in range(n)] for _ in range(n)]


wall = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            wall.append((i,j))




selected = []

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

# Please write your code here.


dxs , dys  = [-1, 1, 0, 0], [0, 0, -1, 1]

def is_range(x,y):
    return 0 <= x < n and 0 <= y < n and temp_grid[x][y] != 1


def bfs():

    dist_grid = [[-1 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    dist_grid[r1][c1] = 0
    

    q = deque()

    q.append((r1,c1))
    visited[r1][c1] = True

    while(q):

        x,y = q.popleft()
        for dx , dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if is_range(nx,ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))
                dist_grid[nx][ny] = dist_grid[x][y] + 1
    
    return dist_grid[r2][c2]
                






min_cnt = sys.maxsize



def choose(start, cnt):
    global min_cnt

    if cnt == k:
        for i in range(n):
            for j in range(n):
                temp_grid[i][j] = grid[i][j]
        for x, y in selected:
            temp_grid[x][y] = 0
        temp_cnt = bfs()
        if temp_cnt != -1:
            min_cnt = min(temp_cnt, min_cnt)
        return


    for i in range(start, len(wall)):
        selected.append(wall[i])
        choose(i + 1, cnt + 1)
        selected.pop()

choose(0,0)


if min_cnt == sys.maxsize:
    min_cnt = -1
print(min_cnt)
    





