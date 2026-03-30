N = int(input())

def magic(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        B = n // 2
    else:
        B = n // 3  
    return 1 + magic(B)
# Please write your code here.


print(magic(N))