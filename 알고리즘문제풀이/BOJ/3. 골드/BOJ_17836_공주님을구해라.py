import sys

N, M, T = map(int, sys.stdin.readline().split())
castle = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
if T < N + M - 2:       # 애초에 시간이 부족한 경우 처리
    print('Fail')

else:
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    visited = [[0] * M for _ in range(N)]
    q = [(0, 0, 0)]         # 각 i, j좌표 및 현재까지 소요된 시간
    visited[0][0] = 1
    ans = 10000             # 빙글빙글 돌아서 모든칸다밟고 가는 경우(9999) + 1
    arrived = 0

    while not arrived and q:        # 도착할 때 까지 돌림
        i, j, t = q.pop(0)
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and castle[ni][nj] != 1:
                if ni == N-1 and nj == M-1:     # 도착했으면
                    if t+1 <= T:                # 시간초과 안됐을 경우
                        ans = min(ans, t+1)     # 현재 저장된 ans 값(10000 or 그람찾고 저장한 값)과 지금 가져온 값중 작은값 저장
                        arrived = 1             # 제일 먼저 도착한 놈이 제일 빠르니까 바로 도착으로 바꾸고 종료
                        break

                if castle[ni][nj] == 0 and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    q.append((ni, nj, t+1))

                elif castle[ni][nj] == 2:
                    visited[ni][nj] = 1
                    if t+1 + N - 1 - ni + M - 1 - nj <= T:      # 칼 줍기까지의 시간 + 공주에게 직진하는 시간
                        ans = min(ans, t+1 + N - 1 - ni + M - 1 - nj)

    if ans == 10000:
        print('Fail')
    else:
        print(ans)