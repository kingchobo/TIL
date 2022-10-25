import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def bfs(i, j, t, l):
    q = deque()
    q.append((0, 0, 0, 1))
    while q:
        i, j, t, l = q.popleft()
        if i == N-1 and j == M-1:
            return l
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if area[ni][nj] == 0:  # 벽 안부수고 이동할 수 있으면
                    q.append((ni, nj, t, l+1))
                elif area[ni][nj] == 1:  # 벽이면
                    if t == 0:
                        q.append((ni, nj, 1, l+1))

ans = bfs(0, 0, 0, 1)

if ans == None:
    print(-1)
else:
    print(ans)