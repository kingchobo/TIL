import sys
input = sys.stdin.readline


def dfs(start):
    global cnt
    if not visited[start]:
        visited[start] = True
        cnt += 1
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
    if cnt == 0:
        return 0
    else:
        return 1


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

cnt_list = []
for i in range(1, n+1):
    cnt = 0
    cnt_list.append(dfs(i))
print(cnt_list.count(1))