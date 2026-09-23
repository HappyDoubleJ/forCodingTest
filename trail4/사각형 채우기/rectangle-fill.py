n = int(input())



# n = 1 : 1
# n = 2 : 2
# n = 3 : 3
# n = 4 : 5
# n = 5 : 4 + 


cnt = [0 for _ in range(n + 1)]

cnt[1] = 1
if n >= 2:
    cnt[2] = 2

if n >=3:
    for i in range(3, n + 1):
        cnt[i] = cnt[i - 1] + cnt[i - 2]



print(cnt[n] % 10007)



