n, m = map(int, input().split())

cnt = 0
# 3의 배수 판별
def isMagicNumber(N):
    return N % 3 == 0

# 3, 6, 9 유무 판별 
def isHaveNumber(N):
    i = 1000000
    while(i > 0):
        M = N // i 
         
        if M == 3 or M == 6 or M == 9:
            return True
        N = N % i
        i = i // 10
    return False    
     


for i in range(n, m + 1, 1):
    if isMagicNumber(i) or isHaveNumber(i):
        cnt = cnt + 1


print(cnt)
# Please write your code here.