import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


def solve(x, y):
    b = [row[:] for row in grid]

    # 1) 폭발 — 십자 크기는 선택한 칸에 적힌 숫자 (값 v -> 각 방향으로 v-1칸)
    size = b[x][y]
    for i in range(size):
        for nx, ny in ((x - i, y), (x + i, y), (x, y - i), (x, y + i)):
            if 0 <= nx < n and 0 <= ny < n:
                b[nx][ny] = 0

    # 2) 중력 — 각 열의 숫자를 아래로
    for c in range(n):
        col = [b[r][c] for r in range(n) if b[r][c]]
        col = [0] * (n - len(col)) + col
        for r in range(n):
            b[r][c] = col[r]

    # 3) 상하좌우로 인접한 같은 숫자 쌍의 개수 (덩어리 크기와 무관)
    cnt = 0
    for r in range(n):
        row = b[r]
        below = b[r + 1] if r + 1 < n else None
        for c in range(n):
            v = row[c]
            if not v:
                continue
            if c + 1 < n and row[c + 1] == v:
                cnt += 1
            if below is not None and below[c] == v:
                cnt += 1
    return cnt


print(max(solve(i, j) for i in range(n) for j in range(n)))