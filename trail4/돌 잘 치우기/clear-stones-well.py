from collections import deque

n, k, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

rocks = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            rocks.append((i, j))


starts = []

for _ in range(k):
    r, c = map(int, input().split())
    starts.append((r-1, c-1))


dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]


selected = []

max_cnt = 0


# 현재 선택한 돌을 제거한 상태에서 BFS
def bfs():

    temp_grid = [row[:] for row in grid]

    # 선택한 돌 제거
    for idx in selected:
        x, y = rocks[idx]
        temp_grid[x][y] = 0


    visited = [[False]*n for _ in range(n)]

    q = deque()


    # K개의 시작점 모두 넣기 (멀티 BFS)
    for x, y in starts:
        q.append((x, y))
        visited[x][y] = True


    cnt = 0


    while q:

        x, y = q.popleft()
        cnt += 1


        for dx, dy in zip(dxs, dys):

            nx = x + dx
            ny = y + dy


            if 0 <= nx < n and 0 <= ny < n:

                if not visited[nx][ny] and temp_grid[nx][ny] == 0:

                    visited[nx][ny] = True
                    q.append((nx, ny))


    return cnt



# 돌 M개 선택하는 백트래킹
def choose(idx, cnt):

    global max_cnt


    # M개 선택 완료
    if cnt == m:

        result = bfs()

        max_cnt = max(max_cnt, result)

        return


    # 모든 돌 확인 완료
    if idx == len(rocks):
        return


    # 현재 돌 선택
    selected.append(idx)
    choose(idx + 1, cnt + 1)
    selected.pop()


    # 현재 돌 선택하지 않음
    choose(idx + 1, cnt)



choose(0, 0)

print(max_cnt)