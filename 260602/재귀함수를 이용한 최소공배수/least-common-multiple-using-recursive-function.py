n = int(input())
arr = list(map(int, input().split()))

def magic(N ,M):

    if M == 0:
        return N
    return magic(M, N%M)

i = 0
while(i < n - 1):
    arr[i+1] = (arr[i] // magic(arr[i], arr[i+1])) * arr[i+1]
    i+=1
print(arr[n - 1])