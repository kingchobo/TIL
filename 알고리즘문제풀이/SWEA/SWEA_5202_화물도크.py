t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = []
    for i in range(n):
        s, e = map(int, input().split())
        arr.append((s, e))
    arr.sort()
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[i][0] >= arr[j][1] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    print(f'#{tc} {max(dp)}')