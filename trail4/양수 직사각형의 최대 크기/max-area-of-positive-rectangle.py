n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def is_y (x1, y1, x2, y2):
    for i in range (x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if grid[i][j] <= 0:
                return False
    return True


def cnt_size (x1, y1, x2, y2):
    cnt = 0
    for i in range (x1, x2 + 1):
        for j in range(y1, y2 + 1):
            cnt += 1
    return cnt  


max_cnt = -1

for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                current_cnt = cnt_size(i,j,k,l)
                if is_y(i,j,k,l):
                    max_cnt = max(max_cnt, current_cnt)


print(max_cnt)



