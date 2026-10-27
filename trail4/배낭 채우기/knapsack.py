N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

diamonds = [(a, b) for a,b in zip(w,v)]

diamonds.sort(key = lambda x : x[0])



dp_v = [-1] * (M + 1)
dp_v[0] = 0

for x, y in diamonds: 
    for i in range(M, x - 1, -1):
        if dp_v[i - x] != -1:
            dp_v[i] = max(dp_v[i], dp_v[i - x] + y)


print(max(dp_v))
