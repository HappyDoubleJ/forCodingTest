N, M, K = map(int, input().split())

current_x = 0
current_y = 0
size = 1
cnt = 0

x, y = [], []
for _ in range(M):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

d, p = [], []
for _ in range(K):
    di, pi = input().split()
    d.append(di)
    p.append(int(pi))


grid = [[0 for _ in range(N)] for _ in range(N)]

grid[0][0] = 1

for i in range(M):
    grid[x[i] - 1][y[i] - 1] = -1

def is_range(a, b):
    return 0 <= a < N and 0 <= b < N

def is_not_body(a,b):
    return grid[a][b] <= 1


def is_apple(a,b):
    return grid[a][b] == -1    

# 겹치고, tail이 아니면 종료


#꼬리부터 머리까지 1씩 늘려나가기

#원래는 꼬리를 없애고, 이동한 흔적에 



magic = {
    'U' : 0,
    'D' : 1,
    'L' : 2,
    'R' : 3
}


dxs, dys = [-1, 1, 0, 0] , [0, 0, -1, 1]


def move(way,length):
    global current_x
    global current_y
    global size
    global cnt

    for i in range(length):
        if is_range(current_x + dxs[magic[way]],current_y + dys[magic[way]]) and is_not_body(current_x + dxs[magic[way]],current_y + dys[magic[way]]):
            if is_apple(current_x + dxs[magic[way]],current_y + dys[magic[way]]) and is_not_body(current_x + dxs[magic[way]],current_y + dys[magic[way]]):
                grid[current_x + dxs[magic[way]]][current_y + dys[magic[way]]] = grid[current_x][current_y] + 1
                size += 1
            else:
                grid[current_x + dxs[magic[way]]][current_y + dys[magic[way]]] = grid[current_x][current_y] + 1
                for j in range(N):
                    for k in range(N):
                        if grid[j][k] > 0:
                            grid[j][k] -= 1
            current_x = current_x + dxs[magic[way]]
            current_y = current_y + dys[magic[way]]
            cnt += 1
        else: 
            cnt += 1
            return True




for i in range(K):
    end = move(d[i],p[i])

    if end:
        break
    


print(cnt)       


        