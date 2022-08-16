T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [[0] * N for _ in range(N)]
    # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    i = 0
    j = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    k = 0
    area[0][0] = 1
    num = 2
    while num <= N*N:
        if 0 <= i + di[k] < N and 0 <= j + dj[k] < N and area[i+di[k]][j+dj[k]] == 0:
            i += di[k]
            j += dj[k]
            area[i][j] = num
            num += 1
        else:
            k = (k + 1) % 4
    print(f"#{tc}")
    for __ in range(N):
        for ___ in range(N):
            print(area[__][___], end = ' ')
        print('')