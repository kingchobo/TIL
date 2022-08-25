def find_route(x, y):
    # 출발점에서 상하좌우로 움직이며 미로 탐색
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    if area[x][y] == '3':
        return 1

    else:
        area[x][y] = '1'
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < 16 and 0 <= ny < 16 and area[nx][ny] != '1':
                if find_route(nx, ny):
                    return 1
        return 0


T = 10
for _ in range(T):
    tc = int(input())
    area = [list(input()) for __ in range(16)]

    # 출발점 '2'의 위치 찾기
    x, y = 0, 0
    for i in range(16):
        for j in range(16):
            if area[i][j] == '2':
                x, y = i, j

    stack = []     # 갈림길 마다 현 위치 저장해 둘 스택 선언
    print(f'#{tc} {find_route(x, y)}')