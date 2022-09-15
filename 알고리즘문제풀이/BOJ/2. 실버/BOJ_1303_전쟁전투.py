import sys


def dfs(r, c):
    # not sure if this is dfs.. but
    # 계속 4개 방향으로 탐색하는데, 같은 색이면서 not visited이면 cnt +=1
    # 최종적으로 cnt(이어져있는 같은옷의 개수) return
    global cnt
    visitied[r][c] = 1
    cnt += 1
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < m and 0 <= nc < n and not visitied[nr][nc]:
            if battleground[nr][nc] == battleground[r][c]:
                dfs(nr, nc)
    return cnt


n, m = map(int, sys.stdin.readline().split())
battleground = [list(sys.stdin.readline().strip()) for _ in range(m)]

visitied = [[0] * n for _ in range(m)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
power_W = 0  # W옷(아군)을 입은 병사의 전투력 합
power_B = 0  # B옷(적군)을 입은 병사의 전투력 합

for r in range(m):
    for c in range(n):
        if not visitied[r][c]:  # 아직 방문 안한 곳이면, cnt 0으로 초기화 한 후 함수 호출
            cnt = 0
            power = dfs(r, c) ** 2
            if battleground[r][c] == 'W':  # 맞는 진영에 파워제곱 더해주기
                power_W += power
            else:
                power_B += power

print(power_W, power_B)