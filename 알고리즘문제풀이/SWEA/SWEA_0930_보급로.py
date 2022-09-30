def bfs(i, j):
    q = [(i, j)]
    while q:
        ti, tj = q.pop(0)
        for k in range(4):
            ni, nj = ti + delta[k][0], tj + delta[k][1]
            if 0 <= ni < N and 0 <= nj < N:
                if dp_area[ni][nj] == -1 or dp_area[ni][nj] > dp_area[ti][tj] + input_area[ni][nj]:
                    dp_area[ni][nj] = dp_area[ti][tj] + input_area[ni][nj]
                    q.append((ni, nj))


T = int(input())
for TC in range(1, T+1):
    N = int(input())
    input_area = [list(map(int, input())) for _ in range(N)]
    dp_area = [[-1] * N for _ in range(N)]
    dp_area[0][0] = input_area[0][0]
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    bfs(0, 0)
    print(f'#{TC} {dp_area[N-1][N-1]}')