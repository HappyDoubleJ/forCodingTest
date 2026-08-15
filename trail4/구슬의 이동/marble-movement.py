n, m, t, k = map(int, input().split())

r, c, d, v = [], [], [], []
for _ in range(m):
    ri, ci, di, vi = input().split()
    r.append(int(ri))
    c.append(int(ci))
    d.append(di)
    v.append(int(vi))

# Please write your code here.

#구슬에 속도를 써놓기
marble_grid = [[[] for _ in range(n)] for _ in range(n)]


def is_range(x,y):
    return 0 <= x < n and 0 <= y < n



for i in range(m):
    marble_grid[r[i] - 1][c[i] - 1].append((i, d[i], v[i]))




mapping = {
    'U' : 0,
    'L' : 1,
    'D' : 2,
    'R' : 3
}

reverse_mapping = {
    0 : 'U',
    1 : 'L',
    2 : 'D',
    3 : 'R'
}


dxs, dys = [-1, 0 , 1, 0] , [0, -1, 0, 1]


def move():
    temp_marble_grid = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for number, direction, vector in marble_grid[i][j]:
                
                target_x = i
                target_y = j
                for l in range(vector):
                    if is_range(target_x + dxs[mapping[direction]], target_y + dys[mapping[direction]]):
                        target_x , target_y = target_x + dxs[mapping[direction]] , target_y + dys[mapping[direction]]
                        
                    else:
                        direction = reverse_mapping[(mapping[direction] + 2) % 4]
                        target_x , target_y = target_x + dxs[mapping[direction]] , target_y + dys[mapping[direction]]
    
                temp_marble_grid[target_x][target_y].append((number, direction, vector))
    
    #정렬하기
    for i in range(n):
        for j in range(n):
            temp_marble_grid[i][j].sort(key = lambda x : (-x[2], -x[0]))
    for i in range(n):
        for j in range(n):
            if len(temp_marble_grid[i][j]) > k:
                for l in range(len(temp_marble_grid[i][j]) - k):
                    temp_marble_grid[i][j].pop()
    
    #다시 복붙
    for i in range(n):
        for j in range(n):
            marble_grid[i][j] = temp_marble_grid[i][j]
    



for i in range(t):
    move()



cnt = 0

for i in range(n):
    for j in range(n):
        cnt += len(marble_grid[i][j])


print(cnt)


