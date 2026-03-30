N = int(input())

def printNumbers(n):
    if n == 0:
        return
    print(n, end = " ")
    printNumbers(n - 1)
    print(n, end = " ")

printNumbers(N)