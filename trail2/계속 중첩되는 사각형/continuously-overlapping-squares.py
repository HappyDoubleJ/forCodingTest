n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

paper = [[0 for i in range(200)] for i in range(200)]
cnt = 0

# 칠하기
def painting(i,x1,y1, x2,y2):
    if i % 2 == 0:
        for j in range(x1 + 100, x2 + 100):
            for k in range(y1 + 100, y2 + 100):
                paper[j][k] = 'R'
    else:
        for j in range(x1 + 100, x2 + 100):
            for k in range(y1 + 100, y2 + 100):
                paper[j][k] = 'B'


for m in range(n):
    painting(m,x1[m],y1[m], x2[m],y2[m])


for i in range(200):
    for j in range(200):
        if paper[i][j] == 'B':
            cnt += 1


print(cnt)