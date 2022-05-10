import sys

sys.stdin = open("2048(easy).txt", "r")

size = int(input())
arr = [list(map(int, input().split())) for _ in range(size)]
s_max = max(max(arr))

"""
def line(list):
    global size
    n_list = []
    for arr in list:
        for i in range(size):
            if arr[i] == 0:
                pass
            else:
                if arr.index(0) < i:
                    arr[arr.index(0)] = arr[i]
                    arr[i] = 0
        for i in range(size - 1):
            if arr[i] == arr[i + 1]:
                arr[i] *= 2
                arr[i + 1] = 0
        for i in range(size):
            if arr[i] == 0:
                pass
            else:
                if arr.index(0) < i:
                    arr[arr.index(0)] = arr[i]
                    arr[i] = 0
        n_list.append(arr)

def find(arr):
    global size
    for i in range(size-1):
        if arr[i] == arr[i+1]:
            arr[i] *= 2
            arr[i+1] = 0
    return arr
"""


arr = [[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4]]
s_max = max(max(arr))
size = 5
def line(list):
    global size
    n_list = []
    for arr in list:
        for i in range(size):
            if arr[i] == 0:
                pass
            else:
                if arr.index(0) < i:
                    arr[arr.index(0)] = arr[i]
                    arr[i] = 0
        for i in range(size - 1):
            if arr[i] == arr[i + 1]:
                arr[i] *= 2
                arr[i + 1] = 0
        for i in range(size):
            if arr[i] == 0:
                pass
            else:
                if arr.index(0) < i:
                    arr[arr.index(0)] = arr[i]
                    arr[i] = 0
        n_list.append(arr)
    list = n_list
    return list

#Left, right, up, down = 0,1,2,3
def turn(list, t):
    global size
    if t == 0:
        list = line(list)
    if t == 1:  #right
        n_list = []
        for arr in list:
            n_arr = []
            for i in range(size):
                n_arr.append(arr[size-i-1])
            n_list.append(n_arr)
        list = n_list
        list = line(list)
        n_list = []
        for arr in list:
            n_arr = []
            for i in range(size):
                n_arr.append(arr[size - i - 1])
            n_list.append(n_arr)
        list = n_list
    elif t == 2:
        n_list = []
        for arr in list:
            n_arr = []
            for i in range(size):
                n_arr.append(arr[size - i - 1])
            n_list.append(n_arr)
        list = n_list

    return list

#print(arr)
#print(line(arr))
#print(turn(arr, 1))


def five(list, count):
    max_a = max(max(list))
    if max_a == s_max * 5:
        return max_a
    if count > 5:
        return max_a
    return max(five(turn(list, 0), count+1),five(turn(list, 1), count+1))


print(five(arr, 0))