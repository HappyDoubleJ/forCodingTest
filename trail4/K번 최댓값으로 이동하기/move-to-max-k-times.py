from collections import deque

n, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

r, c = map(int, input().split())

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def is_range(x, y):
    return 0 <= x < n and 0 <= y < n


def check(start_x, start_y):

    temp_grid = [[0 for _ in range(n)] for _ in range(n)]

    q = deque()

    q.append((start_x, start_y))
    temp_grid[start_x][start_y] = 1

    standard = grid[start_x][start_y]

    candidates = []

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if (
                is_range(nx, ny)
                and temp_grid[nx][ny] == 0
                and grid[nx][ny] < standard
            ):
                temp_grid[nx][ny] = 1
                q.append((nx, ny))

                candidates.append((nx, ny))

    # 갈 수 있는 곳이 없다면
    if len(candidates) == 0:
        return start_x, start_y

    # 숫자가 큰 곳 우선
    # 숫자가 같으면 행 작은 곳
    # 행도 같으면 열 작은 곳
    candidates.sort(
        key=lambda pos: (
            -grid[pos[0]][pos[1]],
            pos[0],
            pos[1]
        )
    )

    return candidates[0]


r -= 1
c -= 1

for _ in range(k):

    nr, nc = check(r, c)

    # 더 이상 이동할 수 없다면 종료
    if nr == r and nc == c:
        break

    r, c = nr, nc


print(r + 1, c + 1)