n = int(input())


result = []


cnt = 0



# Please write your code here.
def beautiful(N):
    global cnt

    if N < 0 :
        return
    
    if N == 0 :
        cnt += 1
        return

    #1
    for i in range(1):
        result.append(i)

    beautiful(N - 1)

    result.pop()


    #2
    for i in range(2):
        result.append(2)

    beautiful(N - 2)

    result.pop()

    #3
    for i in range(3):
        result.append(3)

    beautiful(N - 3)

    result.pop()

    #4
    for i in range(4):
        result.append(4)

    beautiful(N - 4)

    result.pop()




    
beautiful(n)

print(cnt)




