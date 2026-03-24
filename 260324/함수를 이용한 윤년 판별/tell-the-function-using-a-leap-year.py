y = int(input())

def isAnswer(N):
    if N % 100 == 0 and N % 400 != 0:
        return False
    return N % 4 == 0

if isAnswer(y):
    print('true')
else:
    print('false')
# Please write your code here.