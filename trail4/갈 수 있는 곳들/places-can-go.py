from collections import deque

n, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

points = [tuple(map(int, input().split())) for _ in range(k)]

temp_grid = [[0 for _ in range(n)] for _ in range(n)]

cnt = 0

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def is_range(x, y):
    return (
        0 <= x < n
        and 0 <= y < n
        and temp_grid[x][y] == 0
        and grid[x][y] == 0
    )


def bfs(x, y):
    global cnt

    queue = deque()

    queue.append((x, y))

    while queue:

        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):

            nx = x + dx
            ny = y + dy

            if is_range(nx, ny):

                temp_grid[nx][ny] = 1
                cnt += 1

                queue.append((nx, ny))


for x, y in points:

    x -= 1
    y -= 1

    if is_range(x, y):

        temp_grid[x][y] = 1
        cnt += 1

        bfs(x, y)


print(cnt)