import sys

M, N = map(int, sys.stdin.readline().split())
tomato_box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cnt_0 = cnt_em = day = 0
q = []
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if tomato_box[i][j] == 0:
            cnt_0 += 1

        elif tomato_box[i][j] == 1:
            visited[i][j] = 1
            q.append((i, j, 0))

i = 0
comp = len(q) - 1
if q:
    while i <= comp:
        ti, tj, day = q[i]
        i += 1

        for k in range(4):
            ni, nj = ti + delta[k][0], tj + delta[k][1]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if tomato_box[ni][nj] == 0:
                    visited[ni][nj] = 1
                    tomato_box[ni][nj] = 1
                    cnt_0 -= 1
                    q.append((ni, nj, day+1))
                    comp += 1

    if cnt_0 > 0:
        print(-1)
    else:
        print(day)

else:
    print(-1)
