n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
s = [job[0] for job in jobs]
e = [job[1] for job in jobs]
p = [job[2] for job in jobs]

# Please write your code here.




#시작하는 순서로 정렬함.

jobs.sort()

dp = [pay for _, _, pay in jobs]


#해당 값을 마지막으로 다른 선택을 안하는 경우를 말하는 것임
for i in range(n):
    for j in range(i):
        _j, end_j, pay_j = jobs[j]
        start_i, _i, pay_i = jobs[i]

        if end_j < start_i:
            dp[i] = max(dp[i], dp[j] + pay_i)


max_pay = 0

for a in dp:
    max_pay = max(max_pay, a)


print(max_pay)



