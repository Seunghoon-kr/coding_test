import sys
from collections import deque

sys.stdin = open("23288_input.txt", "r")

case = int(input())


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x,y, count):
    q.append([x,y])
    track[x][y] = 1
    main_n = arr[x][y]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if track[nx][ny] == 0 and main_n == arr[nx][ny]:
                    track[nx][ny] = 1
                    q.append([nx,ny])
                    count += 1
    return count


for c in range(case):
    ans = 0

    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dice = [3,4,2,5,1,6] #동,서,북,남,상,하
    x,y,i = 0,0,0

    for k in range(K):
        if not 0 <= x + dx[i] < N or not 0 <= y + dy[i] < M:
            i = (i + 2) % 4
        x += dx[i]
        y += dy[i]

        if i == 0: #right
            dice = [dice[4], dice[5], dice[2], dice[3], dice[1], dice[0]]
        elif i == 1: #down
            dice = [dice[0], dice[1], dice[5], dice[4], dice[2], dice[3]]
        elif i == 2: #left
            dice = [dice[5], dice[4], dice[2], dice[3], dice[0], dice[1]]
        elif i == 3: #up
            dice = [dice[0], dice[1], dice[4], dice[5], dice[3], dice[2]]

        q = deque()
        track = [[0] * M for _ in range(N)]
        ans += bfs(x, y, 1) * arr[x][y]

        if dice[5] == arr[x][y]:
            i = i
        elif dice[5] > arr[x][y]: #90도
            i = (i + 1) % 4
        elif dice[5] < arr[x][y]: #-90도
            i = (i + 3) % 4

    print(f"#{K} {ans}")