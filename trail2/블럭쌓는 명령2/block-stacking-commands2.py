n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

bottom = [0 for i in range(n)]

def add(a, b):
    for i in range (a - 1, b):
        bottom[i] += 1
for x in commands:
    add(x[0], x[1])
    

print(max(bottom))