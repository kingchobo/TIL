# # dfs 풀이 -> 시간초과
# def dfs(i, j, h):
#     global temp_max
#     if i == j == N-1:
#         if h < temp_max:
#             temp_max = h
#         return
#
#     if h >= temp_max:
#         return
#
#     else:
#         for k in range(4):
#             ni, nj = i + delta[k][0], j + delta[k][1]
#             if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
#                 h += area[ni][nj]
#                 visited[ni][nj] = 1
#                 dfs(ni, nj, h)
#                 visited[ni][nj] = 0
#                 h -= area[ni][nj]
#
#
# T = int(input())
# for TC in range(1, T+1):
#     N = int(input())
#     area = [list(map(int, input())) for _ in range(N)]
#     delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#     visited = [[0] * N for _ in range(N)]
#     hours = area[0][0]
#     temp_max = 90000
#
#     dfs(0, 0, hours)
#     print(f'#{TC} {temp_max}')