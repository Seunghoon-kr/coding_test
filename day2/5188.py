import sys

sys.stdin = open("5188_input.txt", "r")


def min_arr(arr, size, count):
    if count == 0:
        for i in range(size-1):
            arr[i+1][0] += arr[i][0]
            arr[0][i+1] += arr[0][i]
        count += 1
    arr[1][1] += min(arr[1][0], arr[0][1])
    for j in range(size-2):
        arr[1][j+2] += min(arr[1][j+1], arr[0][j+2])
        arr[j+2][1] += min(arr[j+1][1], arr[j+2][0])
    if size == 2:
        return arr[1][1]
    return min_arr([row[1:] for row in arr[1:]], size-1, count)


for n in range(int(input())):
    size = int(input())
    dx, dy = 0, 0
    arr = []
    for _ in range(size):
        arr.append(list(map(int, input().split())))
    count = 0
    print(f"#{n+1} {min_arr(arr, size, count)}")
