def can_reach(s, g, graph):
    if g in graph[s]:
        return 1
    else:
        for i in graph[s]:
            if can_reach(i, g, graph):
                return 1
        else:
            return 0
while True:
    try:
        tc, E = map(int, input().split())
        V = 100
        S, G = 0, 99
        graph = {}
        for i in range(V):
            graph[i] = []

        arr = list(map(int, input().split()))
        for j in range(0, E*2, 2):
            a, b = arr[j], arr[j+1]
            graph[a].append(b)

        print(f'#{tc} {can_reach(S, G, graph)}')

    except EOFError:
        break