n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]


bottom = [0 for i in range (101)]
def add_ (a,b):
    for i in range(a,b + 1):
        bottom[i] += 1

for i in segments:
    add_(i[0], i[1])


print(max(bottom))
