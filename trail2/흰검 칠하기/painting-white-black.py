n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# 인덱스에 + 100 씩 하기(현재 위치와 이동할 위치)
current = 100000
# 객체 만들어서, 색과 카운트를 넣기


b_cnt_sum = 0
w_cnt_sum = 0
g_cnt_sum = 0

class something:
    def __init__ (self, col, b_cnt, w_cnt):
        self.col = col
        self.b_cnt = b_cnt
        self.w_cnt = w_cnt


somethings = [something('-', 0,0) for _ in range(200000)]

def painting (amount, direction):
    global current
    if direction == 'R':
        for i in range(current, current + amount):
            somethings[i].col = 'B'
            somethings[i].b_cnt += 1
        current = current + amount - 1
    else:
        for i in range(current, current - amount, -1):
            somethings[i].col = 'W'
            somethings[i].w_cnt += 1
        current = current - amount + 1

for i in range(n):
    painting(x[i], dir[i])

for i in somethings:
    if i.b_cnt >= 2 and i.w_cnt >= 2:
        i.col = 'G'


for i in somethings:
    if i.col == 'B':
        b_cnt_sum += 1
    if i.col == 'W':
        w_cnt_sum += 1
    if i.col == 'G':
        g_cnt_sum += 1

print(f"{w_cnt_sum} {b_cnt_sum} {g_cnt_sum}")