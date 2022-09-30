def dfs(idx):
    global battery
    global battery_list
    visited[idx] = 1

    if sum(visited) == n:
        battery_list.append(battery + area[idx][0])

    else:
        for j in range(n):
            if not visited[j]:
                battery += area[idx][j]
                dfs(j)
                battery -= area[idx][j]
                visited[j] = 0


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    area = [list(map(int, input().split())) for _ in range(n)]
    # print(area) => [[0, 18, 34], [48, 0, 55], [18, 7, 0]]

    battery_list = []

    for i in range(1, n):
        visited = [1] + [0] * (n-1)
        battery = area[0][i]
        dfs(i)

    print(f'#{tc} {min(battery_list)}')