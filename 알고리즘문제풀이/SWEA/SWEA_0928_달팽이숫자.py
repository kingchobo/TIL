T = int(input())
for TC in range(1, T+1):
    N = int(input())
    area = [[0]*N for _ in range(N)]
    # 우, 하, 좌, 상 방향 델타
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    d = 0  # 현재 방향
    k = 1  # 처음 찍을 숫자
    i, j = 0, 0  # 처음 찍을 위치
    while k <= N * N:
        area[i][j] = k
        k += 1
        ni, nj = i + di[d], j + dj[d]
        if 0 <= ni < N and 0 <= nj < N and area[ni][nj] == 0:
            i, j = ni, nj
        else:
            d = (d+1) % 4
            i, j = i + di[d], j + dj[d]

    print(f'#{TC}')
    for i in range(N):
        print(*area[i])
