n = int(input())
word = [input() for _ in range(n)]

sorted_word = sorted(word)

for i in range (n):
    print(sorted_word[i])