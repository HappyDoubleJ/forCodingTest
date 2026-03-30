N = int(input())

def printHellowWorld(n):

    if n == 0:
        return
    printHellowWorld(n-1)
    print('HelloWorld')

printHellowWorld(N)