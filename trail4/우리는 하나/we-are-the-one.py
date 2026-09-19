n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

from collections import deque

max_cnt = -1

start = []


dxs, dys = [-1, 1, 0, 0], [0, 0 , -1, 1]



def is_range(x,y):
    return 0 <= x < n and 0 <= y < n



def bfs():
    global start
    cnt = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque()
    for x,y in start:
        q.append((x,y))
        visited[x][y] =True

    while(q):
        x , y = q.popleft()
        for dx, dy in zip(dxs, dys):
            

            nx = x + dx
            ny = y + dy
            
            if is_range(nx, ny):
                if not visited[nx][ny] and u <= abs(grid[x][y] - grid[nx][ny]) <= d:
                    q.append((nx,ny))
                    visited[nx][ny] = True
    
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += 1

    return cnt

                


def choose(cnt):

    global max_cnt

    if cnt == k:

        temp_cnt = bfs()
        max_cnt = max(temp_cnt, max_cnt)
        return
    
    for i in range(n):
        for j in range(n):

            start.append((i,j))
            choose(cnt + 1)
            start.pop()



choose(0)

print(max_cnt)