K, N = map(int, input().split())

# Please write your code here.


arr = []

def print_arr():
    for elem in arr:
        print(elem, end = " ")
    print()

def array(k, n):

    if n == 0:
        print_arr()
        return

    for i in range(k):
        arr.append(i + 1)
        array(k,n - 1)
        arr.pop()

    return


array(K, N)