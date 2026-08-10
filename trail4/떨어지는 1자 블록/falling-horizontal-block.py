n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

# k ~ k + m - 1 열을 조사하는 함수

def mark(k,m):
    target = n
    for i in range(k - 1, k - 1 + m):
        for j in range(n):
            if grid[j][i] == 1:
                if j < target:
                    target = j
                break;
    return target

def paint(k,m):
    target_row = mark(k,m)

    if (target_row - 1) >= 0:
        for i in range(k - 1, k - 1 + m):
            grid[target_row - 1][i] = 1



paint(k, m)

for row in grid:
    print(*row)