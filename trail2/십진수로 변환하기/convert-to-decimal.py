binary = input()


def T2T (N):
    sum = 0
    for i in range(len(N)):
        sum = (sum * 2) + int(N[i])
    
    return sum


print(T2T(binary))
