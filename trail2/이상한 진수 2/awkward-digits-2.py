a = input()

answer = [int(a[i]) for i in range(len(a))]
# 0이 있을 경우 가장 왼쪽의 0
# 다 1일 경우 맨 오른쪽의 1 변경



for i in range(len(a)):
    if a[i] == '0':
        answer[i] = 1
        break
    if i == len(a) - 1:
        answer[i] = 0

def ttt (x):
    cnt = 0
    for i in range(len(x)):
        cnt += x[i] * (2 ** (len(x) - i - 1))
    return cnt


print(ttt(answer))