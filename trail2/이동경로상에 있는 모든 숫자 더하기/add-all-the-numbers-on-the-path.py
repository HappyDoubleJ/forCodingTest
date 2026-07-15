N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

#상 우 하 좌

dxs, dys = [-1, 0, 1, 0] , [0, 1, 0, -1]

vector = 0


def in_range(x,y):
    return 0 <= x and x < N and  0 <= y and y < N


x, y = N // 2, N // 2

result = board[x][y]

for i in range(T):
    if str[i] == 'F':
        if in_range(x + dxs[vector], y + dys[vector]):
            x += dxs[vector]
            y += dys[vector]
            result += board[x][y]
    if str[i] == 'L':
        vector = (vector + 3) % 4
    if str[i] == 'R':
        vector = (vector + 1) % 4

print(result)
        

