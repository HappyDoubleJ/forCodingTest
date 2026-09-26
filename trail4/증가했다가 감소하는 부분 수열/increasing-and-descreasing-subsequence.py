n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
#일단 해당 값을 종점으로 하는 증가만 하는 수열 값 저장.
#해당 값을 시작으로 하는 감소만 하는 수열 값 저장.



dp_1 = [1 for _ in range(n)]
dp_2 = [1 for _ in range(n)]

dp_1[0] = 1
dp_2[n - 1] = 1


#일단 해당 값을 종점으로 하는 증가만 하는 수열 값 저장.
for i in range(1, n):
    for j in range(i):
        if sequence[j] < sequence[i]:
            dp_1[i] = max(dp_1[i], dp_1[j] + 1)


for i in range(n - 2, -1, -1):
    for j in range(n - 1, i, -1):
        if sequence[j] < sequence[i]:
            dp_2[i] = max(dp_2[i], dp_2[j] + 1)


max_cnt = 0
for i in range(n):

    max_cnt = max(max_cnt, dp_1[i] + dp_2[i] - 1)

print(max_cnt)


