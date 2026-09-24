n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


def is_range(x,y):
    return 0 <= x < n and 0 <= y < n



#dp[i][j] = 최대 칸의 수.


#그냥idx를 해당 칸의 값 순으로 내림차순 정렬을 하기
#근데 어떻게 묶지..?

cells = []

for i in range(n):
    for j in range(n):
        cells.append((grid[i][j], i, j))

cells.sort(reverse=True)


dp = [[1] * n for _ in range(n)]


dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

for value, x, y in cells:
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        
        if is_range(nx, ny) and grid[nx][ny] > grid[x][y]:
            dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)


ans = 0

for i in range(n):
    for j in range(n):
        ans = max(ans, dp[i][j])

print(ans)
        
