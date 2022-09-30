def dfs(i, j):
    global cnt
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < n and 0 <= nj < n:
            if rooms[ni][nj] == rooms[i][j] + 1:
                cnt += 1
                dfs(ni, nj)


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    rooms = [list(map(int, input().split())) for _ in range(n)]
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    cnt_list = []
    for i in range(n):
        for j in range(n):
            cnt = 0
            dfs(i, j)
            cnt_list.append([rooms[i][j], cnt])
    cnt_list.sort()
    cnt_list.sort(key=lambda x:x[1], reverse=True)
    
    print(f'#{tc} {cnt_list[0][0]} {cnt_list[0][1]+1}')