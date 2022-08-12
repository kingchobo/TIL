T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # 가로 탐색
    for i in range(N):
        cnt = 0
        check_list = []
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                check_list.append(cnt)
                cnt = 0
        check_list.append(cnt)
        ans += check_list.count(K)

    # 세로 탐색
    for i in range(N):
        cnt = 0
        check_list = []
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            else:
                check_list.append(cnt)
                cnt = 0
        check_list.append(cnt)
        ans += check_list.count(K)

    print(f'#{tc} {ans}')