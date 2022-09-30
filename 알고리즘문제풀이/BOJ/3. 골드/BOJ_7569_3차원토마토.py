import sys

M, N, H = map(int, sys.stdin.readline().split())

# 0층(맨아래층)부터 쌓아올려지는 각 층의 토마토박스 상태 입력(3차원 리스트)
boxes = []
for __ in range(H):
    tomato_box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    boxes.append(tomato_box)

delta = [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]
cnt_0 = day = 0
q = []
visited = [[[0]*M for _ in range(N)] for __ in range(H)]
for h in range(H):
    for i in range(N):
        for j in range(M):
            if boxes[h][i][j] == 0:
                cnt_0 += 1

            elif boxes[h][i][j] == 1:
                visited[h][i][j] = 1
                q.append((h, i, j, 0))

i = 0
comp = len(q) - 1
if q:
    while i <= comp:
        th, ti, tj, day = q[i]
        i += 1

        for k in range(6):
            nh, ni, nj = th + delta[k][0], ti + delta[k][1], tj + delta[k][2]
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and not visited[nh][ni][nj]:
                if boxes[nh][ni][nj] == 0:
                    visited[nh][ni][nj] = 1
                    boxes[nh][ni][nj] = 1
                    cnt_0 -= 1
                    q.append((nh, ni, nj, day+1))
                    comp += 1

    if cnt_0 > 0:
        print(-1)
    else:
        print(day)

else:
    print(-1)
