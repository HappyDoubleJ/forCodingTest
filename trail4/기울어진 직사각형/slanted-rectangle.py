n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 1번: ↗, 2번: ↖, 3번: ↙, 4번: ↘
dirs = [(-1, 1), (-1, -1), (1, -1), (1, 1)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_rect_sum(x, y, len1, len2):
    total = 0
    lengths = [len1, len2, len1, len2]

    for d in range(4):
        dx, dy = dirs[d]

        for _ in range(lengths[d]):
            x += dx
            y += dy

            if not in_range(x, y):
                return -1

            total += grid[x][y]

    return total

answer = 0

for x in range(n):
    for y in range(n):
        for len1 in range(1, n):
            for len2 in range(1, n):
                answer = max(answer, get_rect_sum(x, y, len1, len2))

print(answer)