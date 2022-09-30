def bfs(N):
    q = []
    q.append((0, 0)) # 시작점 인큐
    di = [-1, 1, 0, 0]     # 상, 하, 좌, 우 이동 델타
    dj = [0, 0, -1, 1]
    while q:
        ti, tj = q.pop(0)  # 현재 위치 ti, tj
        for k in range(4):
            ni, nj = ti + di[k], tj + dj[k]
            # 이동할 위치 ni, nj가 범위 안에 있으면 q에 넣기
            if 0 <= ni < N and 0 <= nj < N:
                # cost_map 갱신
                # 높이가 더 높아져 추가비용 발생하는 경우 처리
                if region[ni][nj] > region[ti][tj]:
                    cost = 1 + (region[ni][nj] - region[ti][tj])
                else:
                    cost = 1
                # 현재 표기된 cost보다 낮은 비용으로 이동할 수 있으면 갱신
                if cost_map[ni][nj] > cost_map[ti][tj] + cost:
                    cost_map[ni][nj] = cost_map[ti][tj] + cost
                    q.append((ni, nj))


T = int(input())
for TC in range(1, T+1):
    N = int(input())
    region = [list(map(int, input().split())) for _ in range(N)]
    cost_map = [[100000]*N for _ in range(N)]
    cost_map[0][0] = 0
    bfs(N)
    print(f'#{TC} {cost_map[N-1][N-1]}')