T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]
    # 십자모양 델타
    ci = [-1, 1, 0, 0]
    cj = [0, 0, -1, 1]
    # X자모양 델타
    xi = [-1, 1, -1, 1]
    xj = [1, -1, -1, 1]
    ans = 0

    for i in range(N):
        for j in range(N):
            # 십자 모양 파리퇴치
            temp_sum = area[i][j]
            for k in range(4):
                for l in range(1, M):
                    ni = i + ci[k] * l
                    nj = j + cj[k] * l
                    if 0 <= ni < N and 0 <= nj < N:
                        temp_sum += area[ni][nj]
            if temp_sum > ans:
                ans = temp_sum
            # X자 모양 파리퇴치
            temp_sum = area[i][j]
            for k in range(4):
                for l in range(1, M):
                    ni = i + xi[k] * l
                    nj = j + xj[k] * l
                    if 0 <= ni < N and 0 <= nj < N:
                        temp_sum += area[ni][nj]
            if temp_sum > ans:
                ans = temp_sum

    print(f'#{TC} {ans}')