n = int(input())
num = list(map(int, input().split()))

import sys

result = []



base_jump = -1
min_jump = sys.maxsize

def jump(idx):
    global base_jump
    global min_jump
    if result and result[-1] == n - 1 and len(result) != -1:
        min_jump = min(min_jump, len(result))
        base_jump = min_jump
        return

    if idx >= n:
        return

    for i in range(1, num[idx] + 1):
        result.append(idx + i)
        jump(idx + i)
        result.pop()
    

jump(0)

print(base_jump)
    

