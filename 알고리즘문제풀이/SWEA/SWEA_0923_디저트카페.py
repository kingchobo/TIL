def f(i, j, si, sj, d, c, N): # i, j: 방문한 카페, si, sj: 첫카페, d: (i,j)로 진입한 방향, c: 지나온 카페수
    global max_V
    if d == 3 and i == si and j == sj:   # 출발지로 되돌아운 경우 c > 0 and...
        if max_V < c:
            max_V = c
    elif menu[area[i][j]]:  # 이미 먹은 경우면
        return

    else:
        menu[area[i][j]] = 1
        # 진입방향 d를 유지하고 이동
        ni, nj = i+di[d], j+dj[d]
        if 0 <= ni < N and 0 <= nj < N:
            f(ni, nj, si, sj, d, c+1, N)

        # d+1 방향으로 이동
        if d < 3:
            ni, nj = i+di[d+1], j+dj[d+1]
            if 0 <= ni < N and 0 <= nj < N:
                f(ni, nj, si, sj, d+1, c+1, N)

        menu[area[i][j]] = 0  # i, j이전에 방향을 전환하기위해 리턴하는 경우


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    area = [list(map(int, input().split())) for _ in range(n)]
    menu = [0] * 101  # 먹은 메뉴 표시를 위한 체크배열
    max_V = -1
    di = [1, 1, -1, -1]
    dj = [1, -1, -1, 1]

    for i in range(n-2):
        for j in range(1, n-1):
            f(i, j, i, j, 0, 0, n)
    print(f'#{tc} {max_V}')