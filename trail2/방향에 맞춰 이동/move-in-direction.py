n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

dx = [-1, 0, 0, +1]
dy = [0, -1, +1, 0]

x = 0
y = 0

for i in range(n):
    if dir[i] == 'W':
        x = x + dist[i] * dx[0]
        y = y + dist[i] * dy[0]
    if dir[i] == 'S':
        x = x + dist[i] * dx[1]
        y = y + dist[i] * dy[1]
    if dir[i] == 'N':
        x = x + dist[i] * dx[2]
        y = y + dist[i] * dy[2]
    if dir[i] == 'E':
        x = x + dist[i] * dx[3]
        y = y + dist[i] * dy[3]

print(x , y)