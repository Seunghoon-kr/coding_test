import sys

sys.stdin = open("5201_input.txt", "r")

def func(truck, con):
    global sub
    if truck == [] or con == []:
        return sub

    for m in truck:
        for n in con:
            if n <= m:
                con = con[con.index(n)+1:]
                truck = truck[truck.index(m)+1:]
                sub += n
                if con == [] or truck == []:
                    return sub
                return func(truck, con)
    if sub == 0:
        return sub
GY
for i in range(int(input())):
    N, M = map(int, input().split())

    con = list(map(int, input().split()))
    con.sort(reverse=True)
    truck = list(map(int, input().split()))
    truck.sort(reverse=True)
    sub = 0
    print(f"#{i+1}", func(truck, con))




