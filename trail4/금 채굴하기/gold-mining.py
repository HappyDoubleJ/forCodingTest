n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_G = 0

#드는 비용
def cost(k):
    return (k * k) + ((k + 1) *(k + 1))

#금의 가치
def money(gold):
    global m
    return gold * m

def max_k(b):
    return 2*(n - 1)



for i in range(n):
    for j in range(n):
        for k in range(max_k(n) + 1):
            current_cost = cost(k)
            sum = 0
            for l in range(n):
                for o in range(n):
                    if abs(l - i) + abs(o - j) <= k:
                        sum += grid[l][o]
            if(money(sum) >= current_cost and sum >= max_G):
                max_G = sum
print(max_G)

