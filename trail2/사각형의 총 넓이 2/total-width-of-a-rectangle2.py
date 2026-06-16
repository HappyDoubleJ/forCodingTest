n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# 원점을 100,100으로 잡아야 됨. 모든 좌표 입력 값에도 +100할거임

paper = [[0 for _ in range(201)] for _ in range(201)]
cnt = 0


for i in range(n):
    #x1부터 x2 행의 y1부터 y2 열을 칠하면 됨.
    for j in range (x1[i] + 100, x2[i] + 100):
        for k in range(y1[i] + 100, y2[i] +100):
            paper[j][k] = 1

for i in range (200):
    for j in range(200):
        if paper[i][j] == 1:
            cnt += 1

print(cnt)