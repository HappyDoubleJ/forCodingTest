n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# 블럭 쌓는거랑 똑같은 거임..

bottom = [0 for i in range(201)]

def add_ (a ,b):
    for i in range(a + 100, b + 100):
        bottom[i] += 1
    
for i in segments:
    add_(i[0], i[1])

print(max(bottom))