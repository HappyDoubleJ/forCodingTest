A = input()


sum = 0

for i in range(len(A)):
    cnt = 0
    if A[i] == '(':
        for j in range(i + 1, len(A)):
            if A[j] == ')':
                cnt +=1
        sum += cnt


print(sum)
