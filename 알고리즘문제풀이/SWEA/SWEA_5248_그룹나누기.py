def bfs(i):
    # 신청서를 제출한 학생의 group에 속한 학생 수 : cnt
    cnt = 1
    q = [i]
    while q:
        t = q.pop(0)
        for j in adjL[t]:
            if not visited[j]:
                visited[j] = 1
                q.append(j)
                cnt += 1
    return cnt


T = int(input())
for TC in range(1, T+1):
    N, M = map(int, input().split())        # N = 학생수, M = 제출한 신청서의 수
    students = [i for i in range(1, N+1)]   # 출석번호 리스트
    arr = list(map(int, input().split()))
    adjL = [[] for _ in range(N+1)]  # 인접리스트 생성
    for i in range(M):
        a, b = arr[i*2], arr[i*2 + 1]
        adjL[a].append(b)
        adjL[b].append(a)
    # print(adjL)
    visited = [0] * (N + 1)
    group = []
    for i in range(1, N+1):
        if len(adjL[i]) >= 1 and not visited[i]:   # 기제출된 신청서에 없던 학생이면 그룹 생성
            visited[i] = 1
            group.append(bfs(i))
    # print(group)
    ans = len(group) + (N - sum(group))
    print(f'#{TC} {ans}')