import sys
sys.stdin = open("23288_input.txt", "r")

case = int(input())

#      동,서,북,남,상,하
dice = [3,4,2,5,1,6]

#주사위와 좌표의 이동 후 변화
def right(n, m, dice):
    return n, m+1, [dice[4],dice[5],dice[2],dice[3],dice[1],dice[0]]
def left(dice):
    return n, m-1, [dice[5],dice[4],dice[2],dice[3],dice[0],dice[1]]
def up(dice):
    return n-1, m, [dice[0],dice[1],dice[4],dice[5],dice[3],dice[2]]
def down(dice):
    return n+1, m, [dice[0],dice[1],dice[5],dice[4],dice[2],dice[3]]

#위치 속 주변의 같은 숫자 카운트
def find(arr, n, m, plus, by):
    global N,M
    if by == "":
        plus +=1
    now = arr[n][m]
    if n-1 >=0 and arr[n-1][m] == now and by != "u":
        plus += 1
        return find(arr, n-1, m, plus, "d")
    if m-1 >=0 and arr[n][m-1] == now and by != "l":
        plus += 1
        return find(arr, n, m-1, plus, "r")
    if n+1 <N and arr[n+1][m] == now and by != "d":
        plus += 1
        return find(arr, n+1, m, plus, "u")
    if m+1 <M and arr[n][m+1] == now and by != "r":
        plus += 1
        return find(arr, n, m+1, plus, "l")
    return plus

def move(arr, n, m, dice, by):
    next = ""
    if dice[5] > arr[n][m]:
        if by == "u": return next = "r"
        elif by == "r": next = "d"
        elif by == "d": next = "l"
        elif by == "l": next = "u"
    if dice[5] < arr[n][m]:

    if dice[5] == arr[n][m]:
        next = by


for i in range(case):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]





    print(f"#{case+1} {result}")