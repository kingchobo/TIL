from sys import stdin
from collections import deque

N, M = map(int, input().split())
area = [list(map(int, stdin.readline().split())) for _ in range(N)]
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
year = 0


def is_divided(total_ice):
    visited = [[0] * M for _ in range(N)]
    i, j = ice_index[0]
    q = deque()
    q.append((i, j))
    cnt = 1
    while q:
        i, j = q.popleft()
        visited[i][j] = 1
        for k in range(4):
            ni, nj = i + delta[k][0], j + delta[k][1]
            if area[ni][nj] and not visited[ni][nj]:
                q.append((ni, nj))
                cnt += 1
    if cnt < total_ice:
        return True
    return False


def melting():
    melted_index = []
    for i, j in ice_index:
        num_water = 0
        for k in range(4):
            ni, nj = i + delta[k][0], j + delta[k][1]
            if not area[ni][nj]:
                num_water += 1
        result = area[i][j] - num_water
        if result > 0:
            melted_index.append((i, j, result))
        else:
            melted_index.append((i, j, 0))

    for i, j, x in melted_index:
        area[i][j] = x


while True:
    num_ice = 0
    ice_index = []
    for i in range(N):
        for j in range(M):
            if area[i][j]:
                num_ice += 1
                ice_index.append((i, j))

    if num_ice < 2:
        print(0)
        break

    if is_divided(num_ice):
        print(year)
        break

    melting()
    year += 1