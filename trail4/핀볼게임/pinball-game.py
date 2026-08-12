n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]



max = 0





# Please write your code here.

#어느쪽에서 가는지로
#위에서, 아래에서, 왼쪽에서, 오른쪽에서
dxs, dys = [1, -1, 0, 0] , [0, 0,1, -1 ]



# / 
def slash(from_):
    if from_ == 0:
        return 3
    if from_ == 1:
        return 2
    if from_ == 2:
        return 1
    if from_ == 3:
        return 0


def inverse_slash(from_):
    if from_ == 0:
        return 2
    if from_ == 1:
        return 3
    if from_ == 2:
        return 0
    if from_ == 3:
        return 1

def is_range(x,y):
    return 0 <= x < n and 0 <= y < n

def run(x, y, from__):
    current_x = x
    current_y = y
    current_from = from__
    cnt = 0
    while(1):
        if is_range(current_x + dxs[current_from], current_y + dys[current_from]):
            if grid[current_x + dxs[current_from]][current_y + dys[current_from]] == 0:
                current_x, current_y = current_x + dxs[current_from] , current_y + dys[current_from]

            elif grid[current_x + dxs[current_from]][current_y + dys[current_from]] == 1:
                current_x, current_y = current_x + dxs[current_from] , current_y + dys[current_from]
                current_from = slash(current_from)

            elif grid[current_x + dxs[current_from]][current_y + dys[current_from]] == 2:
                current_x, current_y = current_x + dxs[current_from] , current_y + dys[current_from]
                current_from = inverse_slash(current_from)
            cnt += 1
        else:
            cnt +=1
            break
    return cnt
            
    


#열
for i in range(n):
    #행
    c_cnt = run(-1, i, 0)

    if max < c_cnt:
        max = c_cnt


for i in range(n):

    c_cnt = run(n, i, 1)

    if max < c_cnt:
        max = c_cnt


for i in range(n):

    c_cnt = run (i, -1, 2)

    if max < c_cnt:
        max = c_cnt


for i in range(n):

    c_cnt = run (i, n, 3)

    if max < c_cnt:
        max = c_cnt



print(max)