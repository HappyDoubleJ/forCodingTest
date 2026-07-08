n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]


dxs , dys = [0, 1, 0, -1] , [1, 0, -1, 0]

x , y = 0, 0
dir_num = 0

arr[x][y] = 1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


for i in range (2, n*m + 1):
    nx, ny = x + dxs[dir_num] , y + dys[dir_num]
    if in_range (nx, ny) and arr[nx][ny] == 0:
        arr[nx][ny] = i
        x, y = nx , ny

    else:
        dir_num = (dir_num + 1) % 4
        nx, ny = x + dxs[dir_num] , y + dys[dir_num]
        arr[nx][ny] = i
        x, y = nx , ny


for i in range (n):
    print(*arr[i])