n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

result = 0

# Please write your code here.


visited= [[False for _ in range(m)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def can_go(x,y):

    return in_range(x,y) and grid[x][y] == 1 and not visited[x][y] 



dxs, dys = [1, 0] , [0, 1]




def run(x, y):
    global result

    if x == n - 1 and y == m - 1:
        result = 1
        return



    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy
        if can_go(next_x, next_y):
            visited[next_x][next_y] = True
            run(next_x, next_y)
            
            


run(0, 0)
print(result)


