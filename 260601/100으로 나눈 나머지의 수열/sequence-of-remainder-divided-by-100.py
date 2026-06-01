N = int(input()) 
# Please write your code here. 
def sequence(N):
    if N == 1:
        return 2
    if N == 2:
        return 4
    return (sequence(N - 1)  * sequence(N - 2)) % 100

print(sequence(N)) 