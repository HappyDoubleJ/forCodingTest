a = int(input())


def isMagicNumber(N):
    if N % 2 == 0 and (N // 10 + N % 10) % 5 == 0:
        return True
    else:
        return False

if isMagicNumber(a):
    print('Yes')
else:
    print('No')

# Please write your code here.