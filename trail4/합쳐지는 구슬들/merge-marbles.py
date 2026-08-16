n, m, t = map(int, input().split())

mapping = {
    'U': 0,
    'L': 1,
    'D': 2,
    'R': 3
}

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def is_range(x, y):
    return 0 <= x < n and 0 <= y < n


# 빈 칸은 None
# 구슬이 있는 칸은 (번호, 무게, 방향)
marble_grid = [[None for _ in range(n)] for _ in range(n)]


for number in range(m):
    r, c, d, w = input().split()

    r = int(r) - 1
    c = int(c) - 1
    w = int(w)
    d = mapping[d]

    marble_grid[r][c] = (number, w, d)


def move():
    temp_marble_grid = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):

            # 구슬 없는 칸
            if marble_grid[i][j] is None:
                continue

            current_number, current_weight, current_direction = marble_grid[i][j]

            nx = i + dxs[current_direction]
            ny = j + dys[current_direction]

            # 벽에 부딪힌 경우
            if not is_range(nx, ny):
                current_direction = (current_direction + 2) % 4

                nx = i
                ny = j

            # 이동한 칸에 아무 구슬도 없다면
            if temp_marble_grid[nx][ny] is None:
                temp_marble_grid[nx][ny] = (
                    current_number,
                    current_weight,
                    current_direction
                )

            # 이미 구슬이 있다면 합치기
            else:
                prev_number, prev_weight, prev_direction = temp_marble_grid[nx][ny]

                # 무게 합치기
                current_weight += prev_weight

                # 번호가 더 큰 구슬의 방향 사용
                if prev_number > current_number:
                    current_number = prev_number
                    current_direction = prev_direction

                temp_marble_grid[nx][ny] = (
                    current_number,
                    current_weight,
                    current_direction
                )

    return temp_marble_grid


for _ in range(t):
    marble_grid = move()


cnt = 0
max_w = -1

for i in range(n):
    for j in range(n):
        if marble_grid[i][j] is not None:
            cnt += 1

            number, weight, direction = marble_grid[i][j]
            max_w = max(max_w, weight)


print(cnt, max_w)