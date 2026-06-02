n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

def starts_with(a, b):
    if len(a) < len(b):
        return False
    return  a[:len(b)] == b


words= []
for i in range (n):
    if starts_with(str[i],t):
        words.append(str[i])

words.sort()
print(words[k-1])