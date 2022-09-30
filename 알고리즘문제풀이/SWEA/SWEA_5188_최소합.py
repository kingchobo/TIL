def dfs(x, y):
    global result
    global ans
    result += area[x][y]

    if x == n-1 and y == n-1:
        if result < ans:
            ans = result

    else:
        for k in range(2):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < n and ny < n:
                dfs(nx, ny)
                result -= area[nx][ny]


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    area = [list(map(int, input().split())) for _ in range(n)]

    dx = [1, 0]
    dy = [0, 1]

    result = 0
    ans = 10 * (2*n - 1)
    dfs(0, 0)
    print(f'#{tc} {ans}')