arr = input()

def isPalindrome(list):
    for i in range(len(list) // 2):
        # 다르면 바로 return False
        if list[i] != list[-i -1]:
            return False
    return True

if isPalindrome(arr):
    print("Yes")
else:
    print("No")