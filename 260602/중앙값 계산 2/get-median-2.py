n = int(input())
arr = list(map(int, input().split()))

def find_med(M):
    sorted_arr = sorted(M)
    return sorted_arr[(len(sorted_arr)//2) + (len(sorted_arr)%2) - 1]

word = []
for i in range (len(arr)):
    word.append(arr[i])
    if (i+1) % 2 != 0:
        print(find_med(word), end = " ")

