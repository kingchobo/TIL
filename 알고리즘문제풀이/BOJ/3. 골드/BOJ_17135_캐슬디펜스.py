import sys
from itertools import combinations

def simulation(area):
    global ans
    simul_area = area[:]
    delta = [(-1, 0), (-1, -1), ()]


N, M, D = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

archers_comb = list(combinations([i for i in range(M)], 3))
ans = 0


for i in range(len(archers_comb)):
    archers = [0] * M
    for j in range(3):
        archers[archers_comb[i][j]] = 2
    area.append(archers)
    simulation(area)
    area.pop()