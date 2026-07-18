n = int(input())
A = list(map(int, input().split()))



for i in range(n):
    sum = 0
    for j in range(n):
        sum += int(abs(j - i)) * A[j]
    if i == 0:
        min = sum
    if min > sum:
        min = sum
    
print(min)
