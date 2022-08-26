import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 문제의 조건에 맞게 순회하기 위해 오름차순으로 정렬
for i in range(n+1):
    graph[i].sort()


def dfs(start):
    print(start, end=' ')
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    queue = [start]
    visited[start] = True
    while queue:
        start = queue.pop(0)
        print(start, end=' ')
        for i in graph[start]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(v)
print()
visited = [False] * (n+1)
bfs(v)