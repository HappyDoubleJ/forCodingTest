n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, d = map(int, input().split())
r -= 1
c -= 1

dx, dy = [-1, -1, 1, 1], [1, -1, -1, 1]

path = []
x, y = r, c
for leg, length in zip((0, 1, 2, 3), (m1, m2, m3, m4)):
    for _ in range(length):
        path.append((x, y))
        x += dx[leg]
        y += dy[leg]

vals = [grid[i][j] for i, j in path]
if d == 0:
    vals = vals[-1:] + vals[:-1]   # 반시계: 경로 다음 칸으로 밀기
else:
    vals = vals[1:] + vals[:1]     # 시계: 경로 이전 칸으로 밀기

for (i, j), v in zip(path, vals):
    grid[i][j] = v

for row in grid:
    print(*row)