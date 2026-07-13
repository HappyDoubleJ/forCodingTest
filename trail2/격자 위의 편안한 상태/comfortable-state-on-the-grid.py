n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]


# Please write your code here.

# 격자 만들기
matrix = [[0 for _ in range (n)] for _ in range (n)]

def in_range(x,y):
    return 0 <= x - 1 and x - 1 < n and 0 <= y - 1 and y - 1 < n

def is_blue(x,y):
    return in_range(x,y) and matrix[x - 1][y - 1] == 1

for x, y in points:
    cnt = 0
    if in_range(x, y):
        matrix[x - 1][y - 1] = 1
    if is_blue(x + 1, y):
        cnt += 1
    if is_blue(x - 1, y):
        cnt += 1
    if is_blue(x, y + 1):
        cnt += 1
    if is_blue(x, y - 1):
        cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)
        
