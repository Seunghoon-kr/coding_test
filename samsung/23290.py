import sys
sys.stdin = open("23290_input.txt", "r")

M, S = map(int, input().split()) #물고기 수, 시행 횟수
plate = [[0]*4 for _ in range(4)]

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

s_dx = [-1,0,1,0]
s_dy = [0,-1,0,1]

fish = []
for _ in range(M):
    x,y,way = map(int, input().split())
    fish.append([x-1,y-1,way-1])

s_x,s_y = map(int, input().split())
shark = [s_x-1,s_y-1]

def move_fish(fish):
    n_fish = []
    for x, y, way in fish:
        while not 0 <= x + dx[way] < 4 or not 0 <= y + dy[way] < 4:
            way -= 1
        x += dx[way]
        y += dy[way]
        n_fish.append([x,y,way])
    return n_fish

def draw_plate(fish):
    plate = [[0] * 4 for _ in range(4)]
    for x,y,_ in fish:
        plate[x][y] += 1
    return plate

track = [[0] * 4 for _ in range(4)]
b_move, move = [0,0,0], [0,0,0]
b_eat = 0

def move_shark(plate, shark, track, count, eat):
    global b_eat, b_move, move

    count += 1

    x,y = shark[0],shark[1]
    track[x][y] = 1
    if count < 4:
        for i in range(4):
            nx, ny = x + s_dx[i], y + s_dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4 and track[nx][ny] == 0:
                move[count-1] = i
                shark = [nx,ny]
                eat += plate[nx][ny]
                return move_shark(plate, shark, track, count, eat)
    elif b_eat < eat:
        b_move = move
        b_eat = eat
        return b_move

print(move_shark(draw_plate(move_fish(fish)), shark, track, 0, 0))

def erase_fish(shark, fish, b_move):
    s_x,s_y = shark
    for i in b_move:
        for j in len(fish):
            x, y, _ = fish[j]
            if s_x + s_dx[i] == x and s_y + s_dy[i] == y:
                fish.pop(j)
    return fish