n = int(input())

a = (1 + n) * (n // 2)
if ( n % 2 == 1):
    a = a + ((1 + n) // 2) 
print(a // 10)
# Please write your code here.