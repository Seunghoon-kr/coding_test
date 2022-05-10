import sys

sys.stdin = open("5189_input.txt", "r")


def func(now, sub):
    global visited, arr, min_v, size
    if False not in visited:
        sub += arr[now][0]
        if min_v > sub:
            min_v = sub
    elif False in visited:
        for i in range(size):
            if visited[i] == False:
                visited[i] = True
                sub += arr[now][i]
                func(i, sub)
                visited[i] = False
                sub -= arr[now][i]


for i in range(int(input())):
    size = int(input())
    visited = [False] * size
    visited[0] = True
    arr = []
    min_v = 999999999999
    for j in range(size):
        arr.append(list(map(int, input().split())))

    func(0, 0)
    print(f"#{i+1} {min_v}")
