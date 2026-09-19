from collections import deque


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = []

melt = []

cnt = 0

last_cnt = 0

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]


def is_range(x, y):
    return 0 <= x < n and 0 <= y < m and not visited[x][y] 


def bfs():
    start = deque()
    temp_cnt = 0
    global melt, visited
    visited =  [[False for _ in range(m)] for _ in range(n)]
    melt_check = [[False for _ in range(m)] for _ in range(n)]
    melt = []
    start.append((0,0))
    visited[0][0] = True

    while(start):
        tx , ty = start.popleft()

        for dx, dy in zip(dxs, dys):
            nx = tx + dx
            ny = ty + dy
            if is_range(nx, ny) and a[nx][ny] == 0:
                start.append((nx,ny))
                visited[nx][ny] = True
            if is_range(nx, ny) and a[nx][ny] == 1 and melt_check[nx][ny] == 0:
                melt.append((nx,ny))
                melt_check[nx][ny] = 1

    return len(melt)

    


while(1):

    last_cnt = bfs()
    if last_cnt != 0:
        last = last_cnt
    else:
        break
    for x, y in melt:
        a[x][y] = 0
    cnt += 1


print(cnt,last)
