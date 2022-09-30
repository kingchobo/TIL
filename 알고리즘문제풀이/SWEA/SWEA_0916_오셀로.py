def setting(): # 초기환경 셋팅
    if n == 4:
        area[1][1] = 'W'
        area[1][2] = 'B'
        area[2][1] = 'B'
        area[2][2] = 'W'
    elif n == 6:
        area[2][2] = 'W'
        area[2][3] = 'B'
        area[3][2] = 'B'
        area[3][3] = 'W'
    elif n == 8:
        area[3][3] = 'W'
        area[3][4] = 'B'
        area[4][3] = 'B'
        area[4][4] = 'W'


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    area = [['O'] * n for _ in range(n)]
    setting()
    for i in range(m):
        x, y, color = map(int, input().split())
        # 내가 알아보기 쉽게 좌표 변경
        r = y-1
        c = x-1
        # 게임플레이를 위한 B, W로의 변경
        if color == 1:
            color = 'B'
        else:
            color = 'W'
        area[r][c] = color

        # 8방향(가로, 세로, 대각선) 탐색
        # 상, 하, 좌, 우, 좌상, 좌하, 우상, 우하
        dc = [0, 0, -1, 1, -1, -1, 1, 1]
        dr = [-1, 1, 0, 0, -1, 1, -1, 1]
        for k in range(8):
            nc, nr = c+dc[k], r+dr[k]
            if 0 <= nc < n and 0 <= nr < n:
                # W 놨는데 인접한 돌이 B인 경우
                if area[nr][nc] == 'B' and color == 'W':
                    temp = [[nr, nc]]  # 좌표 저장
                    idx = 2
                    while True:
                        nc, nr = c + dc[k] * idx, r + dr[k] * idx
                        if 0 <= nc < n and 0 <= nr < n:
                            if area[nr][nc] == 'B':   # 다른 색들은 계속 좌표 저장
                                temp.append([nr, nc])
                                idx += 1
                            elif area[nr][nc] == 'W': # 같은 색 발견하면 스탑!
                                temp.append('find!!')
                                break
                            else:
                                break
                        else:
                            break
                    if 'find!!' in temp:  # 같은 색이 없었으면 색이 안바뀌니까 같은 색이 있었을 때만 색 바꾸기
                        for j in temp[:-1]:
                            area[j[0]][j[1]] = 'W'

                # B 놨는데 인접한 돌이 W인 경우
                # 주석은 위 케이스와 같으므로 생략
                elif area[nr][nc] == 'W' and color == 'B':
                    temp = [[nr, nc]]
                    idx = 2
                    while True:
                        nc, nr = c + dc[k] * idx, r + dr[k] * idx
                        if 0 <= nc < n and 0 <= nr < n:
                            if area[nr][nc] == 'W':
                                temp.append([nr, nc])
                                idx += 1
                            elif area[nr][nc] == 'B':
                                temp.append('find!!')
                                break
                            else:
                                break
                        else:
                            break
                    if 'find!!' in temp:
                        for j in temp[:-1]:
                            area[j[0]][j[1]] = 'B'
    num_B = 0
    num_W = 0
    for i in area:
        num_B += i.count('B')
        num_W += i.count('W')

    print(f'#{tc} {num_B} {num_W}')
    #     #게임하는 코드
    #     # t = 1, n = 4,6,8 중 선택, m = 999 입력
    #     for i in area:
    #         print(*i)
    #     num_B = 0
    #     num_W = 0
    #     for i in area:
    #         num_B += i.count('B')
    #         num_W += i.count('W')
    #     print(f'현재 흑돌의 개수 : {num_B}, 백돌의 개수 : {num_W} 남은 공간 : {n*n - num_W - num_B}')
    #     print('-------------------------')
    #     if n*n - num_W - num_B == 0:
    #         if num_B > num_W:
    #             print('흑돌이 이겼습니다!')
    #         elif num_W > num_B:
    #             print('백돌이 이겼습니다!')
    #         else:
    #             print('비겼습니다!')
    #         break
