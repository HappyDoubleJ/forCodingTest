n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

def is_range(current_row):
    return 0 <= current_row and current_row < n

def check_up(current_row):
    for i in range(m):
        if a[current_row - 1][i] == a[current_row][i]:
            return True
    return False

def check_down(current_row):
    for i in range(m):
        if a[current_row + 1][i] == a[current_row][i]:
            return True
    return False

def change_wind(vec):
    if vec == 'R':
        return 'L'
    else: return 'R'


#오른쪽으로 부는 바람
def right_go_wind(row):
    temp = a[row][m - 1]
    for i in range(m - 1, -1, -1):
        a[row][i] = a[row][i - 1]
    a[row][0] = temp

#왼쪽으로 부는 바람
def left_go_wind(row):
    temp = a[row][0]
    for i in range(m - 1):
        a[row][i] = a[row][i + 1]
    a[row][m - 1] = temp

def move(chr, row):
    if chr == 'R' :
        left_go_wind(row)
    if chr == 'L' :
        right_go_wind(row)    

def move_up(way, row):
    while(1):
        if is_range(row - 1) and check_up(row):
            move(way, row - 1)
            way = change_wind(way)
            row -= 1
        else: break

def move_down(way, row):
    while(1):
        if is_range(row + 1) and check_down(row):
            move(way, row + 1)
            way = change_wind(way)
            row += 1
        else: break


for i in range(q):
    start_row = winds[i][0] - 1
    start_wind = winds[i][1]
    if is_range(start_row):
        move(start_wind, start_row)
        changed_wind = change_wind(start_wind)
        move_up(changed_wind, start_row)
        move_down(changed_wind, start_row)

     
for row in a:
    print(*row)




