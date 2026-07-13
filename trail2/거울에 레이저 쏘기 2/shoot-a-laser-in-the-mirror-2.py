n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())


# start = 0 ~ 3
start = (k // n)
if k % n == 0:
    start -= 1
x = 0
y = 0

line = (k % n) - 1
if line == -1:
    line = n - 1

#경우의 수를 나눠보자
# / 일때, \ 일때
# 방향은 상 우 하 좌 0 1 2 3


#어느 칸으로 이동하는지
# / 일 때 상 -> 좌, 우 -> 하, 하 -> 우, 좌 -> 상
dxs_A, dys_A = [0, 1, 0, -1], [-1, 0, 1, 0]

# 다음 칸에 어떤 방향으로 들어가는지를 표시해야 함!!
vetor_A = [1,0,3,2]

# \ 일 때 상 -> 우, 우 -> 상, 하 -> 좌, 좌 -> 하
dxs_B, dys_B = [0, -1, 0, 1], [1, 0, -1, 0]

vetor_B = [3,2,1,0] # 

if start == 0:
    x = 0
    y = line
if start == 1:
    x = line
    y = n - 1
if start == 2:
    x = n -1
    y = n - line -1
if start == 3:
    x = n - line -1
    y = 0

def is_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

cnt = 0

while(1):
    if is_range(x, y):
        if grid[x][y] == "/":
            cnt += 1
            x += dxs_A[start]
            y += dys_A[start]
            start = vetor_A[start]

        elif grid[x][y] == "\\":
            cnt += 1
            x += dxs_B[start]
            y += dys_B[start]
            start = vetor_B[start]
    else:
        break

print(cnt)



    
