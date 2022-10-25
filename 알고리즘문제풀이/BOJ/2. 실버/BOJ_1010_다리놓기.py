T = int(input())
for TC in range(T):
    N, M = map(int, input().split())
    dp = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if i == j:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = j + 1
            elif i < j:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    # for i in range(N):
    #     print(*dp[i])
    # print('---------------')

    print(dp[N-1][M-1])