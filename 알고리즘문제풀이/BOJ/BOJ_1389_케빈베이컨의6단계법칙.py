# N = 사람의 수, M = 친구 관계의 수
N, M = map(int, input().split())

# 친구관계 그래프 선언
graph = {}
for i in range(1, N+1):
    graph[i] = set()

# 유향 그래프로 표현
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].add(y)

# 무향 그래프로 전환
for i in range(1, N+1):
    for value in graph[i]:
        graph[value].add(i)

# 케빈 베이컨 수 세기
M = 0
idx = 0
kevin = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if j == i:
            pass
        elif j in graph[i]:
            kevin += 1
        else:
            while True:

    if cnt > M:
        M = cnt
        idx = i

print(idx)