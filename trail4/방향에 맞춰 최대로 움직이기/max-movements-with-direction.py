n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())





result = []

max_score = 0

dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1] , [0, 1, 1, 1, 0, -1, -1, -1]

def is_range(x,y):
    return 0 <= x < n and 0 <= y < n





def move(x,y):
    global max_score


    max_score = max(max_score, len(result))
    
    
    
    for i in range(1, n):


        if not is_range(x - 1 + i * dxs[move_dir[x - 1][y - 1] - 1], y - 1 + i * dys[move_dir[x - 1][y - 1] - 1]) or num[x - 1 + i * dxs[move_dir[x - 1][y - 1] - 1]][y - 1 + i * dys[move_dir[x - 1][y - 1] - 1]] <= num[x -1][y - 1]:
            continue
        result.append((x - 1 + i * dxs[move_dir[x - 1][y - 1] - 1], y - 1 + i * dys[move_dir[x - 1][y - 1] - 1]))
        move(x + i * dxs[move_dir[x - 1][y - 1] - 1], y + i * dys[move_dir[x - 1][y - 1] - 1])
        result.pop()


move(r,c)

print(max_score)