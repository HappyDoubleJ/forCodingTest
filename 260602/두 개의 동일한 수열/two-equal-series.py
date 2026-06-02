n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sorted_A = sorted(A)
sorted_B = sorted(B)

i = 0
T = 1
while(i < n):
    if sorted_A[i] != sorted_B[i]:
        T = 0
        break
    i+=1

    
if T:
    print('Yes')
else:
    print('No')