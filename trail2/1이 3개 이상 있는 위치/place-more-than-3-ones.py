n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [1, 0, -1, 0] , [0, 1, 0, -1]

def isValid (a,b):
    return (0 <= a <= n - 1) and (0<= b <= n - 1)

cnt = 0

for i in range(n):
    for j in range(n):
        cnt_one = 0
        for dx, dy in zip(dxs, dys):
            if isValid(i + dx, j + dy) and grid[i + dx][j + dy] == 1:
                cnt_one += 1
        if cnt_one >= 3:
            cnt += 1

print(cnt)





