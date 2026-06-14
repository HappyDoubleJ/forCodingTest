N = input()

def x17 (b):
    sum = 0
    for i in range(len(N)):
        sum = sum *2 + int(b[i])
    return sum * 17

ans = []
def T2B (c):
    global ans
    if c < 2:
        ans.append(c)
        return ans
    T2B (c // 2)
    ans.append(c % 2)
    return ans



print(*T2B(x17(N)), sep = "")


   
