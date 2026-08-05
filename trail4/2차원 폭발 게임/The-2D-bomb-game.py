import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
mark_grid = [[0] * n for _ in range(n)]

def mark(standard):
    found = False
    for col in range(n):
        row = 0
        while row < n:
            if grid[row][col] == 0:      # 빈칸은 건너뛴다
                row += 1
                continue
            end = row
            while end < n and grid[end][col] == grid[row][col]:
                end += 1
            if end - row >= standard:
                for r in range(row, end):
                    mark_grid[r][col] = 1
                found = True
            row = end
    return found

def bomb():
    for i in range(n):
        for j in range(n):
            if mark_grid[i][j]:
                grid[i][j] = 0
                mark_grid[i][j] = 0      # 표시는 여기서 바로 초기화

def align():
    for col in range(n):
        target = n - 1
        for row in range(n - 1, -1, -1):
            if grid[row][col] != 0:
                grid[target][col] = grid[row][col]
                target -= 1
        for row in range(target, -1, -1):
            grid[row][col] = 0           # 남은 위쪽은 비운다

def rotate():
    buf = [[grid[n - 1 - j][i] for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            grid[i][j] = buf[i][j]
    align()

while True:
    while mark(m):
        bomb()
        align()
    if k > 0:
        rotate()
        k -= 1
    else:
        break

print(sum(1 for i in range(n) for j in range(n) if grid[i][j] != 0))