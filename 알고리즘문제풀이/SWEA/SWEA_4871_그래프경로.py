def can_reach(s, g, graph):
    if g in graph[s]:
        return 1
    else:
        for i in graph[s]:
            if can_reach(i, g, graph):
                return 1
        else:
            return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = {}
    for i in range(1, V+1):
        graph[i] = []
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
    S, G = map(int, input().split())
    print(f'#{tc} {can_reach(S, G, graph)}')