n = int(input())

def printStars(N):
    if N == 0:
        return
    print("* " * N)
    printStars(N  - 1)
    print("* " * N)

printStars(n)
# Please write your code here.