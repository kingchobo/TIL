t = int(input())
for tc in range(1, t+1):
    n, price = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]

    # 모든 집의 개수 및 좌표 저장
    num_of_houses = 0
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                num_of_houses += 1
    max_revenue = num_of_houses * price  # 도시에서 얻을 수 있는 최대 수입

    # 도시에서 운영할 수 있는 최대 크기의 k 찾기
    k = 0
    while True:
        k += 1
        if k**2 + (k-1)**2 > max_revenue:
            break

    di = [0, 0, -1, 1, -1, -1, 1, 1]
    dj = [1, -1, 0, 0, 1, -1, -1, 1]

    # 그 범위 내에서 찾기
    ans = 0
    for kk in range(1, k+1):
        cost = kk ** 2 + (kk - 1) ** 2
        max_num = 0
        for i in range(n):
            for j in range(n):
                cnt = 0
                if city[i][j] == 1:
                    cnt = 1
                for l in range(1, kk):
                    ni, nj = i + l, j
                    for x in range(4, 8):
                        for m in range(1, l + 1):
                            ni, nj = ni + di[x], nj + dj[x]
                            if 0 <= ni < n and 0 <= nj < n:
                                if city[ni][nj] == 1:
                                    cnt += 1

                if cnt * price >= cost:
                    if cnt > max_num:
                        max_num = cnt
        if max_num > ans:
            ans = max_num
    print(f'#{tc} {ans}')