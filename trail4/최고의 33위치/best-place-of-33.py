n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
max = 0

#내부 함수
def counting(start_x, start_y, grid_A):
    global cnt
    for i in range(start_x, start_x + 3):
        for j in range(start_y, start_y + 3):
            if grid_A[i][j] == 1:
                cnt += 1


# 
def iterating(grid_A):
    global max
    global cnt
    for i in range(n - 2):
        for j in range (n - 2):
            cnt = 0
            counting(i, j, grid_A)
            if cnt >= max:
                max = cnt

    return max

print(iterating(grid))
