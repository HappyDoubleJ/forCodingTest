n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


count_grid = [[-1 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 3:
            count_grid[i][j] = 0
# Please write your code here.


from collections import deque


visited = [[False for _ in range(n)] for _ in range(n)]

dxs, dys = [-1, 1, 0, 0] , [0, 0, -1, 1]

def is_range(x,y):
    return 0 <= x < n and 0 <= y < n and grid[x][y] != 1

def bfs():

    q = deque()

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 3:
                q.append((i,j))
                visited[i][j] = True
    

    while(q):

        x,y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if is_range(nx,ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))
                count_grid[nx][ny] = count_grid[x][y] + 1



bfs()

for i in range(n):
    for j in range(n):
        if grid[i][j] != 2:
            count_grid[i][j] = 0

for row in count_grid:
    print(*row)








#쉼터를 기준으로 bfs를 한다?
#그러면, 쉼터 가 에서 가장 가까운 사람 A를 선택했을 때,
# 쉼터 나 에서 가장 까운 사람이 B인데 이게 더 거리가 가까우면 어떻게 되는거지..?
# 이것도 쉼터 별로 bfs를 해서 여러번 돌리는 거라, 이 방법을 말하는 게 아닌가 봄..
