n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


cnt = 0
max = 0
#ㄴ 자 ㄱ 자 그 반대, 또 그 반대. 

def module_A(a, b, grid_a):
    global cnt
    global max
    cnt = grid_a[a][b] +grid_a[a + 1][b + 1] + grid_a[a + 1][b]
    if cnt >= max:
        max = cnt
    cnt = 0

    
def module_B(a, b, grid_a):
    global cnt
    global max
    cnt = grid_a[a][b] +grid_a[a][b + 1] + grid_a[a + 1][b + 1]
    if cnt >= max:
        max = cnt
    cnt = 0

def module_C(a, b, grid_a):
    global cnt
    global max
    cnt = grid_a[a][b] +grid_a[a][b + 1] + grid_a[a + 1][b]
    if cnt >= max:
        max = cnt
    cnt = 0

def module_D(a, b, grid_a):
    global cnt
    global max
    cnt = grid_a[a + 1][b] +grid_a[a + 1][b + 1] + grid_a[a][b + 1]
    if cnt >= max:
        max = cnt
    cnt = 0

# - 자 | 자

# - 자 
def module_E(grid_a):
    global cnt
    global max
    for i in range(n):
        for j in range(m - 2):
            cnt = 0
            for k in range(j, j + 3):
                cnt += grid_a[i][k]
            if cnt >= max:
                max = cnt

def module_F(grid_a):
    global cnt
    global max
    for i in range(m):
        for j in range(n - 2):
            cnt = 0
            for k in range(j, j + 3):
                cnt += grid_a[k][i]
            if cnt >= max:
                max = cnt




def iterating(grid_a):
    for i in range(n - 1):
        for j in range(m - 1):
            module_A(i ,j, grid_a)
            module_B(i ,j, grid_a)
            module_C(i ,j, grid_a)
            module_D(i ,j, grid_a)



    
module_E(grid)
module_F(grid)
iterating(grid)

print(max)