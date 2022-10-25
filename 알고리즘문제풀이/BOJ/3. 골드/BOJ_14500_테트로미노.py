import sys

N, M = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 모든 모양의 테트리미노
tetromino_1 = [[(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)]]
tetromino_2 = [[(0, 1), (1, 0), (1, 1)]]
tetromino_3 = [[(1, 0), (2, 0), (2, 1)], [(1, 0), (2, 0), (2, -1)], [(1, 0), (0, 1), (0, 2)], [(0, 1), (0, 2), (1, 2)],
               [(0, 1), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(1, 0), (1, 1), (1, 2)], [(0, 1), (0, 2), (-1, 2)]]
tetromino_4 = [[(1, 0), (1, 1), (2, 1)], [(0, 1), (-1, 1), (-1, 2)], [(0, 1), (1, 1), (1, 2)], [(1, 0), (1, -1), (2, -1)]]
tetromino_5 = [[(1, 0), (2, 0), (1, 1)], [(1, 0), (2, 0), (1, -1)], [(1, 0), (1, -1), (1, 1)], [(0, -1), (0, 1), (1, 0)]]

# 하나로 합치기
tetromino_all = [tetromino_1] + [tetromino_2] + [tetromino_3] + [tetromino_4] + [tetromino_5]


# 모든 좌표를 돌면서 각 좌표마다 블럭의 합들을 계산
ans = 0
for i in range(N):
    for j in range(M):
        for k in tetromino_all:
            for l in range(len(k)):
                temp = area[i][j]
                cnt = 0
                for m in range(3):
                    ni, nj = i + k[l][m][0], j + k[l][m][1]
                    if 0 <= ni < N and 0 <= nj < M:
                        temp += area[ni][nj]
                        cnt += 1
                if cnt == 3 and temp > ans:
                    ans = temp

print(ans)