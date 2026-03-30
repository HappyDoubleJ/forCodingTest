n = int(input())


def printStar(N):
    if N == 0:
        return
    printStar(N - 1)
    print("*" * N)

printStar(n)
# Please write your code here.