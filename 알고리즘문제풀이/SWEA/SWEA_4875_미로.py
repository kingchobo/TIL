def find_route(x, y, N):
    # 출발점에서 상하좌우로 움직이며 미로 탐색
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    if area[x][y] == 3:
        return 1

    else:
        area[x][y] = 1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and area[nx][ny] != 1:
                if find_route(nx, ny, N):
                    return 1
        return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input())) for _ in range(N)]

    # 출발점(2) 위치 탐색
    check = 1
    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if area[i][j] == 2:
                x, y = i, j
                check = 0
                break
        if check == 0:
            break

    print(f'#{tc} {find_route(x, y, N)}')