N = int(input())

def sigmaEven(n):
    if n == 2:
        return 2
    return n + sigmaEven(n - 2)



def sigmaOdd(n):    
    if n == 1:
        return 1
    return n + sigmaOdd(n - 2)


if N % 2 == 0:
    print(sigmaEven(N))
else:
    print(sigmaOdd(N))
# Please write your code here.

