import sys
min_cnt = sys.maxsize
A = input()

# Please write your code here.


def count(string):
    temp_c = string[0]
    cnt = 0
    string_A = []
    string_A.append(temp_c)
    for j in range(len(string)):
        if string[j] == temp_c:
            cnt += 1
        else:
            string_A.append(str(cnt))
            temp_c = string[j]
            string_A.append(temp_c)
            cnt = 1
    string_A.append(str(cnt))
    result = 0
    for k in string_A:
        result += len(k)
        
    return result


        


def shift(n):
    rotated = A[n:] + A[:n]
        
    
    return count(rotated)




for i in range(len(A)):
    current = shift(i)
    min_cnt = min(min_cnt, current)


            
print(min_cnt)