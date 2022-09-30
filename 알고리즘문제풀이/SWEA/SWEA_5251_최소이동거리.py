def dfs(e, w):
    global result
    # 도착했으면 값 비교해서 result에 저장
    if e == N:
        if w < result:
            result = w

    # 이미 기저장되어있는 최소거리보다 같거나 길어지면 중단
    if w >= result:
        return

    # 하나씩 dfs
    for j in adjL[e]:
        dfs(j[0], j[1]+w)


T = int(input())
for TC in range(1, T+1):
    N, E = map(int, input().split())    # N = 마지막 지점 번호, E = 도로의 개수
    adjL = [[] for _ in range(N)]
    result = 100000
    for i in range(E):
        s, e, w = map(int, input().split())
        adjL[s].append((e, w))

    len_list = []
    for i in adjL[0]:
        dfs(i[0], i[1])

    print(f'#{TC} {result}')