n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.


result = []
max_score = 0

# 0부터 k - 1 말의 위치를 표시할 곳이다
base = [1 for _ in range(k)]

def cal():
    global max_score
    global base
    cnt = 0
    #i번째 말을 이동시켜서 base에 표시한다.
    for i, j in zip(result,nums):
        base[i - 1] += j
    for i in base:
        if i >= m: 
            cnt += 1
        
    max_score = max(cnt, max_score)
    base = [1 for _ in range(k)]
    


def make_result():

    if len(result) == n:
        cal()
        return
    
    for i in range(1, k + 1):

        result.append(i)
        make_result()
        result.pop()

make_result()

print(max_score)
