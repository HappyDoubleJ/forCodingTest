
import sys

n = int(input())
a = [int(input()) for _ in range(n)]

# 특정한 방을 하나 정하고,  근데 방향은 0 -> 1 -> 2 -> 3 -> ...


#기본적으로 거리는 i - 시작
# i가 시작보다 작으면, (n - 1 - 시작) + i + 1

sum = 0
min_sum = sys.maxsize
#i는 시작
for i in range(n):
    sum = 0
    for j in range(n):
        dist = j - i
        if (j - i) < 0:
            dist = n - 1 - i + j + 1
        
        sum += dist*a[j]
    if min_sum > sum:
        min_sum = sum
    


print(min_sum)
        

