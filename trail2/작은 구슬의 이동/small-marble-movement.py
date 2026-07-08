n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# 실제 행 열은 -1 해줘야 함.


dxs, dys = [-1, 0, 1, 0] , [0, 1, 0, -1]
mapper = {
    'U' : 0,
    'D' : 2,
    'R' : 1,
    'L' : 3
}

start = mapper[d]
x = r
y = c

def isEnd (a, b):
    return a < 1 or a > n or b < 1 or b > n

while(1):
    if not isEnd(x + dxs[start] , y + dys[start]):
        x, y = x + dxs[start] , y + dys[start]
        t -= 1
    else:
        start = (start + 2) % 4
        t -= 1
    if t == 0:
        print(x, y)
        break
        
    