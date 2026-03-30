n = int(input())

def printOTN(N):
    if N == 0:
        return
    printOTN(N - 1)
    print(N, end = " ")
def printNTO(N):
    if N == 0:
        return
    print(N, end = " ")
    printNTO(N - 1)
    
printOTN(n)
print()
printNTO(n)