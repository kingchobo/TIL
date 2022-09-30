def dfs(n, temp_sum):
    global ans
    if temp_sum >= ans:
        return

    if n == N:
        if ans > temp_sum:
            ans = temp_sum
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(n + 1, temp_sum + arr[n][i])
            visited[i] = 0


T = int(input())
for TC in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = N * 99
    visited = [0] * N
    dfs(0, 0)
    print(f'#{TC} {ans}')