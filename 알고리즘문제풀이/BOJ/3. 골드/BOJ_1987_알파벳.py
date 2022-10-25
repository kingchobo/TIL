from sys import stdin

R, C = map(int, input().split())
area = [list(stdin.readline().rstrip()) for _ in range(R)]
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(i, j, string):
    global ans
    ans = max(ans, len(string))
    for k in range(4):
        ni, nj = i + delta[k][0], j + delta[k][1]
        if 0 <= ni < R and 0 <= nj < C and area[ni][nj] not in string:
            dfs(ni, nj, string + area[ni][nj])


ans = 0
dfs(0, 0, area[0][0])
print(ans)