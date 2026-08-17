n = int(input())
x1, x2 = [], []

for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)

# Please write your code here.
lines = []

max_cnt = 0

def not_duplicate(x, y):
    for xi1, xi2 in lines:
        if not (xi2 < x or y < xi1):
            return False
    
    return True




def mark(N):
    global max_cnt
    
    if N == 0:
        cnt = len(lines)
        max_cnt = max(max_cnt, cnt)
        return

    if not_duplicate(x1[N - 1], x2[N - 1]):
        lines.append((x1[N - 1], x2[N - 1]))
        mark(N - 1)
        lines.pop()
        

    mark(N - 1)
    
    
    


mark(n)

print(max_cnt)