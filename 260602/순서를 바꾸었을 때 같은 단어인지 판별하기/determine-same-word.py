word1 = input()
word2 = input()

sorted_word1 = sorted(word1)
sorted_word2 = sorted(word2)

def magic(n , m):
    if len(n) != len(m):
        return 'No'
    for i in range (len(n)):
        if n[i] != m[i]:
            return 'No'
    return 'Yes'

print(magic(sorted_word1,sorted_word2))