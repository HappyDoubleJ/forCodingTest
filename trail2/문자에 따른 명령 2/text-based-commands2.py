dirs = input()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

start = 1
x,y = 0 , 0
for i in range(len(dirs)):
    if dirs[i] == 'L':
        start = (start + 1) % 4
    if dirs[i] == 'R':
        start = (start + 3) % 4
    if dirs[i] == 'F':
        x += dx[start]
        y += dy[start]

print (x, y)