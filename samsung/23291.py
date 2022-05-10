import sys
from collections import deque
from copy import deepcopy

sys.stdin = open("test.txt", "r")

list = [[8,5,3,4,5],[3,10,1,4],[1,4]]

n_list = deepcopy(list)

for i in range(len(list)):

    for j in range(len(list[i])):
        if i+1 < len(list):
            if j < len(list[i+1]):
                if list[i][j] > list[i+1][j]:
                    n_list[i+1][j] += (list[i][j]-list[i+1][j]) // 5
                    n_list[i][j] -= (list[i][j]-list[i+1][j]) // 5
print(list)
print(n_list)