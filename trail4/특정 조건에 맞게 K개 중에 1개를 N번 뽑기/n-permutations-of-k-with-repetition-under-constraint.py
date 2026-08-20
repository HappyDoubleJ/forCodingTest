K, N = map(int, input().split())

result = []

def sy():

    if len(result) == N:
        print(*result)
        return
    

    for i in range(1, K + 1):
        if len(result) >= 2:
            if result and result[-1] == result[-2] == i:
                continue
        
        result.append(i)
        sy()
        result.pop()

sy()