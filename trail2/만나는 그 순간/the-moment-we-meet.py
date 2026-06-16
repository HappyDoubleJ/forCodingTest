n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

a = []
b = []

current_a = 0
current_b = 0
for i in range(n):
    if d[i] == 'R':
        for i in range(t[i]):
            current_a += 1
            a.append(current_a)
    else:
        for i in range(t[i]):
            current_a -= 1
            a.append(current_a)

for i in range(m):
    if d2[i] == 'R':
        for i in range(t2[i]):
            current_b += 1
            b.append(current_b)
    else:
        for i in range(t2[i]):
            current_b -= 1
            b.append(current_b)

for i in range(len(a)):
    if a[i] == b[i]:
        print(i + 1)
        break
    if i == (len(a) - 1) and a[i] != b[i]:
        print(-1)